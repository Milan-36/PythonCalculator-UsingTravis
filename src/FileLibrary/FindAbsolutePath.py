from pathlib import Path


def findAbsolutePath(filepath):
    relative = Path(filepath)
    return relative.absolute()  # Travis need absolute path to find data file
