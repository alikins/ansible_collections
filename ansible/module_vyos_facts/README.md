# Ansible module: ansible.module_vyos_facts


Collect facts from remote devices running VyOS

## Description

Collects a base set of device facts from a remote device that is running VyOS.  This module prepends all of the base network fact keys with U(ansible_net_<fact>).  The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## Requirements

TODO

## Arguments

``` json
{
    "gather_subset": "{'description': ['When supplied, this argument will restrict the facts collected to a given subset.  Possible values for this argument include all, default, config, and neighbors.  Can specify a list of values to include a larger subset.  Values can also be used with an initial C(M(!)) to specify that a specific subset should not be collected.'], 'required': False, 'default': '!config'}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
}
```

## Examples


``` yaml

- name: collect all facts from the device
  vyos_facts:
    gather_subset: all

- name: collect only the config and default facts
  vyos_facts:
    gather_subset: config

- name: collect everything exception the config
  vyos_facts:
    gather_subset: "!config"

```

## License

TODO

## Author Information
  - ['Nathaniel Case (@qalthos)']
