from setuptools import find_packages
from setuptools import setup

setup(
    name='controller_interface',
    version='0.0.0',
    packages=find_packages(
        include=('controller_interface', 'controller_interface.*')),
)
