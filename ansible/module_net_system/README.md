# Ansible module: ansible.module_net_system


Manage the system attributes on network devices

## Description

This module provides declarative management of node system attributes on network devices.  It provides an option to configure host system parameters or remove those parameters from the device active configuration.

## Requirements

TODO

## Arguments

``` json
{
    "domain_name": "{'description': ['Configure the IP domain name on the remote device to the provided value. Value should be in the dotted name form and will be appended to the C(hostname) to create a fully-qualified domain name.']}",
    "domain_search": "{'description': ['Provides the list of domain suffixes to append to the hostname for the purpose of doing name resolution. This argument accepts a list of names and will be reconciled with the current active configuration on the running node.']}",
    "hostname": "{'description': ['Configure the device hostname parameter. This option takes an ASCII string value.']}",
    "lookup_source": "{'description': ['Provides one or more source interfaces to use for performing DNS lookups.  The interface provided in C(lookup_source) must be a valid interface configured on the device.']}",
    "name_servers": "{'description': ['List of DNS name servers by IP address to use to perform name resolution lookups.  This argument accepts either a list of DNS servers See examples.']}",
    "state": "{'description': ["State of the configuration values in the device's current active configuration.  When set to I(present), the values should be configured in the device active configuration and when set to I(absent) the values should not be in the device active configuration"], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: configure hostname and domain name
  net_system:
    hostname: ios01
    domain_name: test.example.com
    domain-search:
      - ansible.com
      - redhat.com
      - cisco.com

- name: remove configuration
  net_system:
    state: absent

- name: configure DNS lookup sources
  net_system:
    lookup_source: MgmtEth0/0/CPU0/0

- name: configure name servers
  net_system:
    name_servers:
      - 8.8.8.8
      - 8.8.4.4

```

## License

TODO

## Author Information
  - ['Ricardo Carrillo Cruz (@rcarrillocruz)']
