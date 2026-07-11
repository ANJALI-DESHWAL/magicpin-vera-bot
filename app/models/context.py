from typing import Dict, Any, Literal
from pydantic import BaseModel


class ContextRequest(BaseModel):
    scope: Literal["merchant", "customer", "category"]
    context_id: str
    version: int
    payload: Dict[str, Any]
    delivered_at: str