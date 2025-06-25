import shutil
import os

# --- Setup: Create a dummy source file ---
source_file = "source_doc.txt"
with open(source_file, "w") as f:
    f.write("This is the original content.")
print(f"Created '{source_file}' for copying.")

#--- Copy the filee ---
destination_file ="copied_doc.txt"
try:
    shutil.copy(source_file, destination_file)
    print(f"'{source_file}' copied to '{destination_file}' successfully.")
    print(f"Content of '{destination_file}':{open(destination_file).read()}")
    #print (os.walk(source_file_file))
except FileNotFoundError:
    print(f"Error: Source file '{source_file}' not found.")
except Exception as e:
    print(f"An error occured during copy: {e}")

"""
# --- Cleanup---
    if os.path.exists(source_dir):
        shutil.rmtree(source_dir)
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    print("Cleaned up dummy directories.")"""

