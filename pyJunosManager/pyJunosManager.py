"""
.. module:: pyJunosManager
   :platform: Unix, Windows, Mac
   :synopsis: A simplified module to handle common Junos tasks

"""
from jnpr.junos import Device
from jnpr.junos.cfg.resource import Resource
from jnpr.junos.utils.config import Config
from jinja2 import Template

class pyJunosManager():
    def __init__(self,host="",username="",password=""):
        """
        pyJunosManager constructor

        Args:
            :host: string containing the host to connect to
            :username: string containing the username to authenticate with
            :password: string contining the password to authenticate with
        """
        self.dev = Device(host=host,user=username,password=password)
        self.dev.bind(cu=Config)

    def open(self):
        """
        Opens a NETCONF session to the specified Junos-based device

        """
        try:
            self.dev.open()
        except Exception as err:
            print err

    def close(self):
        """
        Closes a NETCONF session to the specified device

        """
        try:
            self.dev.close()
        except Exception as err:
            print err

    def get_facts(self):
        """
        Returns the device facts as a Python dict

        """
        return self.dev.facts

    def open_config(self,type="shared"):
        """
        Opens the configuration of the currently connected device

        """
        try:
            #attempt to open a configuration
            output = self.dev.rpc("<open-configuration><{0}/></open-configuration>".format(type))
        except Exception as err:
            #output an error if the configuration is not availble
            print err

    def close_config(self):
        """
        Closes the exiting opened configuration
        """
        try:
            self.dev.rpc.close_configuration()
        except Exception as err:
            print err

    def load_config_template(self,template,template_vars):
        """
        :template: A templated string using Jinja2 templates
        :template_vars: A dict containing the vars used in the :template: string
        """
        new_template = Template(template)
        final_template = new_template.render(template_vars)

        try:
            output = self.dev.cu.load(final_template,format="text",merge=True)
        except Exception as err:
            print err

    def commit_config(self):
        """
        Commits exiting configuration

        """
        try:
            self.dev.rpc.commit_configuration()
        except Exception as err:
            print err

    def commit_and_quit(self):
        """
        Commits and closes the currently open configration

        """
        try:
            self.dev.rpc.commit_configuration()
            self.close_config()
        except Exception as err:
            print err
