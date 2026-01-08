# ## 🟢 Level 1: Absolute Basics

# 1. **Get Current Directory**
#    Write a program to print the current working directory using the `os` module.
import os 
# print(os.getcwd())

# 2. **List Files**
#    Given a directory path, list all files and folders inside it.
# print(os.getlogin())
# ---

# ## 🟡 Level 2: File & Path Handling

# 3. **Check Path Type**
#    Given a path, check whether it exists.
#    If it exists, tell whether it is a **file** or a **directory**.

path = "/desktop/python-practice"

if os.path.exists(path):
    if os.path.isfile(path):
        print("It is a file")
    elif os.path.isdir(path):
        print("It is a directory")
else:
    print("Path does not exist")


# 4. **Create Directory Safely**
#    Create a directory named `logs`.
#    The program should **not crash** if the directory already exists.

# 5. **Join Paths Correctly**
#    Join the directory `/home/user` with the filename `data.txt` in an OS-independent way.

# ---

# ## 🟠 Level 3: File Operations

# 6. **Rename Files in Bulk**
#    In a directory, rename all `.txt` files by prefixing them with `backup_`.

# 7. **Delete Empty Files**
#    Find and delete all files of size `0 bytes` in a given directory.

# ---

# ## 🔵 Level 4: Directory Traversal

# 8. **Recursive File Search**
#    Recursively search a directory and print the full path of all `.py` files.

# 9. **Directory Statistics Tool**
#    For a given directory, print:

#    * Total number of files
#    * Total number of folders
#    * Total size (in MB)

# ---

# ## 🔴 Level 5: Real-World Automation

# 10. **Auto File Organizer**
#     Given a folder containing mixed files (`.pdf`, `.jpg`, `.py`, `.txt`):

# * Create folders based on file extensions
# * Move each file into its respective folder
#   Example: all `.pdf` → `pdf/`, `.jpg` → `jpg/`

