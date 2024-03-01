import json
import pytest
import os


def extract_values_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    def flatten_json(json_dict):
        values = {}
        for key, value in json_dict.items():
            if isinstance(value, dict):
                nested_values = flatten_json(value)
                for nested_key, nested_value in nested_values.items():
                    values[key + "_" + nested_key] = nested_value
            elif value is None:
                values[key] = "null"
            else:
                values[key] = value
        return values

    return flatten_json(data)


def test_json_data_types():
    # Get the path to the directory containing this script
    script_directory = os.path.dirname(os.path.realpath(__file__))

    # Specify the name of your JSON file
    json_file_name = 'C:\PROJECTS\PYTHON\work\json_type_of_fields.json'

    # Construct the full path to your JSON file
    json_file_path = os.path.join(script_directory, json_file_name)

    # Extract values from the JSON file
    data_values = extract_values_from_json(json_file_path)

    # Print the contents of the dictionary
    print("Extracted values from JSON:", data_values)

    # Define the fields for each type
    string_fields = ['person_name', 'person_surname']
    int_fields = ['person_age']
    float_fields = ['person_height']
    bool_fields = ['person_is_student', 'person_is_married']

    # Test string fields
    for field in string_fields:
        value = data_values.get(field)
        assert value is None or isinstance(value, str), f"Field '{field}' is not of type str or null. Actual type: {type(value)}."

    # Test int fields
    for field in int_fields:
        value = data_values.get(field)
        assert value is None or isinstance(value, int), f"Field '{field}' is not of type int or null. Actual type: {type(value)}."

    # Test float fields
    for field in float_fields:
        value = data_values.get(field)
        assert value is None or isinstance(value, float), f"Field '{field}' is not of type float or null. Actual type: {type(value)}."

    # Test bool fields
    for field in bool_fields:
        value = data_values.get(field)
        assert value is None or isinstance(value, bool), f"Field '{field}' is not of type bool or null. Actual type: {type(value)}."


