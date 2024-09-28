from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AuditTrailCreate(BaseModel):
    approver: Optional[str] = None  # Make optional
    preparer: Optional[str] = None  # Make optional
    audit_date: Optional[datetime] = None  # Make optiona