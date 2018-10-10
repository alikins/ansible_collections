# Ansible module: ansible.module_snmp_facts


Retrieve facts for a device using SNMP

## Description

Retrieve facts for a device using SNMP, the facts will be inserted to the ansible_facts key.

## Requirements

TODO

## Arguments

``` json
{
    "authkey": "{'description': ['Authentication key, required if version is v3'], 'required': False}",
    "community": "{'description': ['The SNMP community string, required if version is v2/v2c'], 'required': False}",
    "host": "{'description': ['Set to target snmp server (normally {{inventory_hostname}})'], 'required': True}",
    "integrity": "{'description': ['Hashing algorithm, required if version is v3'], 'choices': ['md5', 'sha'], 'required': False}",
    "level": "{'description': ['Authentication level, required if version is v3'], 'choices': ['authPriv', 'authNoPriv'], 'required': False}",
    "privacy": "{'description': ['Encryption algorithm, required if level is authPriv'], 'choices': ['des', 'aes'], 'required': False}",
    "privkey": "{'description': ['Encryption key, required if version is authPriv'], 'required': False}",
    "username": "{'description': ['Username for SNMPv3, required if version is v3'], 'required': False}",
    "version": "{'description': ['SNMP Version to use, v2/v2c or v3'], 'choices': ['v2', 'v2c', 'v3'], 'required': True}",
}
```

## Examples


``` yaml

# Gather facts with SNMP version 2
- snmp_facts:
    host: '{{ inventory_hostname }}'
    version: v2c
    community: public
  delegate_to: local

# Gather facts using SNMP version 3
- snmp_facts:
    host: '{{ inventory_hostname }}'
    version: v3
    level: authPriv
    integrity: sha
    privacy: aes
    username: snmp-user
    authkey: abc12345
    privkey: def6789
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Patrick Ogenstad (@ogenstad)']
