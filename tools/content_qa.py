#!/usr/bin/env python3
"""
Settley Article Content QA Tool

Checks article content for:
1. Duplicate text from past articles
2. Brand voice and tone compliance
3. Required elements (CTA, disclaimers, etc.)
4. SEO best practices
5. Target market alignment (UK/US focus)

Usage:
    python tools/content_qa.py check <article_path>
    python tools/content_qa.py scan <content_folder>
    python tools/content_qa.py compare <article1> <article2>
"""

import os
import sys
import re
import json
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from collections import Counter

# ============================================================================
# BRAND GUIDELINES
# ============================================================================

BRAND_GUIDELINES = {
    "voice": {
        "tone": [
            "direct",
            "confident", 
            "educational",
            "no_hype"
        ],
        "avoid": [
            "revolutionary",
            "game-changing",
            "unprecedented",
            "amazing",
            "incredible",
            "best-in-class",
            "world-class"
        ],
        "prefer": [
            "clear",
            "proven",
            "transparent",
            "verified"
        ]
    },
    "required_elements": {
        "cta": {
            "required": True,
            "patterns": [
                r"(get started|join now|sign up|create account|start investing)",
                r"(learn more|read more|discover how)",
                r"(try settley|join settley|become a member)"
            ]
        },
        "disclaimer": {
            "required": True,
            "patterns": [
                r"(not financial advice|for informational purposes|do your own research)",
                r"(investment involves risk|capital at risk|past performance)"
            ]
        },
        "target_market_mention": {
            "required": False,
            "preferred": True,
            "patterns": [
                r"(UK|United Kingdom|London|Manchester|Birmingham)",
                r"(US|United States|America|New York|Miami|Austin)"
            ]
        }
    },
    "seo": {
        "title_length": {
            "min": 30,
            "max": 60,
            "optimal": 50
        },
        "meta_description": {
            "min": 120,
            "max": 160
        },
        "keyword_density": {
            "min": 0.5,
            "max": 2.5
        }
    },
    "content_quality": {
        "min_word_count": 800,
        "max_sentence_length": 35,
        "paragraph_max_sentences": 5
    }
}

# ============================================================================
# DATA CLASSES
# ============================================================================

@dataclass
class QAIssue:
    severity: str  # "critical", "warning", "info"
    category: str  # "duplicate", "brand", "seo", "quality"
    message: str
    location: Optional[str] = None
    suggestion: Optional[str] = None

@dataclass
class QAReport:
    article_path: str
    word_count: int
    issues: List[QAIssue] = field(default_factory=list)
    duplicate_matches: List[Dict] = field(default_factory=list)
    brand_score: float = 0.0
    seo_score: float = 0.0
    quality_score: float = 0.0
    overall_score: float = 0.0
    passed: bool = False

# ============================================================================
# DUPLICATE DETECTION
# ============================================================================

