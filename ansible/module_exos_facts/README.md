# Ansible module: ansible.module_exos_facts


Collect facts from devices running Extreme EXOS

## Description

Collects a base set of device facts from a remote device that is running EXOS.  This module prepends all of the base network fact keys with C(ansible_net_<fact>).  The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## Requirements

TODO

## Arguments

``` json
{
    "gather_subset": "{'description': ['When supplied, this argument will restrict the facts collected to a given subset.  Possible values for this argument include all, hardware, config, and interfaces.  Can specify a list of values to include a larger subset.  Values can also be used with an initial C(M(!)) to specify that a specific subset should not be collected.'], 'required': False, 'default': ['!config']}",
}
```

## Examples


``` yaml

  - name: collect all facts from the device
    exos_facts:
      gather_subset: all

  - name: collect only the config and default facts
    exos_facts:
      gather_subset: config

  - name: do not collect hardware facts
    exos_facts:
      gather_subset: "!hardware"

```

## License

TODO

## Author Information
  - ['Lance Richardson (@hlrichardson)']
