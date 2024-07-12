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

# move files to corresponding directories
def moveFilesToDir(target_dir):
    file_list = checkFile(target_dir)["files"]
    if file_list:
        try:
            for i in range(len(file_list)):
                ext_name = file_list[i].split('.')[-1]
                source = path.join(target_dir, file_list[i])
                target = path.join(target_dir, ext_name)
                shutil.move(source, target)
                print(f"file {file_list[i]} moved to {ext_name}")
        except Exception as e:
            print("Error Moving Files: ", e)
            print("File Organization Successful!")
    else:
        print("Files Organized")

def main(target_dir):
    createDirectories(target_dir)
    moveFilesToDir(target_dir)

if __name__ == "__main__":
    main(TARGET_DIR)