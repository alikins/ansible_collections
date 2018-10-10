# Ansible module: ansible.module_edgeos_facts


Collect facts from remote devices running EdgeOS

## Description

Collects a base set of device facts from a remote device that is running EdgeOS. This module prepends all of the base network fact keys with U(ansible_net_<fact>). The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## Requirements

TODO

## Arguments

``` json
{
    "gather_subset": "{'description': ['When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all, default, config, and neighbors. Can specify a list of values to include a larger subset. Values can also be used with an initial C(M(!)) to specify that a specific subset should not be collected.'], 'required': False, 'default': '!config'}",
}
```

## Examples


``` yaml

- name: collect all facts from the device
  edgeos_facts:
    gather_subset: all

- name: collect only the config and default facts
  edgeos_facts:
    gather_subset: config

- name: collect everything exception the config
  edgeos_facts:
    gather_subset: "!config"

```

## License

TODO

## Author Information
  - ['Nathaniel Case (@qalthos)', 'Sam Doran (@samdoran)']
  - ['Nathaniel Case (@qalthos)', 'Sam Doran (@samdoran)']
