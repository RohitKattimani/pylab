import os
# Recursive function to display directory contents
def display_directory(path):
    for item in os.listdir(path):
full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
print("Folder :", item)
display_directory(full_path)   # recursive call
        else:
print("File   :", item)
# Main program
folder_path = input("Enter folder path: ")
if os.path.exists(folder_path):
print("\nContents of directory:\n")
display_directory(folder_path)
else:
print("Invalid path! Folder does not exist.")
