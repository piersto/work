import json

def test():
    # Specify the path to your text file
    file_path = 'C:\PROJECTS\PYTHON\work\list_from_txt.txt'
    json_file_path = r'C:\PROJECTS\PYTHON\work\json_for_eod.json'  # Define json_file_path here

    # Define slices
    original_slices = [(1, 5), (6, 9), (10, 12), (13, 30), (31, 40), (41, 45), (45, 47), (47, 49), (50, 51),
                       (51, 63), (64, 72)]

    # Open the file in read mode ('r' for reading)
    with open(file_path, 'r') as file:
        # Read the first line from the file
        first_line = file.readline()

        # Adjust slices to be one index smaller
        adjusted_slices = [(start - 1, end - 1) for start, end in original_slices]

        # Initialize a list to store parsed data
        parsed_data = []

        # Extract data based on adjusted slices for the first line
        for start, end in adjusted_slices:
            # Extract the substring from the line using the adjusted slice
            data = first_line[start:end]

            # Check if the extracted data is not an empty string before appending
            if data.strip():  # This checks if the data is not just whitespace
                parsed_data.append(data)

    # Print the parsed data list
    print("This is txt list:")
    print(parsed_data)

    # Extract values from the JSON file using the correct json_file_path
    result_list_json = extract_values_from_json(json_file_path)

    # Print the parsed data list from the JSON file
    print("This is json list:")
    print(result_list_json)

    # Compare the two lists using assert
    assert parsed_data == result_list_json, "Lists do not match!"

    print("Lists match!")

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
        elif isinstance(json_value, bool):
            values.append("Y" if json_value else "N")
        else:
            values.append(str(json_value))
        return values

    return flatten_json(data)


