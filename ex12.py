import shutil
import os

# --- Setup: Create a dummy source directory tree ---

source_dir = "my_source_project"
os.makedirs(os.path.join(source_dir, "css"), exist_ok=True)
os.makedirs(os.path.join(source_dir, "js"), exist_ok=True)
with open(os.path.join(source_dir, "index.html"), "w") as f:
    f.write("<html></html>")
with open(os.path.join(source_dir, "css", "style.css"), "w") as f:
    f.write("body{}")
print(f"Created dummy source directory: '{source_dir}'.")

#--- Copy the directory tree ---
destination_dir ="my_backup_project"
try:
    # If destination_dir already exists  and is not empty, copytree wil
    # To overwrite, you'd typically remove the destination first or ha
    shutil.copytree(source_dir, destination_dir)
    print(f"'{source_dir}' copied to '{destination_dir}' successfully.")
    print(" Contents of destination directory")
    print (os.walk(destination_dir))

    for root, dirs, files in os.walk(destination_dir):
        level = root.replace(destination_dir, '').count(os.sep)
        indent = ''*4*(level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ''*4*(level+1)
        for f in files:
            print(f"{subindent}{f}")
except FileExistsError:
    print(f"Error: Destination directory '{destination_dir}' already exists.")
except Exception as e:
    print(f"An error occured during copytree: {e}")

# --- Cleanup---
    if os.path.exists(source_dir):
        shutil.rmtree(source_dir)
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    print("Cleaned up dummy directories.")


