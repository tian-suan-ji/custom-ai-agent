
import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_directory_absolute = os.path.abspath(working_directory)
        absolute_file_path = os.path.join(working_directory_absolute, file_path)

        if not os.path.isfile(absolute_file_path):
            return f"Errorr: Cannot read \"{file_path}\" as it is outside the permitted directory"
        
        # normalize path
        target_file_path = os.path.normpath(absolute_file_path)
        
        if os.path.isdir(target_file_path):
            return f"Error: Cannot write to \"{file_path}\" as as it is a directory"
        
        # create any missing parent directories
        os.makedirs(target_file_path, exist_ok=True)
        
        # common absolute path
        common_path = os.path.commonpath([working_directory_absolute, target_file_path])

        if common_path != working_directory_absolute:
            return f"Error: File not found or is not a regular file {file_path}"
        
        # write to file
        with open(target_file_path, 'w', encoding="UTF-8") as f:
            new_content = f.write(content)
            
        return f"Successfully wrote to \"{file_path}\" {len(new_content)} characters written"
    except Exception as e:
        return f"Error: {e}"