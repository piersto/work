def test_binary_to_list():
    # Convert the hexadecimal string to bytes
    hex_string = "4a6f686e20446f652c33302c66616c73652c38352e352c39302c37382e332c313233204d61696e205374"
    binary_data = bytes.fromhex(hex_string)

    # Write the binary data to a file
    with open('data.bin', 'wb') as file:
        file.write(binary_data)

    print("Binary file 'data.bin' has been created.")

