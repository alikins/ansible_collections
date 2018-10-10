# Ansible module: ansible.module_vyos_system


Run `set system` commands on VyOS devices

## Description

Runs one or more commands on remote devices running VyOS. This module can also be introspected to validate key parameters before returning successfully.

## Requirements

TODO

## Arguments

``` json
{
    "domain_name": "{'description': ['The new domain name to apply to the device.']}",
    "domain_search": "{'description': ['A list of domain names to search. Mutually exclusive with I(name_server)']}",
    "host_name": "{'description': ['Configure the device hostname parameter. This option takes an ASCII string value.']}",
    "name_servers": "{'description': ['A list of name servers to use with the device. Mutually exclusive with I(domain_search)'], 'aliases': ['name_server']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "state": "{'description': ['Whether to apply (C(present)) or remove (C(absent)) the settings.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: configure hostname and domain-name
  vyos_system:
    host_name: vyos01
    domain_name: test.example.com

- name: remove all configuration
  vyos_system:
    state: absent

- name: configure name servers
  vyos_system:
    name_servers
      - 8.8.8.8
      - 8.8.4.4

- name: configure domain search suffixes
  vyos_system:
    domain_search:
      - sub1.example.com
      - sub2.example.com

```

## License

TODO

## Author Information
  - ['Nathaniel Case (@qalthos)']
