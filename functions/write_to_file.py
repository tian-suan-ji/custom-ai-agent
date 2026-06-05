
import os


def write_to_file(working_directory: str, file_path: str, content) -> None -> str:
    working_directory_absolute = os.path.abspath(working_directory)
    absolute_file_path = os.path.join(working_directory_absolute, file_path)

    if not os.path.isfile(absolute_file_path):
        return f"Errorr: Cannot read \"{file_path}\" as it is outside the permitted directory"
    
    # normalize path
    target_file_path = os.path.normpath(absolute_file_path)
    
    if os.path.isdir(target_file_path):
        return f"Error: Cannot write to \"{file_path}\" as as it is a directory"
    
    # common absolute path
    common_path = os.path.commonpath([working_directory_absolute, target_file_path])
    