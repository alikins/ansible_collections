# Ansible module: ansible.module_routeros_facts


Collect facts from remote devices running MikroTik RouterOS

## Description

Collects a base set of device facts from a remote device that is running RotuerOS.  This module prepends all of the base network fact keys with C(ansible_net_<fact>).  The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## Requirements

TODO

## Arguments

``` json
{
    "gather_subset": "{'description': ['When supplied, this argument will restrict the facts collected to a given subset.  Possible values for this argument include C(all), C(hardware), C(config), and C(interfaces).  Can specify a list of values to include a larger subset.  Values can also be used with an initial C(!) to specify that a specific subset should not be collected.'], 'required': False, 'default': '!config'}",
}
```

## Examples


``` yaml

# Collect all facts from the device
- routeros_facts:
    gather_subset: all

# Collect only the config and default facts
- routeros_facts:
    gather_subset:
      - config

# Do not collect hardware facts
- routeros_facts:
    gather_subset:
      - "!hardware"

```

## License

TODO

## Author Information
  - ['Egor Zaitsev (@heuels)']
