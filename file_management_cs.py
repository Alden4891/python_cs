# File Management Cheat Sheet

# Open File:
# Comment: Opens a file and returns a file object.
# Syntax: open(filename, mode)
# Modes:
# 'r' - Read (default)
# 'w' - Write (creates a new file or truncates an existing file)
# 'a' - Append (writes to the end of a file)
# 'b' - Binary mode (e.g., 'rb' or 'wb')

# Example - Open a file for reading:
file = open("example.txt", "r")

# Example - Open a file for writing:
file = open("example.txt", "w")

# Example - Open a file for appending:
file = open("example.txt", "a")

# Close File:
# Comment: Closes the file to free up resources.
# Syntax: file.close()
file.close()

# Using Context Manager (Preferred Approach):
# Comment: Automatically closes the file when done.
# Syntax: with open(filename, mode) as file: ...
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading from File:
# Comment: Reads content from a file.
# Syntax: file.read(size) or file.readline() or file.readlines()
# Example - Read entire file:
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Example - Read one line at a time:
with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()

# Example - Read all lines into a list:
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')

# Writing to File:
# Comment: Writes content to a file.
# Syntax: file.write(string) or file.writelines(list_of_strings)
# Example - Write string to file:
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")

# Example - Write multiple lines to file:
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)

# Appending to File:
# Comment: Adds content to the end of a file.
# Syntax: open(filename, "a")
# Example - Append string to file:
with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")

# File Positioning:
# Comment: Move cursor to a specific position in the file.
# Syntax: file.seek(offset, whence)
# whence: 0 - absolute file positioning (default), 1 - relative to current position, 2 - relative to file end
# Example - Move to the beginning of the file:
with open("example.txt", "r") as file:
    file.seek(0)
    content = file.read()
    print(content)

# Getting File Information:
# Comment: Get file attributes and metadata.
# Syntax: os.stat(filename)
# Example - Get file size:
import os
file_info = os.stat("example.txt")
print(f"File size: {file_info.st_size} bytes")

# Renaming or Moving a File:
# Comment: Rename or move a file.
# Syntax: os.rename(old_filename, new_filename)
# Example - Rename a file:
os.rename("example.txt", "new_example.txt")

# Deleting a File:
# Comment: Delete a file from the filesystem.
# Syntax: os.remove(filename)
# Example - Remove a file:
os.remove("new_example.txt")

# Checking File Existence:
# Comment: Check if a file exists.
# Syntax: os.path.exists(filename)
# Example - Check if file exists:
if os.path.exists("example.txt"):
    print("File exists.")
else:
    print("File does not exist.")

# Creating and Removing Directories:
# Comment: Create or remove directories.
# Syntax: os.mkdir(directory_name) or os.rmdir(directory_name)
# Example - Create a directory:
os.mkdir("new_directory")

# Example - Remove a directory:
os.rmdir("new_directory")

# Listing Files in a Directory:
# Comment: List files and directories.
# Syntax: os.listdir(directory_name)
# Example - List files in the current directory:
files = os.listdir(".")
print(files)
