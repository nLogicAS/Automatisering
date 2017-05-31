#!/usr/bin/env python3

#
# imports
#
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import sys

netconf_username = 'netconf'
netconf_password = 'netc0nf'

args = sys.argv
if len(args) != 4:
	print('Error: This PyEZ/NetCONF script takes exactly 3 parameters.')
	print('Usage: ./configure_interfaces.py <node> <interface> <access VLAN name>')
	print('Example: ./configure_interfaces.py oslo-switch1.infra.company.no ge-0/0/2 OFFICE')
	sys.exit(2)

# We know that "args" now contains four elements
unused_variable, node, interface, vlan_name = sys.argv

#
# Configuration to be sent to the Juniper node
#
config_template = '''

# In case the interface is configured before.
delete interfaces {{ interface }}
set interfaces {{ interface }} description "Access VLAN {{ vlan_name }}"
set interfaces {{ interface }} unit 0 family ethernet-switching interface-mode access
set interfaces {{ interface }} unit 0 family ethernet-switching vlan members {{ vlan_name }}

'''

#
# Build a list containing each separate line from the template as a list item. In the process
#
set_lines = []
for x in config_template.split('\n'):
    x = x.strip().replace('\n', ' ').replace('\r', '')
    if len(x) > 0 and x[0] != '#':
        x = x.replace('{{ interface }}', interface)
        x = x.replace('{{ vlan_name }}', vlan_name)
        set_lines.append(x)

#
# Connect to node through NETCONF over SSH.
#
print('Connecting to device...')
dev = Device(host=node, user=netconf_username, password=netconf_password).open()
# Entering configurational mode, with exclusive lock
with Config(dev, mode='exclusive') as cu:
    print('Connected, sending config to device')
    for line in set_lines:
        try:
            cu.load(line, format='set')
        except Exception as e:
            print('Note: following line is being rejected by %s: %s' % (node, line))
    #
    # Show the diff from the Juniper node, and request interactive feedback. Configurational mode still locked.
    #
    print('Config diff')
    cu.pdiff()
    response = input('Commit? yes/no: ')
    if response == 'no':
        print('Exiting - nothing changed on %s' % node)
        cu.rollback()
        sys.exit(0)
    elif response == 'yes':
        #
        # Performing the commit
        #
        print('Committing...')
        try:
            cu.commit(comment='Changed interface %s' % interface)
            print('Commit successfull')
        except BaseException as error:
            print('An exception occurred: {}'.format(error))
            print('Unable to commit: %s' % error.message)
            print('Performing rollback')
            cu.rollback()
    else:
        print('Exiting - you did not type "yes" or "no"')
