import os
# Create a new file for testing file handler
# File will be created as dummy.txt and text file
file_name = "dummy.txt"

if os.path.exists(file_name):
    print("File " + file_name + " already exists.")
else:
    file = open(file_name, "xt")

