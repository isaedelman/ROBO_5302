from setuptools import find_packages
from setuptools import setup

setup(
    name='ised7881_service',
    version='0.0.0',
    packages=find_packages(
        include=('ised7881_service', 'ised7881_service.*')),
)
