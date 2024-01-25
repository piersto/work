import json

def test_json():
    json_file_path = r'C:\PROJECTS\PYTHON\work\json_test.json'

    def extract_values_from_json(json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        def flatten_json(json_value):
            values = []
            if isinstance(json_value, dict):
                for key, value in json_value.items():
                    values.extend(flatten_json(value))
            elif isinstance(json_value, list):
                for item in json_value:
                    values.extend(flatten_json(item))
            elif isinstance(json_value, (int, float)):
                # Determine precision of the original value
                precision = len(str(json_value).split(".")[1]) if "." in str(json_value) else 0
                formatted_value = format(float(json_value), f".{precision}f")
                values.append(str(formatted_value))
            else:
                values.append(str(json_value))
            return values

        return flatten_json(data)

    result_list_json = extract_values_from_json(json_file_path)

    print("Values from JSON:")
    print(result_list_json)
