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
    method: Optional[str]
    cheque_no: Optional[str]
    cheque_date: Optional[str]
    bank_name: Optional[str]

    class Config:
        from_attributes = True  # Allow from_orm usage