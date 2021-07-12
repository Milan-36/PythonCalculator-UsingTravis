from pathlib import Path


def findAbsolutePath(filepath):
    relative = Path(filepath)  # Load the filepath in the relative object.
    # absolute() method will return absolute path of the  file.
    # Travis need absolute path to find data file.
    return relative.absolute()
