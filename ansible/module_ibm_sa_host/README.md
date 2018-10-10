# Ansible module: ansible.module_ibm_sa_host


Adds hosts to or removes them from IBM Spectrum Accelerate storage systems

## Description

This module adds hosts to or removes them from IBM Spectrum Accelerate storage systems.

## Requirements

TODO

## Arguments

``` json
{
    "cluster": "{'description': ['The name of the cluster to include the host.'], 'required': False}",
    "domain": "{'description': ['The domains the cluster will be attached to. To include more than one domain, separate domain names with commas. To include all existing domains, use an asterisk ("*").'], 'required': False}",
    "endpoints": "{'description': ['The hostname or management IP of Spectrum Accelerate storage system.'], 'required': True}",
    "host": "{'description': ['Host name.'], 'required': True}",
    "iscsi_chap_name": "{'description': ["The host's CHAP name identifier"], 'required': False}",
    "iscsi_chap_secret": "{'description': ['The password of the initiator used to authenticate to the system when CHAP is enable'], 'required': False}",
    "password": "{'description': ['Password for username on the spectrum accelerate storage system.'], 'required': True}",
    "state": "{'description': ['Host state.'], 'required': True, 'default': 'present', 'choices': ['present', 'absent']}",
    "username": "{'description': ['Management user on the spectrum accelerate storage system.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Define new host.
  ibm_sa_host:
    host: host_name
    state: present
    username: admin
    password: secret
    endpoints: hostdev-system

- name: Delete host.
  ibm_sa_host:
    host: host_name
    state: absent
    username: admin
    password: secret
    endpoints: hostdev-system

```

## License

TODO

## Author Information
  - ['Tzur Eliyahu (tzure@il.ibm.com)']
