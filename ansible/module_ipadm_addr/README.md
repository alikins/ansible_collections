# Ansible module: ansible.module_ipadm_addr


Manage IP addresses on an interface on Solaris/illumos systems

## Description

Create/delete static/dynamic IP addresses on network interfaces on Solaris/illumos systems.
Up/down static/dynamic IP addresses on network interfaces on Solaris/illumos systems.
Manage IPv6 link-local addresses on network interfaces on Solaris/illumos systems.

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['Specifiies an IP address to configure in CIDR notation.'], 'required': False, 'aliases': ['addr']}",
    "addrobj": "{'description': ['Specifies an unique IP address on the system.'], 'required': True}",
    "addrtype": "{'description': ['Specifiies a type of IP address to configure.'], 'required': False, 'default': 'static', 'choices': ['static', 'dhcp', 'addrconf']}",
    "state": "{'description': ['Create/delete/enable/disable an IP address on the network interface.'], 'required': False, 'default': 'present', 'choices': ['absent', 'present', 'up', 'down', 'enabled', 'disabled', 'refreshed']}",
    "temporary": "{'description': ['Specifies that the configured IP address is temporary. Temporary IP addresses do not persist across reboots.'], 'required': False, 'default': False}",
    "wait": "{'description': ['Specifies the time in seconds we wait for obtaining address via DHCP.'], 'required': False, 'default': 60}",
}
```

## Examples


``` yaml

- name: Configure IP address 10.0.0.1 on e1000g0
  ipadm_addr: addr=10.0.0.1/32 addrobj=e1000g0/v4 state=present

- name: Delete addrobj
  ipadm_addr: addrobj=e1000g0/v4 state=absent

- name: Configure link-local IPv6 address
  ipadm_addr: addtype=addrconf addrobj=vnic0/v6

- name: Configure address via DHCP and wait 180 seconds for address obtaining
  ipadm_addr: addrobj=vnic0/dhcp addrtype=dhcp wait=180

```

## License

TODO

## Author Information
  - ['Adam Števko (@xen0l)']
