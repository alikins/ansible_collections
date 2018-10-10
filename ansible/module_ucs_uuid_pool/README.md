# Ansible module: ansible.module_ucs_uuid_pool


Configures server UUID pools on Cisco UCS Manager

## Description

Configures server UUID pools and UUID blocks on Cisco UCS Manager.
Examples can be used with the L(UCS Platform Emulator,https://communities.cisco.com/ucspe).

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['The user-defined description of the UUID pool.', 'Enter up to 256 characters.', 'You can use any characters or spaces except the following:', '` (accent mark),  (backslash), ^ (carat), " (double quote), = (equal sign), > (greater than), < (less than), or \' (single quote).'], 'aliases': ['descr']}",
    "first_uuid": "{'description': ['The first UUID in the block of UUIDs.', 'This is the From field in the UCS Manager UUID Blocks menu.']}",
    "hostname": "{'description': ['IP address or hostname of Cisco UCS Manager.'], 'type': 'str', 'required': True}",
    "last_uuid": "{'description': ['The last UUID in the block of UUIDs.', 'This is the To field in the UCS Manager Add UUID Blocks menu.']}",
    "name": "{'description': ['The name of the UUID pool.', 'This name can be between 1 and 32 alphanumeric characters.', 'You cannot use spaces or any special characters other than - (hyphen), "_" (underscore), : (colon), and . (period).', 'You cannot change this name after the UUID pool is created.'], 'required': True}",
    "order": "{'description': ['The Assignment Order field.', 'This can be one of the following:', 'default - Cisco UCS Manager selects a random identity from the pool.', 'sequential - Cisco UCS Manager selects the lowest available identity from the pool.'], 'choices': ['default', 'sequential'], 'default': 'default'}",
    "org_dn": "{'description': ['The distinguished name (dn) of the organization where the resource is assigned.'], 'default': 'org-root'}",
    "password": "{'description': ['Password for Cisco UCS Manager authentication.'], 'type': 'str', 'required': True}",
    "port": "{'description': ['Port number to be used during connection (by default uses 443 for https and 80 for http connection).'], 'type': 'int'}",
    "prefix": "{'description': ['UUID prefix used for the range of server UUIDs.', "If no value is provided, the system derived prefix will be used (equivalent to selecting 'derived' option in UI).", "If the user provides a value, the user provided prefix will be used (equivalent to selecting 'other' option in UI).", 'A user provided value should be in the format XXXXXXXX-XXXX-XXXX.']}",
    "proxy": "{'description': ["If use_proxy is no, specfies proxy to be used for connection. e.g. 'http://proxy.xy.z:8080'"], 'type': 'str'}",
    "state": "{'description': ['If C(present), will verify UUID pool is present and will create if needed.', 'If C(absent), will verify UUID pool is absent and will delete if needed.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "use_proxy": "{'description': ['If C(no), will not use the proxy as defined by system environment variable.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['Username for Cisco UCS Manager authentication.'], 'type': 'str', 'default': 'admin'}",
}
```

## Examples


``` yaml

- name: Configure UUID address pool
  ucs_uuid_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: UUID-Pool
    order: sequential
    first_uuid: 0000-000000000001
    last_uuid: 0000-000000000078

- name: Remove UUID address pool
  ucs_uuid_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: UUID-Pool
    state: absent

```

## License

TODO

## Author Information
  - ['David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
  - ['David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
