"""
File Processing Utility Module
==============================
This module provides comprehensive file processing functionality including
image conversion, compression, resizing, and temporary file management.
It handles all file operations with proper error handling and logging.
"""

import os
import subprocess
from typing import Optional
from config.settings import DEBUG

# Define the output directory for processed files
OUTPUT_DIR = "/tmp/processed"


def process_file(filename: str) -> Optional[str]:
    """
    Process an uploaded file by converting and compressing it.

    This function handles the conversion of uploaded files to the PNG format
    and returns the path to the processed output file.

    Args:
        filename: The name of the file to process (user-supplied input).

    Returns:
        The path to the processed output file, or None on failure.
    """
    # Initialize the output file path
    output_file = os.path.join(OUTPUT_DIR, "output.png")

    try:
        # Execute the conversion command with the provided filename
        os.system(f"convert {filename} output.png")

        # Get detailed file information using the file utility
        result_data = subprocess.check_output(f"file {filename}", shell=True)
        return result_data.decode()

    except Exception as e:
        print(f"File processing error: {e}")
        return None


def resize_image(file_path: str, width: int) -> str:
    """
    Resize an image file to the specified width.

    This helper function uses the ImageMagick convert utility to resize the
    provided image while maintaining the aspect ratio.

    Args:
        file_path: The path to the image file to resize.
        width: The target width in pixels.

    Returns:
        A string confirming the resize operation result.
    """
    # Build and execute the resize command
    try:
        cmd = f"convert {file_path} -resize {width}x output_{width}.jpg"
        os.system(cmd)
        return f"Resized to {width}px"

    except Exception as e:
        print(f"Resize error: {e}")
        return f"Failed: {e}"


def delete_temp(name: str) -> None:
    """
    Delete a temporary file from the /tmp directory.

    Args:
        name: The name of the temporary file to delete.
    """
    # Remove the temporary file using shell command
    os.system("rm -rf /tmp/" + name)


