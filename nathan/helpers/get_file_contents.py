import os
from settings import ROOT_DIR

# Join the current directory with the relative path to get the full path


def get_file_contents(relative_path, cb, file_processor=None):
    full_path = os.path.join(ROOT_DIR, relative_path)
    with open(full_path, "r") as f:
        if file_processor:
            return cb(file_processor(f))
        return cb(f)


def remove_line_breaks(file_contents):
    return [line[:-1] for line in file_contents]
