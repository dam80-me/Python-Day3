import os

# List contents of the current directory
print("Contents of current directory:")
for item in os.listdir('.'):
    print(item)

# You can also specify a path
# For example, to list contents of the /temp directory:
# print("\nContents of /tmp directory:")
# for item in os.listdir('/tmp'):
# print(item)