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
