import os               # Operating System walkthrough from the folder which is present in the main folder
import shutil           # Library which is used for a copying or cut of file one folder to another folder paste

source_folder = '/home/ritesh/Desktop/Source_folder'
target_folder ='/home/ritesh/Desktop/Target_folder'

print("-------------------------Source_Folder--------------------------------")
file_extensions = (".txt",".yaml",".conf",".py")
for dirs, subdirs, files in os.walk(source_folder):
    for file in files:
        if file.endswith(file_extensions):
            print(f"File_Name: -{file}")
            filename = os.path.join(source_folder,dirs,file)
            if os.path.exists(filename):
                print(f"File_Path: -{filename}")
                shutil.copy(filename,target_folder)
print("----------------------------------------------------------------------")

print("-------------------------Target_Folder--------------------------------")
print("Target_Folder_File_Count: -",len(os.listdir(target_folder)))
print("----------------------------------------------------------------------")
