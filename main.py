import json
import read_json_from_file
from textblob import TextBlob
from transformers import pipeline

vcon = read_json_from_file.read('test vcon.json')

# Extract relevant customer and conversation information
customer_info = vcon['parties'][1]
customer_name = customer_info['name']
customer_email = customer_info['mailto']

print(f"Customer Name: {customer_name}")
print(f"Customer Email: {customer_email}")

# Extract conversation data
dialog = vcon['analysis'][0]['body']

print('\n\nDialog:')
for line in dialog:
    print(f"{line['speaker']}: {line['message']}")


print('\n\nSentiment:')
for line in dialog:
    sentiment = TextBlob(line['message']).sentiment.polarity
    sentiment_label = 'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral'
    print(f"{line['speaker']}: {line['message']} (Sentiment: {sentiment_label})")

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
revision = "714eb0f"

# Load a pre-trained text classification pipeline for sentiment analysis
classifier = pipeline('sentiment-analysis', model=model_name, revision=revision)

conversation = "I work as a manager in a construction firm, and I've been there for over 20 years."
result = classifier(conversation)