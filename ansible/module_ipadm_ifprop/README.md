# Ansible module: ansible.module_ipadm_ifprop


Manage IP interface properties on Solaris/illumos systems

## Description

Modify IP interface properties on Solaris/illumos systems.

## Requirements

TODO

## Arguments

``` json
{
    "interface": "{'description': ['Specifies the IP interface we want to manage.'], 'required': True, 'aliases': ['nic']}",
    "property": "{'description': ['Specifies the name of the property we want to manage.'], 'required': True, 'aliases': ['name']}",
    "protocol": "{'description': ['Specifies the procotol for which we want to manage properties.'], 'required': True}",
    "state": "{'description': ['Set or reset the property value.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent', 'reset']}",
    "temporary": "{'description': ['Specifies that the property value is temporary. Temporary property values do not persist across reboots.'], 'required': False, 'default': False}",
    "value": "{'description': ['Specifies the value we want to set for the property.'], 'required': False}",
}
```

## Examples


``` yaml

- name: Allow forwarding of IPv4 packets on network interface e1000g0
  ipadm_ifprop: protocol=ipv4 property=forwarding value=on interface=e1000g0

- name: Temporarily reset IPv4 forwarding property on network interface e1000g0
  ipadm_ifprop: protocol=ipv4 interface=e1000g0  temporary=true property=forwarding state=reset

- name: Configure IPv6 metric on network interface e1000g0
  ipadm_ifprop: protocol=ipv6 nic=e1000g0 name=metric value=100

- name: Set IPv6 MTU on network interface bge0
  ipadm_ifprop: interface=bge0 name=mtu value=1280 protocol=ipv6

```

## License

TODO

## Author Information
  - ['Adam Števko (@xen0l)']
