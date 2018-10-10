# Ansible module: ansible.module_iosxr_banner


Manage multiline banners on Cisco IOS XR devices

## Description

This module will configure both exec and motd banners on remote device running Cisco IOS XR. It allows playbooks to add or remove banner text from the running configuration.

## Requirements

TODO

## Arguments

``` json
{
    "banner": "{'description': ['Specifies the type of banner to configure on remote device.'], 'required': True, 'choices': ['login', 'motd']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "state": "{'description': ['Existential state of the configuration on the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "text": "{'description': ['Banner text to be configured. Accepts multiline string, without empty lines. Requires I(state=present).']}",
}
```

## Examples


``` yaml

- name: configure the login banner
  iosxr_banner:
    banner: login
    text: |
      this is my login banner
      that contains a multiline
      string
    state: present
- name: remove the motd banner
  iosxr_banner:
    banner: motd
    state: absent
- name: Configure banner from file
  iosxr_banner:
    banner:  motd
    text: "{{ lookup('file', './config_partial/raw_banner.cfg') }}"
    state: present

```

## License

TODO

## Author Information
  - ['Trishna Guha (@trishnaguha)', 'Kedar Kekan (@kedarX)']
  - ['Trishna Guha (@trishnaguha)', 'Kedar Kekan (@kedarX)']
