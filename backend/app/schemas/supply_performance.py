from pydantic import BaseModel
from typing import Optional

class SupplyPerformanceCreate(BaseModel):
    performance_metrics: Optional[str]

class SupplyPerformance(BaseModel):
    id: int
    performance_metrics: Optional[str]

    class Config:
        from_attributes = True  # Allow from_orm usage