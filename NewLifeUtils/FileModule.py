import os
import yaml
import collections

wd_name = "NLU Config"
cwd = os.path.join(os.getcwd(), wd_name)

files = {}


def get_cfgfld_name():
    return wd_name


def get_cfgfld_path():
    return os.path.join(cwd, wd_name)


def create_dirs(path):
    if not os.path.exists(path):
        os.makedirs(path)


def create_config(alias, filename, folderpath, default_obj={}):
    directory = os.path.join(cwd, folderpath)
    files[alias] = os.path.join(directory, filename)

    create_dirs(directory)
    if not os.path.exists(os.path.join(directory, filename)) or rawread(alias) == "":
        f = open(os.path.join(directory, filename), "w")
        yaml_write = yaml.dump(default_obj, default_flow_style=False)
        file_rewrite(alias, yaml_write)
        return False


def get_pointyaml(alias):
    class AttrDict(collections.defaultdict):
        __getattr__ = dict.__getitem__
        __setattr__ = dict.__setitem__
        __delattr__ = dict.__delitem__

        def __missing__(self, key):
            return f"UNK: {key}"

    yobj = AttrDict(yaml.load(rawread(alias), Loader=yaml.FullLoader))
    return yobj


def rewrite_yaml(alias, obj):
    yaml_write = yaml.dump(obj, default_flow_style=False)
    file_rewrite(alias, yaml_write)


def get_from_alias(alias):
    try:
        files[alias]
    except:
        return False
    else:
        return os.path.exists(files[alias])


def file_rewrite(filename, data, end="\n"):
    f = open(files[filename], "w")
    f.write(data + end)
    f.close()


def file_apwrite(filename, data, end="\n", coding="utf-8"):
    f = open(files[filename], "a", encoding=coding)
    f.write(data + end)
    f.close()


def rawread(alias):
    f = open(files[alias], "r")
    r = f.read()
    f.close()
    return r


def get_files_from_dir(folder):
    path = os.path.join(os.path.join(cwd, folder), "")
    create_dirs(path)
    path = os.listdir(path)
    dirfiles = []
    for some in path:
        if path.isfile(os.path.join(path, some)):
            dirfiles.append(some)
    return dirfiles
