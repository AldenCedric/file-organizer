# OBJECTIVES
from os import listdir, path, mkdir
import shutil

# Usage: TARGET_DIR = "{output_files}"
TARGET_DIR = ""

# list files in a directory
def listFiles(target_dir):
    files = listdir(target_dir)
    return files