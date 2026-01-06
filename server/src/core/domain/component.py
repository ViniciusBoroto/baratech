from pydantic import BaseModel
from typing import Dict, Any

class Component(BaseModel):
    name: str
    price: float
    performance_score: int  # 1-100
    specs: Dict[str, Any]
    category: str  # cpu, gpu, ram, storage, motherboard, power_supply, case