# Ansible module: ansible.module_ipmi_power


Power management for machine

## Description

Use this module for power management

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Hostname or ip address of the BMC.'], 'required': True}",
    "password": "{'description': ['Password to connect to the BMC.'], 'required': True}",
    "port": "{'description': ['Remote RMCP port.'], 'default': 623}",
    "state": "{'description': ['Whether to ensure that the machine in desired state.'], 'required': True, 'choices': ['on -- Request system turn on', 'off -- Request system turn off without waiting for OS to shutdown', 'shutdown -- Have system request OS proper shutdown', 'reset -- Request system reset without waiting for OS', "boot -- If system is off, then 'on', else 'reset'"]}",
    "timeout": "{'description': ['Maximum number of seconds before interrupt request.'], 'default': 300}",
    "user": "{'description': ['Username to use to connect to the BMC.'], 'required': True}",
}
```

## Examples


``` yaml

# Ensure machine is powered on.
- ipmi_power:
    name: test.testdomain.com
    user: admin
    password: password
    state: on

```

## License

TODO

## Author Information
  - ['Bulat Gaifullin (gaifullinbf@gmail.com)']
