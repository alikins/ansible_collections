# Ansible module: ansible.module_timezone


Configure timezone setting

## Description

This module configures the timezone setting, both of the system clock and of the hardware clock. If you want to set up the NTP, use M(service) module.
It is recommended to restart C(crond) after changing the timezone, otherwise the jobs may run at the wrong time.
Several different tools are used depending on the OS/Distribution involved. For Linux it can use C(timedatectl) or edit C(/etc/sysconfig/clock) or C(/etc/timezone) and C(hwclock). On SmartOS, C(sm-set-timezone), for macOS, C(systemsetup), for BSD, C(/etc/localtime) is modified.
As of version 2.3 support was added for SmartOS and BSDs.
As of version 2.4 support was added for macOS.
Windows, AIX and HPUX are not supported, please let us know if you find any other OS/distro in which this fails.

## Requirements

TODO

## Arguments

``` json
{
    "hwclock": "{'description': ['Whether the hardware clock is in UTC or in local timezone. Default is to keep current setting. Note that this option is recommended not to change and may fail to configure, especially on virtual environments such as AWS. B(At least one of name and hwclock are required.) I(Only used on Linux.)'], 'aliases': ['rtc'], 'choices': ['UTC', 'local']}",
    "name": "{'description': ['Name of the timezone for the system clock. Default is to keep current setting. B(At least one of name and hwclock are required.)']}",
}
```

## Examples


``` yaml

- name: set timezone to Asia/Tokyo
  timezone:
    name: Asia/Tokyo

```

## License

TODO

## Author Information
  - ['Shinichi TAMURA (@tmshn)', 'Jasper Lievisse Adriaanse (@jasperla)', 'Indrajit Raychaudhuri (@indrajitr)']
  - ['Shinichi TAMURA (@tmshn)', 'Jasper Lievisse Adriaanse (@jasperla)', 'Indrajit Raychaudhuri (@indrajitr)']
  - ['Shinichi TAMURA (@tmshn)', 'Jasper Lievisse Adriaanse (@jasperla)', 'Indrajit Raychaudhuri (@indrajitr)']
