import os
from dotenv import load_dotenv
from file_names import hash_map

load_dotenv()

folder_path = os.getenv('FOLDER_PATH')

if not folder_path:
    raise ValueError("FOLDER_PATH not set in .env file")

def is_executable_file(path):
    return (
        os.path.isfile(path) and os.access(path, os.X_OK)  
    )

def organize(folder_path):
    for file in os.listdir(folder_path):
        old_file_path = os.path.join(folder_path,file)

        if not os.path.isfile(old_file_path):
            continue 

        if is_executable_file(old_file_path):
            os.remove(old_file_path)
            continue
        
        _, ext = os.path.splitext(file)
        if not ext:
            print(f"Skipped file with no extension: {file}")
            continue

        new_folder = hash_map.get(ext.lower(), "others")
        new_folder_path = os.path.join(folder_path,new_folder)
        new_file_path = os.path.join(new_folder_path, file)

        if not os.path.exists(new_folder_path):
            os.mkdir(new_folder_path)
            print(f'New Directory {new_folder_path} created')
            
        os.rename(old_file_path,new_file_path)
        print(f'File {file} moved from {folder_path} to {new_folder_path}')
        print('\n')

organize(folder_path)