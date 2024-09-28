import google.generativeai as genai
import json
from app.core.config import settings
class ParseModel:
    
    def __init__(self):
        api_key = settings.GENERATIVE_AI_API_KEY
        genai.configure(api_key=api_key)
    def upload_pdf_to_model(self, file_path):
        return genai.upload_file(file_path)
    def generate_invoice_json(self,model, sample_pdf, business_categories, status, format_structure):
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
    def clean_response_text(self,response_text):
        cleaned_text = '\n'.join(response_text.splitlines()[1:])
        cleaned_text = cleaned_text.strip().replace('```', '')
        return cleaned_text
    def parse_json(self, json_string):
        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
        
    def get_response(self,sample_pdf, business_categories, status, format_structure):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = self.generate_invoice_json(model, sample_pdf, business_categories, status, format_structure)
        json_string_cleaned = self.clean_response_text(response.text)
        json_response = self.parse_json(json_string_cleaned)
        return json_response