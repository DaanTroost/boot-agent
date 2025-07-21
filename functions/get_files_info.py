import pathlib as pl

def get_files_info(working_directory, directory ="."):
    try:
        working_dir = pl.Path(working_directory)
        target_dir = pl.Path.joinpath(working_dir, pl.Path(directory))
        abs_working_dir = pl.Path.absolute(working_dir)
        abs_target = pl.Path.absolute(target_dir)
        if not abs_target == abs_working_dir and not abs_working_dir in abs_target.parents:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not pl.Path.is_dir(abs_target):
            return f'Error: "{directory}" is not a directory'
        
        stringbuilder = ""
        for item in abs_target.iterdir():
            stringbuilder += f"{item.name}: file_size={item.lstat().st_size}, is_dir={item.is_dir()}\n"
        
        return stringbuilder
    except Exception as e:
        return f'Error: {e}'