import os

def ensure_upload_dir(upload_dir: str) -> str:
    """Ensure the upload directory exists; create it if it doesn't."""
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return upload_dir

def get_file_uploader_dir() -> str:
    """Get the file uploader directory in the app folder."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    media_dir = os.path.join(current_dir, "../media")  # Adjust path as needed
    return ensure_upload_dir(media_dir)
