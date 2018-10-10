# Ansible module: ansible.module_vyos_lldp_interface


Manage LLDP interfaces configuration on VyOS network devices

## Description

This module provides declarative management of LLDP interfaces configuration on VyOS network devices.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['List of interfaces LLDP should be configured on.']}",
    "name": "{'description': ['Name of the interface LLDP should be configured on.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "state": "{'description': ['State of the LLDP configuration.'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled']}",
}
```

## Examples


``` yaml

- name: Enable LLDP on eth1
  net_lldp_interface:
    state: present

- name: Enable LLDP on specific interfaces
  net_lldp_interface:
    interfaces:
      - eth1
      - eth2
    state: present

- name: Disable LLDP globally
  net_lldp_interface:
    state: disabled

- name: Create aggregate of LLDP interface configurations
  vyos_lldp_interface:
    aggregate:
    - name: eth1
    - name: eth2
    state: present

- name: Delete aggregate of LLDP interface configurations
  vyos_lldp_interface:
    aggregate:
    - name: eth1
    - name: eth2
    state: absent

```

## License

TODO

## Author Information
  - ['Ricardo Carrillo Cruz (@rcarrillocruz)']
