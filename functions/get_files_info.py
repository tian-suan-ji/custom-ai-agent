
import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    working_directory = os.path.abspath(working_directory)
    directory = os.path.join(working_directory, directory)
    target_path = os.path.normpath(directory)