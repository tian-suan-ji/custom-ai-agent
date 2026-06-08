
import os
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="list the contents of a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="""list a file's content from within the working directory""",
            ),
        },
    ),
)

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_directory_absolute = os.path.abspath(working_directory)
        full_file_path = os.path.join(working_directory_absolute, file_path)
        
        if not os.path.isdir(full_file_path):
            return f"Errorr: Cannot read \"{file_path}\" as it is outside the permitted directory"
        
        target_file = os.path.normpath(full_file_path)
        
        valid_common_directory = os.path.commonpath([working_directory_absolute, target_file])
        if valid_common_directory != working_directory_absolute:
            return f"Error: File not found or is not a regular file {file_path}"
        
        # read file
        with open(target_file, 'r', encoding="UTF-8") as f:
            content = f.read(10_000)
            
            if f.read(1) != '':
                content += f"[...File \"{file_path}\" truncated at 10_000 characters]"
            return content
    except Exception as e:
        return f"Error: {e}"