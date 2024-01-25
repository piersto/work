import json
import xml.etree.ElementTree as ET

xml_file_path = r'/xml_test.xml'
json_file_path = r'/json_test.json'

def extract_values_from_json(json_file_path):


    with open(json_file_path, 'r') as file:
        data = json.load(file)

    def flatten_json(json_dict):
        values = []
        for key, value in json_dict.items():
            if isinstance(value, dict):
                values.extend(flatten_json(value))
            elif value is None:
                values.append("null")
            elif isinstance(value, (int, float)):
                formatted_value = format(float(value), ".2f")
                print(f"Original value: {value}, Formatted value: {formatted_value}")
                values.append(formatted_value)
            else:
                values.append(str(value))
        return values

    return flatten_json(data)

def extract_values_from_xml(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    def extract_values(element):
        values = []
        for child in element:
            if child.text and child.text.strip():
                values.append(child.text.strip())
            values.extend(extract_values(child))
        return values

    return extract_values(root)

result_list_json = extract_values_from_json(json_file_path)

result_list_xml = extract_values_from_xml(xml_file_path)

print("Values from XML:")
print(result_list_xml)

print("Values from JSON:")
print(result_list_json)

# Compare the two lists using assert
assert result_list_json == result_list_xml, "Lists do not match!"