class DuplicateDetector:
    def __init__(self, content_folder: str = "content/articles"):
        self.content_folder = Path(content_folder)
        self.article_cache: Dict[str, str] = {}
        self.ngram_index: Dict[str, List[str]] = {}
        
    def load_articles(self) -> List[str]:
        """Load all articles from content folder."""
        articles = []
        if self.content_folder.exists():
            for ext in ["*.md", "*.txt"]:
                articles.extend(self.content_folder.glob(ext))
        return [str(a) for a in articles]
    
    def extract_text(self, file_path: str) -> str:
        """Extract clean text from article (remove markdown, headers, etc.)."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove markdown formatting
            text = re.sub(r'#{1,6}\s+', '', content)  # Headers
            text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # Bold
            text = re.sub(r'\*([^*]+)\*', r'\1', text)  # Italic
            text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # Links
            text = re.sub(r'`([^`]+)`', r'\1', text)  # Code
            text = re.sub(r'```[\s\S]*?```', '', text)  # Code blocks
            
            # Remove frontmatter
            if text.startswith('---'):
                text = re.sub(r'---[\s\S]*?---', '', text, count=1)
            
            return text.strip()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return ""
    
    def create_ngrams(self, text: str, n: int = 5) -> List[str]:
        """Create word n-grams for comparison."""
        words = re.findall(r'\b\w+\b', text.lower())
        return [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]
    
    def index_article(self, file_path: str):
        """Index an article for duplicate detection."""
        text = self.extract_text(file_path)
        self.article_cache[file_path] = text
        
        ngrams = self.create_ngrams(text, n=5)
        for ngram in ngrams:
            if ngram not in self.ngram_index:
                self.ngram_index[ngram] = []
            self.ngram_index[ngram].append(file_path)
    
    def check_duplicates(self, file_path: str, threshold: float = 0.7) -> List[Dict]:
        """
        Check for duplicate content against indexed articles.
        Returns list of matches with similarity scores.
        """
        if file_path not in self.article_cache:
            self.index_article(file_path)
        
        text = self.article_cache[file_path]
        ngrams = self.create_ngrams(text, n=5)
        
        if not ngrams:
            return []
        
        # Count overlapping n-grams with other articles
        overlap_counts = Counter()
        for ngram in ngrams:
            if ngram in self.ngram_index:
                for other_file in self.ngram_index[ngram]:
                    if other_file != file_path:
                        overlap_counts[other_file] += 1
        
        # Calculate similarity scores
        matches = []
        total_ngrams = len(ngrams)
        
        for other_file, overlap in overlap_counts.items():
            if other_file not in self.article_cache:
                self.index_article(other_file)
            
            other_ngrams = len(self.create_ngrams(self.article_cache[other_file], n=5))
            
            if other_ngrams == 0:
                continue
            
            # Jaccard-like similarity
            similarity = overlap / max(total_ngrams, other_ngrams)
            
            if similarity >= threshold:
                matches.append({
                    "file": other_file,
                    "similarity": round(similarity, 3),
                    "overlapping_ngrams": overlap,
                    "total_ngrams": total_ngrams
                })
        
        return sorted(matches, key=lambda x: x["similarity"], reverse=True)

# ============================================================================
# BRAND COMPLIANCE CHECKER
# ============================================================================

class BrandComplianceChecker:
    def __init__(self):
        self.guidelines = BRAND_GUIDELINES
    
    def check_voice(self, text: str) -> List[QAIssue]:
        """Check for brand voice compliance."""
        issues = []
        text_lower = text.lower()
        
        # Check for avoided words
        for word in self.guidelines["voice"]["avoid"]:
            pattern = r'\b' + re.escape(word) + r'\b'
            matches = re.finditer(pattern, text_lower, re.IGNORECASE)
            for match in matches:
                issues.append(QAIssue(
                    severity="warning",
                    category="brand",
                    message=f"Avoid hype word: '{word}'",
                    location=f"Position {match.start()}",
                    suggestion=f"Replace with clearer, more direct language"
                ))
        
        # Check for preferred words (positive reinforcement)
        preferred_count = sum(
            len(re.findall(r'\b' + re.escape(word) + r'\b', text_lower))
            for word in self.guidelines["voice"]["prefer"]
        )
        
        if preferred_count == 0 and len(text) > 500:
            issues.append(QAIssue(
                severity="info",
                category="brand",
                message="Consider using more brand-aligned language",
                suggestion="Words like 'clear', 'proven', 'transparent' align with Settley voice"
            ))
        
        return issues
    
    def check_required_elements(self, text: str, file_path: str) -> List[QAIssue]:
        """Check for required article elements."""
        issues = []
        
        # CTA check
        cta_config = self.guidelines["required_elements"]["cta"]
        if cta_config["required"]:
            has_cta = any(
                re.search(pattern, text, re.IGNORECASE)
                for pattern in cta_config["patterns"]
            )
            if not has_cta:
                issues.append(QAIssue(
                    severity="critical",
                    category="brand",
                    message="Missing call-to-action (CTA)",
                    location=file_path,
                    suggestion="Add a clear CTA: 'Get started', 'Join now', or 'Learn more'"
                ))
        
        # Disclaimer check
        disclaimer_config = self.guidelines["required_elements"]["disclaimer"]
        if disclaimer_config["required"]:
            has_disclaimer = any(
                re.search(pattern, text, re.IGNORECASE)
                for pattern in disclaimer_config["patterns"]
            )
            if not has_disclaimer:
                issues.append(QAIssue(
                    severity="critical",
                    category="brand",
                    message="Missing legal disclaimer",
                    location=file_path,
                    suggestion="Add: 'This is not financial advice. Investment involves risk.'"
                ))
        
        # Target market mention (preferred)
        market_config = self.guidelines["required_elements"]["target_market_mention"]
        if market_config.get("preferred", False):
            has_market_mention = any(
                re.search(pattern, text, re.IGNORECASE)
                for pattern in market_config["patterns"]
            )
            if not has_market_mention and len(text) > 1000:
                issues.append(QAIssue(
                    severity="info",
                    category="brand",
                    message="No mention of target markets (UK/US)",
                    location=file_path,
                    suggestion="Mention UK/US markets to reinforce geographic focus"
                ))
        
        return issues
    
    def calculate_brand_score(self, issues: List[QAIssue]) -> float:
        """Calculate brand compliance score (0-100)."""
        if not issues:
            return 100.0
        
        # Weight by severity
        severity_weights = {"critical": 25, "warning": 10, "info": 3}
        total_deduction = sum(
            severity_weights.get(issue.severity, 0)
            for issue in issues
            if issue.category == "brand"
        )
        
        return max(0, 100 - total_deduction)

# ============================================================================
# SEO CHECKER
# ============================================================================

class SEOChecker:
    def __init__(self):
        self.guidelines = BRAND_GUIDELINES["seo"]
    
    def check_article(self, text: str, title: str = "") -> List[QAIssue]:
        """Check SEO best practices."""
        issues = []
        
        # Title length
        if title:
            title_len = len(title)
            if title_len < self.guidelines["title_length"]["min"]:
                issues.append(QAIssue(
                    severity="warning",
                    category="seo",
                    message=f"Title too short ({title_len} chars)",
                    suggestion=f"Aim for {self.guidelines['title_length']['min']}-{self.guidelines['title_length']['max']} characters"
                ))
            elif title_len > self.guidelines["title_length"]["max"]:
                issues.append(QAIssue(
                    severity="warning",
                    category="seo",
                    message=f"Title too long ({title_len} chars)",
                    suggestion=f"Keep under {self.guidelines['title_length']['max']} characters for search results"
                ))
        
        # Word count
        word_count = len(text.split())
        min_words = self.guidelines["content_quality"]["min_word_count"]
        if word_count < min_words:
            issues.append(QAIssue(
                severity="warning",
                category="seo",
                message=f"Article too short ({word_count} words)",
                suggestion=f"Aim for at least {min_words} words for SEO"
            ))
        
        return issues
    
    def calculate_seo_score(self, issues: List[QAIssue], word_count: int) -> float:
        """Calculate SEO score (0-100)."""
        base_score = 100.0
        
        # Deduct for issues
        for issue in issues:
            if issue.category == "seo":
                if issue.severity == "critical":
                    base_score -= 20
                elif issue.severity == "warning":
                    base_score -= 10
                else:
                    base_score -= 5
        
        # Bonus for good word count
        min_words = self.guidelines["content_quality"]["min_word_count"]
        if word_count >= min_words * 1.5:
            base_score = min(100, base_score + 5)
        
        return max(0, base_score)

# ============================================================================
# QUALITY CHECKER
# ============================================================================

class QualityChecker:
    def __init__(self):
        self.guidelines = BRAND_GUIDELINES["content_quality"]
    
    def check_article(self, text: str) -> List[QAIssue]:
        """Check content quality metrics."""
        issues = []
        
        # Sentence length
        sentences = re.split(r'[.!?]+', text)
        for i, sentence in enumerate(sentences):
            words = sentence.split()
            if len(words) > self.guidelines["max_sentence_length"]:
                issues.append(QAIssue(
                    severity="info",
                    category="quality",
                    message=f"Sentence {i+1} is too long ({len(words)} words)",
                    suggestion="Break into shorter sentences for readability"
                ))
        
        # Paragraph structure
        paragraphs = text.split('\n\n')
        for i, para in enumerate(paragraphs):
            para_sentences = len(re.split(r'[.!?]+', para))
            if para_sentences > self.guidelines["paragraph_max_sentences"]:
                issues.append(QAIssue(
                    severity="info",
                    category="quality",
                    message=f"Paragraph {i+1} has too many sentences ({para_sentences})",
                    suggestion="Break into smaller paragraphs"
                ))
        
        return issues
    
    def calculate_quality_score(self, issues: List[QAIssue], word_count: int) -> float:
        """Calculate quality score (0-100)."""
        base_score = 100.0
        
        # Word count bonus/penalty
        min_words = self.guidelines["min_word_count"]
        if word_count < min_words:
            base_score -= 20
        elif word_count >= min_words * 2:
            base_score += 5
        
        # Deduct for quality issues (capped)
        quality_issues = [i for i in issues if i.category == "quality"]
        deduction = min(30, len(quality_issues) * 3)
        base_score -= deduction
        
        return max(0, base_score)

# ============================================================================
# MAIN QA TOOL
# ============================================================================

class ContentQATool:
    def __init__(self, content_folder: str = "content/articles"):
        self.duplicate_detector = DuplicateDetector(content_folder)
        self.brand_checker = BrandComplianceChecker()
        self.seo_checker = SEOChecker()
        self.quality_checker = QualityChecker()
        
        # Index existing articles
        self._index_existing_articles()
    
    def _index_existing_articles(self):
        """Index all existing articles for duplicate detection."""
        articles = self.duplicate_detector.load_articles()
        for article in articles:
            self.duplicate_detector.index_article(article)
    
    def check_article(self, file_path: str) -> QAReport:
        """Run full QA check on an article."""
        # Extract text
        text = self.duplicate_detector.extract_text(file_path)
        if not text:
            return QAReport(
                article_path=file_path,
                word_count=0,
                issues=[QAIssue("critical", "quality", "Could not read article")],
                passed=False
            )
        
        word_count = len(text.split())
        all_issues = []
        
        # 1. Duplicate detection
        duplicates = self.duplicate_detector.check_duplicates(file_path)
        for dup in duplicates:
            if dup["similarity"] > 0.8:
                all_issues.append(QAIssue(
                    severity="critical",
                    category="duplicate",
                    message=f"High similarity ({dup['similarity']*100:.0f}%) with {Path(dup['file']).name}",
                    suggestion="Rewrite to ensure original content"
                ))
            elif dup["similarity"] > 0.5:
                all_issues.append(QAIssue(
                    severity="warning",
                    category="duplicate",
                    message=f"Moderate similarity ({dup['similarity']*100:.0f}%) with {Path(dup['file']).name}",
                    suggestion="Review and differentiate content"
                ))
        
        # 2. Brand compliance
        brand_issues = self.brand_checker.check_voice(text)
        brand_issues.extend(self.brand_checker.check_required_elements(text, file_path))
        all_issues.extend(brand_issues)
        brand_score = self.brand_checker.calculate_brand_score(brand_issues)
        
        # 3. SEO check
        title = self._extract_title(text)
        seo_issues = self.seo_checker.check_article(text, title)
        all_issues.extend(seo_issues)
        seo_score = self.seo_checker.calculate_seo_score(seo_issues, word_count)
        
        # 4. Quality check
        quality_issues = self.quality_checker.check_article(text)
        all_issues.extend(quality_issues)
        quality_score = self.quality_checker.calculate_quality_score(quality_issues, word_count)
        
        # Calculate overall score
        overall_score = (brand_score * 0.4 + seo_score * 0.3 + quality_score * 0.3)
        
        # Determine pass/fail
        critical_issues = [i for i in all_issues if i.severity == "critical"]
        passed = len(critical_issues) == 0 and overall_score >= 70
        
        return QAReport(
            article_path=file_path,
            word_count=word_count,
            issues=all_issues,
            duplicate_matches=duplicates,
            brand_score=brand_score,
            seo_score=seo_score,
            quality_score=quality_score,
            overall_score=overall_score,
            passed=passed
        )
    
    def _extract_title(self, text: str) -> str:
        """Extract title from article text."""
        lines = text.split('\n')
        for line in lines[:10]:
            if line.startswith('# '):
                return line[2:].strip()
        return ""
    
    def print_report(self, report: QAReport):
        """Print QA report to console."""
        print("\n" + "="*70)
        print(f"QA REPORT: {Path(report.article_path).name}")
        print("="*70)
        
        # Scores
        print(f"\n📊 SCORES:")
        print(f"   Overall: {report.overall_score:.1f}/100 {'✅ PASS' if report.passed else '❌ FAIL'}")
        print(f"   Brand:   {report.brand_score:.1f}/100")
        print(f"   SEO:     {report.seo_score:.1f}/100")
        print(f"   Quality: {report.quality_score:.1f}/100")
        print(f"   Words:   {report.word_count}")
        
        # Duplicates
        if report.duplicate_matches:
            print(f"\n⚠️  DUPLICATES FOUND:")
            for dup in report.duplicate_matches:
                print(f"   • {Path(dup['file']).name}: {dup['similarity']*100:.0f}% similar")
        
        # Issues by severity
        if report.issues:
            print(f"\n📋 ISSUES ({len(report.issues)} total):")
            
            critical = [i for i in report.issues if i.severity == "critical"]
            warnings = [i for i in report.issues if i.severity == "warning"]
            info = [i for i in report.issues if i.severity == "info"]
            
            if critical:
                print(f"\n   🔴 CRITICAL ({len(critical)}):")
                for issue in critical:
                    print(f"      • [{issue.category}] {issue.message}")
                    if issue.suggestion:
                        print(f"        → {issue.suggestion}")
            
            if warnings:
                print(f"\n   🟡 WARNINGS ({len(warnings)}):")
                for issue in warnings:
                    print(f"      • [{issue.category}] {issue.message}")
                    if issue.suggestion:
                        print(f"        → {issue.suggestion}")
            
            if info:
                print(f"\n   🔵 INFO ({len(info)}):")
                for issue in info:
                    print(f"      • [{issue.category}] {issue.message}")
        
        print("\n" + "="*70)

# ============================================================================
# CLI INTERFACE
# ============================================================================

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    command = sys.argv[1]
    tool = ContentQATool()
    
    if command == "check" and len(sys.argv) >= 3:
        article_path = sys.argv[2]
        report = tool.check_article(article_path)
        tool.print_report(report)
        sys.exit(0 if report.passed else 1)
    
    elif command == "scan" and len(sys.argv) >= 3:
        folder = sys.argv[2]
        articles = list(Path(folder).glob("*.md"))
        
        print(f"Scanning {len(articles)} articles in {folder}...")
        
        passed = 0
        failed = 0
        
        for article in articles:
            report = tool.check_article(str(article))
            if report.passed:
                passed += 1
                print(f"✅ {article.name}")
            else:
                failed += 1
                print(f"❌ {article.name} (score: {report.overall_score:.1f})")
        
        print(f"\n{'='*70}")
        print(f"SUMMARY: {passed} passed, {failed} failed out of {len(articles)} articles")
        sys.exit(0 if failed == 0 else 1)
    
    elif command == "compare" and len(sys.argv) >= 4:
        article1 = sys.argv[2]
        article2 = sys.argv[3]
        
        text1 = tool.duplicate_detector.extract_text(article1)
        text2 = tool.duplicate_detector.extract_text(article2)
        
        ngrams1 = set(tool.duplicate_detector.create_ngrams(text1, n=5))
        ngrams2 = set(tool.duplicate_detector.create_ngrams(text2, n=5))
        
        overlap = len(ngrams1 & ngrams2)
        total = len(ngrams1 | ngrams2)
        similarity = overlap / total if total > 0 else 0
        
        print(f"\nComparison: {Path(article1).name} vs {Path(article2).name}")
        print(f"Similarity: {similarity*100:.1f}%")
        print(f"Overlapping phrases: {overlap}")
        
        if similarity > 0.7:
            print("⚠️  HIGH SIMILARITY - Consider rewriting one article")
        else:
            print("✅ Acceptable similarity level")
    
    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)

if __name__ == "__main__":
    main()
