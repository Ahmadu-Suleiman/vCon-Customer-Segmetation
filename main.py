import read_json_from_file
from gemini import get_customer_info

vcon = read_json_from_file.read('test vcon.json')

# Extract relevant customer and conversation information
customer_info = vcon['parties'][1]
customer_name = customer_info['name']
customer_email = customer_info['mailto']

print(f"Customer Name: {customer_name}")
print(f"Customer Email: {customer_email}")

# Extract conversation data
dialog = vcon['analysis'][0]['body']

dialog_text = ''
print('\n\nDialog:')
for line in dialog:
    dialog_text += f"\n{line['speaker']}: {line['message']}"

print(dialog_text)
print(get_customer_info(dialog_text))
