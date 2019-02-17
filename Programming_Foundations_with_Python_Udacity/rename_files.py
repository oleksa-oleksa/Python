import os

def rename_files():
    # 1. get file names from the folder
    file_list = os.listdir("img")
    print(file_list)
    saved_path = os.getcwd()
    print("Started at " + saved_path)
    os.chdir("./img")
    cur_path = os.getcwd()
    print("Current folders " + cur_path)

    # 2. for each file, rename the filename
    for file_name in file_list:
        os.rename(file_name, (file_name.translate(None, "0123456789")))
    os.chdir(saved_path)

rename_files()