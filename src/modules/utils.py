import os

def check_path(path: str) -> bool:
    """Check if the path exists"""
    return os.path.isfile(path)
        
def create_file(path: str) -> None:
    pass

