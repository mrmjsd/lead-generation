from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PaymentCreate(BaseModel):
    method: Optional[str]
    cheque_no: Optional[str]
    cheque_date: Optional[str]
    bank_name: Optional[str]

class Payment(BaseModel):
    id: int
    cheque_no: Optional[str] = "N/A"
    cheque_date: Optional[str] = "N/A"
    bank_name: Optional[str] = "N/A"

    class Config:
        from_attributes = True  # Allow from_orm usage