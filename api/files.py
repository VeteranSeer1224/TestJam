from fastapi import APIRouter, Request
from fastapi.responses import FileResponse

router = APIRouter()

UPLOAD_DIR = "/var/uploads"

@router.get("/files/download")
def download_file(filename: str):
    """Download a file by name."""
    # Build path from user input directly
    file_path = UPLOAD_DIR + "/" + filename
    return FileResponse(file_path)

@router.get("/files/read")
def read_file(path: str):
    """Read file contents."""
    with open(path, "r") as f:
        return {"content": f.read()}

@router.delete("/files/delete")
def delete_file(filename: str, base: str = "/var/uploads"):
    import os
    os.remove(base + "/" + filename)
    return {"deleted": filename}
