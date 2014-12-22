from jnpr.junos import Device
from jnpr.junos.cfg.resource import Resource
from jnpr.junos.utils.config import Config
from jinja2 import Template

class JunosDevice():
    """
    JunosDevice

    Args:
        :host: string containing the host to connect to
        :username: string containing the username to authenticate with
        :password: string contining the password to authenticate with



    Examples:

    Basic device connection:

    .. code-block:: python

        from pyJunosManager import JunosDevice

        dev = JunosDevice(host="1.2.3.4",username="root",password="Juniper")
        dev.open()
        print dev.get_facts()
        dev.close()

    """
    def __init__(self,host="",username="",password=""):
        self.dev = Device(host=host,user=username,password=password)
        self.dev.bind(cu=Config)

    def open(self):
        """
        Opens a NETCONF session to the specified Junos-based device

        Example:

        .. code-block:: python

            from pyJunosManager import JunosDevice

            //creates a connection to the Junos device
            dev = JunosDevice(host="1.2.3.4",username="root",password="Juniper")
            dev.open()

        """
        try:
            self.dev.open()
        except Exception as err:
            print err

    def close(self):
        """
        Closes a NETCONF session to the specified device

        Example:

        .. code-block:: python

            from pyJunosManager import JunosDevice

            dev = JunosDevice(host="1.2.3.4",username="root",password="Juniper")
            dev.open()
            dev.close()

        """
        try:
            self.dev.close()
        except Exception as err:
            print err

    def get_facts(self):
        """
        Returns the device facts as a Python dict

        Example:

        .. code-block:: python

            from pyJunosManager import JunosDevice
            import pprint

            dev = JunosDevice(host="1.2.3.4",username="root",password="Juniper")
            dev.open()
            facts = dev.get_facts()
            dev.close()

            pprint facts
        """
        return self.dev.facts

    def open_config(self,type="shared"):
        """
        Opens the configuration of the currently connected device

        Args:
            :type: The type of configuration you want to open. Any string can be provided, however the standard supported options are: **exclusive**, **private**, and **shared**. The default mode is **shared**.

        Examples:

        .. code-block:: python

            #Open shared config

            from pyJunosManager import JunosDevice

            dev = JunosDevice(host="1.2.3.4",username="root",password="Juniper")
            dev.open()
            dev.open_config()
            dev.close_config()
            dev.close()

            #Open private config

            from pyJunosManager import JunosDevice

            dev = JunosDevice(host="1.2.3.4",username="root",password="Juniper")
            dev.open()
            dev.open_config("private")
            dev.close_config()
            dev.close()
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

        Example:

        .. code-block:: python

            from pyJunosManager import JunosDevice

            dev = JunosDevice(host="1.2.3.4",username="root",password="Juniper")
            dev.open()
            dev.open_config()
            dev.close_config()
            dev.close()

        """
        try:
            self.dev.rpc.close_configuration()
        except Exception as err:
            print err

    def load_config_template(self,template,template_vars):
        """
        :template: A templated string using Jinja2 templates
        :template_vars: A dict containing the vars used in the :template: string

        Uses standard `Jinja2`_ Templating.

        .. _`Jinja2`: http://jinja.pocoo.org/

        Example:

        .. code-block:: python

            from pyJunosManager import JunosDevice

            config_template = "system { host-name {{ hostname }}; }"

            dev = JunosDevice(host="1.2.3.4",username="root",password="Juniper")
            dev.open()
            dev.load_config_template(config_template,hostname="foo")
            dev commit_and_quit()
            dev.close()

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

        Example:

        .. code-block:: python

            from pyJunosManager import JunosDevice

            dev = JunosDevice(host="1.2.3.4",username="root",password="Juniper")
            dev.open()
            dev.open_config()
            dev.commit_config()
            dev.close_config()
            dev.close()
        """
        try:
            self.dev.rpc.commit_configuration()
        except Exception as err:
            print err

    def commit_and_quit(self):
        """
        Commits and closes the currently open configration. Saves a step by not needing to manually close the config.

        Example:

        .. code-block:: python

            from pyJunosManager import JunosDevice

            dev = JunosDevice(host="1.2.3.4",username="root",password="Juniper")
            dev.open()
            dev.load_config_template("system{ host-name {{ hostname }};}",hostname="foo")
            dev commit_and_quit()
            dev.close()

        """
        try:
            self.dev.rpc.commit_configuration()
            self.close_config()
        except Exception as err:
            print err
