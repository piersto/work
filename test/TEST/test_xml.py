# Working XML

import json
import xml.etree.ElementTree as ET
from decimal import Decimal


xml_file_path = r'C:\PROJECTS\PYTHON\work\xml_test.xml'
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
        elif isinstance(json_value, float):
            # Determine precision of the original value using decimal module
            precision = -Decimal(str(json_value)).as_tuple().exponent
            formatted_value = format(float(json_value), f".{precision}f")
            values.append(str(formatted_value))
        else:
            values.append(str(json_value))
        return values

    return flatten_json(data)

def extract_values_from_xml(xml_element, include_tags=True):
    values = []
    if include_tags and xml_element.text and xml_element.text.strip():
        values.append(xml_element.text.strip())
    for child in xml_element:
        values.extend(extract_values_from_xml(child, include_tags))
    return values

def extract_values_from_xml_file(xml_file_path, include_tags=True):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    return extract_values_from_xml(root, include_tags)

result_list_json = extract_values_from_json(json_file_path)
result_list_xml = extract_values_from_xml_file(xml_file_path)

print("Values from XML:")
print(result_list_xml)

print("Values from JSON:")
print(result_list_json)

# Compare the two lists using assert
assert result_list_json == result_list_xml, "Lists do not match!"
