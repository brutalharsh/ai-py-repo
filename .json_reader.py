import json
import os

def read_json_file(file_path):
    """
    Reads the contents of a JSON file and returns it as a dictionary.

    Parameters:
    file_path (str): The path to the JSON file.

    Returns:
    dict or None: The contents of the JSON file as a dictionary if successful.
                  None if the file does not exist or the content is not valid JSON.
    """
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return None

    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    file_path = 'example.json'
    result = read_json_file(file_path)
    if result is not None:
        print("JSON file contents:", result)
    else:
        print("Failed to read JSON file.")

