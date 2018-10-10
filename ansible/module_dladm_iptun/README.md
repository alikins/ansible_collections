# Ansible module: ansible.module_dladm_iptun


Manage IP tunnel interfaces on Solaris/illumos systems

## Description

Manage IP tunnel interfaces on Solaris/illumos systems.

## Requirements

TODO

## Arguments

``` json
{
    "local_address": "{'description': ['Literat IP address or hostname corresponding to the tunnel source.'], 'required': False, 'aliases': ['local']}",
    "name": "{'description': ['IP tunnel interface name.'], 'required': True}",
    "remote_address": "{'description': ['Literal IP address or hostname corresponding to the tunnel destination.'], 'required': False, 'aliases': ['remote']}",
    "state": "{'description': ['Create or delete Solaris/illumos VNIC.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "temporary": "{'description': ['Specifies that the IP tunnel interface is temporary. Temporary IP tunnel interfaces do not persist across reboots.'], 'required': False, 'default': False}",
    "type": "{'description': ['Specifies the type of tunnel to be created.'], 'required': False, 'default': 'ipv4', 'choices': ['ipv4', 'ipv6', '6to4'], 'aliases': ['tunnel_type']}",
}
```

## Examples


``` yaml

- name: Create IPv4 tunnel interface 'iptun0'
  dladm_iptun: name=iptun0 local_address=192.0.2.23 remote_address=203.0.113.10 state=present

- name: Change IPv4 tunnel remote address
  dladm_iptun: name=iptun0 type=ipv4 local_address=192.0.2.23 remote_address=203.0.113.11

- name: Create IPv6 tunnel interface 'tun0'
  dladm_iptun: name=tun0 type=ipv6 local_address=192.0.2.23 remote_address=203.0.113.42

- name: Remove 'iptun0' tunnel interface
  dladm_iptun: name=iptun0 state=absent

```

## License

TODO

## Author Information
  - ['Adam Števko (@xen0l)']
