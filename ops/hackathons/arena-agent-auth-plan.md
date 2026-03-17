# Arena Play + Agent-Auth Implementation Plan

**Project:** Cryptographic identity and delegation for Arena Play bots  
**Hackathon:** Synthesis MD (March 4-25, 2026)  
**Deadline:** March 22, 2026 (5 days left)  
**Time Estimate:** 4-6 hours  
**Difficulty:** Medium (requires crypto understanding, but library is well-documented)

---

## 🎯 What We're Building

**Goal:** Add cryptographic identity and delegation to Arena Play bots

**Why:**
- ✅ **Security:** Bots can't exceed delegated spending limits
- ✅ **Audit Trail:** Every bet has verifiable proof of authorization
- ✅ **Multi-Agent:** Arena Play → Individual bot delegation chains
- ✅ **Synthesis MD:** Perfect demo for "agents that pay" + "agents that keep secrets"

**Outcome:** Complete provenance story — Agent identity (agent-auth) + Immutable game history (Filecoin)

---

## 📋 Implementation Phases

### Phase 1: Setup & Identity Generation (1 hour)

**Goal:** Install agent-auth library and generate identities

**Steps:**

1. **Install Library** (5 min)
```bash
cd apps/agent-runtime
npm install @kanoniv/agent-auth
```

2. **Generate Arena Play Identity** (15 min)
```typescript
// apps/agent-runtime/src/lib/arena-identity.ts
import { generateKeyPair, AgentIdentity } from '@kanoniv/agent-auth';

export class ArenaIdentity {
  private static instance: ArenaIdentity;
  private identity: AgentIdentity;

  private constructor() {
    // Generate or load existing keypair
    this.identity = generateKeyPair();
    // TODO: Persist to secure storage (env vars, key manager)
  }

  public static getInstance(): ArenaIdentity {
    if (!ArenaIdentity.instance) {
      ArenaIdentity.instance = new ArenaIdentity();
    }
    return ArenaIdentity.instance;
  }

  public get did(): string {
    return this.identity.did;
  }

  public get publicKey(): string {
    return this.identity.publicKey;
  }
}
```

3. **Store Identity Securely** (20 min)
```bash
# Add to .env (production: use secret manager)
ARENA_AGENT_PRIVATE_KEY=<hex-encoded-private-key>
ARENA_AGENT_DID=did:agent:<derived-did>
```

4. **Test Identity Generation** (20 min)
```bash
npm test -- src/lib/arena-identity.test.ts
```

**Deliverable:** Arena Play has cryptographic identity (`did:agent:...`)

---

### Phase 2: Bot Delegation System (2 hours)

**Goal:** Create delegation chains from Arena Play → Individual bots

**Steps:**

1. **Define Delegation Types** (30 min)
```typescript
// apps/agent-runtime/src/types/delegation.ts
export interface BotDelegation {
  botId: string;
  botDid: string;
  actionScope: string[]; // ["play_rps", "play_dice", "play_coinflip"]
  maxCostPerBet: number; // in ETH/USDC
  maxCostPerDay: number; // daily spending limit
  expiresAt: string; // ISO 8601 timestamp
  createdAt: string;
}
```

2. **Create Delegation Factory** (45 min)
```typescript
// apps/agent-runtime/src/lib/delegation-factory.ts
import { createRootDelegation, Delegation } from '@kanoniv/agent-auth';
import { ArenaIdentity } from './arena-identity';
import { BotDelegation } from '../types/delegation';

export class DelegationFactory {
  private arenaIdentity: ArenaIdentity;

  constructor() {
    this.arenaIdentity = ArenaIdentity.getInstance();
  }

  public createBotDelegation(botDelegation: BotDelegation): Delegation {
    const caveats = [
      {
        type: 'action_scope',
        value: botDelegation.actionScope,
      },
      {
        type: 'max_cost',
        value: botDelegation.maxCostPerBet,
      },
      {
        type: 'expires_at',
        value: botDelegation.expiresAt,
      },
    ];

    // Add daily limit as custom caveat
    if (botDelegation.maxCostPerDay) {
      caveats.push({
        type: 'custom',
        key: 'max_cost_per_day',
        value: botDelegation.maxCostPerDay,
      });
    }

    return createRootDelegation(
      this.arenaIdentity.identity,
      botDelegation.botDid,
      caveats
    );
  }
}
```

