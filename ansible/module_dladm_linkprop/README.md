# Ansible module: ansible.module_dladm_linkprop


Manage link properties on Solaris/illumos systems

## Description

Set / reset link properties on Solaris/illumos systems.

## Requirements

TODO

## Arguments

``` json
{
    "link": "{'description': ['Link interface name.'], 'required': True, 'aliases': ['nic', 'interface']}",
    "property": "{'description': ['Specifies the name of the property we want to manage.'], 'required': True, 'aliases': ['name']}",
    "state": "{'description': ['Set or reset the property value.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent', 'reset']}",
    "temporary": "{'description': ['Specifies that lin property configuration is temporary. Temporary link property configuration does not persist across reboots.'], 'required': False, 'type': 'bool', 'default': False}",
    "value": "{'description': ['Specifies the value we want to set for the link property.'], 'required': False}",
}
```

## Examples


``` yaml

- name: Set 'maxbw' to 100M on e1000g1
  dladm_linkprop: name=e1000g1 property=maxbw value=100M state=present

- name: Set 'mtu' to 9000 on e1000g1
  dladm_linkprop: name=e1000g1 property=mtu value=9000

- name: Reset 'mtu' property on e1000g1
  dladm_linkprop: name=e1000g1 property=mtu state=reset

```

## License

TODO

## Author Information
  - ['Adam Števko (@xen0l)']
