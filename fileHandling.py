# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line of text\n")
except IOError:
    print("An error occurred while creating the file.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You do not have permission to read the file.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is line 4\n")
        file.write("67890\n")
        file.write("Yet another line of text\n")
except IOError:
    print("An error occurred while appending to the file.")

# Error Handling
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You do not have permission to read the file.")
finally:
    print("Error handling example complete.")
