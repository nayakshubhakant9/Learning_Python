# Write a python program to print the contents of a directory using the os module. search online for the function which does that.
import os

def print_directory_contents(directory_path):
    try:
        for item in os.listdir(directory_path):
            print(item)
    except FileNotFoundError:
        print("Directory not found.")
    except PermissionError:
        print("Permission denied.")

# Replace 'your_directory_path_here' with the path you want to check
directory_path = "/"
print_directory_contents(directory_path)
