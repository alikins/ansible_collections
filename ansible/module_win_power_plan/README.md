# Ansible module: ansible.module_win_power_plan


Changes the power plan of a Windows system

## Description

This module will change the power plan of a Windows system to the defined string.
Windows defaults to C(balanced) which will cause CPU throttling. In some cases it can be preferable to change the mode to C(high performance) to increase CPU performance.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['String value that indicates the desired power plan. The power plan must already be present on the system. Commonly there will be options for C(balanced) and C(high performance).'], 'required': True}",
}
```

## Examples


``` yaml

- name: Change power plan to high performance
  win_power_plan:
    name: high performance

```

## License

TODO

## Author Information
  - ['Noah Sparks (@nwsparks)']
