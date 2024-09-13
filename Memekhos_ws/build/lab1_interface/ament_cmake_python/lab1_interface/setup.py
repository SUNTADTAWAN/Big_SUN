from setuptools import find_packages
from setuptools import setup

setup(
    name='lab1_interface',
    version='0.0.0',
    packages=find_packages(
        include=('lab1_interface', 'lab1_interface.*')),
)
