# Ansible module: ansible.module_hpilo_facts


Gather facts through an HP iLO interface

## Description

This module gathers facts for a specific system using its HP iLO interface. These facts include hardware and network related information useful for provisioning (e.g. macaddress, uuid).
This module requires the hpilo python module.

## Requirements

TODO

## Arguments

``` json
{
    "host": "{'description': ['The HP iLO hostname/address that is linked to the physical system.'], 'required': True}",
    "login": "{'description': ['The login name to authenticate to the HP iLO interface.'], 'default': 'Administrator'}",
    "password": "{'description': ['The password to authenticate to the HP iLO interface.'], 'default': 'admin'}",
    "ssl_version": "{'description': ['Change the ssl_version used.'], 'default': 'TLSv1', 'choices': ['SSLv3', 'SSLv23', 'TLSv1', 'TLSv1_1', 'TLSv1_2'], 'version_added': '2.4'}",
}
```

## Examples


``` yaml

# Task to gather facts from a HP iLO interface only if the system is an HP server
- hpilo_facts:
    host: YOUR_ILO_ADDRESS
    login: YOUR_ILO_LOGIN
    password: YOUR_ILO_PASSWORD
  when: cmdb_hwmodel.startswith('HP ')
  delegate_to: localhost

- fail:
    msg: 'CMDB serial ({{ cmdb_serialno }}) does not match hardware serial ({{ hw_system_serial }}) !'
  when: cmdb_serialno != hw_system_serial

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
