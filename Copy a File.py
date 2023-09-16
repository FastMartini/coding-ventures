# copyfile() = copies content of a file
# copy() = copyfile() + permission mode + destruction can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

source = "C:\\Users\\rober\\OneDrive\\Desktop\\hello.txt"
destination = "C:\\Users\\rober\\OneDrive\\Desktop\\folder"
try:
    shutil.copy(source, destination)    # src.dst
except FileNotFoundError:
    print("That file could not be traced to copy.")
except PermissionError:
    print("You do not have permission to delte that")
else:
    print(source+" has been successfully copied to "+destination+".")
