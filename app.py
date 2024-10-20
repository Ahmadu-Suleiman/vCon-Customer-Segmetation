import json

import streamlit as st

import segmentation

# Streamlit app layout
st.title("ConSeg: Customer Segmentation using vCon Data")
st.text("""
This project aims to build an AI-powered tool that classifies customers based on 
behaviors and preferences detected in virtual conversations (vCon data). The 
segmentation will allow businesses to create targeted marketing strategies 
and enhance customer satisfaction.""")

# Step 1: Upload JSON file
uploaded_file = st.file_uploader("Upload a vCon file", type="json")

if uploaded_file is not None:
    # Step 2: Read and display uploaded JSON
    input_json = json.load(uploaded_file)
    st.write("Uploaded vCon:")
    st.json(input_json)

    # Step 3: Process the JSON
    json_seg = segmentation.segment(input_json)

    # Step 4: Display the processed JSON
    st.write("Customer Segmentation Info:")
    st.json(json_seg)

    # Step 5: Prepare the processed JSON for download
    json_str = json.dumps(json_seg)
    json_bytes = json_str.encode()

    # Step 6: Provide download button
    st.download_button(label="Download",
                       data=json_bytes,
                       file_name='customer_segmentation_info.json',
                       mime='application/json')
