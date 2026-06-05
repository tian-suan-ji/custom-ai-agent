
import os


def write_to_file(working_directory: str, file_path: str, content) -> None -> str:
    working_directory_absolute = os.path.abspath(working_directory)
    absolute_file_path = os.path.join(working_directory_absolute, file_path)
    
    # normalize path
    target_file_path = os.path.normpath(absolute_file_path)
    
    # common absolute path
    common_path = os.path.commonpath([working_directory_absolute, target_file_path])
    