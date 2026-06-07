
import os
from google.genai import types

# determine the available function
schema_get_files_info = types.FunctionDeclaration(
    # describes the function and its purpose
    name="get_files_info",
    description="lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        # describes function type and its acceptable argument types
        type=types.Type.OBJECT,
        properties={
            # describes function parameters in a hashmap
            # key is parameter name
            # value is a typees.Schema function call of key's expected value type
            "directory": types.Schema(
                # describe type of expected type and its purpose
                type=types.Type.STRING,
                description="path to list files from relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_directory_absolute = os.path.abspath(working_directory)
        full_directory = os.path.join(working_directory_absolute, directory)
        
        if not os.path.isdir(full_directory):
            return f"\"{directory}\" is not a directory"
        
        target_directory = os.path.normpath(full_directory)
        
        # prepare to print resulsts of the directory
        print(f"Result for \"{directory}\" directorry:")
        
        valid_common_directory = os.path.commonpath([working_directory_absolute, target_directory])
        if valid_common_directory != working_directory_absolute:
            return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
        
        # get files in target path
        directory_contents = ""
        try:
            for item in os.listdir(target_directory):
                item_abs = os.path.join(full_directory, item)
                
                directory_contents += f"{item}: file_size={os.path.getsize(item_abs)} bytes, is_dir={os.path.isdir(item_abs)}"
                if item != os.listdir(target_directory)[-1]:
                    directory_contents += "\n"
        except Exception as e:
            return f"Error: {e}"
        print(directory_contents)
        if os.path.exists(target_directory):
            return f"Success: \"{directory}\" is within the working directory"
    
    except Exception as e:
        return f"Error: {e}"