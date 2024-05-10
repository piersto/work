import json


def test_jsov_vs_json_data_2():
    import json

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

    def compare_json_files(file1_path, file2_path, float_tolerance=1e-9):
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

            # If values are floating-point numbers, compare them within tolerance
            if isinstance(val1, float) and isinstance(val2, float):
                if abs(val1 - val2) > float_tolerance:
                    print(f"Attribute '{key}' has different values in the two files:")
                    print(f"File 1: {val1}")
                    print(f"File 2: {val2}")
                    return False
            # If values are boolean, convert them to lowercase for comparison
            elif isinstance(val1, bool) and isinstance(val2, bool):
                if str(val1).lower() != str(val2).lower():
                    print(f"Attribute '{key}' has different values in the two files:")
                    print(f"File 1: {val1}")
                    print(f"File 2: {val2}")
                    return False
            # For other types, directly compare
            elif val1 != val2:
                print(f"Attribute '{key}' has different values in the two files:")
                print(f"File 1: {val1}")
                print(f"File 2: {val2}")
                return False

        print("All attribute values are identical.")
        return True

    if __name__ == "__main__":
        file1_path = r'C:\PROJECTS\PYTHON\work\json_type_of_fields.json'
        file2_path = r'C:\PROJECTS\PYTHON\work\json_type_of_fields_2.json'

        are_identical = compare_json_files(file1_path, file2_path)

        if are_identical:
            print("The attribute values in both JSON files are identical.")
        else:
            print("There are differences in attribute values between the JSON files.")