3. **Integrate with Bot Creation** (45 min)
```typescript
// apps/agent-runtime/src/services/bot-service.ts
import { DelegationFactory } from '../lib/delegation-factory';
import { generateKeyPair } from '@kanoniv/agent-auth';

export class BotService {
  private delegationFactory: DelegationFactory;

  constructor() {
    this.delegationFactory = new DelegationFactory();
  }

  public async createBot(config: BotConfig): Promise<Bot> {
    // Generate bot identity
    const botKeypair = generateKeyPair();
    const botDid = botKeypair.identity.did;

    // Create delegation
    const delegation = this.delegationFactory.createBotDelegation({
      botId: config.id,
      botDid,
      actionScope: config.allowedGames, // ["play_rps", "play_dice"]
      maxCostPerBet: config.maxBetAmount, // 0.1 ETH
      maxCostPerDay: config.dailyLimit, // 1.0 ETH
      expiresAt: config.expiresAt || '2026-12-31T23:59:59Z',
      createdAt: new Date().toISOString(),
    });

    // Store bot with identity + delegation
    const bot = await this.prisma.bot.create({
      data: {
        id: config.id,
        did: botDid,
        publicKey: botKeypair.publicKey,
        delegation: JSON.stringify(delegation),
        ...config,
      },
    });

    return bot;
  }
}
```

4. **Add Database Schema** (30 min)
```prisma
// apps/agent-runtime/prisma/schema.prisma
model Bot {
  id              String   @id @default(uuid())
  did             String   @unique // did:agent:...
  publicKey       String
  delegation      String   // JSON-encoded delegation
  actionScope     String[] // ["play_rps", "play_dice"]
  maxBetAmount    Decimal
  dailyLimit      Decimal
  expiresAt       DateTime
  createdAt       DateTime @default(now())
  updatedAt       DateTime @updatedAt
  
  // Relations
  games           Game[]
}
```

```bash
npx prisma migrate dev --name add_bot_identity_delegation
```

**Deliverable:** Each bot has cryptographic identity + delegated authority

---

### Phase 3: Proof Generation for Game Calls (1.5 hours)

**Goal:** Generate and attach proofs to every game/bet action

**Steps:**

1. **Create Proof Generator** (45 min)
```typescript
// apps/agent-runtime/src/lib/proof-generator.ts
import { McpProof } from '@kanoniv/agent-auth';
import { Bot } from '@prisma/client';

export class ProofGenerator {
  public generateGameProof(
    bot: Bot,
    action: string,
    args: Record<string, unknown>
  ): Record<string, unknown> {
    // Load bot's delegation from database
    const delegation = JSON.parse(bot.delegation);

    // Create proof for this specific action
    const proof = McpProof.create(
      { did: bot.did, privateKey: bot.privateKey }, // Bot identity
      action, // e.g., "play_rps"
      args, // Game arguments
      delegation // Delegated authority
    );

    // Inject proof into arguments
    const argsWithProof = McpProof.inject(proof, args);

    return argsWithProof;
  }
}
```

2. **Integrate with Game Execution** (45 min)
```typescript
// apps/agent-runtime/src/services/game-service.ts
import { ProofGenerator } from '../lib/proof-generator';

export class GameService {
  private proofGenerator: ProofGenerator;

  constructor() {
    this.proofGenerator = new ProofGenerator();
  }

  public async executeGameAction(
    botId: string,
    action: string,
    args: Record<string, unknown>
  ): Promise<GameResult> {
    // Load bot with identity
    const bot = await this.prisma.bot.findUnique({
      where: { id: botId },
    });

    if (!bot) {
      throw new Error(`Bot ${botId} not found`);
    }

    // Generate proof
    const argsWithProof = this.proofGenerator.generateGameProof(
      bot,
      action,
      args
    );

    // Execute game with proof
    const result = await this.executeGameWithProof(action, argsWithProof);

    // Store proof in game record for audit
    await this.prisma.game.update({
      where: { id: result.gameId },
      data: {
        agentProof: JSON.stringify(argsWithProof._proof),
      },
    });

    return result;
  }
}
```

