from setuptools import setup, find_packages
from os.path import join, dirname

import NewLifeUtils

install_requires = [open(join(dirname(__file__), 'requirements.txt')).read().split('\n')]

setup(
    name="NewLifeUtils", 
    version=NewLifeUtils.__version__,
    author='New Life',
    author_email='semechkagent@gmail.com',
    url='https://github.com/NewLife1324/NewLifeUtils-Dev',
    description='View changelog.txt at https://raw.githubusercontent.com/NewLife1324/NewLifeUtils-Dev/main/CHANGELOG.txt',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    platforms=['Windows'],
    license='MIT'
)