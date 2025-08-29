def modify_content(content):
    # Example modification: convert to uppercase
    return content.upper()

def process_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as infile:
            original_content = infile.read()
            modified_content = modify_content(original_content)

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Could not read or write to the file.")

process_file()
