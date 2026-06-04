
import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    
    try:
        if not os.path.isdir(directory):
            return f"\"{directory}\" is not a directory"

        working_directory_absolute = os.path.abspath(working_directory)
        
        full_directory = os.path.join(working_directory_absolute, directory)
        
        target_directory = os.path.normpath(full_directory)
        
        valid_common_directory = os.path.commonpath([working_directory_absolute, target_directory])
        
        if valid_common_directory != working_directory_absolute:
            return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
        # get files in target path
        directory_contents = ""
        for item in os.listdir(target_directory):
            #item = os.path.abspath(item)
            item_abs = os.path.join(full_directory, item)
            
            directory_contents += f"{item}: file_size={os.path.getsize(item_abs)} bytes, is_dir={os.path.isdir(item_abs)}"
            if item != os.listdir(target_directory)[-1]:
                directory_contents += "\n"
            
        print(directory_contents)
        if os.path.exists(target_directory):
            return f"Success: \"{directory}\" is within the working directory"
    
    except Exception as e:
        return f"Error: {e}"