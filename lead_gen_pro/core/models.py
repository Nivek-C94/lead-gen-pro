from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class Lead(BaseModel):
    id: str
    name: Optional[str]
    source: str
    url: str
    location: Optional[str]
    score: Optional[float] = 0.0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    details: Optional[str]
