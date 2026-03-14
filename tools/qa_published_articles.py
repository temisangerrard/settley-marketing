#!/usr/bin/env python3
"""
QA Audit for Published Settley Articles

Fetches articles from the Settley API and runs comprehensive QA checks including:
- Design compliance (breadcrumbs, CTAs, disclaimers, typography)
- Brand voice and required elements
- SEO best practices
- Content quality

Usage:
    python tools/qa_published_articles.py
"""

import requests
import json
from pathlib import Path
from content_qa import ContentQATool, QAReport

API_BASE_URL = "https://settley.fly.dev"

def fetch_articles():
    """Fetch all published articles from the API."""
    try:
        response = requests.get(f"{API_BASE_URL}/articles", timeout=30)
        response.raise_for_status()
        data = response.json()
        
        if data.get("status") == 200:
            return data.get("data", [])
        else:
            print(f"Error: API returned status {data.get('status')}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching articles: {e}")
        return []

def main():
    print("🔍 Fetching published articles from Settley API...")
    articles = fetch_articles()
    
    if not articles:
        print("No articles found or API unavailable.")
        return
    
    print(f"✅ Found {len(articles)} published articles\n")
    
    # Initialize QA tool
    qa_tool = ContentQATool(api_base_url=API_BASE_URL)
    
    # Run QA on each article
    reports = []
    for article in articles:
        article_id = article.get("_id", "unknown")
        title = article.get("title", "Untitled")
        status = article.get("status", "unknown")
        
        if status != "published":
            continue
        
        print(f"Checking: {title}...")
        report = qa_tool.check_api_article(article)
        report.design_score = qa_tool.design_checker.calculate_design_score(
            [i for i in report.issues if i.category == "design"]
        )
        reports.append((article_id, title, report))
    
    # Print summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    
    passed = sum(1 for _, _, r in reports if r.passed)
    failed = len(reports) - passed
    
    print(f"\nTotal Articles: {len(reports)}")
    print(f"✅ Passed: {passed} ({passed/len(reports)*100:.1f}%)")
    print(f"❌ Failed: {failed} ({failed/len(reports)*100:.1f}%)")
    
    # Average scores
    avg_overall = sum(r.overall_score for _, _, r in reports) / len(reports)
    avg_brand = sum(r.brand_score for _, _, r in reports) / len(reports)
    avg_design = sum(r.design_score for _, _, r in reports) / len(reports)
    avg_seo = sum(r.seo_score for _, _, r in reports) / len(reports)
    avg_quality = sum(r.quality_score for _, _, r in reports) / len(reports)
    
    print(f"\nAverage Scores:")
    print(f"   Overall:  {avg_overall:.1f}/100")
    print(f"   Brand:    {avg_brand:.1f}/100")
    print(f"   Design:   {avg_design:.1f}/100")
    print(f"   SEO:      {avg_seo:.1f}/100")
    print(f"   Quality:  {avg_quality:.1f}/100")
    
    # Print detailed reports
    print("\n\n" + "="*70)
    print("DETAILED REPORTS")
    print("="*70)
    
    for article_id, title, report in reports:
        qa_tool.print_api_report(report, article_id)
        
        # Show first 3 issues if any
        if report.issues:
            print(f"\nTop Issues:")
            for i, issue in enumerate(report.issues[:3]):
                print(f"  {i+1}. [{issue.severity.upper()}] {issue.message}")
            if len(report.issues) > 3:
                print(f"  ... and {len(report.issues) - 3} more")
        
        print("\n" + "-"*70)
    
    # Save report to file
    report_data = {
        "date": "2026-03-14",
        "total_articles": len(reports),
        "passed": passed,
        "failed": failed,
        "average_scores": {
            "overall": round(avg_overall, 1),
            "brand": round(avg_brand, 1),
            "design": round(avg_design, 1),
            "seo": round(avg_seo, 1),
            "quality": round(avg_quality, 1)
        },
        "articles": [
            {
                "id": article_id,
                "title": title,
                "passed": report.passed,
                "overall_score": round(report.overall_score, 1),
                "brand_score": round(report.brand_score, 1),
                "design_score": round(report.design_score, 1),
                "seo_score": round(report.seo_score, 1),
                "quality_score": round(report.quality_score, 1),
                "word_count": report.word_count,
                "issue_count": len(report.issues)
            }
            for article_id, title, report in reports
        ]
    }
    
    report_path = Path("content/QA_PUBLISHED_ARTICLES_REPORT_2026-03-14.json")
    with open(report_path, 'w') as f:
        json.dump(report_data, f, indent=2)
    
    print(f"\n💾 Full report saved to: {report_path}")

if __name__ == "__main__":
    main()
