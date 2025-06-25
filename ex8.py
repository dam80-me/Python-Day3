import os

folder_to_remove = "empty_folder_to_delete"
os.mkdir(folder_to_remove) # Create it for demonstration

try:
    os.rmdir(folder_to_remove)
    print(f"Directory '{folder_to_remove}' removed successfully.")
except OSError as e:
    print(f"Error removing directory '{folder_to_remove}': {e}")
