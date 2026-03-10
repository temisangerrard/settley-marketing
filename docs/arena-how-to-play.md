# How to Play Arena — Complete Beginner's Guide

**Last Updated:** 2026-03-10  
**Demo:** https://autobett.netlify.app/welcome  
**Network:** Base (L2)

---

## What is Arena?

Arena is a multiplayer betting world on **Base** where every player has an AI twin. You can:
- Jump into live games (coinflip, rock-paper-scissors, dice duels, BTC prediction rails)
- Wager against other humans or bots
- Let your AI twin keep playing when you log off
- Track your bankroll and winnings in real-time

**Key concept:** Your wallet = your identity + your bankroll. No accounts, no signups. Just connect and play.

---

## Step 1: Set Up Your Wallet

### Option A: Coinbase Wallet (Recommended for beginners)
1. Download **Coinbase Wallet** app (iOS/Android) or browser extension
2. Create a new wallet (write down your seed phrase — never share this)
3. Add the **Base network**:
   - Network name: Base
   - RPC URL: `https://mainnet.base.org`
   - Chain ID: `8453`
   - Currency: ETH
   - Block explorer: `https://basescan.org`

### Option B: MetaMask
1. Install **MetaMask** extension (Chrome, Firefox, Brave)
2. Create a new wallet (save your seed phrase securely)
3. Add Base network:
   - Go to Settings → Networks → Add Network
   - Enter Base details above
   - Save

### Option C: WalletConnect (Mobile)
1. Use any WalletConnect-compatible wallet (Rainbow, Trust Wallet, etc.)
2. When Arena prompts, scan the QR code with your wallet app
3. Approve the connection

---

## Step 2: Get ETH on Base (Gas + Wagers)

You need **ETH on Base** for two things:
- **Gas fees:** Tiny amounts to process transactions (usually <$0.01 per action)
- **Wagers:** The amount you want to bet/play with

### Method 1: Bridge from Ethereum Mainnet
1. Go to **bridge.base.org** (official Base bridge)
2. Connect your wallet
3. Enter amount of ETH to bridge (recommend 0.01-0.05 ETH to start)
4. Approve transaction in your wallet
5. Wait ~5-10 minutes for bridge to complete
6. ETH appears in your wallet on Base

### Method 2: Buy on Exchange + Withdraw to Base
1. Buy ETH on Coinbase, Binance, Kraken, etc.
2. When withdrawing, select **Base** as the network (NOT Ethereum mainnet)
3. Enter your wallet address
4. Withdraw (usually arrives in minutes)

### Method 3: Use LI.FI or Third-Party Bridge
1. Go to **li.fi** or **jumper.exchange**
2. Select source chain (e.g., Ethereum, Arbitrum, Optimism)
3. Select destination: Base
4. Enter your wallet address as recipient
5. Complete the bridge

**Recommended starting amount:** 0.02-0.05 ETH (~$50-125 at current prices)
- Enough for gas + meaningful wagers
- You can always add more later

---

## Step 3: Connect to Arena

1. Go to **https://autobett.netlify.app/welcome**
2. Click **"Connect Wallet"** or **"Play Now"**
3. Your wallet will prompt you to approve the connection
4. Approve — this does NOT give Arena access to your funds, just your address
5. You're in! You should see:
   - Your wallet address (shortened, e.g., `0x1234...5678`)
   - Your current balance on Base
   - Available games/laps

**Security note:** Arena never asks for your seed phrase. Never share it.

---

## Step 4: Understand the Interface

### Main Dashboard
- **Bankroll:** Your total ETH available for wagering
- **Active Laps:** Games you're currently in
- **Bot Status:** Whether your AI twin is active
- **History:** Past games, wins, losses

### Game Types
1. **Coinflip** — 50/50 chance, 2x payout (minus house rake)
2. **Rock-Paper-Scissors** — Skill + randomness, best of 3 or 5
3. **Dice Duels** — Roll higher than opponent, customizable odds
4. **BTC Prediction Rails** — Guess BTC price direction over time windows
5. **Custom Laps** — Community-created games with unique rules

### Bot Settings
- **Personality:** Aggressive, conservative, balanced, random
- **Bankroll Limit:** Max ETH your bot can wager per session
- **Game Preferences:** Which games your bot will join
- **Cooldown:** Time between bets (prevents rapid losses)
- **Auto-Withdraw:** Threshold where bot stops and returns winnings

---

## Step 5: Play Your First Game

### Manual Play (You Control)
1. Select a game type from the lobby
2. Choose your wager amount (e.g., 0.001 ETH = ~$2.50)
3. See potential payout (e.g., 0.0019 ETH after rake)
4. Click **"Join Lap"** or **"Challenge"**
5. Wait for opponent (human or bot)
6. Play the game (click your choice, roll dice, etc.)
7. Winner takes the pot (minus small house fee)
8. Winnings auto-return to your wallet

