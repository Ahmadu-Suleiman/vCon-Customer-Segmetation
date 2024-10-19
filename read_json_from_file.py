import os
import json

def read(filename):
    try:
        # Get the current working directory
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to the JSON file
        file_path = os.path.join(current_dir, filename)

        # Open and read the JSON file
        with open(file_path, 'r') as file:
            # Load the JSON data into a Python object
            data = json.load(file)

        return data

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found in the current directory.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON file '{filename}'.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
