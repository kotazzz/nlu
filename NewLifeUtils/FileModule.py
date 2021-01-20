import os
from yaml import load, FullLoader

wd_name = "NLU Config"
cwd = os.path.join(os.getcwd(), wd_name)

files = {}


def get_cwd(folder):
    return os.path.join(cwd,folder)
def create_dirs(path):
    if not os.path.exists(path):
        os.makedirs(path)


def create_files(filename, file, path="", default_data=""):
    fullpath = os.path.join(os.path.join(cwd, path), "")
    create_dirs(fullpath)
    try:
        f = open(fullpath + f"{file}", "a")
        state = False
    except:
        f = open(fullpath + f"{file}", "w")
        file_rewrite(filename, default_data)
        state = True
    files[filename] = os.path.join(cwd, path) + f"\\{file}"
    f.close()
    return state

def file_exist(filename):
    try:
        files[filename]
    except:
        return False
    else:
        return os.path.exists(files[filename])


def get_files(filename):
    return files[filename]

def get_file(filename, file, path=""):
    return os.path.join(os.path.join(cwd, path), file)

def file_rewrite(filename, data, end ='\n'):
    f = open(files[filename], "w")
    f.write(data+end)
    f.close()


def file_apwrite(filename, data, end ='\n', coding = "utf-8"):
    f = open(files[filename], "a", encoding=coding)
    f.write(data+end)
    f.close()


def readall(filename):
    f = open(files[filename], "r")
    r = f.read()
    f.close()
    return r


def get_yaml(filename, regen_data = ''):
    try:
        retobj = load(readall(filename), Loader=FullLoader)
        if retobj == None:
            raise Exception
        else:
            return retobj
    except Exception as e:
        if regen_data != '':
            file_rewrite(filename, regen_data)
        try:
            return load(readall(filename), Loader=FullLoader)
        except Exception as e2:
            return None