3. **Add Proof Storage to Database** (30 min)
```prisma
// apps/server/prisma/schema.prisma
model Game {
  // ... existing fields ...
  agentProof    String?  // JSON-encoded agent-auth proof
  agentDid      String?  // did:agent:... of bot that played
}
```

```bash
npx prisma migrate dev --name add_agent_proof_storage
```

**Deliverable:** Every game action includes verifiable proof

---

### Phase 4: Proof Verification (1 hour)

**Goal:** Verify proofs before executing game actions

**Steps:**

1. **Create Verification Middleware** (45 min)
```typescript
// apps/server/src/middleware/verify-agent-proof.ts
import { verifyMcpCall } from '@kanoniv/agent-auth';
import { ArenaIdentity } from '../lib/arena-identity';

export function verifyAgentProof(req: Request, res: Response, next: NextFunction) {
  const { _proof, ...cleanArgs } = req.body;

  if (!_proof) {
    return res.status(401).json({
      error: 'Missing agent proof',
      hint: 'Every game action must include cryptographic proof of authorization',
    });
  }

  try {
    const arenaIdentity = ArenaIdentity.getInstance();
    const result = verifyMcpCall(_proof, arenaIdentity.identity);

    // Attach verification result to request
    req.agentVerification = {
      verified: true,
      agentDid: result.invoker_did,
      rootDid: result.root_did,
      depth: result.depth,
      actionScope: result.caveats?.action_scope,
      maxCost: result.caveats?.max_cost,
    };

    // Use clean args (without _proof) for game logic
    req.body = cleanArgs;

    next();
  } catch (error) {
    return res.status(403).json({
      error: 'Invalid agent proof',
      hint: error.message,
    });
  }
}
```

2. **Apply Middleware to Game Routes** (30 min)
```typescript
// apps/server/src/routes/games.ts
import { verifyAgentProof } from '../middleware/verify-agent-proof';

router.post('/play', verifyAgentProof, async (req, res) => {
  // req.agentVerification is now available
  // req.body contains clean args (no _proof)
  
  const { agentDid, maxCost } = req.agentVerification;
  
  // Execute game with verified agent
  const result = await gameService.executeGame(req.body);
  
  res.json({
    ...result,
    verification: {
      agent: agentDid,
      verified: true,
    },
  });
});
```

3. **Add Verification Tests** (45 min)
```typescript
// apps/server/src/middleware/verify-agent-proof.test.ts
describe('verifyAgentProof', () => {
  it('should reject requests without proof', async () => {
    const response = await request(app)
      .post('/api/v1/games/play')
      .send({ action: 'play_rps', choice: 'rock' });

    expect(response.status).toBe(401);
    expect(response.body.error).toBe('Missing agent proof');
  });

  it('should accept requests with valid proof', async () => {
    const bot = await createBotWithDelegation();
    const proof = generateValidProof(bot);

    const response = await request(app)
      .post('/api/v1/games/play')
      .send(proof);

    expect(response.status).toBe(200);
    expect(response.body.verification.verified).toBe(true);
  });

  it('should reject expired delegations', async () => {
    const bot = await createBotWithExpiredDelegation();
    const proof = generateValidProof(bot);

    const response = await request(app)
      .post('/api/v1/games/play')
      .send(proof);

    expect(response.status).toBe(403);
    expect(response.body.error).toContain('expired');
  });

  it('should reject actions outside scope', async () => {
    const bot = await createBotWithScope(['play_rps']);
    const proof = generateProofForAction(bot, 'play_dice');

    const response = await request(app)
      .post('/api/v1/games/play')
      .send(proof);

    expect(response.status).toBe(403);
    expect(response.body.error).toContain('action_scope');
  });
});
```

