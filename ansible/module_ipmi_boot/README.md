# Ansible module: ansible.module_ipmi_boot


Management of order of boot devices

## Description

Use this module to manage order of boot devices

## Requirements

TODO

## Arguments

``` json
{
    "bootdev": "{'description': ['Set boot device to use on next reboot'], 'required': True, 'choices': ['network -- Request network boot', 'floppy -- Boot from floppy', 'hd -- Boot from hard drive', "safe -- Boot from hard drive, requesting 'safe mode'", 'optical -- boot from CD/DVD/BD drive', 'setup -- Boot into setup utility', 'default -- remove any IPMI directed boot device request']}",
    "name": "{'description': ['Hostname or ip address of the BMC.'], 'required': True}",
    "password": "{'description': ['Password to connect to the BMC.'], 'required': True}",
    "persistent": "{'description': ['If set, ask that system firmware uses this device beyond next boot. Be aware many systems do not honor this.'], 'type': 'bool', 'default': False}",
    "port": "{'description': ['Remote RMCP port.'], 'default': 623}",
    "state": "{'description': ['Whether to ensure that boot devices is desired.'], 'default': 'present', 'choices': ['present -- Request system turn on', 'absent -- Request system turn on']}",
    "uefiboot": "{'description': ['If set, request UEFI boot explicitly. Strictly speaking, the spec suggests that if not set, the system should BIOS boot and offers no "don\'t care" option. In practice, this flag not being set does not preclude UEFI boot on any system I\'ve encountered.'], 'type': 'bool', 'default': False}",
    "user": "{'description': ['Username to use to connect to the BMC.'], 'required': True}",
}
```

## Examples


``` yaml

# Ensure bootdevice is HD.
- ipmi_boot:
    name: test.testdomain.com
    user: admin
    password: password
    bootdev: hd

# Ensure bootdevice is not Network
- ipmi_boot:
    name: test.testdomain.com
    user: admin
    password: password
    bootdev: network
    state: absent

```

## License

TODO

## Author Information
  - ['Bulat Gaifullin (gaifullinbf@gmail.com)']
