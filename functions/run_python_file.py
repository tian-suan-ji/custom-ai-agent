
import os


def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    working_directory_absolute = os.path.abspath(working_directory)
    file_path_absolute = os.path.join(working_directory_absolute, file_path)
    
    # validate path
    if not os.path.isdir(file_path_absolute):
        return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"
    
