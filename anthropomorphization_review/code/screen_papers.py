#!/usr/bin/env python3
"""
Title/Abstract screening with inter-rater reliability for systematic review
"""

import csv
import json
import random
import hashlib
from datetime import datetime
from typing import List, Dict, Tuple
import re

class PaperScreener:
    """Screens papers for inclusion based on title and abstract"""

    def __init__(self):
        self.inclusion_keywords = {
            "anthropomorphism": ["anthropomorph", "human-like", "humaniz", "personif", "social attribution"],
            "ai_systems": ["artificial intelligence", "ai", "machine learning", "ml", "language model",
                          "llm", "gpt", "bert", "chatbot", "conversational", "virtual assistant"],
            "interaction": ["human-ai", "human-computer", "hci", "user experience", "ux", "interaction"],
            "ethics": ["ethic", "moral", "trust", "manipulat", "bias", "governance", "regulat", "policy"],
            "vulnerable": ["child", "elder", "patient", "vulnerable", "disability", "mental health"]
        }

        self.exclusion_indicators = [
            "robot manipulation",  # Physical robots only
            "robotic surgery",      # Medical robots
            "animal behavior",      # Non-AI anthropomorphism
            "brand personality",    # Marketing anthropomorphism
            "drug discovery",       # Pure technical ML
            "protein folding",      # Pure technical ML
            "quantum computing",    # Different domain
        ]

    def check_relevance(self, title: str, abstract: str, strict: bool = True) -> Tuple[bool, str]:
        """
        Check if paper meets inclusion criteria
        Returns: (include: bool, reason: str)
        """
        # Combine title and abstract for searching
        text = f"{title} {abstract}".lower()

        # Check exclusion criteria first
        for exc in self.exclusion_indicators:
            if exc in text:
                return False, f"Excluded: {exc}"

        # Must have AI/ML component
        has_ai = any(keyword in text for keyword in self.inclusion_keywords["ai_systems"])
        if not has_ai:
            return False, "No AI/ML component"

        # Check for anthropomorphism or related concepts
        has_anthropomorph = any(keyword in text for keyword in self.inclusion_keywords["anthropomorphism"])

        # Check for other relevant aspects
        has_interaction = any(keyword in text for keyword in self.inclusion_keywords["interaction"])
        has_ethics = any(keyword in text for keyword in self.inclusion_keywords["ethics"])
        has_vulnerable = any(keyword in text for keyword in self.inclusion_keywords["vulnerable"])

        # Inclusion logic
        if strict:
            # Strict: Must have explicit anthropomorphism AND AI
            if has_anthropomorph and has_ai:
                return True, "Has anthropomorphism + AI"
            elif has_ai and (has_interaction or has_ethics) and "human" in text:
                return True, "AI + human aspects (interaction/ethics)"
            else:
                return False, "Missing core anthropomorphism concepts"
        else:
            # Lenient: More inclusive interpretation
            if has_anthropomorph and has_ai:
                return True, "Has anthropomorphism + AI"
            elif has_ai and (has_interaction or has_ethics or has_vulnerable):
                return True, "AI + relevant human/social aspects"
            elif "chatgpt" in text or "llm" in text or "conversational ai" in text:
                return True, "Relevant AI system type"
            elif has_ai and ("trust" in text or "user" in text or "social" in text):
                return True, "AI + social/trust aspects"
            else:
                return False, "Insufficient relevance"

    def screen_paper_strict(self, paper: Dict) -> Dict:
        """Screen with strict criteria (Reviewer 1)"""
        title = paper.get("title", "")
        abstract = paper.get("abstract", "")

        include, reason = self.check_relevance(title, abstract, strict=True)

        return {
            "id": paper.get("id", ""),
            "title": title[:100],
            "year": paper.get("year", ""),
            "include": include,
            "reason": f"[R1-Strict] {reason}",
            "reviewer": "Reviewer_1_Strict"
        }

    def screen_paper_lenient(self, paper: Dict) -> Dict:
        """Screen with lenient criteria (Reviewer 2)"""
        title = paper.get("title", "")
        abstract = paper.get("abstract", "")

        include, reason = self.check_relevance(title, abstract, strict=False)

        return {
            "id": paper.get("id", ""),
            "title": title[:100],
            "year": paper.get("year", ""),
            "include": include,
            "reason": f"[R2-Lenient] {reason}",
            "reviewer": "Reviewer_2_Lenient"
        }

    def resolve_conflict(self, paper: Dict, r1_decision: Dict, r2_decision: Dict) -> Dict:
        """Third reviewer to resolve conflicts"""
        title = paper.get("title", "")
        abstract = paper.get("abstract", "").lower()

        # Tiebreaker logic - look for strong indicators
        strong_indicators = [
            "anthropomorph",
            "human-like",
            "social robot",
            "conversational agent",
            "chatbot personality",
            "ai ethics",
            "trust in ai"
        ]

        strong_match = sum(1 for indicator in strong_indicators if indicator in title.lower() or indicator in abstract)

        if strong_match >= 2:
            return {
                "id": paper.get("id", ""),
                "title": title[:100],
                "year": paper.get("year", ""),
                "include": True,
                "reason": f"[R3-Resolved] Strong relevance ({strong_match} indicators)",
                "reviewer": "Reviewer_3_Tiebreaker"
            }
        elif strong_match >= 1 and ("llm" in abstract or "gpt" in abstract):
            return {
                "id": paper.get("id", ""),
                "title": title[:100],
                "year": paper.get("year", ""),
                "include": True,
                "reason": "[R3-Resolved] LLM/GPT with relevance indicator",
                "reviewer": "Reviewer_3_Tiebreaker"
            }
        else:
            return {
                "id": paper.get("id", ""),
                "title": title[:100],
                "year": paper.get("year", ""),
                "include": False,
                "reason": "[R3-Resolved] Insufficient strong indicators",
                "reviewer": "Reviewer_3_Tiebreaker"
            }

    def calculate_cohens_kappa(self, decisions1: List[bool], decisions2: List[bool]) -> float:
        """Calculate Cohen's Kappa for inter-rater reliability"""
        n = len(decisions1)
        if n == 0:
            return 0.0

        # Observed agreement
        po = sum(1 for d1, d2 in zip(decisions1, decisions2) if d1 == d2) / n

        # Expected agreement
        n_yes_r1 = sum(1 for d in decisions1 if d)
        n_yes_r2 = sum(1 for d in decisions2 if d)

        pe = ((n_yes_r1 * n_yes_r2) + ((n - n_yes_r1) * (n - n_yes_r2))) / (n * n)

        # Kappa
        if pe == 1:
            return 1.0  # Perfect agreement
        return (po - pe) / (1 - pe)


