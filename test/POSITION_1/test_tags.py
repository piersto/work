import json


def test_tags():
    # Path to your JSON file
    json_file_path = "C:\PROJECTS\PYTHON\work\complex.json"

    # Function to extract all keys (tags)
    def extract_keys(data):
        keys = set()
        if isinstance(data, dict):
            for key, value in data.items():
                keys.add(key)
                keys.update(extract_keys(value))
        elif isinstance(data, list):
            for item in data:
                keys.update(extract_keys(item))
        return keys

    # Read JSON file
    with open(json_file_path, "r") as file:
        json_data = json.load(file)

    # Extract tags
    tags_list = list(extract_keys(json_data))

    # List of tags from specifications
    tags_from_specs = [
        "company",
        "founded_year",
        "employees",
        "name",
        "position",
        "age",
        "departments",
        "contact",
        "email",
        "phone",
        "projects",
        "name",
        "status",
        "start_date",
        "end_date",
        "team",
        "name",
        "role",
        "address",
        "street",
        "city",
        "state",
        "zipcode"
    ]

    # Check if all tags from the extracted list are present in the specifications
    for tag in tags_list:
        assert tag in tags_from_specs, f"Unexpected tag '{tag}' found in the JSON data."

    # Check for missing tags in the specifications
    missing_tags = [tag for tag in tags_from_specs if tag not in tags_list]
    if missing_tags:
        print("The following tags specified in the specifications are missing from the JSON data:")
        for tag in missing_tags:
            print(tag)

    assert not missing_tags, "Some tags specified in the specifications are missing from the JSON data."

    print("All tags present in the JSON data are in the specifications.")
