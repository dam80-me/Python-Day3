import os

current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")


# Define the directory you want to change to
# Make sure this directory exists on your system
new_directory ="./tmp" #Example for Linum/MacOS
# For Windows it might be something like "C:\\Users\\YourUser\\Domuments"
print(os.path.basename)
if os.path.exists(new_directory) and os.path.isdir(new_directory):
    os.chdir(new_directory)
    print(f"Changed Directory to: {os.getcwd()}")
else:
    print(f"Directory '{new_directory}' does not exist or is not a d")