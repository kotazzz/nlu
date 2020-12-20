from NewLifeUtils import os
currentDirectory = os.getcwd() + "\\"
workDirectory = currentDirectory + "NewLifeUtils Directory\\"
space = "   "
branch = "│  "
tee = "├─ "
last = "└─ "

def get_path( path=""):
    if path == "":
        path = workDirectory
    elif path[0] == "+":
        if path[-1] not in ["/", "\\"]:
            path += "\\"
        path = workDirectory + path[1:]
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def open_file( name, mode="", path="", encoding="utf8"):
    path = get_path(path)

    try:
        open(path + name)
    except:
        open(path + name, "w")
    finally:
        if mode == "":
            f = open(path + name, encoding=encoding)
        else:
            f = open(path + name, mode, encoding=encoding)
    return f

def get_directory_content( directory=""):
    return os.listdir(get_path(directory))

def exists( path):
    return os.path.exists(get_path(path))

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
