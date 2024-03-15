import json

def test_test():
  def print_person_info(data, indent=0):
    """Prints information about a person from a dictionary with custom formatting."""
    for key, value in data.items():
      if isinstance(value, dict):
        # Flatten subkeys by iterating and recursively calling the function
        for subkey, subvalue in value.items():
          print(f"{' ' * indent}{key}.{subkey}: {subvalue}")
      else:
        # Handle boolean values and format output
        if isinstance(value, bool):
          value = "Y" if value else "N"
        print(f"{' ' * indent}{key}: {value}")

  # Replace "your_json_file.json" with the actual path to your JSON file
  with open("C:\PROJECTS\PYTHON\work\json_type_of_fields.json", "r") as f:
    # Load the JSON data
    data = json.load(f)

    # Find the first dictionary containing person information (assuming unique structure)
    for key, value in data.items():
      if isinstance(value, dict):
        person_info = value
        break

    # Print information if person information is found
    if person_info:
      print_person_info(person_info)
    else:
      print("Person information not found in the provided JSON file.")
