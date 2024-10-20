import read_json_from_file
from gemini import get_customer_info
import streamlit as st
import json

import pprint

try:

    st.title("JSON Processing App")

    # Display sample JSON
    st.subheader("Sample JSON")
    st.json(sample_json)
    user_input_json = st.text_area("Enter your JSON here", value=json.dumps(sample_json))

    vcon = read_json_from_file.read('test vcon.json')

    # Extract conversation data
    dialog = vcon['analysis'][0]['body']

    dialog_text = ''
    for line in dialog:
        dialog_text += f"\n{line['speaker']}: {line['message']}"

    # Print the customer info if extraction was successful
    pprint.pprint(get_customer_info(dialog_text))

except FileNotFoundError:
    print("Error: The file 'test vcon.json' was not found.")
except KeyError as e:
    print(f"Error: Missing key in the JSON structure: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

