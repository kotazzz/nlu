print("Hello, im starting!")
import json
import sys
import os

configfile = open("config.json", encoding="utf-8")
config = json.loads(configfile.read())
configfile.close()
filename = config["filename"]
path = config["path"]
file = f'{path}\\{filename}'
from cx_Freeze import setup, Executable

executables = [Executable(file)]

options = {
    "build_exe": {
        "include_msvcr": True,
    }
}

sys.path.insert(0, path)

setup(
    name=__import__(filename.rsplit(".", 1)[0]).name,
    version=__import__(filename.rsplit(".", 1)[0]).__version__,
    description=__import__(filename.rsplit(".", 1)[0]).description,
    executables=executables,
    options=options,
)
