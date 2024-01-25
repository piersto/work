import json


def test_test():
    import json

    def count_trailing_zeros(json_data, path=""):
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                new_path = f"{path}.{key}" if path else key
                count_trailing_zeros(value, new_path)
        elif isinstance(json_data, list):
            for i, item in enumerate(json_data):
                new_path = f"{path}[{i}]"
                count_trailing_zeros(item, new_path)
        elif isinstance(json_data, float):
            str_value = format(json_data, 'f')  # Format as string without removing trailing zeros
            if "." in str_value:
                decimal_part = str_value.split(".")[1]
                num_zeros = len(decimal_part)
                print(f'"{path}": has {num_zeros} zeros after the decimal')

    # Load the JSON data
    json_file_path = r'/json_test.json'
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Count trailing zeros after the decimal for each "projectId"
    count_trailing_zeros(data)
