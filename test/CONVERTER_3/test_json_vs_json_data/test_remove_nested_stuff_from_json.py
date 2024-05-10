import json
import os
def test():
    def remove_parents(json_data):
        new_json = {}
        for key, value in json_data.items():
            if isinstance(value, dict):
                new_json.update(remove_parents(value))
            else:
                new_json[key] = value
        return new_json

    def main():
        file_path = input("Enter the path to the JSON file: ")

        # Load JSON data from file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Remove parent nodes
        new_data = remove_parents(data)

        # Get the top-level key
        top_level_key = list(new_data.keys())[0]

        # Create a new file name for the modified JSON
        new_file_path = f"{os.path.splitext(os.path.basename(file_path))[0]}_copy.json"

        # Save modified JSON to a new file
        with open(new_file_path, 'w') as new_file:
            json.dump(new_data[top_level_key], new_file, indent=2)

        print(f"Modified JSON saved to: {new_file_path}")

    if __name__ == "__main__":
        main()
