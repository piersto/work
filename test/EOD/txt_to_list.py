def test():
    import xml.etree.ElementTree as ET

    # Specify the path to your text file
    file_path = 'C:\PROJECTS\PYTHON\work\list_from_txt.txt'
    xml_file_path = r'C:\PROJECTS\PYTHON\work\xml_test.xml'

    # Define slices
    original_slices = [(1, 5), (6, 9), (10, 12), (13, 30), (31, 40), (41, 45), (45, 47), (47, 49), (50, 51),
                       (51, 63), (64, 72)]

    def parse_text_file(file_path, original_slices):
        # Adjust slices to be one index smaller
        adjusted_slices = [(start - 1, end - 1) for start, end in original_slices]

        # Open the file in read mode ('r' for reading)
        with open(file_path, 'r') as file:
            # Initialize a list to store parsed data from each line
            parsed_data_list = []

            # Iterate through each line in the file
            for line in file:
                # Initialize an empty list to store the parsed data for the current line
                parsed_data = []

                # Extract data based on adjusted slices
                for start, end in adjusted_slices:
                    # Extract the substring from the line using the adjusted slice
                    data = line[start:end]

                    # Check if the extracted data is not an empty string before appending
                    if data.strip():  # This checks if the data is not just whitespace
                        parsed_data.append(data)

                # Append the parsed data for the current line to the parsed_data_list
                parsed_data_list.append(parsed_data)

        # Return the list of parsed data for all lines
        return parsed_data_list

    # Call the function to parse the text file and get the returned list
    returned_list = parse_text_file(file_path, original_slices)

    # Print the parsed data list
    print(returned_list)

# Call the test function
test()