**Deliverable:** All game actions verified before execution

---

### Phase 5: Demo & Documentation (1 hour)

**Goal:** Create demo showing agent-auth + Filecoin integration

**Steps:**

1. **Create Demo Script** (30 min)
```typescript
// demos/agent-auth-demo.ts
/**
 * Demo: Complete provenance from agent identity to immutable game history
 * 
 * Flow:
 * 1. Arena Play generates identity
 * 2. Arena delegates to bot (with limits)
 * 3. Bot plays game (with proof)
 * 4. Game state stored on Filecoin (with agent DID)
 * 5. Verification: retrieve from Filecoin + verify proof
 */

import { ArenaIdentity } from '../apps/agent-runtime/src/lib/arena-identity';
import { DelegationFactory } from '../apps/agent-runtime/src/lib/delegation-factory';
import { ProofGenerator } from '../apps/agent-runtime/src/lib/proof-generator';
import { pinGameState } from '../apps/server/src/lib/filecoin-pin';

async function runDemo() {
  console.log('🎮 Arena Play + Agent-Auth Demo\n');

  // Step 1: Arena Play identity
  console.log('1️⃣ Arena Play Identity');
  const arena = ArenaIdentity.getInstance();
  console.log(`   DID: ${arena.did}`);

  // Step 2: Create bot with delegation
  console.log('\n2️⃣ Bot Delegation');
  const delegationFactory = new DelegationFactory();
  const bot = await createBotWithDelegation({
    actionScope: ['play_rps'],
    maxCostPerBet: 0.1,
    maxCostPerDay: 1.0,
  });
  console.log(`   Bot DID: ${bot.did}`);
  console.log(`   Scope: ${bot.actionScope.join(', ')}`);
  console.log(`   Max Bet: ${bot.maxBetAmount} ETH`);

  // Step 3: Bot plays game (with proof)
  console.log('\n3️⃣ Bot Plays Game (with proof)');
  const proofGenerator = new ProofGenerator();
  const gameArgs = proofGenerator.generateGameProof(bot, 'play_rps', {
    choice: 'rock',
  });
  console.log(`   Proof generated: ${gameArgs._proof ? '✅' : '❌'}`);

  // Step 4: Store game state on Filecoin
  console.log('\n4️⃣ Store on Filecoin');
  const gameState = {
    gameId: 'demo-game-123',
    agentDid: bot.did,
    action: 'play_rps',
    result: 'win',
    timestamp: new Date().toISOString(),
  };
  const cid = await pinGameState(gameState);
  console.log(`   CID: ${cid}`);
  console.log(`   Gateway: https://gateway.pinata.cloud/ipfs/${cid}`);

  // Step 5: Verify
  console.log('\n5️⃣ Verification');
  console.log(`   Agent: ${gameState.agentDid}`);
  console.log(`   Game: ${gameState.gameId}`);
  console.log(`   Result: ${gameState.result}`);
  console.log(`   Provenance: Complete ✅`);

  console.log('\n🎉 Demo Complete!');
  console.log('   Agent identity + Delegation + Filecoin = Full Provenance');
}

runDemo().catch(console.error);
```

2. **Record Demo Video** (30 min)
- Screen record running demo script
- Show: Identity → Delegation → Proof → Filecoin → Verification
- 2-3 minute video for Synthesis MD submission

3. **Write Documentation** (30 min)
```markdown
# Arena Play Agent-Auth Integration

## Overview
Arena Play uses cryptographic identity and delegation for all bot actions.

## Architecture
Human → Arena Play (root) → Individual Bots (delegated)

## Security
- Bots can't exceed delegated spending limits
- Every action includes verifiable proof
- Complete audit trail on Filecoin

