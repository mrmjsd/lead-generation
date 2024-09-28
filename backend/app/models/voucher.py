from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship
from app.db.base import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255), nullable=True)
    code = Column(String(length=255), nullable=True)

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    method = Column(String(length=255), nullable=True)
    cheque_no = Column(String(length=255), nullable=True)
    cheque_date = Column(String(length=255), nullable=True)
    bank_name = Column(String(length=255), nullable=True)

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(length=255), nullable=True)
    amount = Column(Float, nullable=True)
    voucher_id = Column(Integer, ForeignKey("vouchers.id"))

class VendorDetails(Base):
    __tablename__ = "vendor_details"
    id = Column(Integer, primary_key=True, index=True)
    vendor_name = Column(String(length=255), nullable=True)
    vendor_contact = Column(String(length=255), nullable=True)

class FinancialReporting(Base):
    __tablename__ = "financial_reporting"
    id = Column(Integer, primary_key=True, index=True)
    report_period = Column(String(length=255), nullable=True)
    report_type = Column(String(length=255), nullable=True)

class SupplyPerformance(Base):
    __tablename__ = "supply_performance"
    id = Column(Integer, primary_key=True, index=True)
    performance_metrics = Column(String(length=255), nullable=True)

class AuditTrail(Base):
    __tablename__ = "audit_trail"
    id = Column(Integer, primary_key=True, index=True)
    approver = Column(String(length=255), nullable=True)  
    preparer = Column(String(length=255), nullable=True)  # New field added
    action = Column(String(length=255), nullable=True)
    audit_date = Column(DateTime, default=func.now())  # This should capture the current date
    description = Column(String(length=512), nullable=True)

class Voucher(Base):
    __tablename__ = "vouchers"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(String(length=255), nullable=False)
    voucher_no = Column(String(length=255), nullable=True)
    prepared_by = Column(String(length=255), nullable=True)
    approved_by = Column(String(length=255), nullable=True)
    authorized_by = Column(String(length=255), nullable=True)
    receiver_signature = Column(String(length=255), nullable=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    payment_id = Column(Integer, ForeignKey("payments.id"))
    total_amount = Column(Float, nullable=True)
    in_words = Column(String(length=255), nullable=True)
    expense_category = Column(String(length=255), nullable=True)
    payment_status = Column(String(length=255), nullable=True)
    payment_dues = Column(Float, nullable=True)
    cash_flow_impact = Column(String(length=255), nullable=True)
    vendor_details_id = Column(Integer, ForeignKey("vendor_details.id"))
    financial_reporting_id = Column(Integer, ForeignKey("financial_reporting.id"))
    supply_performance_id = Column(Integer, ForeignKey("supply_performance.id"))
    audit_trail_id = Column(Integer, ForeignKey("audit_trail.id"))

    # Relationships
    employee = relationship("Employee")
    payment = relationship("Payment")
    items = relationship("Item")
    vendor_details = relationship("VendorDetails")
    financial_reporting = relationship("FinancialReporting")
    supply_performance = relationship("SupplyPerformance")
    audit_trail = relationship("AuditTrail")
