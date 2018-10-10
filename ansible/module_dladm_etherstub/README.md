# Ansible module: ansible.module_dladm_etherstub


Manage etherstubs on Solaris/illumos systems

## Description

Create or delete etherstubs on Solaris/illumos systems.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Etherstub name.'], 'required': True}",
    "state": "{'description': ['Create or delete Solaris/illumos etherstub.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "temporary": "{'description': ['Specifies that the etherstub is temporary. Temporary etherstubs do not persist across reboots.'], 'required': False, 'default': False, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Create 'stub0' etherstub
- dladm_etherstub:
    name: stub0
    state: present

# Remove 'stub0 etherstub
- dladm_etherstub:
    name: stub0
    state: absent

```

## License

TODO

## Author Information
  - ['Adam Števko (@xen0l)']
