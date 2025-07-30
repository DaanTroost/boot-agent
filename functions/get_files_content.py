import pathlib as pl
from google.genai import types

from config import MAX_FILE_READ

def get_files_content(working_directory, file_path):
    try:
        working_dir = pl.Path(working_directory)
        target_dir = pl.Path.joinpath(working_dir, pl.Path(file_path))
        abs_working_dir = pl.Path.absolute(working_dir)
        abs_target = pl.Path.absolute(target_dir)
        if not abs_target == abs_working_dir and not abs_working_dir in abs_target.parents:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        
        if not pl.Path.is_file(abs_target):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        file_content = ""
        with open(abs_target, "r") as file:
            file_content = file.read(MAX_FILE_READ)
            if len(file_content) == MAX_FILE_READ:
                file_content += f'[...File "{file_path}" truncated at {MAX_FILE_READ} characters]'
        return file_content
            
    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_FILE_READ} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)