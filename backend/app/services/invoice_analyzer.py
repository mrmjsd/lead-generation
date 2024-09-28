from collections import defaultdict
from app.schemas.voucher import VoucherModel
from typing import List
class InvoicesAnalyzer:
    def __init__(self, invoices:List[VoucherModel]) -> None:
        self.invoices = invoices
        
    def calculate_payment_dues(self):
        return sum(invoice.payment_dues for invoice in self.invoices)

    def analyze_cashflow(self):
        cashflow_data = {'Inflow': 0.0, 'Outflow': 0.0}
        for invoice in self.invoices:
            cashflow_data[invoice.cash_flow_impact] += invoice.total_amount
        return cashflow_data

    def categorize_expenses(self):
        categories = defaultdict(float)
        for invoice in self.invoices:
            categories[invoice.expense_category] += invoice.total_amount
        return dict(categories)

    def get_vendor_details(self):
        vendor_data = defaultdict(float)
        for invoice in self.invoices:
            # Access the vendor_name attribute instead of using subscript notation
            vendor_name = invoice.vendor_details.vendor_name
            vendor_data[vendor_name] += invoice.total_amount
        return dict(vendor_data)

    def total_amounts(self):
        return sum(invoice.total_amount for invoice in self.invoices)

    def list_item_details(self):
        items_details = []
        for invoice in self.invoices:
            for item in invoice.items:
                items_details.append({
                    'description': item.description,  # Access attributes directly
                    'amount': item.amount,
                    'voucher_no': invoice.voucher_no
                })
        return items_details


    def financial_reporting(self):
        reports = []
        for invoice in self.invoices:
            reports.append({
                'voucher_no': invoice.voucher_no,
                'total_amount': invoice.total_amount,
            })
        return reports

    def payment_status(self):
        status_data = defaultdict(int)
        for invoice in self.invoices:
            status_data[invoice.payment_status] += invoice.total_amount
        return dict(status_data)

    def supply_performance(self):
        performance_metrics = defaultdict(list)
        for invoice in self.invoices:
            # Ensure that the supply_performance is accessed as an object
            if invoice.supply_performance:  # Check if the relationship is not None
                performance_metrics[invoice.supply_performance.performance_metrics].append(invoice.vendor_details.vendor_name)
        return dict(performance_metrics)


    def auditing(self):
        audit_records = []
        for invoice in self.invoices:
            audit_records.append({
                'voucher_no': invoice.voucher_no,
                'approver': invoice.audit_trail.approver,  # Access the attribute directly
                'audit_date': invoice.audit_trail.audit_date
            })
        return audit_records

    
    
