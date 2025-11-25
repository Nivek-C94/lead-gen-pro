import sqlite3
import uuid
from lead_gen_pro.core.db import get_db
from lead_gen_pro.core.lead_scorer import score_lead
from lead_gen_pro.core.models import Lead
from lead_gen_pro.scrapers.base import BaseScraper, ScraperResultNormalizer
from typing import List, Dict, Any


class LeadOrchestrator:
    def __init__(self, scrapers: List[BaseScraper]):
        self.scrapers = scrapers

    def run_leadgen(
        self, keyword: str, location: str | None = None, radius_km: int | None = None
    ) -> List[Lead]:
        all_leads = []
        for scraper in self.scrapers:
            try:
                results = scraper.search(keyword, location, radius_km)
                normalized = [
                    ScraperResultNormalizer.normalize(r, scraper.__class__.__name__)
                    for r in results
                ]
                all_leads.extend(normalized)
            except Exception as e:
                print(f"Error running scraper {scraper.__class__.__name__}: {e}")
        self._save_to_db(all_leads)
        return [Lead(**l) for l in all_leads]

    def _save_to_db(self, leads: List[Dict[str, Any]]):
        with get_db() as conn:
            for lead in leads:
                lead_id = lead.get("id") or str(uuid.uuid4())
                score = score_lead(lead)
                conn.execute(
                    """INSERT OR REPLACE INTO leads (id, name, source, url, location, score, created_at, details)
                    VALUES (?, ?, ?, ?, ?, ?, datetime('now'), ?)""",
                    (
                        lead_id,
                        lead.get("name"),
                        lead.get("source"),
                        lead.get("url"),
                        lead.get("location"),
                        score,
                        lead.get("details"),
                    ),
                )
            conn.commit()