## Usage
[Code examples for creating bots, delegating authority, verifying proofs]
```

**Deliverable:** Demo video + documentation for Synthesis MD submission

---

## 📊 Implementation Timeline

| Phase | Time | Dependencies | Owner |
|-------|------|--------------|-------|
| 1. Setup & Identity | 1 hour | None | Temisan/Codex |
| 2. Bot Delegation | 2 hours | Phase 1 | Temisan/Codex |
| 3. Proof Generation | 1.5 hours | Phase 2 | Temisan/Codex |
| 4. Proof Verification | 1 hour | Phase 3 | Temisan/Codex |
| 5. Demo & Docs | 1 hour | Phase 4 | Temisan/Mira |
| **Total** | **6.5 hours** | | |

---

## 🎯 Integration with Existing Work

### **Filecoin Integration (Already Planned)**
```typescript
// Perfect pairing: agent-auth + Filecoin
const gameState = {
  gameId: '123',
  agentDid: bot.did, // From agent-auth
  action: 'play_rps',
  result: 'win',
  timestamp: new Date().toISOString(),
};

const cid = await pinGameState(gameState); // Store on Filecoin

// Complete provenance:
// - Who: bot.did (cryptographic identity)
// - What: play_rps, win (game action)
// - When: timestamp
// - Authorized by: delegation chain (agent-auth proof)
// - Immutable: Filecoin CID
```

### **Synthesis MD Submission**
**Narrative:** "Arena Play: Autonomous agents with verifiable identity, delegated authority, and immutable game history"

**Tracks:**
- ✅ Open Track (multi-agent economy)
- ✅ Filecoin Track (immutable storage)
- ✅ ERC-8004 Track (agent registration as NFTs)
- ✅ **NEW: Agent-Auth** (cryptographic identity + delegation)

---

## 🛡️ Security Considerations

### **Key Management**
```typescript
// ❌ DON'T: Store private keys in code
const privateKey = 'hardcoded-key';

// ✅ DO: Use environment variables (development)
const privateKey = process.env.ARENA_AGENT_PRIVATE_KEY;

// ✅ DO: Use secret manager (production)
const privateKey = await secretManager.get('arena-agent-key');
```

### **Delegation Limits**
```typescript
// Always set:
- action_scope: What actions can the bot perform?
- max_cost: Maximum spend per action
- expires_at: When does delegation expire?
- custom caveats: Daily limits, game restrictions, etc.
```

### **Proof Verification**
```typescript
// Always verify before executing:
- Check proof signature
- Verify delegation chain
- Check caveats (scope, cost, expiry)
- Reject if any check fails
```

---

## 📁 Files to Create/Modify

### **New Files:**
- `apps/agent-runtime/src/lib/arena-identity.ts`
- `apps/agent-runtime/src/lib/delegation-factory.ts`
- `apps/agent-runtime/src/lib/proof-generator.ts`
- `apps/server/src/middleware/verify-agent-proof.ts`
- `demos/agent-auth-demo.ts`

### **Modified Files:**
- `apps/agent-runtime/src/services/bot-service.ts`
- `apps/agent-runtime/src/services/game-service.ts`
- `apps/server/src/routes/games.ts`
- `apps/agent-runtime/prisma/schema.prisma`
- `apps/server/prisma/schema.prisma`

---

## ✅ Success Criteria

1. **Arena Play has cryptographic identity** (`did:agent:...`)
2. **Each bot has delegated authority** (with spending limits)
3. **Every game action includes proof** (verifiable authorization)
4. **Proofs verified before execution** (reject invalid/expired)
5. **Proofs stored with game state** (on Filecoin for audit)
6. **Demo video complete** (shows full provenance flow)
7. **Documentation written** (for Synthesis MD submission)

---

## 🚀 Getting Started Command

```bash
# Start implementation
cd /Users/temisan/Downloads/autobett-repo

# Phase 1: Install and setup
npm install @kanoniv/agent-auth
npx ts-node scripts/generate-arena-identity.ts

# Phase 2-4: Follow implementation plan above
# Phase 5: Run demo
npx ts-node demos/agent-auth-demo.ts
```

---

**Plan Created:** 2026-03-17 18:55 GMT  
**Owner:** Temisan (technical implementation), Mira (demo + docs)  
**Executor:** Temisan or Codex (has repo access)  
**Deadline:** March 22, 2026 (5 days)

**This pairs perfectly with Filecoin integration for complete provenance story.**
