# Ansible module: ansible.module_junos_banner


Manage multiline banners on Juniper JUNOS devices

## Description

This will configure both login and motd banners on network devices. It allows playbooks to add or remote banner text from the active running configuration.

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ['Specifies whether or not the configuration is active or deactivated'], 'type': 'bool', 'default': True}",
    "banner": "{'description': ['Specifies which banner that should be configured on the remote device. Value C(login) indicates system login message prior to authenticating, C(motd) is login announcement after successful authentication.'], 'required': True, 'choices': ['login', 'motd']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "state": "{'description': ['Specifies whether or not the configuration is present in the current devices active running configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "text": "{'description': ['The banner text that should be present in the remote device running configuration.  This argument accepts a multiline string, with no empty lines. Requires I(state=present).']}",
}
```

## Examples


``` yaml

- name: configure the login banner
  junos_banner:
    banner: login
    text: |
      this is my login banner
      that contains a multiline
      string
    state: present

- name: remove the motd banner
  junos_banner:
    banner: motd
    state: absent

- name: deactivate the motd banner
  junos_banner:
    banner: motd
    state: present
    active: False

- name: activate the motd banner
  junos_banner:
    banner: motd
    state: present
    active: True

- name: Configure banner from file
  junos_banner:
    banner:  motd
    text: "{{ lookup('file', './config_partial/raw_banner.cfg') }}"
    state: present

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)']
