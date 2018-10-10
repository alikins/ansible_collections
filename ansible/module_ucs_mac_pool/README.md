# Ansible module: ansible.module_ucs_mac_pool


Configures MAC address pools on Cisco UCS Manager

## Description

Configures MAC address pools and MAC address blocks on Cisco UCS Manager.
Examples can be used with the UCS Platform Emulator U(https://communities.cisco.com/ucspe).

## Requirements

TODO

## Arguments

``` json
{
    "descrption": "{'description': ['A description of the MAC pool.', 'Enter up to 256 characters.', 'You can use any characters or spaces except the following:', '` (accent mark),  (backslash), ^ (carat), " (double quote), = (equal sign), > (greater than), < (less than), or \' (single quote).'], 'aliases': ['descr']}",
    "first_addr": "{'description': ['The first MAC address in the block of addresses.', 'This is the From field in the UCS Manager MAC Blocks menu.']}",
    "hostname": "{'description': ['IP address or hostname of Cisco UCS Manager.'], 'type': 'str', 'required': True}",
    "last_addr": "{'description': ['The last MAC address in the block of addresses.', 'This is the To field in the UCS Manager Add MAC Blocks menu.']}",
    "name": "{'description': ['The name of the MAC pool.', 'This name can be between 1 and 32 alphanumeric characters.', 'You cannot use spaces or any special characters other than - (hyphen), "_" (underscore), : (colon), and . (period).', 'You cannot change this name after the MAC pool is created.'], 'required': True}",
    "order": "{'description': ['The Assignment Order field.', 'This can be one of the following:', 'default - Cisco UCS Manager selects a random identity from the pool.', 'sequential - Cisco UCS Manager selects the lowest available identity from the pool.'], 'choices': ['default', 'sequential'], 'default': 'default'}",
    "org_dn": "{'description': ['The distinguished name (dn) of the organization where the resource is assigned.'], 'default': 'org-root'}",
    "password": "{'description': ['Password for Cisco UCS Manager authentication.'], 'type': 'str', 'required': True}",
    "port": "{'description': ['Port number to be used during connection (by default uses 443 for https and 80 for http connection).'], 'type': 'int'}",
    "proxy": "{'description': ["If use_proxy is no, specfies proxy to be used for connection. e.g. 'http://proxy.xy.z:8080'"], 'type': 'str'}",
    "state": "{'description': ['If C(present), will verify MAC pool is present and will create if needed.', 'If C(absent), will verify MAC pool is absent and will delete if needed.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "use_proxy": "{'description': ['If C(no), will not use the proxy as defined by system environment variable.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['Username for Cisco UCS Manager authentication.'], 'type': 'str', 'default': 'admin'}",
}
```

## Examples


``` yaml

- name: Configure MAC address pool
  ucs_mac_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: mac-A
    first_addr: 00:25:B5:00:66:00
    last_addr: 00:25:B5:00:67:F3
    order: sequential

- name: Remove MAC address pool
  ucs_mac_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: mac-A
    state: absent

```

## License

TODO

## Author Information
  - ['David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
  - ['David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
