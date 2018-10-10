# Ansible module: ansible.module_hpilo_boot


Boot system using specific media through HP iLO interface

## Description

This module boots a system through its HP iLO interface. The boot media can be one of: cdrom, floppy, hdd, network or usb.
This module requires the hpilo python module.

## Requirements

TODO

## Arguments

``` json
{
    "force": "{'description': ['Whether to force a reboot (even when the system is already booted).', 'As a safeguard, without force, hpilo_boot will refuse to reboot a server that is already running.'], 'default': False, 'type': 'bool'}",
    "host": "{'description': ['The HP iLO hostname/address that is linked to the physical system.'], 'required': True}",
    "image": "{'description': ['The URL of a cdrom, floppy or usb boot media image. protocol://username:password@hostname:port/filename', "protocol is either 'http' or 'https'", 'username:password is optional', 'port is optional']}",
    "login": "{'description': ['The login name to authenticate to the HP iLO interface.'], 'default': 'Administrator'}",
    "media": "{'description': ['The boot media to boot the system from'], 'default': 'network', 'choices': ['cdrom', 'floppy', 'hdd', 'network', 'normal', 'usb']}",
    "password": "{'description': ['The password to authenticate to the HP iLO interface.'], 'default': 'admin'}",
    "ssl_version": "{'description': ['Change the ssl_version used.'], 'default': 'TLSv1', 'choices': ['SSLv3', 'SSLv23', 'TLSv1', 'TLSv1_1', 'TLSv1_2'], 'version_added': '2.4'}",
    "state": "{'description': ['The state of the boot media.', 'no_boot: Do not boot from the device', 'boot_once: Boot from the device once and then notthereafter', 'boot_always: Boot from the device each time the serveris rebooted', 'connect: Connect the virtual media device and set to boot_always', 'disconnect: Disconnects the virtual media device and set to no_boot', 'poweroff: Power off the server'], 'default': 'boot_once', 'choices': ['boot_always', 'boot_once', 'connect', 'disconnect', 'no_boot', 'poweroff']}",
}
```

## Examples


``` yaml

- name: Task to boot a system using an ISO from an HP iLO interface only if the system is an HP server
  hpilo_boot:
    host: YOUR_ILO_ADDRESS
    login: YOUR_ILO_LOGIN
    password: YOUR_ILO_PASSWORD
    media: cdrom
    image: http://some-web-server/iso/boot.iso
  when: cmdb_hwmodel.startswith('HP ')
  delegate_to: localhost

- name: Power off a server
  hpilo_boot:
    host: YOUR_ILO_HOST
    login: YOUR_ILO_LOGIN
    password: YOUR_ILO_PASSWORD
    state: poweroff
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
