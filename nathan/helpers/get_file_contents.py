import os
from settings import ROOT_DIR

# Join the current directory with the relative path to get the full path


def get_file_contents(relative_path, cb):
    full_path = os.path.join(ROOT_DIR, relative_path)
    with open(full_path, "r") as f:
        return cb(f)
