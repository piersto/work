import xml.etree.ElementTree as ET
import json

def extract_data_from_xml_extended_fields(xml_file_path):
    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Extract the namespace from the root element
    namespace = root.tag.split('}')[0][1:]  # Extract namespace without braces

    # Construct the namespace dictionary
    namespace_dict = {'ns': namespace}

    # Locate the 'ExtendedFields' element
    extended_fields_element = root.find('.//ns:ExtendedFields', namespace_dict)

    # If 'ExtendedFields' element is found, proceed with extraction
    if extended_fields_element is not None:
        # Create an empty list to store extracted data
        field_data_list = []

        # Iterate over each 'Field' element within 'ExtendedFields'
        for field_element in extended_fields_element.findall('ns:Field', namespace_dict):
            # Extract values
            field_value = field_element.text
            calcrt_value = field_element.get('calcrt')
            name_value = field_element.get('name')

            # Append to the list
            if field_value:
                field_data_list.append(field_value)
            field_data_list.append(calcrt_value)
            field_data_list.append(name_value)

        # Return the result
        return field_data_list
    else:
        # Return an empty list if 'ExtendedFields' is not found
        return []

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
        elif isinstance(json_value, bool):
            values.append(str(json_value).lower())  # Preserve case for boolean values
        elif isinstance(json_value, (int, float)):
            precision = len(str(json_value).split(".")[1]) if "." in str(json_value) else 0
            formatted_value = format(float(json_value), f".{precision}f")
            values.append(str(formatted_value))
        else:
            values.append(str(json_value))
        return values

    return flatten_json(data)

# Specify the paths to your XML and JSON files
xml_file_path = 'C:\PROJECTS\PYTHON\work\extended_fields.xml'  # Replace with the actual path to your XML file
json_file_path = 'C:\PROJECTS\PYTHON\work\extended_fields.json'  # Replace with the actual path to your JSON file

# Call the functions and store the results for later comparison
result_list_xml = extract_data_from_xml_extended_fields(xml_file_path)
result_list_json = extract_values_from_json(json_file_path)

# Print the results for verification
print("Values from XML:")
print(result_list_xml)

print("Values from JSON:")
print(result_list_json)

# Add an assertion to compare the two lists
assert result_list_json == result_list_xml, "Lists do not match!"
