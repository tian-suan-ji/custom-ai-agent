
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
        
        
        # normalize file path
        target_file_path = os.path.normpath(file_path_absolute)
        
        valid_common_directory = os.path.commonpath([working_directory_absolute, target_file_path])
        if valid_common_directory != working_directory_absolute:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # validate file on disc
        if not os.path.isfile(target_file_path):
            return f"Error: \"{file_path}\" does not exist or is not a regular file"
        
        # is file extension python
        if not file_path.endswith(".py"):
            return f"Error: \"{file_path}\" is not a Python file"
        
        # create command
        command = ["python", target_file_path]
        if args is not None:
            command.extend(args)
        
        # subprocess
        status = subprocess.run(command, cwd=working_directory_absolute, text=True, capture_output=True, timeout=30)
        
        # validate status
        output = []
        if status.returncode != 0:
            output.append(f"Process exited with code {status.returncode}")
        if not status.stdout and not status.stderr:
            output.append("No output produced")
        
        if status.stdout:
            output.append(f"STDOUT:\n{status.stdout}")
        if status.stderr:
            output.append(f"STDERR:\n{status.stderr}")
        return '\n'.join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"

