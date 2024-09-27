from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Employee(BaseModel):
    name: str
    code: str

class Payment(BaseModel):
    method: str
    cheque_no: Optional[str]
    cheque_date: Optional[str]
    bank_name: Optional[str]

class Item(BaseModel):
    description: str
    amount: float

class VendorDetails(BaseModel):
    vendor_name: str
    vendor_contact: str

class FinancialReporting(BaseModel):
    report_period: str
    report_type: str

class SupplyPerformance(BaseModel):
    performance_metrics: str

class AuditTrail(BaseModel):
    approver: str
    preparer: str
    audit_date: Optional[str]



# Define the base class with all common fields
class VoucherBase(BaseModel):
    date: str
    voucher_no: str
    prepared_by: str
    approved_by: str
    authorized_by: str
    receiver_signature: str
    employee_id: Optional[int]  # Make optional for create/update cases
    payment_id: Optional[int]    # Make optional for create/update cases
    total_amount: float
    in_words: str
    expense_category: str
    payment_status: str
    payment_dues: float
    cash_flow_impact: str
    vendor_details_id: Optional[int]
    financial_reporting_id: Optional[int]
    supply_performance_id: Optional[int]
    audit_trail_id: Optional[int]

    class Config:
        from_attributes = True  # Allow from_orm usage

# Create model extends VoucherBase but does not include 'id'
class VoucherCreate(VoucherBase):
    pass  # Inherits everything from VoucherBase

# Read model extends VoucherBase and includes 'id'
class VoucherRead(VoucherBase):
    id: int  # 'id' is only needed when reading data



class VoucherUpdate(VoucherBase):
    date: Optional[str] = None
    voucher_no: Optional[str] = None
    prepared_by: Optional[str] = None
    approved_by: Optional[str] = None
    authorized_by: Optional[str] = None
    receiver_signature: Optional[str] = None
    employee_id: Optional[int] = None
    payment_id: Optional[int] = None
    total_amount: Optional[float] = None
    in_words: Optional[str] = None
    expense_category: Optional[str] = None
    payment_status: Optional[str] = None
    payment_dues: Optional[float] = None
    cash_flow_impact: Optional[str] = None
    vendor_details_id: Optional[int] = None
    financial_reporting_id: Optional[int] = None
    supply_performance_id: Optional[int] = None
    audit_trail_id: Optional[int] = None
