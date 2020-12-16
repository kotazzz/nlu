from setuptools import setup, find_packages
from os.path import join, dirname

import NewLifeUtils

setup(
    name=NewLifeUtils.name, 
    version=NewLifeUtils.__version__,
    author='New Life',
    author_email='semechkagent@gmail.com',
    url='newlife-learn.h1n.ru',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
)