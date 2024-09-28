import os
import google.generativeai as genai
import json
from app.core.config import settings


def configure_genai(api_key):
    genai.configure(api_key=api_key)


def get_file_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(_file_))
    media_dir = os.path.join(current_dir, "../media")
    os.makedirs(media_dir, exist_ok=True)  # Ensure directory exists
    return os.path.join(media_dir, file_name)


def upload_pdf_to_model(file_path):
    return genai.upload_file(file_path)


def generate_invoice_json(model, sample_pdf, business_categories, status, format_structure):
    query = f"""
    I am providing an invoice as my file. Please extract all data from the invoice and return the following:
    - *Gross value* for each spend item
    - *Predicted category* for each spend item, selected from the following categories:
    {business_categories}
    Please return the data in the following JSON format:
    {format_structure}
    The status should be one of the following: {status}.
    If you cannot extract specific fields, return ⁠ null ⁠ for those fields.
    expense_category value will be the category based on the categories of all the individual items.
    Please generate the in_words value in the response if not present that will be the total_amount in words.
    Finally, please ensure the JSON is beautified and neatly formatted.
    """
    return model.generate_content([query, sample_pdf])


def clean_response_text(response_text):
    cleaned_text = '\n'.join(response_text.splitlines()[1:])
    cleaned_text = cleaned_text.strip().replace('```', '')
    return cleaned_text


def parse_json(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None


def main(file_name):
    api_key = settings.API_KEY
    configure_genai(api_key)

    file_path = get_file_path(file_name)
    sample_pdf = upload_pdf_to_model(file_path)

    business_categories = [
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

    status = ["paid", "pending", "unknown"]

    format_structure = """
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

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = generate_invoice_json(model, sample_pdf, business_categories, status, format_structure)

    json_string_cleaned = clean_response_text(response.text)
    json_response = parse_json(json_string_cleaned)

    if json_response:
        print(json.dumps(json_response, indent=2))


if _name_ == "_main_":
    main("invoice_1.pdf")