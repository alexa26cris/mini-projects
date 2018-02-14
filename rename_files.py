import os       #OS
import string

def rename_files():     #function definition
    #1 get the file names from a folder
    file_list = os.listdir(r"path_of_the_folder") #listdir() lists all the files, 'r' means 'raw path'
    print(file_list)
    
    saved_path = os.getcwd()
    print("Current Working directory is: "+saved_path)
    os.chdir("change_the_current_working_directory")
    
    #2 for each file, rename it and remove numbers from the name.
    for file_name in file_list:
        print("Old Name: " + file_name)
        print("New Name: " + file_name.translate(None,'0123456789'))
        os.rename(file_name,file_name.translate(None,'0123456789'))
    os.chdir(saved_path)
    
rename_files()
