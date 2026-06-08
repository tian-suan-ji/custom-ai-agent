
import os
import subprocess
from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="run a python file and any special given arguments within the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The executable file to be run",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="each argument is a string",
                ),
                description="arguments to supply to executable file",
            ),
        },
    ),
)

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_directory_absolute = os.path.abspath(working_directory)
        file_path_absolute = os.path.join(working_directory_absolute, file_path)
        
        # validate path
        if os.path.isdir(file_path_absolute):
            return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"
        
        # normalize file path
        target_file_path = os.path.normpath(file_path_absolute)
        
        # validate file on disc
        if not os.path.isfile(target_file_path):
            return f"Error: \"{file_path}\" does not exist or is not a regular file"
        valid_common_directory = os.path.commonpath([working_directory_absolute, target_file_path])
        if valid_common_directory != working_directory_absolute:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # is file extension python
        if not file_path.endswith("py"):
            return f"Error: \"{file_path}\" is not a Python file"
        
        # create command
        command = ["python", file_path_absolute]
        if args is not None:
            command.extend(args)
        
        # subprocess
        status = subprocess.run(command, cwd=working_directory_absolute, text=True, capture_output=True, timeout=30)
        
        # validate status
        if status.returncode != 0:
            return f"Process exited with code {status.returncode}"
        elif status.stdout is None and status.stderr is None:
            return "no output produced"
        else:
            return f"STDOUT: {status.stdout} STDERR: {status.stderr}"
    except Exception as e:
        return f"Error: Executing Python file: {e}"

