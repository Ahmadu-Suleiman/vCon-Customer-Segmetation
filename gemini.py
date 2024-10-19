import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# configure gemini
gemini_api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

import json


def get_customer_info(dialog):
    response = model.generate_content(f"""
    Extract the following information from the provided chat data in a return it in a plain text, 
    valid, parsable JSON format:

    **Demographic Segmentation:**

    * **age:** The person's age.
    * **gender:** The person's gender.
    * **income:** The person's estimated income level (e.g., low, medium, high).
    * **education:** The person's highest level of education (e.g., high school, bachelor's, master's).
    * **religion:** The person's religion.
    * **profession:** The person's occupation.

    **Psychographic Segmentation:**

    * **personality:** The person's personality traits (e.g., extroverted, introverted, conscientious).
    * **hobbies:** The person's interests and hobbies.
    * **social_status:** The person's social standing (e.g., upper class, middle class, working class).
    * **opinions:** The person's opinions on various topics (e.g., politics, social issues).
    * **life_goals:** The person's aspirations and ambitions.
    * **values_and_beliefs:** The person's core values and beliefs.
    * **lifestyle:** The person's way of life (e.g., active, sedentary, hedonistic).

    **Geographic Segmentation:**

    * **climate:** The region's climate (e.g., tropical, temperate, arid).
    * **culture:** The region's cultural characteristics (e.g., traditions, customs, values).
    * **language:** The region's primary language(s).
    * **population_density:** The region's population density (e.g., urban, suburban, rural).

    **Behavioral Segmentation:**

    * **spending_habits:** The person's spending patterns (e.g., frugal, impulsive, brand-conscious).
    * **purchasing_habits:** The person's buying behavior (e.g., frequency, quantity, channel).
    * **browsing_habits:** The person's online behavior (e.g., websites visited, time spent).
    * **interactions_with_brand:** The person's interactions with your brand (e.g., customer service inquiries, social media engagement).
    * **loyalty_to_brand:** The person's level of loyalty to your brand (e.g., repeat customer, brand advocate).
    * **product_feedback:** The person's feedback on your products or services.


    Return only a valid, parsable JSON string and no other additional details.
    **Chat Data:**
    {dialog}""", generation_config={"response_mime_type": "application/json"})

    try:
        print(response.text)
        response_json = json.loads(response.text)
        return response_json
    except json.JSONDecodeError:
        print("Error parsing JSON response.")
        return None


def extract_json(text_response):
    pattern = r'\{[^{}]*\}'
