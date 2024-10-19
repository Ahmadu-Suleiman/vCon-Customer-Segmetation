import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# configure gemini
gemini_api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')


def get_customer_info(dialog):
    response = model.generate_content(f"""
    Extract the following information of the customer in JSON format from the provided chat data:
    
    * **name:** The full name of the person.
    * **age:** The person's age.
    * **gender:** The person's gender.
    * **income:** The person's estimated income level (e.g., low, medium, high).
    * **education:** The person's highest level of education (e.g., high school, bachelor's, master's).
    * **profession:** The person's occupation.
    
    Return only the JSON string and no other additional details.
    
    **Chat Data:**
    {dialog}""")
    return response.text