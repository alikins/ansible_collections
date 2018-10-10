# Ansible module: ansible.module_vyos_interface


Manage Interface on VyOS network devices

## Description

This module provides declarative management of Interfaces on VyOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of Interfaces definitions.']}",
    "delay": "{'description': ['Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are I(state) with values C(up)/C(down) and I(neighbors).'], 'default': 10}",
    "description": "{'description': ['Description of Interface.']}",
    "duplex": "{'description': ['Interface link status.'], 'default': 'auto', 'choices': ['full', 'half', 'auto']}",
    "enabled": "{'description': ['Interface link status.']}",
    "mtu": "{'description': ['Maximum size of transmit packet.']}",
    "name": "{'description': ['Name of the Interface.'], 'required': True}",
    "neighbors": "{'description': ['Check the operational state of given interface C(name) for LLDP neighbor.', 'The following suboptions are available.'], 'suboptions': {'host': {'description': ['LLDP neighbor host for given interface C(name).']}, 'port': {'description': ['LLDP neighbor port to which given interface C(name) is connected.']}}, 'version_added': 2.5}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "speed": "{'description': ['Interface link speed.']}",
    "state": "{'description': ['State of the Interface configuration, C(up) means present and operationally up and C(down) means present and operationally C(down)'], 'default': 'present', 'choices': ['present', 'absent', 'up', 'down']}",
}
```

## Examples


``` yaml

- name: configure interface
  vyos_interface:
    name: eth0
    description: test-interface

- name: remove interface
  vyos_interface:
    name: eth0
    state: absent

- name: make interface down
  vyos_interface:
    name: eth0
    enabled: False

- name: make interface up
  vyos_interface:
    name: eth0
    enabled: True

- name: Configure interface speed, mtu, duplex
  vyos_interface:
    name: eth5
    state: present
    speed: 100
    mtu: 256
    duplex: full

- name: Set interface using aggregate
  vyos_interface:
    aggregate:
      - { name: eth1, description: test-interface-1,  speed: 100, duplex: half, mtu: 512}
      - { name: eth2, description: test-interface-2,  speed: 1000, duplex: full, mtu: 256}

- name: Disable interface on aggregate
  net_interface:
    aggregate:
      - name: eth1
      - name: eth2
    enabled: False

- name: Delete interface using aggregate
  net_interface:
    aggregate:
      - name: eth1
      - name: eth2
    state: absent

- name: Check lldp neighbors intent arguments
  vyos_interface:
    name: eth0
    neighbors:
    - port: eth0
      host: netdev

- name: Config + intent
  vyos_interface:
    name: eth1
    enabled: False
    state: down

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
