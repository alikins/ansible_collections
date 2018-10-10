# Ansible module: ansible.module_ipadm_if


Manage IP interfaces  on Solaris/illumos systems

## Description

Create, delete, enable or disable IP interfaces on Solaris/illumos systems.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['IP interface name.'], 'required': True}",
    "state": "{'description': ['Create or delete Solaris/illumos IP interfaces.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled']}",
    "temporary": "{'description': ['Specifies that the IP interface is temporary. Temporary IP interfaces do not persist across reboots.'], 'required': False, 'default': False, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Create vnic0 interface
- ipadm_if:
    name: vnic0
    state: enabled

# Disable vnic0 interface
- ipadm_if:
    name: vnic0
    state: disabled

```

## License

TODO

## Author Information
  - ['Adam Števko (@xen0l)']
