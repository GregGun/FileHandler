import os

file_name = "dummy.txt"

if os.path.exists(file_name):
    os.remove(file_name)
    print("Removed " + file_name)
else:
    print("File " + file_name + " does not exists.")
