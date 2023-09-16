import os

source = "C:\\Users\\rober\\PycharmProjects\\hello.txt"
destination = "C:\\Users\\rober\\OneDrive\\Desktop\\hello.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there.")
    else:
        os.replace(source,destination)
        print(source+" was moved.")
except FileNotFoundError:
    print(source+" was not found.")