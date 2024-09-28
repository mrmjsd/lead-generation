import os
from app.utils.parse_model import ParseModel
from app.services.voucher_service import VoucherService
class InvoiceProcessor:
    def __init__(self, file_name,db):
        self.file_name = file_name
        self.media_dir = self._create_media_dir()
        self.parse_model = ParseModel()
        self.db = db
        

    def _create_media_dir(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        media_dir = os.path.join(current_dir, "../media")
        os.makedirs(media_dir, exist_ok=True)
        return media_dir

    def get_file_path(self):
        return os.path.join(self.media_dir, self.file_name)

    async def parse_pdf(self):
        file_path = self.get_file_path()
        sample_pdf = self.parse_model.upload_pdf_to_model(file_path)
        parsed_data = self._extract_data(sample_pdf)

        # Pass the parsed data to VoucherService to create the voucher
        voucher_service = VoucherService(self.db)
        created_voucher =await voucher_service.create_voucher_from_json(parsed_data)
        return created_voucher  # Return the created voucher details

    def _extract_data(self, sample_pdf):
        business_categories = self._get_business_categories()
        status = self._get_status()
        format_structure = self._get_format_structure()
        return self.parse_model.get_response(sample_pdf, business_categories, status, format_structure)

    def _get_business_categories(self):
        # Return a list of business categories
        return [
        "Advertising & Marketing",
        "Employee Salaries & Wages",
        "Office Supplies",
        "Software & Subscriptions",
        "Utilities",
        "Rent & Lease Payments",
        "Training & Professional Development",
        "Travel & Accommodation",
        "Meals & Entertainment",
        "Insurance",
        "Legal & Accounting Services",
        "Taxes",
        "Consulting & Professional Fees",
        "Shipping & Delivery",
        "Inventory Purchases",
        "Vehicle Expenses",
        "Repairs & Maintenance",
        "Loan Interest",
        "Depreciation",
        "Bank Fees",
        "IT & Hardware Purchases",
        "Research & Development",
        "Customer Support",
        "Donations & Charitable Contributions",
        "Licensing & Permits",
        "Freelance & Contract Labor",
        "Communications",
        "Recruitment & Hiring",
        "Healthcare & Employee Benefits",
        "Facility Expenses",
        "Marketing Materials",
        "Product Development",
        "Miscellaneous Expenses",
        "salary"
    ]


    def _get_status(self):
        # Return a list of status options
        return ["paid", "pending", "unknown"]

    def _get_format_structure(self):
        # Return the format structure as a string
        return """
        {
        "voucher": {
            "date": "13-09-2024",
            "voucher_no": "XXXXX",
            "prepared_by": "Prepared Name",
            "approved_by": "Approver Name",
            "authorized_by": "Authorizer Name",
            "receiver_signature": "Receiver Name",
            "voucher_to": {
            "name": "Mrutyunjaya Patra",
            "code": "1061"
            "address":""
            },
            "payment": {
            "method": "Cash",
            "cheque_no": "XXXXX",
            "cheque_date": "XXXXX",
            "bank_name": "XXXXX"
            },
            "items": [
            {
                "description": "Namaste Frontend System Design Course",
                "amount": 7929.00,
                "category:XXXXXX
            }
            ],
            "total_amount": 7929.00,
            "in_words": "Seven thousand, nine hundred twenty-nine",
            "expense_category": "Training",
            "payment_status": "Paid",
            "payment_dues": 0.00,
            "cash_flow_impact": "Outflow",
            "vendor_details": {
            "vendor_name": "XXXXX",
            "vendor_contact": "XXXXX",
            "vendor_address": "XXXXXX"
            },
            "financial_reporting": {
            "report_period": "Monthly",
            "report_type": "Expense Report"
            },
            "supply_performance": {
            "performance_metrics": "XXXXX"
            },
            "audit_trail": {
            "approver": "Approver Name",
            "preparer": "Prepared Name",
            "audit_date": "XXXXX"
            }
        }
        }
        """