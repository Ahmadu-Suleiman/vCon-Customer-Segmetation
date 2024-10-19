import os

import google.generativeai as genai
from dotenv import load_dotenv
from google.generativeai.types import StopCandidateException


load_dotenv()

# configure gemini
gemini_api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')


def get_response(prompt, number):
    try:
        history = firebase.get_member_history(number)
        if len(history) == 0:
            prompt = textwrap.dedent(f''' You are a friendly sustainability assistant. Help users learn about 
            eco-friendly practices, reduce waste, and conserve resources. Use simple language and ask follow-up 
            questions to provide more tailored information. Keep responses concise and informative. 
            Here is their first question:\n"{prompt}".''')
            history = [{"role": "user", "parts": [{"text": prompt}]}]

        chat = model.start_chat(history=history)
        response = chat.send_message(prompt)
        history = jsonpickle.encode(chat.history, True)
        firebase.set_member_history(number=number, history=history)

        return wrapper.fill(response.text.replace('*', ''))
    except StopCandidateException:
        return 'Error, please ask another question'
