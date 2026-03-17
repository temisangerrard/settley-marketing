#!/usr/bin/env node

const { CoinGeckoClient } = require('coingecko-api-v3');

const client = new CoinGeckoClient({
  timeout: 10000,
  autoRetry: true,
});

async function getPrice(coinId = 'bitcoin') {
  try {
    const price = await client.price({
      ids: [coinId],
      vs_currencies: ['usd', 'eur', 'gbp'],
      include_24hr_vol: true,
      include_24hr_change: true,
    });
    console.log(JSON.stringify(price, null, 2));
  } catch (error) {
    console.error('Error fetching price:', error.message);
    process.exit(1);
  }
}

async function getTrending() {
  try {
    const trending = await client.trending();
    console.log(JSON.stringify(trending, null, 2));
  } catch (error) {
    console.error('Error fetching trending:', error.message);
    process.exit(1);
  }
}

// Main
const command = process.argv[2] || 'price';
const coinId = process.argv[3] || 'bitcoin';

if (command === 'price') {
  getPrice(coinId);
} else if (command === 'trending') {
  getTrending();
} else {
  console.log('Usage: coingecko-price [price|trending] [coin-id]');
  console.log('Examples:');
  console.log('  coingecko-price price bitcoin');
  console.log('  coingecko-price price ethereum');
  console.log('  coingecko-price trending');
}
