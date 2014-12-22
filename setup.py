#!/usr/bin/env python
from setuptools import setup, find_packages
import pyJunosManager
import os

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    html_theme = 'default'
else:
    html_theme = 'nature'

# otherwise, readthedocs.org uses their theme by default, so no need to specify it

setup(
    name='pyJunosManager',
    version=pyJunosManager.__version__,
    description='A simplified module to handle common Junos tasks',
    url='https://github.com/JNPRAutomate/pyJunosManager',
    license='Apache 2.0',
    author='Rob Cameron',
    install_requires=["junos-eznc>=1.0.2","Jinja2>=2.7.3"],
    author_email='rcameron@juniper.net',
    packages=['pyJunosManager'],
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 2.7'
    ]
)
