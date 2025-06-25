import os

path_to_check_file = "C://Users/Student_15/Python Day3/my_existing_file.txt"
path_to_check_dir = "C://Users/Student_15/Python Day3"

# Creates a dummy for demonstration
with open(path_to_check_file, 'w') as f:
    f.write("Hello")
os.makedirs(path_to_check_dir, exist_ok=True)


if os.path.exists(path_to_check_file):
    print(f"'{path_to_check_file}' exists.")
else:
    print(f"'{path_to_check_file}' does not exist.")

if os.path.exists(path_to_check_dir):
    print(f"'{path_to_check_dir}' exists.")
else:
    print(f"'{path_to_check_dir}' does not exist.")