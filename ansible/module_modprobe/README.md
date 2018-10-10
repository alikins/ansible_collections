# Ansible module: ansible.module_modprobe


Load or unload kernel modules

## Description

Load or unload kernel modules.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'required': True, 'description': ['Name of kernel module to manage.']}",
    "params": "{'description': ['Modules parameters.'], 'default': '', 'version_added': '1.6'}",
    "state": "{'description': ['Whether the module should be present or absent.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Add the 802.1q module
  modprobe:
    name: 8021q
    state: present

- name: Add the dummy module
  modprobe:
    name: dummy
    state: present
    params: 'numdummies=2'

```

## License

TODO

## Author Information
  - ['David Stygstra (@stygstra)', 'Julien Dauphant', 'Matt Jeffery']
  - ['David Stygstra (@stygstra)', 'Julien Dauphant', 'Matt Jeffery']
  - ['David Stygstra (@stygstra)', 'Julien Dauphant', 'Matt Jeffery']
