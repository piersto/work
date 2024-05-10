import json
import pytest

def flatten_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    def flatten(json_value, parent_key='', separator='_'):
        items = {}
        for key, value in json_value.items():
            new_key = parent_key + separator + key if parent_key else key
            if isinstance(value, dict):
                items.update(flatten(value, new_key, separator))
            else:
                items[new_key] = value
        return items

    return flatten(data)

def compare_json_files(file1_path, file2_path):
    # Flatten the first JSON file
    flattened_data1 = flatten_json(file1_path)

    # Flatten the second JSON file
    flattened_data2 = flatten_json(file2_path)

    # Find common keys in both files
    common_keys = set(flattened_data1.keys()) & set(flattened_data2.keys())

    # Check if attribute values are identical
    for key in common_keys:
        val1 = flattened_data1[key]
        val2 = flattened_data2[key]

        # If values are integers, compare them directly
        if isinstance(val1, int) and isinstance(val2, int):
            if val1 != val2:
                print(f"Attribute '{key}' has different integer values in the two files:")
                print(f"File 1: {val1}")
                print(f"File 2: {val2}")
                return False
        # For other types, compare them as strings
        elif str(val1) != str(val2):
            print(f"Attribute '{key}' has different values in the two files:")
            print(f"File 1: {val1}")
            print(f"File 2: {val2}")
            return False

    print("All attribute values are identical.")
    return True

def test_compare_json_files():
    file1_path = r'C:\PROJECTS\PYTHON\work\json_type_of_fields.json'
    file2_path = r'C:\PROJECTS\PYTHON\work\json_type_of_fields_2.json'

    assert compare_json_files(file1_path, file2_path) == True

if __name__ == "__main__":
    pytest.main([__file__])
