from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Employee(BaseModel):
    name: str
    code: str

class Payment(BaseModel):
    method: str
    cheque_no: Optional[str] = "N/A"
    cheque_date: Optional[str] = "N/A"
    bank_name: Optional[str] = "N/A"

class Item(BaseModel):
    description: str
    amount: float

class VendorDetails(BaseModel):
    vendor_name: str
    vendor_contact: str

class FinancialReporting(BaseModel):
    report_period: str
    report_type: str

class SupplyPerformanceModel(BaseModel):
    performance_metrics: str  # or other fields...
    class Config:
        arbitrary_types_allowed = True

class AuditTrail(BaseModel):
    approver: str
    preparer: str
    audit_date: Optional[str]



# Define the base class with all common fields
class VoucherBase(BaseModel):
    date: str
    voucher_no: Optional[str]  # Making optional since it can be NULL
    prepared_by: Optional[str]  # Making optional since it can be NULL
    approved_by: Optional[str]  # Making optional since it can be NULL
    authorized_by: Optional[str]  # Making optional since it can be NULL
    receiver_signature: Optional[str]  # Making optional since it can be NULL
    employee_id: Optional[int]  # Make optional for create/update cases
    payment_id: Optional[int]    # Make optional for create/update cases
    total_amount: float
    in_words: Optional[str]  # Making optional since it can be NULL
    expense_category: Optional[str]  # Making optional since it can be NULL
    payment_status: Optional[str]  # Making optional since it can be NULL
    payment_dues: Optional[float]  # Making optional since it can be NULL
    cash_flow_impact: Optional[str]  # Making optional since it can be NULL
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

class ItemModel(BaseModel):
    description: str
    amount: float

class EmployeeModel(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None

class PaymentModel(BaseModel):
    method: str
    cheque_no: Optional[str]
    cheque_date: Optional[str]
    bank_name: Optional[str]

class VendorDetailsModel(BaseModel):
    vendor_name: Optional[str]
    vendor_contact: Optional[str]

class AuditTrailModel(BaseModel):
    approver: Optional[str]
    preparer: Optional[str]
    audit_date: Optional[datetime]

class VoucherModel(BaseModel):
    date: str
    voucher_no: Optional[str]
    prepared_by: Optional[str]
    approved_by: Optional[str]
    authorized_by: Optional[str]
    receiver_signature: Optional[str]
    employee: EmployeeModel
    payment: PaymentModel
    items: List[ItemModel]
    total_amount: float
    in_words: str
    expense_category: str
    payment_status: str
    payment_dues: float
    cash_flow_impact: str
    vendor_details: VendorDetailsModel
    audit_trail: AuditTrailModel

    class Config:
        from_attributes = True  # Allow from_orm usage        