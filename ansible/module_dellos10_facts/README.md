# Ansible module: ansible.module_dellos10_facts


Collect facts from remote devices running Dell EMC Networking OS10

## Description

Collects a base set of device facts from a remote device that is running OS10.  This module prepends all of the base network fact keys with C(ansible_net_<fact>).  The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## Requirements

TODO

## Arguments

``` json
{
    "gather_subset": "{'description': ['When supplied, this argument will restrict the facts collected to a given subset.  Possible values for this argument include all, hardware, config, and interfaces.  Can specify a list of values to include a larger subset.  Values can also be used with an initial C(M(!)) to specify that a specific subset should not be collected.'], 'default': ['!config']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['User to authenticate the SSH session to the remote device. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Password to authenticate the SSH session to the remote device. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'ssh_keyfile': {'description': ['Path to an ssh key used to authenticate the SSH session to the remote device.  If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'timeout': {'description': ['Specifies idle timeout (in seconds) for the connection. Useful if the console freezes before continuing. For example when saving configurations.'], 'default': 10}}}",
}
```

## Examples


``` yaml

# Collect all facts from the device
- dellos10_facts:
    gather_subset: all

# Collect only the config and default facts
- dellos10_facts:
    gather_subset:
      - config

# Do not collect hardware facts
- dellos10_facts:
    gather_subset:
      - "!hardware"

```

## License

TODO

## Author Information
  - ['Senthil Kumar Ganesan (@skg-net)']
