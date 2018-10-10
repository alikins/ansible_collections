# Ansible module: ansible.module_ipadm_addrprop


Manage IP address properties on Solaris/illumos systems

## Description

Modify IP address properties on Solaris/illumos systems.

## Requirements

TODO

## Arguments

``` json
{
    "addrobj": "{'description': ['Specifies the address object we want to manage.'], 'required': True, 'aliases': ['nic', 'interface']}",
    "property": "{'description': ['Specifies the name of the address property we want to manage.'], 'required': True, 'aliases': ['name']}",
    "state": "{'description': ['Set or reset the property value.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent', 'reset']}",
    "temporary": "{'description': ['Specifies that the address property value is temporary. Temporary values do not persist across reboots.'], 'required': False, 'default': False}",
    "value": "{'description': ['Specifies the value we want to set for the address property.'], 'required': False}",
}
```

## Examples


``` yaml

- name: Mark address on addrobj as deprecated
  ipadm_addrprop: property=deprecated value=on addrobj=e1000g0/v6

- name: Set network prefix length for addrobj
  ipadm_addrprop: addrobj=bge0/v4 name=prefixlen value=26

```

## License

TODO

## Author Information
  - ['Adam Števko (@xen0l)']
