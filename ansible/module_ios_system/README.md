# Ansible module: ansible.module_ios_system


Manage the system attributes on Cisco IOS devices

## Description

This module provides declarative management of node system attributes on Cisco IOS devices.  It provides an option to configure host system parameters or remove those parameters from the device active configuration.

## Requirements

TODO

## Arguments

``` json
{
    "auth_pass": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes) with C(become_pass).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}",
    "authorize": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "domain_name": "{'description': ['Configure the IP domain name on the remote device to the provided value. Value should be in the dotted name form and will be appended to the C(hostname) to create a fully-qualified domain name.']}",
    "domain_search": "{'description': ['Provides the list of domain suffixes to append to the hostname for the purpose of doing name resolution. This argument accepts a list of names and will be reconciled with the current active configuration on the running node.']}",
    "hostname": "{'description': ['Configure the device hostname parameter. This option takes an ASCII string value.']}",
    "lookup_enabled": "{'description': ['Administrative control for enabling or disabling DNS lookups.  When this argument is set to True, lookups are performed and when it is set to False, lookups are not performed.'], 'type': 'bool'}",
    "lookup_source": "{'description': ['Provides one or more source interfaces to use for performing DNS lookups.  The interface provided in C(lookup_source) must be a valid interface configured on the device.']}",
    "name_servers": "{'description': ['List of DNS name servers by IP address to use to perform name resolution lookups.  This argument accepts either a list of DNS servers See examples.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(IOS Platform Options guide, ../network/user_guide/platform_ios.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}}}",
    "state": "{'description': ["State of the configuration values in the device's current active configuration.  When set to I(present), the values should be configured in the device active configuration and when set to I(absent) the values should not be in the device active configuration"], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: configure hostname and domain name
  ios_system:
    hostname: ios01
    domain_name: test.example.com
    domain_search:
      - ansible.com
      - redhat.com
      - cisco.com

- name: remove configuration
  ios_system:
    state: absent

- name: configure DNS lookup sources
  ios_system:
    lookup_source: MgmtEth0/0/CPU0/0
    lookup_enabled: yes

- name: configure name servers
  ios_system:
    name_servers:
      - 8.8.8.8
      - 8.8.4.4

```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip)']
