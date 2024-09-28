from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class VendorDetailsCreate(BaseModel):
    vendor_name: Optional[str]
    vendor_contact: Optional[str]

class VendorDetails(BaseModel):
    id: int
    vendor_name: Optional[str]
    vendor_contact: Optional[str]

    class Config:
        from_attributes = True  # Allow from_orm usage