#!/usr/bin/env node

/**
 * GitHub PR Status Checker
 * 
 * Analyzes a PR for readiness and provides actionable feedback.
 * Usage: node scripts/check-pr-status.js <pr-number>
 * 
 * Requires: gh CLI installed and authenticated
 */

const { execSync } = require('child_process');

const prNumber = process.argv[2];

if (!prNumber) {
  console.log('Usage: node check-pr-status.js <pr-number>');
  console.log('\nAnalyzes PR for:');
  console.log('- Title clarity and descriptiveness');
  console.log('- Issue linkage');
  console.log('- Reviewer assignment');
  console.log('- CI status');
  console.log('- Branch age');
  console.log('- Merge conflicts');
  console.log('- Commit message quality');
  process.exit(1);
}

// Helper to run gh CLI commands
function runGhCommand(args) {
  try {
    const output = execSync(`gh ${args}`, { encoding: 'utf8' });
    return JSON.parse(output);
  } catch (error) {
    console.error(`Error running gh ${args}:`, error.message);
    process.exit(1);
  }
}

// Analyze PR
async function analyzePR(prNum) {
  const results = {
    score: 100,
    issues: [],
    suggestions: [],
    metrics: {},
    ready: true
  };

  console.log(`\n=== Analyzing PR #${prNum} ===\n`);

  // Fetch PR details
  const pr = runGhCommand(`pr view ${prNum} --json title,body,author,reviewers,assignees,labels,commits,mergeable,headRefName,baseRefName,state`);
  
  // Check title quality
  const title = pr.title;
  results.metrics.titleLength = title.length;
  
  if (title.length < 10) {
    results.issues.push(`Title too short (${title.length} chars)`);
    results.suggestions.push('Add more context (what was fixed/changed)');
    results.score -= 15;
  } else if (title.length > 80) {
    results.issues.push(`Title too long (${title.length} chars)`);
    results.suggestions.push('Shorten to < 80 characters');
    results.score -= 10;
  }
  
  // Check for issue reference in title
  const hasIssueRef = /#\d+|fixes|closes|resolves/i.test(title);
  if (!hasIssueRef) {
    results.issues.push('No issue reference in title');
    results.suggestions.push('Add issue number (e.g., "Fix: Auth timeout #123")');
    results.score -= 5;
  }

  // Check body/description
  const body = pr.body || '';
  results.metrics.bodyLength = body.length;
  
  if (body.length < 50) {
    results.issues.push('PR description too short');
    results.suggestions.push('Add context: what changed, why, how tested');
    results.score -= 20;
  }
  
  // Check for issue linkage in body
  const hasFixesKeyword = /fixes #\d+|closes #\d+|resolves #\d+/i.test(body);
  if (!hasFixesKeyword && !hasIssueRef) {
    results.issues.push('No issue linkage (Fixes #123)');
    results.suggestions.push('Add "Fixes #<number>" to auto-close issue');
    results.score -= 10;
  }

  // Check reviewers
  const reviewers = pr.reviewers || [];
  results.metrics.reviewersCount = reviewers.length;
  
  if (reviewers.length === 0) {
    results.issues.push('No reviewers assigned');
    results.suggestions.push('Add 1-2 reviewers (@username)');
    results.score -= 15;
  } else if (reviewers.length === 1) {
    results.suggestions.push('Consider adding 2nd reviewer for important changes');
  }

  // Check assignees
  const assignees = pr.assignees || [];
  results.metrics.assigneesCount = assignees.length;
  
  if (assignees.length === 0) {
    results.issues.push('No assignees');
    results.suggestions.push('Assign yourself or relevant team member');
    results.score -= 5;
  }

  // Check labels
  const labels = pr.labels || [];
  results.metrics.labelsCount = labels.length;
  
  if (labels.length === 0) {
    results.issues.push('No labels');
    results.suggestions.push('Add labels (bug, feature, enhancement, etc.)');
    results.score -= 5;
  }

  // Check mergeability
  if (pr.mergeable === 'CONFLICTING') {
    results.issues.push('MERGE CONFLICTS detected');
    results.suggestions.push('Rebase on latest main and resolve conflicts');
    results.score -= 30;
    results.ready = false;
  } else if (pr.mergeable === 'UNKNOWN') {
    results.suggestions.push('Merge status unknown (may need refresh)');
  }

  // Check branch age (commits)
  const commits = pr.commits || [];
  results.metrics.commitsCount = commits.length;
  
  if (commits.length > 20) {
    results.issues.push(`Too many commits (${commits.length})`);
    results.suggestions.push('Consider squashing or breaking into smaller PRs');
    results.score -= 10;
  }

  // Check commit messages
  const hasWIP = commits.some(c => /wip|work in progress|temp|fixme/i.test(c.messageHeadline));
  if (hasWIP && pr.state !== 'DRAFT') {
    results.issues.push('Contains WIP/temp commits but PR is not draft');
    results.suggestions.push('Squash WIP commits or mark as draft');
    results.score -= 15;
  }

  // Check for conventional commits
  const conventionalPattern = /^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?:/;
  const hasConventionalCommits = commits.some(c => conventionalPattern.test(c.messageHeadline));
  
  if (!hasConventionalCommits && commits.length > 0) {
    results.suggestions.push('Consider using conventional commits (feat:, fix:, etc.)');
  }

  // Check CI status (requires additional API call)
  try {
    const checks = runGhCommand(`pr checks ${prNum} --json name,status`);
    const failedChecks = checks.filter(c => c.status === 'FAILED');
    const pendingChecks = checks.filter(c => c.status === 'PENDING');
    
    results.metrics.ciTotal = checks.length;
    results.metrics.ciFailed = failedChecks.length;
    results.metrics.ciPending = pendingChecks.length;
    
    if (failedChecks.length > 0) {
      results.issues.push(`${failedChecks.length} CI check(s) failing`);
      results.suggestions.push('Fix failing checks before merging');
      results.score -= 25;
      results.ready = false;
    }
    
    if (pendingChecks.length > 0) {
      results.suggestions.push(`${pendingChecks.length} CI check(s) still running`);
    }
  } catch (error) {
    results.suggestions.push('Could not fetch CI status (run gh pr checks manually)');
  }

  // Ensure score doesn't go below 0
  results.score = Math.max(0, results.score);

  // Add overall assessment
  if (results.score >= 90) {
    results.assessment = 'Excellent - ready to merge';
  } else if (results.score >= 75) {
    results.assessment = 'Good - minor improvements suggested';
  } else if (results.score >= 60) {
    results.assessment = 'Needs work before merging';
  } else {
    results.assessment = 'Not ready - address issues first';
  }

  return results;
}

// Run analysis
analyzePR(prNumber)
  .then(analysis => {
    // Output results
    console.log(`Title: "${analysis.metrics.titleLength} chars"`);
    console.log(`Description: ${analysis.metrics.bodyLength} chars`);
    console.log(`Reviewers: ${analysis.metrics.reviewersCount}`);
    console.log(`Assignees: ${analysis.metrics.assigneesCount}`);
    console.log(`Labels: ${analysis.metrics.labelsCount}`);
    console.log(`Commits: ${analysis.metrics.commitsCount}`);
    if (analysis.metrics.ciTotal) {
      console.log(`CI Status: ${analysis.metrics.ciFailed || 0} failing, ${analysis.metrics.ciPending || 0} pending`);
    }
    
    console.log(`\nOverall Score: ${analysis.score}/100`);
    console.log(`Assessment: ${analysis.assessment}`);
    console.log(`Ready to Merge: ${analysis.ready ? '✅ Yes' : '❌ No'}\n`);

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
    process.exit(analysis.ready ? 0 : 1);
  })
  .catch(error => {
    console.error('Error analyzing PR:', error.message);
    process.exit(1);
  });
