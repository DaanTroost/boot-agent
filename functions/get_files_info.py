import pathlib as pl

def get_files_info(working_directory, directory ="."):
    try:
        abs_working_dir = pl.Path(pl.Path.absolute(working_directory))
        abs_target = pl.Path(pl.Path.absolute(pl.Path.joinpath(working_directory, directory)))
        if not abs_target == abs_working_dir and not abs_working_dir in abs_target.parents():
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not pl.Path.is_dir(abs_target):
            return f'Error: "{directory}" is not a directory'
        
        stringbuilder = ""
        for item in pl.Path.iterdir():
            stringbuilder += f"{item.name}: file_size={item.lstat().st_size}, is_dir={pl.Path.is_dir}"
        
        return stringbuilder
    except Exception as e:
        return f'Error: {e}'