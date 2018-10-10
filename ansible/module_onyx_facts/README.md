# Ansible module: ansible.module_onyx_facts


Collect facts from Mellanox ONYX network devices

## Description

Collects a base set of device facts from a ONYX Mellanox network devices This module prepends all of the base network fact keys with C(ansible_net_<fact>).  The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## Requirements

TODO

## Arguments

``` json
{
    "gather_subset": "{'description': ['When supplied, this argument will restrict the facts collected to a given subset.  Possible values for this argument include all, version, module, and interfaces.  Can specify a list of values to include a larger subset.  Values can also be used with an initial C(M(!)) to specify that a specific subset should not be collected.'], 'required': False, 'default': 'version'}",
}
```

## Examples


``` yaml

---
- name: Collect all facts from the device
  onyx_facts:
    gather_subset: all

- name: Collect only the interfaces facts
  onyx_facts:
    gather_subset:
      - interfaces

- name: Do not collect version facts
  onyx_facts:
    gather_subset:
      - "!version"

```

## License

TODO

## Author Information
  - ['Waleed Mousa (@waleedym), Samer Deeb (@samerd)']
