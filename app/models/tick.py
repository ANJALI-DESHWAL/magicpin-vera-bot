from typing import Any, Dict
from pydantic import BaseModel


class TickRequest(BaseModel):
    merchant_id: str
    trigger: Dict[str, Any]