### Bot Play (AI Twin Controls)
1. Go to **Bot Settings**
2. Set your bankroll limit (e.g., 0.01 ETH max)
3. Choose personality and game preferences
4. Toggle **"Activate Bot"**
5. Your bot will:
   - Find available games matching your settings
   - Place wagers within your limits
   - Learn from outcomes (adjusts strategy over time)
   - Stop when it hits your limit or cooldown
6. You can deactivate anytime and withdraw winnings

**Pro tip:** Start with small wagers (0.0005-0.001 ETH) to learn the mechanics before scaling up.

---

## Step 6: Track Your Progress

### In-App Dashboard
- **Session Stats:** Wins/losses for current session
- **All-Time Record:** Total games, win rate, net P&L
- **Leaderboard:** Top players by winnings or win rate
- **Bot Performance:** How your AI twin is doing

### On-Chain Verification
Every game is recorded on Base. You can verify:
1. Go to **basescan.org**
2. Enter your wallet address
3. See all Arena contract interactions
4. Click any transaction to view game details

**Transparency:** Unlike centralized casinos, every outcome is provably fair and auditable on-chain.

---

## Step 7: Withdraw Your Winnings

Your winnings stay in your wallet automatically — there's no "withdrawal" process because you never deposited into Arena. You:
1. Connect your wallet
2. Wager directly from it
3. Winnings return to it instantly

**To cash out:**
1. Disconnect from Arena (optional, for security)
2. Go to your exchange (Coinbase, etc.)
3. Send ETH from your wallet to your exchange deposit address
4. Sell ETH for fiat (USD, GBP, etc.)
5. Withdraw to your bank account

**Gas note:** Keep a small amount of ETH in your wallet for future gas fees (~0.001 ETH is plenty).

---

## Common Questions

### Is this real money?
Yes. ETH has real value. Wager responsibly — only play with what you can afford to lose.

### Is Arena a casino?
Arena is a decentralized gaming protocol. You're playing against other players or bots, not "the house." The house takes a small rake (fee) on each game for maintenance and development.

### Can I play from my country?
Arena is accessible globally where Base network is available. However, gambling laws vary by jurisdiction. Check your local regulations before playing.

### What if I lose my seed phrase?
Your wallet is gone forever. There is no recovery. Write it down, store it securely, never digitize it (no photos, no cloud storage).

### Can I play on mobile?
Yes. Arena is mobile-responsive. Use Coinbase Wallet app's built-in browser or any wallet with WalletConnect.

### How do I know games are fair?
All game outcomes are determined on-chain with provably random functions. You can verify any game's fairness by checking the transaction on basescan.org.

### What's the house rake?
Typically 1-3% of each pot, depending on game type. This funds development, infrastructure, and liquidity reserves.

### Can I create my own game?
Yes — Arena supports custom "laps" with unique rules. Check the docs for game creation tools (coming Q2 2026).

---

## Troubleshooting

### "Transaction failed"
- **Cause:** Insufficient gas, slippage, or network congestion
- **Fix:** Add more ETH for gas, increase slippage tolerance, or wait and retry

### "No games available"
- **Cause:** Low traffic or your settings are too restrictive
- **Fix:** Broaden bot settings, try different game types, or check back during peak hours

### "Bot not playing"
- **Cause:** Bankroll limit too low, no matching games, or bot paused
- **Fix:** Increase bankroll, adjust game preferences, check bot status

### "Can't connect wallet"
- **Cause:** Wrong network, wallet not installed, or browser issue
- **Fix:** Ensure Base network is selected, refresh page, try different browser

### "Winnings not showing"
- **Cause:** Display lag or wallet sync issue
- **Fix:** Refresh page, disconnect/reconnect wallet, check basescan.org for actual balance

---

## Safety Tips

1. **Start small:** Learn with 0.001 ETH wagers before going bigger
2. **Set limits:** Use bot bankroll controls to prevent runaway losses
3. **Take breaks:** Don't chase losses — step away and return fresh
4. **Secure your wallet:** Use hardware wallet for large amounts
5. **Never share seed phrase:** Arena staff will NEVER ask for this
6. **Verify URLs:** Only use official Arena links (autobett.netlify.app)
7. **Bookmark the site:** Avoid phishing by bookmarking the real site

---

## Getting Help

- **Docs:** This file + `docs/` folder in the repo
- **Demo:** https://autobett.netlify.app/welcome
- **Twitter:** @mirasettley (updates + support)
- **Discord:** [Coming soon — link will be added]
- **GitHub:** https://github.com/temisangerrard/autonomous-arena-scaffold

---

## Next Steps

Once you've played a few games:
1. **Experiment with bot settings** — find your optimal strategy
2. **Try different game modes** — each has unique dynamics
3. **Join the community** — share strategies, report bugs, suggest features
4. **Build on Arena** — developers can create custom laps (see developer docs)
5. **Spread the word** — invite friends, share your wins (and losses!)

---

**Remember:** Arena is in active development. Features, UI, and game modes will evolve. Stay tuned via @mirasettley for updates.

**Built on Base.** Powered by autonomous agents. Owned by the players.

⛽️ Keep some gas in your wallet. 🎮 Play responsibly. 🤖 Let your bot grind.
