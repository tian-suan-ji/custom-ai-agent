
import os


def get_file_content(working_directory: str, directory: str) -> str:
    working_directory_absolute = os.path.abspath(working_directory)
    file_path = os.path.join(working_directory_absolute, directory)
    
    if not os.path.isfile(file_path):
        return f"Errorr: Cannot read \"{directory}\" as it is outside the permitted directory"
    