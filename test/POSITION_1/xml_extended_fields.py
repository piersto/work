import xml.etree.ElementTree as ET

def extract_data_from_xml_extended_fields(xml_file_path):
    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Create an empty list to store extracted data
    field_data_list = []

    # Iterate over each 'field' element
    for field_element in root.findall('field'):
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

# Specify the path to your XML file
xml_file_path = 'C:/PROJECTS/PYTHON/work/extended_fields.xml'

# Call the function and store the result for later comparison
result_list = extract_data_from_xml_extended_fields(xml_file_path)

# Print the result for verification
print(result_list)
