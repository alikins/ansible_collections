# Ansible module: ansible.module_macports


Package manager for MacPorts

## Description

Manages MacPorts packages (ports)

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['A list of port names.'], 'aliases': ['port']}",
    "selfupdate": "{'description': ['Update Macports and the ports tree, either prior to installing ports or as a separate step.', 'Equivalent to running C(port selfupdate).'], 'aliases': ['update_cache', 'update_ports'], 'default': False, 'type': 'bool'}",
    "state": "{'description': ['Indicates the desired state of the port.'], 'choices': ['present', 'absent', 'active', 'inactive'], 'default': 'present'}",
    "upgrade": "{'description': ['Upgrade all outdated ports, either prior to installing ports or as a separate step.', 'Equivalent to running C(port upgrade outdated).'], 'default': False, 'type': 'bool', 'version_added': '2.8'}",
    "variant": "{'description': ['A port variant specification.', 'C(variant) is only supported with state: I(installed)/I(present).'], 'aliases': ['variants'], 'version_added': '2.7'}",
}
```

## Examples


``` yaml

- name: Install the foo port
  macports:
    name: foo

- name: Install the universal, x11 variant of the foo port
  macports:
    name: foo
    variant: +universal+x11

- name: Install a list of ports
  macports:
    name: "{{ ports }}"
  vars:
    ports:
    - foo
    - foo-tools

- name: Update Macports and the ports tree, then upgrade all outdated ports
  macports:
    selfupdate: yes
    upgrade: yes

- name: Update Macports and the ports tree, then install the foo port
  macports:
    name: foo
    selfupdate: yes

- name: Remove the foo port
  macports:
    name: foo
    state: absent

- name: Activate the foo port
  macports:
    name: foo
    state: active

- name: Deactivate the foo port
  macports:
    name: foo
    state: inactive

```

## License

TODO

## Author Information
  - ['Jimmy Tang (@jcftang)']
