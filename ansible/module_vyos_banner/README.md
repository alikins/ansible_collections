# Ansible module: ansible.module_vyos_banner


Manage multiline banners on VyOS devices

## Description

This will configure both pre-login and post-login banners on remote devices running VyOS. It allows playbooks to add or remote banner text from the active running configuration.

## Requirements

TODO

## Arguments

``` json
{
    "banner": "{'description': ['Specifies which banner that should be configured on the remote device.'], 'required': True, 'choices': ['pre-login', 'post-login']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "state": "{'description': ['Specifies whether or not the configuration is present in the current devices active running configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "text": "{'description': ['The banner text that should be present in the remote device running configuration. This argument accepts a multiline string, with no empty lines. Requires I(state=present).']}",
}
```

## Examples


``` yaml

- name: configure the pre-login banner
  vyos_banner:
    banner: pre-login
    text: |
      this is my pre-login banner
      that contains a multiline
      string
    state: present
- name: remove the post-login banner
  vyos_banner:
    banner: post-login
    state: absent

```

## License

TODO

## Author Information
  - ['Trishna Guha (@trishnaguha)']
