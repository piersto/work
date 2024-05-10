import json
import pytest
import math

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

def remove_parent_lines(json_file_path, copy_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    if isinstance(data, dict) and len(data) == 1:
        key = list(data.keys())[0]
        data = data[key]
    with open(copy_file_path, 'w') as copy_file:
        json.dump(data, copy_file)

def compare_json_files(file1_path, file2_path, float_tolerance=1e-9):
    # Remove parent lines from both files
    copy_file1_path = file1_path + "_copy.json"
    copy_file2_path = file2_path + "_copy.json"
    remove_parent_lines(file1_path, copy_file1_path)
    remove_parent_lines(file2_path, copy_file2_path)

    # Flatten both copied JSON files
    flattened_data1 = flatten_json(copy_file1_path)
    flattened_data2 = flatten_json(copy_file2_path)

    # Check if attribute values are identical
    for key1, val1 in flattened_data1.items():
        # Find the corresponding key in flattened_data2
        if key1 not in flattened_data2:
            print(f"Attribute '{key1}' does not exist in the second file.")
            continue

        val2 = flattened_data2[key1]

        # If values are integers, compare them directly
        if isinstance(val1, int) and isinstance(val2, int):
            if val1 != val2:
                print(f"Attribute '{key1}' has different integer values in the two files:")
                print(f"File 1: {val1}")
                print(f"File 2: {val2}")
                return False
        # If values are floating-point numbers (doubles), compare them within tolerance
        elif isinstance(val1, float) and isinstance(val2, float):
            if math.isclose(val1, val2, rel_tol=float_tolerance):
                continue
            else:
                print(f"Attribute '{key1}' has different floating-point values in the two files:")
                print(f"File 1: {val1}")
                print(f"File 2: {val2}")
                return False
        # For other types, compare them as strings
        elif str(val1) != str(val2):
            print(f"Attribute '{key1}' has different values in the two files:")
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
