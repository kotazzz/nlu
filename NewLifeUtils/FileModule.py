import os
from yaml import load, FullLoader

wd_name = "NLU Config"
cwd = os.path.join(os.getcwd(), wd_name)

configs = {}


def create_dirs(path):
    if not os.path.exists(path):
        os.makedirs(path)


def create_config(configname, file, path="", default_data=""):
    fullpath = os.path.join(os.path.join(cwd, path), "")
    create_dirs(fullpath)
    try:
        f = open(fullpath + f"\\{file}", "a")
        state = False
    except:
        f = open(fullpath + f"\\{file}", "w")
        config_rewrite(configname, default_data)
        state = True
    configs[configname] = os.path.join(cwd, path) + f"\\{file}"
    f.close()
    return state


def get_configs():
    return configs


def config_rewrite(configname, data):
    f = open(configs[configname], "w")
    f.write(data)
    f.close()


def config_apwrite(configname, data):
    f = open(configs[configname], "a")
    f.write(data)
    f.close()


def readall(configname):
    f = open(configs[configname], "r")
    r = f.read()
    f.close()
    return r


def get_yaml(configname, regen_data = ''):
    try:
        retobj = load(readall(configname), Loader=FullLoader)
        if retobj == None:
            raise Exception
        else:
            return retobj
    except Exception as e:
        if regen_data != '':
            config_rewrite(configname, regen_data)
        try:
            return load(readall(configname), Loader=FullLoader)
        except Exception as e2:
            return None
