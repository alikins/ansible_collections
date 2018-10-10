# Ansible module: ansible.module_asa_acl


Manage access-lists on a Cisco ASA

## Description

This module allows you to work with access-lists on a Cisco ASA device.

## Requirements

TODO

## Arguments

``` json
{
    "after": "{'description': ['The ordered set of commands to append to the end of the command stack if a changed needs to be made.  Just like with I(before) this allows the playbook designer to append a set of commands to be executed after the command set.']}",
    "authorize": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "before": "{'description': ['The ordered set of commands to push on to the command stack if a change needs to be made.  This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system.']}",
    "config": "{'description': ['The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source.  There are times when it is not desirable to have the task get the current running-config for every task in a playbook.  The I(config) argument allows the implementer to pass in the configuruation to use as the base config for comparison.']}",
    "context": "{'description': ['Specifies which context to target if you are running in the ASA in multiple context mode. Defaults to the current context you login to.']}",
    "force": "{'description': ['The force argument instructs the module to not consider the current devices running-config.  When set to true, this will cause the module to push the contents of I(src) into the device without first checking if already configured.'], 'type': 'bool', 'default': False}",
    "lines": "{'description': ['The ordered set of commands that should be configured in the section.  The commands must be the exact same commands as found in the device running-config.  Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser.'], 'required': True, 'aliases': ['commands']}",
    "match": "{'description': ['Instructs the module on the way to perform the matching of the set of commands against the current device config.  If match is set to I(line), commands are matched line by line.  If match is set to I(strict), command lines are matched with respect to position.  Finally if match is set to I(exact), command lines must be an equal match.'], 'default': 'line', 'choices': ['line', 'strict', 'exact']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.']}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}, 'timeout': {'description': ['Specifies idle timeout in seconds for the connection, in seconds. Useful if the console freezes before continuing. For example when saving configurations.'], 'default': 10}}}",
    "replace": "{'description': ['Instructs the module on the way to perform the configuration on the device.  If the replace argument is set to I(line) then the modified lines are pushed to the device in configuration mode.  If the replace argument is set to I(block) then the entire command block is pushed to the device in configuration mode if any line is not correct.'], 'default': 'line', 'choices': ['line', 'block']}",
}
```

## Examples


``` yaml

# Note: examples below use the following provider dict to handle
#       transport and authentication to the node.
---
vars:
  cli:
    host: "{{ inventory_hostname }}"
    username: cisco
    password: cisco
    transport: cli
    authorize: yes
    auth_pass: cisco

---
- asa_acl:
    lines:
      - access-list ACL-ANSIBLE extended permit tcp any any eq 82
      - access-list ACL-ANSIBLE extended permit tcp any any eq www
      - access-list ACL-ANSIBLE extended permit tcp any any eq 97
      - access-list ACL-ANSIBLE extended permit tcp any any eq 98
      - access-list ACL-ANSIBLE extended permit tcp any any eq 99
    before: clear configure access-list ACL-ANSIBLE
    match: strict
    replace: block
    provider: "{{ cli }}"

- asa_acl:
    lines:
      - access-list ACL-OUTSIDE extended permit tcp any any eq www
      - access-list ACL-OUTSIDE extended permit tcp any any eq https
    context: customer_a
    provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Patrick Ogenstad (@ogenstad)']
