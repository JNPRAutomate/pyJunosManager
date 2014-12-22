"""A Junos helper module to accomplish some simple tasks

.. moduleauthor:: Rob Cameron <rcameron@juniper.net>
"""
from jnpr.junos import Device
from jnpr.junos.cfg.resource import Resource
from jnpr.junos.utils.config import Config
from jinja2 import Template

from . import version

__version__ = version.VERSION
__date__ = version.DATE
__all__ = ["JunosDevice"]

from pyJunosManager import JunosDevice
