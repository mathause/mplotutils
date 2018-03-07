#!/usr/bin/env python

from setuptools import setup, find_packages


NAME = 'mplotutils'

# get version
with open(NAME + "/version.py") as f:
    l = f.readline().strip().replace(' ', '').replace('"', '')
    version = l.split('=')[1]
    __version__ = version


setup(
    name=NAME,
    version=__version__,
    description='utilities for matplotlib and cartopy',
    author='mathause',
    author_email='mathause@ethz.com',
    packages=find_packages(),
    url='https://github.com/mathause/mplotutils',
    install_requires=open('requirements.txt').read().split(),
    long_description='See https://github.com/mathause/mplotutils'
)


