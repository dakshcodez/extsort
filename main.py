import os
from dotenv import load_dotenv

load_dotenv()

folder_path = os.getenv('FOLDER_PATH')

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


def organize(folder_path):
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path,file)):
            ext = file[file.index('.'):]
            new_folder = hash_map[ext]

            old_file_path = os.path.join(folder_path,file)
            
            new_folder_path = os.path.join(folder_path,new_folder)
            new_file_path = os.path.join(new_folder_path, file)

            if not os.path.exists(new_folder_path):
                os.mkdir(new_folder_path)
                print("file created")

            

organize(folder_path)