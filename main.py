# OBJECTIVES
from os import listdir, path, mkdir
import shutil

# Usage: TARGET_DIR = "{output_files}"
TARGET_DIR = ""

# list files in a directory
def listFiles(target_dir):
    files = listdir(target_dir)
    return files

# check files (folders or files)
def checkFile(target_dir):
    folders = []
    files = []
    files_list = listFiles(target_dir)

    for i in files_list:
        try:
            listFiles(path.join(target_dir, i))
            folders.append(i)
        except:
            files.append(i)

    return{"folders": folders, "files": files}

# check extension name
def checkExt(target_dir):
    ext_list = []
    files_list = checkFile(target_dir)["files"]
    for i in files_list:
        ext_list.append(i.split('.')[-1])

    filtered_ext = list(dict.fromkeys(ext_list))
    return filtered_ext

# create directories
def createDirectories(target_dir):
    for i in checkExt(target_dir):
        try:
            mkdir(path.join(target_dir, i))
            print(f"Folder {i} Created")
        except:
            print(f"Folder {i} Exist")
            