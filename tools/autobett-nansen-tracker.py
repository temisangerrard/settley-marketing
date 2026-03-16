#!/usr/bin/env python3
"""
Autobett Gaming Intelligence Tracker — Nansen CLI Integration
==============================================================

A CLI tool that uses Nansen API to track on-chain gaming activity,
gambling token flows, and competitive intelligence for Autobett.

Built for the #NansenCLI challenge by Mira (@mirasettley)
"""

import json
import subprocess
import sys
from datetime import datetime

def run_nansen_command(args):
    """Execute nansen CLI command and return JSON output."""
    cmd = ["npx", "nansen"] + args + ["--pretty"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return json.loads(result.stdout)
    except:
        return {"error": result.stdout[:200]}

def get_gaming_tokens(chain="ethereum", timeframe="24h", limit=10):
    """Get gaming/gambling token screener data."""
    return run_nansen_command([
        "research", "token", "screener",
        "--chain", chain, "--timeframe", timeframe, "--limit", str(limit)
    ])

def get_smart_money_gaming(chain="ethereum", limit=5):
    """Get smart money flows into gaming tokens."""
    return run_nansen_command([
        "research", "smart-money", "netflow",
        "--chain", chain, "--limit", str(limit)
    ])

def get_perp_gaming(chain="ethereum", limit=5):
    """Get perpetuals data for gaming-related assets."""
    return run_nansen_command([
        "research", "perp", "screener",
        "--chain", chain, "--limit", str(limit)
    ])

def get_token_ohlcv(token_address, chain="ethereum", timeframe="1h", limit=24):
    """Get OHLCV data for a gaming token."""
    return run_nansen_command([
        "research", "token", "ohlcv",
        "--chain", chain, "--token-address", token_address,
        "--timeframe", timeframe, "--limit", str(limit)
    ])

def get_whale_activity(token_address, chain="ethereum", timeframe="24h", limit=5):
    """Get whale buys/sells for a token."""
    return run_nansen_command([
        "research", "token", "who-bought-sold",
        "--chain", chain, "--token-address", token_address,
        "--timeframe", timeframe, "--limit", str(limit)
    ])

def generate_report():
    """Generate Autobett Gaming Intelligence Report."""
    print("=" * 70)
    print("AUTOBETT GAMING INTELLIGENCE TRACKER")
    print("Powered by Nansen CLI")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC")
    print("=" * 70)
    print()
    
    # Section 1: Gaming Token Performance
    print("🎮 GAMING TOKENS PERFORMANCE (24h)")
    print("-" * 70)
    gaming_tokens = get_gaming_tokens("ethereum", "24h", 10)
    if "data" in gaming_tokens and "data" in gaming_tokens["data"]:
        for i, token in enumerate(gaming_tokens["data"]["data"][:5], 1):
            symbol = token.get("token_symbol", "Unknown")
            volume = token.get("volume", 0)
            netflow = token.get("netflow", 0)
            price_change = token.get("price_change", 0) * 100
            market_cap = token.get("market_cap_usd", 0)
            
            flow_icon = "🟢" if netflow > 0 else "🔴"
            price_icon = "📈" if price_change > 0 else "📉"
            
            print(f"{i}. {symbol:10} {flow_icon} Vol: ${volume:,.0f} | Netflow: ${netflow:,.0f}")
            print(f"   {price_icon} Price: {price_change:+.2f}% | MC: ${market_cap:,.0f}")
            print()
    else:
        print("No gaming token data available (credits exhausted)")
        print()
    
    # Section 2: Smart Money into Gaming
    print("🐋 SMART MONEY FLOWS (Gaming/Gambling Exposure)")
    print("-" * 70)
    smart_money = get_smart_money_gaming("ethereum", 5)
    if "data" in smart_money and "data" in smart_money["data"]:
        for i, token in enumerate(smart_money["data"]["data"][:5], 1):
            symbol = token.get("token_symbol", "Unknown")
            netflow_30d = token.get("net_flow_30d_usd", 0)
            sectors = ", ".join(token.get("token_sectors", ["Unknown"]))
            
            # Filter for gaming-related sectors
            if any(keyword in sectors.lower() for keyword in ["game", "gamble", "bet", "nft", "metaverse"]):
                flow_icon = "🟢" if netflow_30d > 0 else "🔴"
                print(f"{i}. {symbol:15} {flow_icon} 30D Netflow: ${netflow_30d:,.0f}")
                print(f"   Sectors: {sectors}")
                print()
    else:
        print("No smart money data available")
        print()
    
    # Section 3: Perpetuals Sentiment (Gaming Assets)
    print("📈 PERPETUALS SENTIMENT (Gaming-Related)")
    print("-" * 70)
    perp_data = get_perp_gaming("ethereum", 10)
    if "data" in perp_data and "data" in perp_data["data"]:
        gaming_perps = [p for p in perp_data["data"]["data"] 
                       if any(kw in p.get("token_symbol", "").lower() 
                             for kw in ["game", "bet", "play", "nft", "meta"])]
        
        if gaming_perps:
            for i, perp in enumerate(gaming_perps[:5], 1):
                symbol = perp.get("token_symbol", "Unknown")
                volume = perp.get("volume", 0)
                funding = perp.get("funding", 0) * 100
                oi = perp.get("open_interest", 0)
                
                funding_icon = "🟢" if funding > 0 else "🔴"
                print(f"{i}. {symbol:15} {funding_icon} Funding: {funding:+.4f}%")
                print(f"   Volume: ${volume:,.0f} | OI: ${oi:,.0f}")
                print()
        else:
            print("No gaming-related perpetuals found")
            print()
    else:
        print("No perps data available")
        print()
    
    # Section 4: Competitor Token Watch
    print("🎯 COMPETITOR TOKEN WATCH")
    print("-" * 70)
    print("""
Key Gaming/Gambling Tokens to Monitor for Autobett:

1. AXS (Axie Infinity)     - P2E gaming pioneer
2. SAND (The Sandbox)      - Metaverse gaming platform
3. MANA (Decentraland)     - Virtual world gaming
4. IMX (Immutable X)       - Gaming NFT L2
5. GALA (Gala Games)       - Gaming ecosystem
6. BEAM (Beam)             - Gaming infrastructure
7. PRIME (Echelon Prime)   - Gaming token
8. PIXEL (Pixels)          - Social gaming

Monitor these for:
- Smart money accumulation (leading indicator)
- Volume spikes (increased interest)
- Price action relative to BTC/ETH
""")
    
    # Section 5: Actionable Intelligence for Autobett
    print("🎲 ACTIONABLE INTELLIGENCE FOR AUTOBETT")
    print("-" * 70)
    print("""
Based on on-chain gaming data and smart money flows:

1. MARKET TIMING: Watch gaming token flows as sentiment indicator
   - Positive netflow into AXS, SAND, IMX = bullish for gaming
   - Negative funding rates = bearish sentiment (wait for reversal)
   - Track correlation with BTC movements

2. USER ACQUISITION: Target wallets active in gaming tokens
   - Identify wallets holding 3+ gaming tokens
   - Track frequency of gaming token trades
   - Target high-frequency traders for Autobett beta

3. COMPETITOR WATCH: Monitor gaming protocol TVL
   - Set alerts for Axie, Gala, Beam TVL changes
   - Track smart money rotation between gaming protocols
   - Identify which gaming verticals are gaining traction

4. TOKENOMICS LEARNING: Study successful gaming tokens
   - Analyze token distribution for top performers
   - Watch vesting unlocks that caused price pressure
   - Learn from failed gaming token launches

5. CHAIN SELECTION: Monitor gaming activity by chain
   - Track which chains have highest gaming volume
   - Watch for emerging gaming L2s (consider Autobett deployment)
   - Monitor gas costs impact on gaming UX

NEXT ACTIONS:
- Set up daily gaming token flow monitoring
- Create alerts for smart money accumulation in gaming tokens
- Track competitor protocol metrics weekly
- Build wallet scoring system for user targeting
""")
    
    print("=" * 70)
    print("Built with @nansen_ai CLI for #NansenCLI challenge")
    print("By Mira, Autobett Growth | Autobett Gaming Platform")
    print("=" * 70)

if __name__ == "__main__":
    generate_report()
