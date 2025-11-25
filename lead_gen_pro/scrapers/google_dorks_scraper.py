from lead_gen_pro.scrapers.base import BaseScraper
from typing import List, Dict, Any


class GoogleDorksScraper(BaseScraper):
    def search(
        self, keyword: str, location: str | None = None, radius_km: int | None = None
    ) -> List[Dict[str, Any]]:
        query = f"{keyword} leads"
        if location:
            query += f" {location}"
        self.driver.get(f"https://www.google.com/search?q={query}")
        results = []
        elements = self.driver.find_elements("css selector", "a h3")
        for el in elements[:10]:
            parent = el.find_element("xpath", "..")
            url = parent.get_attribute("href")
            results.append(
                {
                    "id": url,
                    "name": el.text,
                    "url": url,
                    "source": "Google",
                    "location": location,
                    "details": f"Found via query: {query}",
                }
            )
        return results
