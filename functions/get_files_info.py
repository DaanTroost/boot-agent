import os
import pathlib as pl

def get_files_info(working_directory, directory ="."):
    abs_working_dir = pl.Path(os.path.abspath(working_directory))
    abs_target = pl.Path(os.path.join(os.path.abspath(working_directory, directory)))
    if not abs_target == abs_working_dir and not abs_working_dir in abs_target.parents():
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    


