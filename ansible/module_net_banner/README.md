# Ansible module: ansible.module_net_banner


Manage multiline banners on network devices

## Description

This will configure both login and motd banners on network devices. It allows playbooks to add or remove banner text from the active running configuration.

## Requirements

TODO

## Arguments

``` json
{
    "banner": "{'description': ['Specifies which banner that should be configured on the remote device.'], 'required': True, 'choices': ['login', 'motd']}",
    "state": "{'description': ['Specifies whether or not the configuration is present in the current devices active running configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "text": "{'description': ['The banner text that should be present in the remote device running configuration.  This argument accepts a multiline string, with no empty lines. Requires I(state=present).']}",
}
```

## Examples


``` yaml

- name: configure the login banner
  net_banner:
    banner: login
    text: |
      this is my login banner
      that contains a multiline
      string
    state: present

- name: remove the motd banner
  net_banner:
    banner: motd
    state: absent

- name: Configure banner from file
  net_banner:
    banner:  motd
    text: "{{ lookup('file', './config_partial/raw_banner.cfg') }}"
    state: present


```

## License

TODO

## Author Information
  - ['Ricardo Carrillo Cruz (@rcarrillocruz)']
