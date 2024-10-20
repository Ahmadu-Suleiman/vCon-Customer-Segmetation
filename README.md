# ConSeg: Customer Segmentation using vCon Data

## Project Overview
This project is an AI-powered tool that classifies customers based on behaviors and preferences detected in virtual conversations (vCon data). The segmentation will allow businesses to create targeted marketing strategies and enhance customer satisfaction.

## Features
- **Customer Segmentation**: Classifies customers using vCon data into categories like Age, Gender, Income, Level of Education, Religion, and Profession/Role in the company.
- **Natural Language Processing (NLP)**: Uses NLP techniques to analyze customer conversations for behavioral insights.
- **Automated Information Extraction**: Automatically extracts demographic data such as age, gender, profession, and more from interaction data.
- **Integration with Google Gemini**: Leverages Google Gemini’s powerful NLP tools for accurate entity recognition and data classification.
  
## Data Source
We use **vCon JSON data** containing structured metadata and conversation transcripts between agents and customers. This data is parsed and analyzed to extract customer attributes.

## Technologies Used
- **Python**: Core programming language for data parsing and analysis.
- **Google Gemini API**: For natural language understanding (NLU), entity recognition, and sentiment analysis.
- **JSON**: For handling and parsing vCon data.

## Testing
Try out the application [here](https://conseg.streamlit.app/).
