# Ansible module: ansible.module_cnos_facts


Collect facts from remote devices running Lenovo CNOS

## Description

Collects a base set of device facts from a remote Lenovo device running on CNOS.  This module prepends all of the base network fact keys with C(ansible_net_<fact>).  The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## Requirements

TODO

## Arguments

``` json
{
    "auth_pass": "{'version_added': '2.6', 'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}",
    "authorize": "{'version_added': '2.6', 'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "gather_subset": "{'version_added': '2.6', 'description': ['When supplied, this argument will restrict the facts collected to a given subset.  Possible values for this argument include all, hardware, config, and interfaces.  Can specify a list of values to include a larger subset.  Values can also be used with an initial C(M(!)) to specify that a specific subset should not be collected.'], 'required': False, 'default': '!config'}",
    "provider": "{'version_added': '2.6', 'description': ['A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
}
```

## Examples


``` yaml

Tasks: The following are examples of using the module cnos_facts.
---
- name: Test cnos Facts
  cnos_facts:
    provider={{ cli }}

  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: 22
      username: admin
      password: admin
      transport: cli
      timeout: 30
      authorize: True
      auth_pass:

---
# Collect all facts from the device
- cnos_facts:
    gather_subset: all
    provider: "{{ cli }}"

# Collect only the config and default facts
- cnos_facts:
    gather_subset:
      - config
    provider: "{{ cli }}"

# Do not collect hardware facts
- cnos_facts:
    gather_subset:
      - "!hardware"
    provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Anil Kumar Muraleedharan (@amuraleedhar)']
