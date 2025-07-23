import pathlib as pl

def write_file(working_file_path, file_path, content):
    try:
        working_dir = pl.Path(working_file_path)
        target_dir = pl.Path.joinpath(working_dir, pl.Path(file_path))
        abs_working_dir = pl.Path.absolute(working_dir)
        abs_target = pl.Path.absolute(target_dir)
        if not abs_target == abs_working_dir and not abs_working_dir in abs_target.parents:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working file_path'
        
        with open(abs_target, "w") as target_file:
            target_file.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'