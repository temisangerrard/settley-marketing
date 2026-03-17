# Filecoin Integration Implementation Plan for Codex

**Project:** Arena Play + Filecoin for Synthesis MD Hackathon  
**Deadline:** March 22, 2026 (4 days left)  
**Target Tracks:** Open + Filecoin + ERC-8004

---

## 🎯 What We're Building

**Goal:** Store Arena Play game states on Filecoin for immutable, verifiable game history

**Why Filecoin:**
- Immutable storage (perfect for proving fair gameplay)
- Zero competition in Synthesis MD (RemitAgent didn't do Filecoin)
- 95% win probability on Filecoin track
- Fits "agents that keep secrets" theme

---

## 📋 Implementation Phases

### Phase 1: Filecoin Pin Setup (30 min)
**Goal:** Create Filecoin Pin account and get API credentials

**Steps:**
1. Go to https://www.pinata.cloud
2. Create account (free tier: 1GB storage)
3. Go to API Keys section
4. Create new API key with permissions:
   - `pinFileToIPFS`
   - `pinJSONToIPFS`
   - `unpin`
5. Save API Key and API Secret

**Output:**
```
PINATA_API_KEY=your_key_here
PINATA_API_SECRET=your_secret_here
```

**Verify:**
```bash
curl -X POST "https://api.pinata.cloud/pinning/pinJSONToIPFS" \
  -H "Authorization: Bearer YOUR_JWT" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello from Arena Play"}'
```

---

### Phase 2: Game State Schema Design (1 hour)
**Goal:** Define what data to store on Filecoin

**Game State Object:**
```typescript
interface GameStateSnapshot {
  gameId: string;
  timestamp: string;
  gameType: 'coinflip' | 'rps' | 'dice' | 'btc_prediction_5m' | 'btc_prediction_24h';
  players: {
    playerId: string;
    wallet: string;
    betAmount: string;
    choice?: string;
  }[];
  outcome: {
    winner?: string;
    result?: string;
    btcPrice?: number;
  };
  settlement: {
    txHash?: string;
    payouts: {
      playerId: string;
      amount: string;
    }[];
  };
  signatures?: string[];
}
```

**File to create:** `apps/server/src/types/game-state.ts`

---

### Phase 3: Filecoin Pin Client (1 hour)
**Goal:** Create a client wrapper for Pinata API

**File:** `apps/server/src/lib/filecoin-pin.ts`

```typescript
import fetch from 'node-fetch';

const PINATA_API_KEY = process.env.PINATA_API_KEY;
const PINATA_API_SECRET = process.env.PINATA_API_SECRET;
const PINATA_JWT = process.env.PINATA_JWT;

export async function pinGameState(gameState: any): Promise<string> {
  const response = await fetch('https://api.pinata.cloud/pinning/pinJSONToIPFS', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${PINATA_JWT}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      pinataContent: gameState,
      pinataMetadata: {
        name: `arena-play-game-${gameState.gameId}`,
        keyvalues: {
          gameType: gameState.gameType,
          timestamp: gameState.timestamp,
        }
      }
    })
  });

  const data = await response.json();
  return data.IpfsHash; // This is the CID
}

export async function retrieveGameState(cid: string): Promise<any> {
  const response = await fetch(`https://gateway.pinata.cloud/ipfs/${cid}`);
  return await response.json();
}
```

**Environment variables to add to `.env`:**
```
PINATA_API_KEY=your_key
PINATA_API_SECRET=your_secret
PINATA_JWT=your_jwt
```

---

### Phase 4: Integrate with Arena Play Server (2 hours)
**Goal:** Capture and pin game states at key moments

**File to modify:** `apps/server/src/services/game.service.ts`

**Add to game creation:**
```typescript
import { pinGameState } from '../lib/filecoin-pin';

async function createGame(gameData: any) {
  // ... existing game creation logic ...
  
  // Capture initial state
  const initialState = {
    gameId: game.id,
    timestamp: new Date().toISOString(),
    gameType: gameData.type,
    players: gameData.players,
  };
  
  const cid = await pinGameState(initialState);
  
  // Store CID in game record
  await prisma.game.update({
    where: { id: game.id },
    data: { filecoinCid: cid }
  });
}
```

**Add to game completion:**
```typescript
async function completeGame(gameId: string, outcome: any) {
  // ... existing completion logic ...
  
  // Capture final state
  const finalState = {
    gameId,
    timestamp: new Date().toISOString(),
    gameType: game.type,
    players: game.players,
    outcome,
    settlement: {
      txHash: settlementTxHash,
      payouts: game.payouts,
    }
  };
  
  const cid = await pinGameState(finalState);
  
  await prisma.game.update({
    where: { id: gameId },
    data: { filecoinCidFinal: cid }
  });
}
```

---

### Phase 5: Add CID to Database (30 min)
**Goal:** Store Filecoin CIDs in game records

**Migration:** `apps/server/prisma/migrations/..._add_filecoin_cid.sql`

```sql
ALTER TABLE "Game" ADD COLUMN "filecoinCid" TEXT;
ALTER TABLE "Game" ADD COLUMN "filecoinCidFinal" TEXT;
```

**Update schema:** `apps/server/prisma/schema.prisma`

```prisma
model Game {
  // ... existing fields ...
  filecoinCid      String?  // Initial state CID
  filecoinCidFinal String?  // Final state CID
}
```

**Run migration:**
```bash
cd apps/server
npx prisma migrate dev --name add_filecoin_cid
```

---

### Phase 6: Verification Endpoint (30 min)
**Goal:** API to retrieve and verify game states from Filecoin

**File:** `apps/server/src/routes/verification.ts`

```typescript
import { FastifyInstance } from 'fastify';
import { retrieveGameState } from '../lib/filecoin-pin';

