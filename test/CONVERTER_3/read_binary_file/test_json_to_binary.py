import json


def test_binary():
    # JSON data
    data = {
        "name": "John Doe",
        "age": 30,
        "is_student": False,
        "grades": [
            85.5,
            90,
            78.3
        ],
        "address": {
            "street": "123 Main St",
            "city": "Exampletown"
        }
    }

    # Convert JSON to bytes
    binary_data = json.dumps(data).encode('utf-8')

    # Write binary data to a file
    with open('data.bin', 'wb') as file:
        file.write(binary_data)

    print("Data has been written to data.bin")
