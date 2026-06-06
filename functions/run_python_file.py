
import os


def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    working_directory_absolute = os.path.abspath(working_directory)
    file_path_absolute = os.path.join(working_directory_absolute, file_path)
    
    # validate path
    if not os.path.isdir(file_path_absolute):
        return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"
    
    # normalize file path
    target_file_path = os.path.normpath(file_path_absolute)
    
    # validate file on disc
    if not os.path.isfile(target_file_path):
        return f"Error: \"{file_path}\" does not exist or is not a regular file"
    
    # is file extension python
    if not file_path.endswith("py"):
        return f"Error: \"{file_path}\" is not a Python file"
