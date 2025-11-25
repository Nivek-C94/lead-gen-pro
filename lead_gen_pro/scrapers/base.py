from botasaurus_driver import Driver
from typing import Any, Dict, List


class BaseScraper:
    def __init__(self, headless: bool = True):
        self.driver = Driver(headless=headless)

    def search(
        self, keyword: str, location: str | None = None, radius_km: int | None = None
    ) -> List[Dict[str, Any]]:
        raise NotImplementedError("Subclasses must implement search()")

    def close(self):
        self.driver.quit()


class ScraperResultNormalizer:
    @staticmethod
    def normalize(raw_data: Dict[str, Any], source: str) -> Dict[str, Any]:
        return {
            "id": raw_data.get("id") or raw_data.get("url"),
            "name": raw_data.get("name"),
            "source": source,
            "url": raw_data.get("url"),
            "location": raw_data.get("location"),
            "details": raw_data.get("details"),
        }
