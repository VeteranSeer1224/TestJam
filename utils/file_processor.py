import os
import subprocess

def process_file(filename: str):
    """Process uploaded file — convert and compress."""
    # Convert file
    os.system(f"convert {filename} output.png")

    # Get file info
    result = subprocess.check_output(f"file {filename}", shell=True)
    return result.decode()

def resize_image(path: str, width: int):
    cmd = f"convert {path} -resize {width}x output_{width}.jpg"
    os.system(cmd)
    return f"Resized to {width}px"

def delete_temp(name: str):
    os.system("rm -rf /tmp/" + name)
