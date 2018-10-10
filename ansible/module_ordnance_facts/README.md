# Ansible module: ansible.module_ordnance_facts


Collect facts from Ordnance Virtual Routers over SSH

## Description

Collects a base set of device facts from an Ordnance Virtual router over SSH. This module prepends all of the base network fact keys with C(ansible_net_<fact>).  The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## Requirements

TODO

## Arguments

``` json
{
    "gather_subset": "{'description': ['When supplied, this argument will restrict the facts collected to a given subset.  Possible values for this argument include all, hardware, config, and interfaces.  Can specify a list of values to include a larger subset.  Values can also be used with an initial C(M(!)) to specify that a specific subset should not be collected.'], 'required': False, 'default': '!config'}",
}
```

## Examples


``` yaml

---
# Note: examples below use the following provider dict to handle
#       transport and authentication to the node.
vars:
  cli:
    host: "{{ inventory_hostname }}"
    username: RouterName
    password: ordnance
    transport: cli

---
# Collect all facts from the device
- ordnance_facts:
    gather_subset: all
    provider: "{{ cli }}"

# Collect only the config and default facts
- ordnance_facts:
    gather_subset:
      - config
    provider: "{{ cli }}"

# Do not collect hardware facts
- ordnance_facts:
    gather_subset:
      - "!hardware"
    provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Alexander Turner (alex.turner@ordnance.io)']
