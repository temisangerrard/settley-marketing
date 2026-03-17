#!/usr/bin/env node

/**
 * Email Subject Line Analyzer
 * 
 * Analyzes subject lines for effectiveness and provides actionable feedback.
 * Usage: node scripts/analyze-subject-line.js "Your subject line here"
 */

const subjectLine = process.argv.slice(2).join(' ');

if (!subjectLine) {
  console.log('Usage: node analyze-subject-line.js "Your subject line here"');
  console.log('\nAnalyzes subject lines for:');
  console.log('- Length (optimal: 40-60 characters)');
  console.log('- Clarity and specificity');
  console.log('- Curiosity factor');
  console.log('- Spam trigger words');
  console.log('- Personalization');
  console.log('- Urgency (genuine vs. fake)');
  process.exit(1);
}

// Analysis functions
function analyzeSubjectLine(subject) {
  const results = {
    score: 100,
    issues: [],
    suggestions: [],
    metrics: {},
    pattern: null
  };

  // Length check
  const length = subject.length;
  results.metrics.length = length;
  
  if (length > 60) {
    results.issues.push(`Too long (${length} chars) — may get cut off in mobile inboxes`);
    results.suggestions.push('Shorten to 40-60 characters for optimal display');
    results.score -= 15;
  } else if (length < 20) {
    results.issues.push(`Too short (${length} chars) — may lack context`);
    results.suggestions.push('Add more specificity (target 40-60 characters)');
    results.score -= 10;
  } else if (length <= 40) {
    results.suggestions.push('Great length for mobile!');
    results.score += 5;
  }

  // Check for spam trigger words
  const spamWords = [
    'free', 'buy now', 'act now', 'limited time', 'urgent', 'guarantee',
    'no risk', 'cash', 'discount', 'special offer', 'winner', 'congratulations',
    '!!!', '???', 'CLICK HERE', 'ORDER NOW', 'APPLY NOW'
  ];
  
  const lowerSubject = subject.toLowerCase();
  const spamCount = spamWords.filter(word => lowerSubject.includes(word.toLowerCase())).length;
  
  if (spamCount > 0) {
    results.issues.push(`Contains ${spamCount} spam trigger word(s)`);
    results.suggestions.push('Replace with benefit-driven language (avoid hype)');
    results.score -= spamCount * 10;
  }

  // Check for personalization
  const hasName = /\b[A-Z][a-z]+\b/.test(subject) && subject.length > 15;
  const hasYou = /\byou\b|\byour\b/i.test(subject);
  
  if (hasName || hasYou) {
    results.suggestions.push('Good personalization!');
    results.score += 5;
  } else {
    results.issues.push('No personalization detected');
    results.suggestions.push('Add recipient name or "you/your" for relevance');
  }

  // Check for numbers (specificity indicator)
  const hasNumbers = /\d+/.test(subject);
  
  if (hasNumbers) {
    results.suggestions.push('Numbers add specificity — good!');
    results.score += 5;
  } else {
    results.issues.push('No numbers — could add specificity');
    results.suggestions.push('Consider adding numbers (e.g., "3 ways", "10 minutes", "£100")');
  }

  // Check for question format
  const isQuestion = subject.trim().endsWith('?');
  
  if (isQuestion) {
    results.pattern = 'Question';
    results.suggestions.push('Question format can boost engagement');
    results.score += 5;
  }

  // Check for how-to format
  if (lowerSubject.startsWith('how to')) {
    results.pattern = 'How-To';
    results.suggestions.push('How-to format performs well for educational content');
    results.score += 5;
  }

  // Check for urgency (genuine vs. fake)
  const urgencyWords = ['now', 'today', 'hours', 'deadline', 'ends', 'last chance'];
  const hasUrgency = urgencyWords.some(word => lowerSubject.includes(word));
  
  if (hasUrgency) {
    results.pattern = 'Urgency';
    // Check if it seems genuine (has specific time)
    const hasSpecificTime = /\d+\s*(hours?|days?|minutes?)/i.test(subject);
    
    if (hasSpecificTime) {
      results.suggestions.push('Specific urgency (good) — feels genuine');
      results.score += 5;
    } else {
      results.issues.push('Urgency without specificity (may feel manipulative)');
      results.suggestions.push('Add specific deadline (e.g., "24 hours" not "now")');
      results.score -= 5;
    }
  }

  // Check for clarity (no vague words)
  const vagueWords = ['update', 'information', 'announcement', 'news', 'something'];
  const vagueCount = vagueWords.filter(word => lowerSubject.includes(word)).length;
  
  if (vagueCount > 0) {
    results.issues.push(`Vague language detected (${vagueCount} words)`);
    results.suggestions.push('Be specific about what\'s inside (avoid "update", "news", etc.)');
    results.score -= 15;
  }

  // Check for benefit
  const benefitWords = ['earn', 'save', 'get', 'achieve', 'build', 'grow', 'learn', 'discover'];
  const hasBenefit = benefitWords.some(word => lowerSubject.includes(word));
  
  if (hasBenefit) {
    results.suggestions.push('Benefit-driven language — good!');
    results.score += 5;
  } else {
    results.issues.push('No clear benefit stated');
    results.suggestions.push('Lead with what they get (not what you\'re sending)');
  }

  // Check for curiosity gap
  const curiosityPatterns = [
    /the \w+ about/i,
    /what \w+ don't/i,
    /why \w+/i,
    /surprising/i,
    /mistake/i
  ];
  
  const hasCuriosity = curiosityPatterns.some(pattern => pattern.test(subject));
  
  if (hasCuriosity) {
    results.pattern = 'Curiosity';
    results.suggestions.push('Curiosity gap can boost opens (ensure email delivers)');
    results.score += 5;
  }

  // Ensure score doesn't go below 0
  results.score = Math.max(0, results.score);

  // Add overall assessment
  if (results.score >= 80) {
    results.assessment = 'Strong subject line — ready to send';
  } else if (results.score >= 60) {
    results.assessment = 'Good, but could be improved';
  } else if (results.score >= 40) {
    results.assessment = 'Needs revision before sending';
  } else {
    results.assessment = 'Weak — rewrite recommended';
  }

  return results;
}

// Run analysis
const analysis = analyzeSubjectLine(subjectLine);

// Output results
console.log('\n=== SUBJECT LINE ANALYSIS ===\n');
console.log(`Subject: "${subjectLine}"`);
console.log(`Length: ${analysis.metrics.length} characters`);
console.log(`Pattern: ${analysis.pattern || 'Mixed/Other'}`);
console.log(`\nOverall Score: ${analysis.score}/100`);
console.log(`Assessment: ${analysis.assessment}\n`);

if (analysis.issues.length > 0) {
  console.log('ISSUES FOUND:');
  analysis.issues.forEach((issue, i) => {
    console.log(`  ${i + 1}. ${issue}`);
  });
  console.log('');
}

if (analysis.suggestions.length > 0) {
  console.log('SUGGESTIONS:');
  analysis.suggestions.forEach((suggestion, i) => {
    console.log(`  ${i + 1}. ${suggestion}`);
  });
  console.log('');
}

console.log('=== END ANALYSIS ===\n');

// Exit with appropriate code
process.exit(analysis.score >= 70 ? 0 : 1);
