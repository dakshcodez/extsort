import os
from dotenv import load_dotenv

load_dotenv()

folder_path = os.getenv('FOLDER_PATH')

if not folder_path:
    raise ValueError("FOLDER_PATH not set in .env file")

hash_map = {
    ".txt": "text_file",
    ".py": "python",
    ".c": "c",
    ".cpp": "c++",
    ".js": "javascript",
    ".java": "java",
    ".rb": "ruby",
    ".go": "go",
    ".php": "php",
    ".html": "html",
    ".css": "css",
    ".json": "json",
    ".xml": "xml",
    ".sh": "shell_script",
    ".md": "markdown",
    ".ts": "typescript",
    ".swift": "swift",
    ".kt": "kotlin",
    ".rs": "rust",
    ".scala": "scala",
    ".pl": "perl",
    ".bat": "batch_file",
    ".sql": "sql",
    ".r": "r",
    ".dart": "dart",
    ".erl": "erlang",
    ".hs": "haskell",
}

def is_executable_file(path):
    return (
        os.path.isfile(path) and os.access(path, os.X_OK)  
    )

def organize(folder_path):
    for file in os.listdir(folder_path):
        old_file_path = os.path.join(folder_path,file)

        if os.path.isfile(old_file_path) and not is_executable_file(old_file_path):
            ext = file[file.find('.'):]
            new_folder = hash_map[ext]
            
            new_folder_path = os.path.join(folder_path,new_folder)
            new_file_path = os.path.join(new_folder_path, file)

            if not os.path.exists(new_folder_path):
                os.mkdir(new_folder_path)
                print(f'New Directory {new_folder_path} created')
            
            os.rename(old_file_path,new_file_path)
            print(f'File {file} moved from {folder_path} to {new_folder_path}')
            print('\n')

        elif is_executable_file(old_file_path):
            os.remove(old_file_path)

organize(folder_path)