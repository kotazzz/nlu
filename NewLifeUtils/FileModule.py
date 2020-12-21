import os
from pathlib import Path
from itertools import islice

working_directory = os.path.join(os.getcwd(), 'NewLifeUtils Directory')
if not os.path.exists(working_directory):
    os.mkdir(working_directory)


def get_path(folder):
    return os.path.join(working_directory, folder)
    
def get_dir_content( directory=""):
    return os.listdir(directory)
def tree(
    
    dir_path: Path,
    level: int = -1,
    limit_to_directories: bool = False,
    length_limit: int = 1000,
):
    """Given a directory Path object print a visual tree structure"""
    resultpath = ""
    dir_path = Path(dir_path)  # accept string coerceable to Path
    files = 0
    directories = 0

    def inner(dir_path: Path, prefix: str = "", level=-1):
        nonlocal files, directories
        if not level:
            return  # 0, stop iterating
        if limit_to_directories:
            contents = [d for d in dir_path.iterdir() if d.is_dir()]
        else:
            contents = list(dir_path.iterdir())
        pointers = [tee] * (len(contents) - 1) + [last]
        for pointer, path in zip(pointers, contents):
            if path.is_dir():
                yield prefix + pointer + path.name
                directories += 1
                extension = branch if pointer == tee else space
                yield from inner(path, prefix=prefix + extension, level=level - 1)
            elif not limit_to_directories:
                yield prefix + pointer + path.name
                files += 1

    resultpath += "\n" + (dir_path.name)
    iterator = inner(dir_path, level=level)
    for line in islice(iterator, length_limit):
        resultpath += "\n" + (line)
    if next(iterator, None):
        resultpath += "\n" + (
            f"... length_limit, {length_limit}, reached, counted:"
        )
    resultpath += "\n" + ("")
    resultpath += "\n" + (
        f"{directories} directories" + (f", {files} files" if files else "")
    )
    return resultpath

def old_tree(startpath):
    resultpath = ""
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, "").count(os.sep)
        indent = " " * 4 * (level)
        resultpath += "\n" + ("{}{}/".format(indent, os.path.basename(root)))
        subindent = " " * 4 * (level + 1)
        for f in files:
            resultpath += "\n" + ("{}{}".format(subindent, f))
    return resultpath
