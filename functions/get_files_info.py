
import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        if not os.path.isdir(directory):
            return f"\"{directory}\" is not a directory"

        working_directory_absolute = os.path.abspath(working_directory)
        full_directory = os.path.join(working_directory_absolute, directory)
        target_directory = os.path.normpath(full_directory)
        
        valid_common_directory = os.paath.commonpath(working_directory, target_directory)
        if valid_common_directory != working_directory:
            return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
        
        if os.path.exists(target_directory):
            return f"\"{target_directory}\" is within the working directory"
    
    except Exception as e:
        return f"Error: {e}"

