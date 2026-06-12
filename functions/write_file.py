
import os
from google.genai import types


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="write to a specified file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path", "content"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file to be written to",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="the changes to be made to the file",
            ),
        },
    ),
)

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_directory_absolute = os.path.abspath(working_directory)
        full_file_path = os.path.join(working_directory_absolute, file_path)
        
        target_file = os.path.normpath(full_file_path)
        
        valid_common_directory = os.path.commonpath([working_directory_absolute, target_file])
        if valid_common_directory != working_directory_absolute:
            return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory"
        
        # check if file is a directory
        if os.path.isdir(target_file):
            return f"Error: Cannot write to \"{file_path}\" as it is a directory"
        
        # create any missing parent directories
        parent_directory = os.path.dirname(target_file)
        os.makedirs(parent_directory, exist_ok=True)
        
        # write to file
        with open(target_file, 'w', encoding="UTF-8") as f:
            f.write(content)
            
            
        return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
    except Exception as e:
        return f"Error: {e}"