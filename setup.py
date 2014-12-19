#!/usr/bin/env python
from setuptools import setup, find_packages

import pyJunosManager

setup(
    name='pyJunosManager',
    version=pyJunosManager.__version__,
    description='A simplified module to handle common Junos tasks',
    url='https://github.com/JNPRAutomate/pyJunosManager',
    license='???',
    author='Rob Cameron',
    install_requires=["junos-eznc>=1.0.2","Jinja2>=2.7.3"],
    author_email='rcameron@juniper.net',
    packages=['pyJunosManager'],
    include_package_data=True
)
