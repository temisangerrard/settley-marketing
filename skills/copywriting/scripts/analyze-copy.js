#!/usr/bin/env node

/**
 * Copywriting Quality Analyzer
 * 
 * Analyzes copy for common issues and provides actionable feedback.
 * Usage: node scripts/analyze-copy.js "Your copy here"
 */

const copy = process.argv.slice(2).join(' ');

if (!copy) {
  console.log('Usage: node analyze-copy.js "Your copy text here"');
  console.log('\nAnalyzes copy for:');
  console.log('- Feature vs. benefit ratio');
  console.log('- Jargon detection');
  console.log('- Hedging language');
  console.log('- CTA clarity');
  console.log('- Readability score');
  process.exit(1);
}

// Analysis functions
function analyzeCopy(text) {
  const results = {
    score: 100,
    issues: [],
    suggestions: [],
    metrics: {}
  };

  // Check for hedging language
  const hedgingWords = ['believe', 'think', 'possibly', 'maybe', 'might', 'could', 'would', 'should', 'try', 'attempt'];
  const hedgingCount = hedgingWords.filter(word => text.toLowerCase().includes(word)).length;
  
  if (hedgingCount > 0) {
    results.issues.push(`Found ${hedgingCount} hedging words (weakens confidence)`);
    results.suggestions.push('Replace hedging with confident, direct language');
    results.score -= hedgingCount * 5;
  }

  // Check for vague superlatives
  const vagueWords = ['industry-leading', 'best-in-class', 'cutting-edge', 'innovative', 'revolutionary', 'game-changing'];
  const vagueCount = vagueWords.filter(word => text.toLowerCase().includes(word)).length;
  
  if (vagueCount > 0) {
    results.issues.push(`Found ${vagueCount} vague superlatives (lacks proof)`);
    results.suggestions.push('Replace with specific numbers, data, or customer proof');
    results.score -= vagueCount * 10;
  }

  // Check for jargon
  const jargonWords = ['blockchain', 'tokenization', 'ERC-20', 'SPV', 'DeFi', 'Web3', 'synergy', 'paradigm', 'leverage'];
  const jargonCount = jargonWords.filter(word => text.toLowerCase().includes(word)).length;
  
  if (jargonCount > 0) {
    results.issues.push(`Found ${jargonCount} jargon terms (may confuse readers)`);
    results.suggestions.push('Explain jargon or replace with simple language');
    results.score -= jargonCount * 3;
  }

  // Check for benefits vs. features
  const benefitIndicators = ['you', 'your', 'save', 'earn', 'get', 'gain', 'achieve', 'result', 'outcome'];
  const featureIndicators = ['we', 'our', 'platform', 'system', 'technology', 'feature', 'uses', 'includes'];
  
  const benefitCount = benefitIndicators.filter(word => text.toLowerCase().includes(word)).length;
  const featureCount = featureIndicators.filter(word => text.toLowerCase().includes(word)).length;
  
  if (featureCount > benefitCount * 2) {
    results.issues.push(`Feature-heavy copy (${featureCount} features vs. ${benefitCount} benefits)`);
    results.suggestions.push('Convert features to benefits: "What does this do for the customer?"');
    results.score -= 15;
  }

  // Check for social proof
  const proofIndicators = ['users', 'customers', 'members', '%', 'converted', 'rate', 'testimonial', 'review', 'star'];
  const proofCount = proofIndicators.filter(word => text.toLowerCase().includes(word)).length;
  
  if (proofCount === 0) {
    results.issues.push('No social proof detected');
    results.suggestions.push('Add user counts, conversion rates, testimonials, or case studies');
    results.score -= 10;
  }

  // Check for risk disclosure
  const riskIndicators = ['risk', 'lose', 'capital', 'volatile', 'caution', 'warning', 'disclosure'];
  const riskCount = riskIndicators.filter(word => text.toLowerCase().includes(word)).length;
  
  if (riskCount === 0 && text.toLowerCase().includes('invest')) {
    results.issues.push('Investment copy without risk disclosure');
    results.suggestions.push('Add clear risk disclosure (required for compliance)');
    results.score -= 20;
  }

  // Check readability (simple heuristic)
  const sentences = text.split(/[.!?]+/).filter(s => s.trim().length > 0);
  const avgSentenceLength = sentences.reduce((acc, s) => acc + s.split(' ').length, 0) / sentences.length;
  
  if (avgSentenceLength > 25) {
    results.issues.push(`Long sentences (avg ${avgSentenceLength.toFixed(1)} words)`);
    results.suggestions.push('Break into shorter sentences (target 15-20 words)');
    results.score -= 10;
  }

  // Check for CTA
  const ctaIndicators = ['click', 'join', 'sign up', 'get started', 'learn more', 'buy', 'subscribe', 'download'];
  const hasCTA = ctaIndicators.some(word => text.toLowerCase().includes(word));
  
  if (!hasCTA) {
    results.issues.push('No clear call-to-action detected');
    results.suggestions.push('Add ONE primary CTA that tells readers what to do next');
    results.score -= 15;
  }

  // Calculate metrics
  results.metrics = {
    wordCount: text.split(' ').length,
    sentenceCount: sentences.length,
    avgSentenceLength: avgSentenceLength.toFixed(1),
    hedgingWords: hedgingCount,
    vagueWords: vagueCount,
    jargonWords: jargonCount,
    benefitRatio: `${benefitCount}:${featureCount}`,
    socialProof: proofCount,
    riskDisclosure: riskCount
  };

  // Ensure score doesn't go below 0
  results.score = Math.max(0, results.score);

  return results;
}

// Run analysis
const analysis = analyzeCopy(copy);

// Output results
console.log('\n=== COPY ANALYSIS RESULTS ===\n');
console.log(`Overall Score: ${analysis.score}/100\n`);

console.log('METRICS:');
Object.entries(analysis.metrics).forEach(([key, value]) => {
  console.log(`  ${key}: ${value}`);
});

if (analysis.issues.length > 0) {
  console.log('\nISSUES FOUND:');
  analysis.issues.forEach((issue, i) => {
    console.log(`  ${i + 1}. ${issue}`);
  });
}

if (analysis.suggestions.length > 0) {
  console.log('\nSUGGESTIONS:');
  analysis.suggestions.forEach((suggestion, i) => {
    console.log(`  ${i + 1}. ${suggestion}`);
  });
}

console.log('\n=== END ANALYSIS ===\n');

// Exit with appropriate code
process.exit(analysis.score >= 70 ? 0 : 1);
