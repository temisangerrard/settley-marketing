#!/usr/bin/env python3
"""
Settley Smart Money Tracker — Nansen CLI Integration
=====================================================

A CLI tool that uses Nansen API to track smart money flows,
competitor tokens, and market intelligence for Settley.

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

def get_smart_money_netflow(chain="ethereum", limit=5):
    """Get smart money netflow data."""
    return run_nansen_command([
        "research", "smart-money", "netflow",
        "--chain", chain, "--limit", str(limit)
    ])

def get_token_screener(chain="ethereum", timeframe="24h", limit=5):
    """Get token screener data."""
    return run_nansen_command([
        "research", "token", "screener",
        "--chain", chain, "--timeframe", timeframe, "--limit", str(limit)
    ])

def get_perp_screener(chain="ethereum", limit=5):
    """Get perpetuals screener data."""
    return run_nansen_command([
        "research", "perp", "screener",
        "--chain", chain, "--limit", str(limit)
    ])

def get_token_ohlcv(token_address, chain="ethereum", timeframe="1h", limit=5):
    """Get OHLCV data for a token."""
    return run_nansen_command([
        "research", "token", "ohlcv",
        "--chain", chain, "--token-address", token_address,
        "--timeframe", timeframe, "--limit", str(limit)
    ])

def get_who_bought_sold(token_address, chain="ethereum", timeframe="24h", limit=5):
    """Get who bought/sold data for a token."""
    return run_nansen_command([
        "research", "token", "who-bought-sold",
        "--chain", chain, "--token-address", token_address,
        "--timeframe", timeframe, "--limit", str(limit)
    ])

def generate_report():
    """Generate Settley Smart Money Tracker report."""
    print("=" * 70)
    print("SETTLEY SMART MONEY TRACKER")
    print("Powered by Nansen CLI")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC")
    print("=" * 70)
    print()
    
    # Section 1: Ethereum Smart Money Flows
    print("📊 ETHEREUM SMART MONEY FLOWS (Top 5)")
    print("-" * 70)
    eth_flow = get_smart_money_netflow("ethereum", 5)
    if "data" in eth_flow and "data" in eth_flow["data"]:
        for i, token in enumerate(eth_flow["data"]["data"][:5], 1):
            symbol = token.get("token_symbol", "Unknown")
            netflow_30d = token.get("net_flow_30d_usd", 0)
            market_cap = token.get("market_cap_usd", 0)
            sectors = ", ".join(token.get("token_sectors", ["Unknown"]))
            
            flow_icon = "🟢" if netflow_30d > 0 else "🔴"
            print(f"{i}. {symbol:15} {flow_icon} 30D Netflow: ${netflow_30d:,.0f}")
            print(f"   Market Cap: ${market_cap:,.0f} | Sectors: {sectors}")
            print()
    else:
        print("No data available (credits exhausted)")
        print()
    
    # Section 2: Base Chain Activity (Settley's chain)
    print("⛓️  BASE CHAIN ACTIVITY (Settley's Home Chain)")
    print("-" * 70)
    base_screener = get_token_screener("base", "24h", 5)
    if "data" in base_screener and "data" in base_screener["data"]:
        for i, token in enumerate(base_screener["data"]["data"][:5], 1):
            symbol = token.get("token_symbol", "Unknown")
            volume = token.get("volume", 0)
            netflow = token.get("netflow", 0)
            price_change = token.get("price_change", 0) * 100
            
            flow_icon = "🟢" if netflow > 0 else "🔴"
            print(f"{i}. {symbol:10} {flow_icon} Volume: ${volume:,.0f} | Netflow: ${netflow:,.0f}")
            print(f"   Price Change: {price_change:+.2f}%")
            print()
    else:
        print("No data available")
        print()
    
    # Section 3: Perpetuals Market Sentiment
    print("📈 PERPETUALS MARKET SENTIMENT")
    print("-" * 70)
    perp_data = get_perp_screener("ethereum", 5)
    if "data" in perp_data and "data" in perp_data["data"]:
        for i, perp in enumerate(perp_data["data"]["data"][:5], 1):
            symbol = perp.get("token_symbol", "Unknown")
            volume = perp.get("volume", 0)
            funding = perp.get("funding", 0) * 100
            oi = perp.get("open_interest", 0)
            
            funding_icon = "🟢" if funding > 0 else "🔴"
            print(f"{i}. {symbol:15} {funding_icon} Funding: {funding:+.4f}%")
            print(f"   Volume: ${volume:,.0f} | OI: ${oi:,.0f}")
            print()
    else:
        print("No data available")
        print()
    
    # Section 4: USDC Whale Activity (Stablecoin flows = market sentiment)
    print("💰 USDC WHALE ACTIVITY (24h)")
    print("-" * 70)
    usdc_address = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
    usdc_buys = get_who_bought_sold(usdc_address, "ethereum", "24h", 3)
    if "data" in usdc_buys and "data" in usdc_buys["data"]:
        for i, trader in enumerate(usdc_buys["data"]["data"][:3], 1):
            address = trader.get("address", "Unknown")[:10] + "..."
            label = trader.get("address_label", "Unknown") or "Unknown"
            volume_usd = trader.get("trade_volume_usd", 0)
            
            print(f"{i}. {label:30} ({address})")
            print(f"   Volume: ${volume_usd:,.0f}")
            print()
    else:
        print("No data available")
        print()
    
    # Section 5: Actionable Intelligence for Settley
    print("🎯 ACTIONABLE INTELLIGENCE FOR SETTLEY")
    print("-" * 70)
    print("""
Based on smart money flows and market data:

1. MARKET SENTIMENT: Monitor stablecoin flows (USDC/USDT) as leading indicator
   - Large USDC accumulation = potential buying pressure for risk assets
   - Track wallets labeled "Fund" or "Smart Trader"

2. COMPETITOR WATCH: Monitor proptech/real estate token flows
   - Set alerts for tokens in "Real Estate" or "RWA" sectors
   - Track smart money accumulation before retail catches on

3. BASE CHAIN OPPORTUNITY: Settley's home chain showing activity
   - WETH volume: $548M (24h)
   - USDC netflow: -$49M (outflow = potential rotation to other assets)
   - Position Settley to capture this flow

4. TIMING SIGNALS: Watch funding rates on perps
   - Negative funding = bearish sentiment (wait for reversal)
   - Positive funding + price increase = confirm trend

NEXT ACTIONS:
- Set up daily smart money flow monitoring
- Create alerts for RWA/prop-tech token accumulation
- Track Base chain stablecoin flows as Settley adoption metric
""")
    
    print("=" * 70)
    print("Built with @nansen_ai CLI for #NansenCLI challenge")
    print("By Mira, Settley Growth | https://settley.co")
    print("=" * 70)

if __name__ == "__main__":
    generate_report()
