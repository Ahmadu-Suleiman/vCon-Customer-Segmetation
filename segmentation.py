import read_json_from_file
from gemini import get_customer_info


def segmentation(json_v_con):
    try:
        vcon = read_json_from_file.read(json_v_con)

        # Extract conversation data
        dialog = vcon['analysis'][0]['body']

        dialog_text = ''
        for line in dialog:
            dialog_text += f"\n{line['speaker']}: {line['message']}"

        return get_customer_info(dialog_text)

    except FileNotFoundError:
        print("Error: The file 'test vcon.json' was not found.")
        return None
    except KeyError as e:
        print(f"Error: Missing key in the JSON structure: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
