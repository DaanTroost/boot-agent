import pathlib as pl
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        working_dir = pl.Path(working_directory)
        target_dir = pl.Path.joinpath(working_dir, pl.Path(file_path))
        abs_working_dir = pl.Path.absolute(working_dir).resolve()
        abs_target = pl.Path.absolute(target_dir).resolve()
        if not abs_target == abs_working_dir and not abs_working_dir in abs_target.parents:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not abs_target.is_file():
            return f'Error: File "{file_path}" not found.'
        
        if not abs_target.suffix == ".py":
            return f'Error: "{file_path}" is not a Python file.'
        process_args = ["python", abs_target] + args
        process = subprocess.run(process_args, capture_output=True, cwd=abs_working_dir, timeout=30)
        printstdout = f"STDOUT: {process.stdout.decode().strip()}"
        printstderr = f"STDERR: {process.stderr.decode().strip()}"
        printcode = ""
        if not process.returncode == 0:
            printcode = f'Process exited with code {process.returncode}'
        if len(process.stdout.decode().strip()) == 0 and len(process.stderr.decode().strip()) == 0:
            return "No output produced."

        return f"{printstdout}, {printstderr}, {printcode}"

    except Exception as e:
        return f'Error: executing Python file: {e}'