import xml.etree.ElementTree as ET

def test_extract_tags_from_xml():
    # Parse the XML file
    tree = ET.parse(r'C:\PROJECTS\PYTHON\work\xml_test.xml')
    root = tree.getroot()


    # Function to extract tags recursively
    def extract_tags(element):
        tags = [element.tag]
        for child in element:
            tags.extend(extract_tags(child))
        return tags


    # Extract tags from the root element
    all_tags = extract_tags(root)

    # Print the list of tags
    print(all_tags)
