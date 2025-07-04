import pathlib
import os


#print(f"Path did not exist for cleanup: {path}")

# ---1. Creating Path Objects---
print("\n---1. Creating Path Objects---")
#Current working directory
print(pathlib.Path)
current_dir=pathlib.Path.cwd()
print(f"Current working directory (Path object): {current_dir}")

# A relative path
relative_file = pathlib.Path('my_document.txt')
print(f"Relative file path: {relative_file}")

# An absolute path (example, adjust)
absolute_path = pathlib.Path('/tmp/test_dir')

print(f"Absolute path (example): {absolute_path}")


"""
print("")
# --- Setup: Create a dummy directory for archiving ---

data_folder = "my_data_for_archive"
os.makedirs(os.path.join(data_folder, "docs"), exist_ok=True)
with open(os.path.join(data_folder, "important.txt"), "w") as f:
    f.write("Important data here.")
with open(os.path.join(data_folder, "docs", "notes.md"), "w") as f:
    f.write("# Meeting Notes")
print(f"Created dummy folder for archiving:'{data_folder}' .")

#--- Create a Zip archive---
archive_name = "my_data_archive"
try:
    # Creates my_data_archive.zip in the current directory,
    # containing the contents of my_data_for_archive
    archive_path = shutil.make_archive(archive_name, 'zip', root_dir=data_folder)
    print(f"Archive created: '{archive_path}'")
    print(f"Does archive exist? {os.path.exists(archive_path)}")
except Exception as e:
    print(f"An error occured during archiviny: {e}")  
 
# --- Cleanup---
if os.path.exists(data_folder):
        shutil.rmtree(data_folder)
if os.path.exists(archive_path):
        os.remove(archive_path)
print("Cleaned up dummy files and archives.")"""