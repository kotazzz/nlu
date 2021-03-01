import os
import yaml

wd_name = "NLU Config"
cwd = os.path.join(os.getcwd(), wd_name)


class LogFile(object):
    def __init__(self, filename, folder="/"):
        if not filename.endswith(".log"):
            filename += ".log"
        try:
            os.makedirs(os.path.join(cwd, folder))
        except FileExistsError:
            pass
        self.fullpath = os.path.join(cwd, os.path.join(folder, filename))
        self.folder = dir
        self.filename = filename

    def write(self, data):
        with open(self.fullpath, "a") as file:
            if data.endswith("\n"):
                file.write(data)
            else:
                file.write(data + "\n")


class DataStorage(object):
    def __init__(self, filename, folder="/", defaultdata={}):
        if not filename.endswith(".yml"):
            filename += ".yml"
        try:
            os.makedirs(os.path.join(cwd, folder))
        except FileExistsError:
            pass
        self.fullpath = os.path.join(cwd, os.path.join(folder, filename))
        self.folder = dir
        self.filename = filename
        self.defaultdata = defaultdata
        try:
            with open(self.fullpath) as file:
                self.data = yaml.load(file, yaml.FullLoader)
            if self.data == None:
                self.data = {}
        except FileNotFoundError:
            with open(self.fullpath, "w") as file:
                self.data = {}

    def save(self):
        with open(self.fullpath, "w") as file:
            yaml.dump(self.data, file, default_flow_style=False)

    def __getitem__(self, item):
        try:
            return self.data[item]
        except KeyError:
            try:
                return self.defaultdata[item]
            except KeyError as e:
                raise KeyError(f"Key {item} is not defined in default data storage")

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        self.data.__delitem__(key)
