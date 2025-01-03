# Function to write content to a file
def write_to_file(filename, content):
    """
    Write content to a file.

    Args:
    filename (str): The name of the file to write to.
    content (str): The content to write to the file.
    """
    with open(filename, "w") as file:
        file.write(content)

# Function to read content from a file
def read_from_file(filename):
    """
    Read content from a file.

    Args:
    filename (str): The name of the file to read from.

    Returns:
    str: The content of the file.
    """
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: The file does not exist."

# Main script
filename = "example.txt"
content = "Hello, this is a test file.\nPython file handling is riveting."

write_to_file(filename, content)  # Write content to the file
print("File written successfully. Now reading the file...")

file_content = read_from_file(filename)  # Read the content of the file
print("File Contents:")
print(file_content)