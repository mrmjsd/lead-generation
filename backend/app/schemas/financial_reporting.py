from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FinancialReportingCreate(BaseModel):
    report_period: Optional[str]
    report_type: Optional[str]

class FinancialReporting(BaseModel):
    id: int
    report_period: Optional[str]
    report_type: Optional[str]

    class Config:
        from_attributes = True  # Allow from_orm usage