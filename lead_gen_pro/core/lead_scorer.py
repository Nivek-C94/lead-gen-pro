from typing import Dict, Any


def score_lead(lead: Dict[str, Any]) -> float:
    score = 0.0
    if lead.get("name"):
        score += 1.0
    if lead.get("url"):
        score += 1.0
    if lead.get("location"):
        score += 0.5
    if "premium" in (lead.get("details") or "").lower():
        score += 0.5
    return min(score, 5.0)
