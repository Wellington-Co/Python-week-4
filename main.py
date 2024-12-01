#filename
filename = input("Enter the filename to read from: ")

try:
    # Open the file 
    with open(filename, 'r') as file:
        content = file.read()

    # Modify the content: Adjust spacing between words (replace multiple spaces with a single space)
    modified_content = ' '.join(content.split())

    # Write the modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, 'w') as new_file:
        new_file.write(modified_content)

    print(f"File has been modified and saved as {new_filename}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: There was an issue reading the file '{filename}'.")
