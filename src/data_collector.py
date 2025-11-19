import os
from typing import Dict, Any, List
from duckduckgo_search import DDGS

class DataCollector:
    def __init__(self):
        self.ddgs = DDGS()

    def collect_data(self, company_identifier: str) -> Dict[str, Any]:
        """
        Orchestrates the data collection process for a given company.
        """
        print(f"Collecting data for: {company_identifier}")
        
        raw_data = {
            "company_identifier": company_identifier,
            "general_info": self._search_general_info(company_identifier),
            "c_suite": self._search_c_suite(company_identifier),
            "products": self._search_products(company_identifier),
            "reviews": self._search_reviews(company_identifier),
            "news": self._search_news(company_identifier)
        }
        return raw_data

    def _search_general_info(self, query: str) -> List[Dict[str, str]]:
        """Searches for general company info (Mission, Vision, History)."""
        print("  - Searching general info...")
        results = self.ddgs.text(f"{query} company mission vision history", max_results=5)
        return results

    def _search_c_suite(self, query: str) -> List[Dict[str, str]]:
        """Searches for C-Suite leadership info."""
        print("  - Searching C-Suite info...")
        results = self.ddgs.text(f"{query} company CEO CFO CTO leadership team", max_results=5)
        return results

    def _search_products(self, query: str) -> List[Dict[str, str]]:
        """Searches for products and services."""
        print("  - Searching products and services...")
        results = self.ddgs.text(f"{query} company products services", max_results=5)
        return results

    def _search_reviews(self, query: str) -> List[Dict[str, str]]:
        """Searches for customer reviews (G2, Capterra, Glassdoor)."""
        print("  - Searching reviews...")
        results = self.ddgs.text(f"{query} reviews G2 Capterra Glassdoor", max_results=5)
        return results

    def _search_news(self, query: str) -> List[Dict[str, str]]:
        """Searches for recent news and press releases."""
        print("  - Searching recent news...")
        results = self.ddgs.news(f"{query}", max_results=5)
        return results

if __name__ == "__main__":
    # Test the collector
    collector = DataCollector()
    data = collector.collect_data("OpenAI")
    import json
    print(json.dumps(data, indent=2))
