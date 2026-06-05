
import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_directory_absolute = os.path.abspath(working_directory)
        full_file_path = os.path.join(working_directory_absolute, file_path)
        
        if os.path.isdir(full_file_path):
            return f"Errorr: Cannot write to \"{file_path}\" as it is outside the permitted directory"
        
        target_file = os.path.normpath(full_file_path)
        
        valid_common_directory = os.path.commonpath([working_directory_absolute, target_file])
        if valid_common_directory != working_directory_absolute:
            return f"Error: File not found or is not a regular file {file_path}"
        # second second validation
# create any missing parent directories
        if not os.path.exists(os.path.dirname(target_file)):
            os.makedirs(target_file, exist_ok=True)
        
        # write to file
        with open(target_file, 'w', encoding="UTF-8") as f:
            f.write(content)
            
            
            return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
    except Exception as e:
        return f"Error: {e}"