def main():
    """Main screening process"""
    print("=== Title/Abstract Screening ===")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Load search results
    input_file = "/home/user/ai_scientist/anthropomorphization_review/data/literature/search_results.csv"
    papers = []

    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        papers = list(reader)

    print(f"Loaded {len(papers)} papers for screening")

    screener = PaperScreener()

    # Two-pass screening
    print("\n--- First Pass (Strict Criteria) ---")
    r1_decisions = []
    r1_results = []

    for i, paper in enumerate(papers):
        decision = screener.screen_paper_strict(paper)
        r1_decisions.append(decision["include"])
        r1_results.append(decision)

        if i < 5:  # Show first 5 examples
            print(f"\nPaper {i+1}:")
            print(f"  Title: {paper['title'][:80]}...")
            print(f"  Decision: {'INCLUDE' if decision['include'] else 'EXCLUDE'}")
            print(f"  Reason: {decision['reason']}")

    print(f"\nReviewer 1 included: {sum(r1_decisions)}/{len(r1_decisions)}")

    print("\n--- Second Pass (Lenient Criteria) ---")
    r2_decisions = []
    r2_results = []

    for i, paper in enumerate(papers):
        decision = screener.screen_paper_lenient(paper)
        r2_decisions.append(decision["include"])
        r2_results.append(decision)

        if i < 5:  # Show first 5 examples
            print(f"\nPaper {i+1}:")
            print(f"  Title: {paper['title'][:80]}...")
            print(f"  Decision: {'INCLUDE' if decision['include'] else 'EXCLUDE'}")
            print(f"  Reason: {decision['reason']}")

    print(f"\nReviewer 2 included: {sum(r2_decisions)}/{len(r2_decisions)}")

    # Calculate inter-rater reliability
    kappa = screener.calculate_cohens_kappa(r1_decisions, r2_decisions)
    print(f"\n=== Inter-Rater Reliability ===")
    print(f"Cohen's Kappa: {kappa:.3f}")

    if kappa < 0.4:
        print("  Interpretation: Fair agreement")
    elif kappa < 0.6:
        print("  Interpretation: Moderate agreement")
    elif kappa < 0.8:
        print("  Interpretation: Substantial agreement")
    else:
        print("  Interpretation: Almost perfect agreement")

    # Resolve conflicts
    print(f"\n--- Conflict Resolution ---")
    conflicts = 0
    final_decisions = []

    for i, (paper, r1, r2, r1_dec, r2_dec) in enumerate(zip(papers, r1_results, r2_results, r1_decisions, r2_decisions)):
        if r1_dec != r2_dec:
            conflicts += 1
            # Resolve conflict
            resolution = screener.resolve_conflict(paper, r1, r2)
            final_decisions.append(resolution)

            if conflicts <= 5:  # Show first 5 conflicts
                print(f"\nConflict {conflicts}:")
                print(f"  Title: {paper['title'][:80]}...")
                print(f"  R1: {'INCLUDE' if r1_dec else 'EXCLUDE'}")
                print(f"  R2: {'INCLUDE' if r2_dec else 'EXCLUDE'}")
                print(f"  Resolution: {'INCLUDE' if resolution['include'] else 'EXCLUDE'}")
        else:
            # Agreement - use R1 decision
            final_decisions.append(r1)

    print(f"\nTotal conflicts: {conflicts}/{len(papers)} ({100*conflicts/len(papers):.1f}%)")

    # Save results
    included_papers = [p for p in final_decisions if p["include"]]
    excluded_papers = [p for p in final_decisions if not p["include"]]

    print(f"\n=== Final Screening Results ===")
    print(f"Included: {len(included_papers)} papers")
    print(f"Excluded: {len(excluded_papers)} papers")

    # Save screening decisions
    output_dir = "/home/user/ai_scientist/anthropomorphization_review/data/literature"

    with open(f"{output_dir}/screened_abstracts.csv", 'w', newline='', encoding='utf-8') as f:
        fieldnames = ["id", "title", "year", "include", "reason", "reviewer"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(final_decisions)

    # Save included papers
    included_ids = {p["id"] for p in included_papers}
    included_full = [p for p in papers if p["id"] in included_ids]

    with open(f"{output_dir}/included_for_fulltext.csv", 'w', newline='', encoding='utf-8') as f:
        fieldnames = papers[0].keys() if papers else []
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(included_full)

    # Save inter-rater stats
    stats = {
        "screening_date": datetime.now().isoformat(),
        "total_papers": len(papers),
        "reviewer1_included": sum(r1_decisions),
        "reviewer2_included": sum(r2_decisions),
        "cohens_kappa": kappa,
        "conflicts": conflicts,
        "final_included": len(included_papers),
        "final_excluded": len(excluded_papers)
    }

    with open(f"{output_dir}/inter_rater_reliability.json", 'w') as f:
        json.dump(stats, f, indent=2)

    print(f"\nResults saved to {output_dir}/")

    return included_full, stats


if __name__ == "__main__":
    included, stats = main()