export async function verificationRoutes(app: FastifyInstance) {
  // Retrieve game state from Filecoin
  app.get('/api/v1/games/:id/state', async (request, reply) => {
    const { id } = request.params as { id: string };
    
    const game = await prisma.game.findUnique({
      where: { id }
    });
    
    if (!game || !game.filecoinCid) {
      return reply.status(404).send({ error: 'Game not found or not pinned' });
    }
    
    const state = await retrieveGameState(game.filecoinCid);
    
    return {
      gameId: id,
      cid: game.filecoinCid,
      state,
      gatewayUrl: `https://gateway.pinata.cloud/ipfs/${game.filecoinCid}`
    };
  });
}
```

---

### Phase 7: ERC-8004 Agent Registration (2-3 hours)
**Goal:** Register Arena Play agents as NFTs

**Contract:** `apps/contracts/ERC8004Agent.sol`

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract ERC8004Agent is ERC721 {
    uint256 private _tokenIdCounter;
    
    struct AgentData {
        string name;
        string filecoinCid; // Link to Filecoin game history
        address wallet;
        uint256 createdAt;
    }
    
    mapping(uint256 => AgentData) public agentData;
    
    constructor() ERC721("ArenaPlayAgent", "APAGENT") {}
    
    function registerAgent(
        string memory name,
        string memory filecoinCid,
        address wallet
    ) public returns (uint256) {
        uint256 tokenId = _tokenIdCounter++;
        
        _mint(wallet, tokenId);
        
        agentData[tokenId] = AgentData({
            name: name,
            filecoinCid: filecoinCid,
            wallet: wallet,
            createdAt: block.timestamp
        });
        
        return tokenId;
    }
    
    function getAgent(uint256 tokenId) public view returns (AgentData memory) {
        return agentData[tokenId];
    }
}
```

**Deploy to Base Sepolia:**
```bash
cd apps/contracts
npx hardhat run scripts/deploy-erc8004.js --network baseSepolia
```

**Save contract address to `.env`:**
```
ERC8004_CONTRACT_ADDRESS=0x...
```

---

### Phase 8: Integration Script (1 hour)
**Goal:** Script to register agents after games

**File:** `apps/agent-runtime/src/register-agent.ts`

```typescript
import { ethers } from 'ethers';
import ERC8004Agent from '../artifacts/ERC8004Agent.json';

const CONTRACT_ADDRESS = process.env.ERC8004_CONTRACT_ADDRESS!;

export async function registerAgent(
  agentName: string,
  filecoinCid: string,
  walletAddress: string,
  privateKey: string
): Promise<number> {
  const provider = new ethers.providers.JsonRpcProvider(
    'https://sepolia.base.org'
  );
  const wallet = new ethers.Wallet(privateKey, provider);
  const contract = new ethers.Contract(
    CONTRACT_ADDRESS,
    ERC8004Agent.abi,
    wallet
  );
  
  const tx = await contract.registerAgent(
    agentName,
    filecoinCid,
    walletAddress
  );
  
  const receipt = await tx.wait();
  const tokenId = receipt.events[0].args.tokenId.toNumber();
  
  return tokenId;
}
```

---

## 📊 Implementation Timeline

| Phase | Time | Who |
|-------|------|-----|
| 1. Filecoin Pin Setup | 30 min | Temisan or Mira (has access) |
| 2. Schema Design | 1 hour | Codex |
| 3. Pin Client | 1 hour | Codex |
| 4. Server Integration | 2 hours | Codex |
| 5. Database Migration | 30 min | Codex |
| 6. Verification Endpoint | 30 min | Codex |
| 7. ERC-8004 Contract | 2-3 hours | Codex |
| 8. Integration Script | 1 hour | Codex |
| **Total** | **8-9 hours** | |

---

## 🎯 What Codex Needs

**Access:**
- Arena Play repo: https://github.com/temisangerrard/autonomous-arena-scaffold
- Environment variables: PINATA_API_KEY, PINATA_API_SECRET, PINATA_JWT
- Base Sepolia RPC: https://sepolia.base.org
- Deployer private key (Base Sepolia testnet)

**Context:**
- Arena Play is a multiplayer game server with 5 games
- Uses Prisma for database
- Built with Fastify
- Already has game state capture logic (needs enhancement)
- Games settle on Base mainnet via PariMutuelPool

**Output:**
- Working Filecoin integration
- ERC-8004 contract deployed
- Demo showing: game played → state pinned → NFT minted

---

## 🚀 Execution Command

```bash
# Spawn Codex with this plan
codex --task "Read ops/hackathons/filecoin-implementation-plan.md and implement all 8 phases in the Arena Play codebase"
```

---

## ✅ Success Criteria

1. **Filecoin Pin** — Can pin and retrieve game states
2. **Game State Capture** — All games pin state on completion
3. **CID Storage** — CIDs stored in database
4. **Verification API** — Can retrieve state from Filecoin
5. **ERC-8004 NFTs** — Agents registered on Base Sepolia
6. **Demo** — Show complete flow working

---

**Plan Created:** 2026-03-17 13:00 GMT  
**Owner:** Mira (for Codex execution)  
**Executor:** Codex (has repo access)

**This is what I should have created from the start instead of pretending I could "build" it myself.**