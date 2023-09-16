import os
import shutil

path = 'bye.txt'

try:
    os.remove(path) # <-------- To remove a file
    #os.rmdir(path)  # <-------- To delete an empty folder
    #shutil.rmtree(path) # <-------- Deletes all files and the directory containing it. !!!DANGEROUS!!!
except FileNotFoundError:
    print("That file was not found.")
except PermissionError:
    print("You do not have permission to delete that.")
except NotADirectoryError:
    print("That is not a directory.")
except OSError:
    print("You cannot delete that using that function.")
else:
    print(path+" was deleted.")