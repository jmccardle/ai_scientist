#!/usr/bin/env python3
"""
Systematic literature search across multiple databases
for anthropomorphization of AI review
"""

import json
import csv
import time
import requests
from datetime import datetime
from typing import List, Dict, Any
import hashlib

class LiteratureSearcher:
    """Conducts systematic literature searches across databases"""

    def __init__(self):
        self.search_log = []
        self.all_results = []

    def search_openalex(self, query: str, from_date: str = "2015-01-01",
                       to_date: str = "2024-11-14") -> List[Dict]:
        """Search OpenAlex API"""
        base_url = "https://api.openalex.org/works"

        # Build search parameters
        params = {
            "search": query,
            "filter": f"from_publication_date:{from_date},to_publication_date:{to_date}",
            "per_page": 200,
            "page": 1
        }

        results = []
        max_pages = 5  # Limit to avoid too many API calls

        for page in range(1, max_pages + 1):
            params["page"] = page
            try:
                response = requests.get(base_url, params=params, timeout=30)
                if response.status_code == 200:
                    data = response.json()
                    if "results" not in data or not data["results"]:
                        break

                    for work in data["results"]:
                        # Extract authors safely
                        authors = []
                        for authorship in work.get("authorships", [])[:5]:
                            author_info = authorship.get("author", {})
                            if author_info and author_info.get("display_name"):
                                authors.append(author_info.get("display_name"))

                        paper = {
                            "id": work.get("id", ""),
                            "doi": work.get("doi", ""),
                            "title": work.get("title", "") or "",
                            "year": work.get("publication_year", ""),
                            "authors": ", ".join(authors) if authors else "",
                            "abstract": work.get("abstract", "") or "",
                            "source": "OpenAlex",
                            "query_used": query[:100]
                        }
                        results.append(paper)

                    time.sleep(1)  # Rate limiting

            except Exception as e:
                print(f"Error searching OpenAlex page {page}: {e}")
                break

        return results

    def search_arxiv(self, query: str, max_results: int = 500) -> List[Dict]:
        """Search arXiv API"""
        import urllib.parse
        base_url = "http://export.arxiv.org/api/query"

        # Format query for arXiv
        formatted_query = query.replace(" AND ", " AND all:").replace(" OR ", " OR all:")
        formatted_query = f"all:{formatted_query}"

        params = {
            "search_query": formatted_query,
            "start": 0,
            "max_results": max_results,
            "sortBy": "relevance",
            "sortOrder": "descending"
        }

        results = []

        try:
            response = requests.get(base_url, params=params, timeout=30)
            if response.status_code == 200:
                # Parse XML response (simplified)
                import xml.etree.ElementTree as ET
                root = ET.fromstring(response.text)

                ns = {"arxiv": "http://www.w3.org/2005/Atom"}

                for entry in root.findall("arxiv:entry", ns):
                    title = entry.find("arxiv:title", ns)
                    published = entry.find("arxiv:published", ns)
                    summary = entry.find("arxiv:summary", ns)
                    authors = entry.findall("arxiv:author/arxiv:name", ns)
                    arxiv_id = entry.find("arxiv:id", ns)

                    # Extract year from published date
                    year = ""
                    if published is not None and published.text:
                        year = published.text[:4]

                    # Filter by date range (2015-2024)
                    if year and int(year) >= 2015:
                        paper = {
                            "id": arxiv_id.text if arxiv_id is not None else "",
                            "doi": "",  # arXiv doesn't use DOIs
                            "title": title.text.strip() if title is not None and title.text else "",
                            "year": year,
                            "authors": ", ".join([
                                author.text for author in authors[:5] if author.text
                            ]),
                            "abstract": summary.text.strip()[:500] if summary is not None and summary.text else "",
                            "source": "arXiv",
                            "query_used": query[:100]
                        }
                        results.append(paper)

        except Exception as e:
            print(f"Error searching arXiv: {e}")

        return results

    def deduplicate_results(self, results: List[Dict]) -> List[Dict]:
        """Remove duplicate papers based on title similarity and DOI"""
        seen_dois = set()
        seen_titles = set()
        unique_results = []

        for paper in results:
            # Skip if no title
            if not paper.get("title"):
                continue

            # Check DOI first
            if paper.get("doi") and paper["doi"] in seen_dois:
                continue

            # Check title (normalized)
            title_key = paper["title"].lower().strip()
            if not title_key:  # Skip empty titles
                continue

            title_hash = hashlib.md5(title_key.encode()).hexdigest()

            if title_hash in seen_titles:
                continue

            # Add to unique results
            unique_results.append(paper)
            if paper.get("doi"):
                seen_dois.add(paper["doi"])
            seen_titles.add(title_hash)

        return unique_results

    def save_results(self, results: List[Dict], filename: str):
        """Save search results to CSV"""
        if not results:
            print(f"No results to save for {filename}")
            return

        fieldnames = ["id", "doi", "title", "year", "authors", "abstract", "source", "query_used"]

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)

        print(f"Saved {len(results)} results to {filename}")

    def log_search(self, database: str, query: str, result_count: int):
        """Log search details"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "database": database,
            "query": query,
            "result_count": result_count
        }
        self.search_log.append(log_entry)

    def execute_comprehensive_search(self):
        """Execute the full search strategy"""

        # Define our search queries
        queries = {
            "primary": "anthropomorphism OR anthropomorphization OR human-like traits AND artificial intelligence OR AI OR large language model OR LLM OR chatbot",
            "interaction": "human-AI interaction AND anthropomorphic OR human-like AND language model OR chatbot",
            "ethics": "anthropomorphism AND AI OR artificial intelligence AND ethics OR vulnerable OR children OR elderly",
            "regulation": "AI Bill of Rights OR AI governance OR trustworthy AI AND anthropomorphic"
        }

        all_results = []

        # Search OpenAlex
        print("\n=== Searching OpenAlex ===")
        for query_name, query_string in queries.items():
            print(f"Query: {query_name}")
            results = self.search_openalex(query_string)
            print(f"Found {len(results)} results")
            all_results.extend(results)
            self.log_search("OpenAlex", query_name, len(results))
            time.sleep(2)

        # Search arXiv
        print("\n=== Searching arXiv ===")
        for query_name, query_string in queries.items():
            print(f"Query: {query_name}")
            results = self.search_arxiv(query_string, max_results=200)
            print(f"Found {len(results)} results")
            all_results.extend(results)
            self.log_search("arXiv", query_name, len(results))
            time.sleep(2)

        # Deduplicate
        print(f"\nTotal results before deduplication: {len(all_results)}")
        unique_results = self.deduplicate_results(all_results)
        print(f"Total unique results: {len(unique_results)}")

        return unique_results

    def save_search_log(self, filename: str):
        """Save search log to JSON"""
        with open(filename, 'w') as f:
            json.dump(self.search_log, f, indent=2)
        print(f"Search log saved to {filename}")


def main():
    """Main execution"""
    print("Starting systematic literature search...")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    searcher = LiteratureSearcher()

    # Execute comprehensive search
    results = searcher.execute_comprehensive_search()

    # Save results
    output_dir = "/home/user/ai_scientist/anthropomorphization_review/data/literature"
    searcher.save_results(results, f"{output_dir}/search_results.csv")
    searcher.save_search_log(f"{output_dir}/search_log.json")

    # Print summary statistics
    print("\n=== Search Summary ===")
    print(f"Total unique papers found: {len(results)}")

    # Count by source
    by_source = {}
    for paper in results:
        source = paper.get("source", "Unknown")
        by_source[source] = by_source.get(source, 0) + 1

    print("\nResults by database:")
    for source, count in by_source.items():
        print(f"  {source}: {count}")

    # Count by year
    by_year = {}
    for paper in results:
        year = paper.get("year", "")
        if year:
            by_year[year] = by_year.get(year, 0) + 1

    print("\nResults by year:")
    for year in sorted(by_year.keys()):
        print(f"  {year}: {by_year[year]}")

    return results


if __name__ == "__main__":
    results = main()