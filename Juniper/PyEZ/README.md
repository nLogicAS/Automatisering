Forskjellige scripts som bruker PyEZ for å utføre oppgaver. Se nlogic.no/automatiseringsforum for forklaring på scriptene.


-----------

Disclaimer: All of the textual content below are from juniper.net's web page.

Merknad: Alt tekstinnholdet under er fra juniper.net sin nettside.

Source/kilde: http://www.juniper.net/documentation/en_US/junos-pyez/topics/concept/junos-pyez-overview.html


# Understanding Junos PyEZ
> Junos PyEZ is a microframework for Python that enables you to manage and automate devices running the Junos operating system (Junos OS). Junos PyEZ is designed to provide the capabilities that a user would have on the Junos OS command-line interface (CLI) in an environment built for automation tasks. Junos PyEZ does not require extensive knowledge of Junos OS or the Junos XML APIs.

> Junos PyEZ enables you to manage devices running Junos OS using the familiarity of Python. However, you do not have to be an experienced programmer to use Junos PyEZ. Non-programmers can quickly execute simple commands in Python interactive mode, and more experienced programmers can opt to create more complex, robust, and reusable programs to perform tasks.

> Junos PyEZ enables you to connect to devices running Junos OS using a serial console connection, telnet, or a NETCONF session over SSH. You can use Junos PyEZ to initially configure a new, or zeroized device that is not yet configured for remote access by using either a serial console connection when you are directly connected to the device or by using telnet through a console server that is directly connected to the device.

> Junos PyEZ enables you to perform specific operational and configuration tasks on devices running Junos OS. Using Junos PyEZ, you can easily retrieve facts and operational information from a device and execute any remote procedure call (RPC) available through the Junos XML API. Junos PyEZ provides software utilities for installing the Junos OS software and rebooting or shutting down managed devices. Junos PyEZ configuration management utilities enable you to retrieve and compare configurations, create a rescue configuration, roll back a configuration, and upload configuration changes. Junos PyEZ supports standard formats for configuration data including ASCII text, Junos XML elements, Junos OS set commands, and JavaScript Object Notation (JSON), and also supports using Jinja2 templates and template files for added flexibility and customization. In addition, you can use Tables and Views to define structured resources that you can use to programmatically configure a device. Junos PyEZ also provides file system utilities to perform common administrative tasks such as copying files and calculating checksums.

> Junos PyEZ provides Tables and Views to enable you to both configure devices running Junos OS and extract specific operational information or configuration data from the devices. Tables and Views are defined using simple YAML files that contain key:value pair mappings, so no complex coding is required to use them. Using Tables and Views, you can retrieve the device configuration or the output for any Junos OS command that has an RPC equivalent and then extract a customized subset of information. This is useful when you need to retrieve information from a few specific fields that are embedded in extensive command output such as for the show route or show interfaces command. In addition, starting in Junos PyEZ Release 2.0, you can use Tables and Views to define structured configuration resources. Junos PyEZ dynamically creates configuration classes for the resources, which enables you to programmatically configure the resource on a device.


# For additional information about Junos PyEZ, see:
* Junos PyEZ TechWiki page at http://forums.juniper.net/t5/Automation-Scripting/Junos-PyEZ/ta-p/280496
* Junos PyEZ API documentation at http://junos-pyez.readthedocs.org/
* Junos PyEZ GitHub repository at https://github.com/Juniper/py-junos-eznc/
