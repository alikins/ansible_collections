# Ansible module: ansible.module_ucs_wwn_pool


Configures WWNN or WWPN pools on Cisco UCS Manager

## Description

Configures WWNNs or WWPN pools on Cisco UCS Manager.
Examples can be used with the UCS Platform Emulator U(https://communities.cisco.com/ucspe).

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['A description of the WWNN or WWPN pool.', 'Enter up to 256 characters.', 'You can use any characters or spaces except the following:', '` (accent mark),  (backslash), ^ (carat), " (double quote), = (equal sign), > (greater than), < (less than), or \' (single quote).'], 'aliases': ['descr']}",
    "first_addr": "{'description': ['The first initiator in the World Wide Name (WWN) block.', 'This is the From field in the UCS Manager Add WWN Blocks menu.']}",
    "hostname": "{'description': ['IP address or hostname of Cisco UCS Manager.'], 'type': 'str', 'required': True}",
    "last_addr": "{'description': ['The last initiator in the Worlde Wide Name (WWN) block.', 'This is the To field in the UCS Manager Add WWN Blocks menu.', 'For WWxN pools, the pool size must be a multiple of ports-per-node + 1.', 'For example, if there are 7 ports per node, the pool size must be a multiple of 8.', 'If there are 63 ports per node, the pool size must be a multiple of 64.']}",
    "name": "{'description': ['The name of the World Wide Node Name (WWNN) or World Wide Port Name (WWPN) pool.', 'This name can be between 1 and 32 alphanumeric characters.', 'You cannot use spaces or any special characters other than - (hyphen), "_" (underscore), : (colon), and . (period).', 'You cannot change this name after the WWNN or WWPN pool is created.'], 'required': True}",
    "order": "{'description': ['The Assignment Order field.', 'This can be one of the following:', 'default - Cisco UCS Manager selects a random identity from the pool.', 'sequential - Cisco UCS Manager selects the lowest available identity from the pool.'], 'choices': ['default', 'sequential'], 'default': 'default'}",
    "org_dn": "{'description': ['Org dn (distinguished name)'], 'default': 'org-root'}",
    "password": "{'description': ['Password for Cisco UCS Manager authentication.'], 'type': 'str', 'required': True}",
    "port": "{'description': ['Port number to be used during connection (by default uses 443 for https and 80 for http connection).'], 'type': 'int'}",
    "proxy": "{'description': ["If use_proxy is no, specfies proxy to be used for connection. e.g. 'http://proxy.xy.z:8080'"], 'type': 'str'}",
    "purpose": "{'description': ['Specify whether this is a node (WWNN) or port (WWPN) pool.', 'Optional if state is absent.'], 'choices': ['node', 'port'], 'required': True}",
    "state": "{'description': ['If C(present), will verify WWNNs/WWPNs are present and will create if needed.', 'If C(absent), will verify WWNNs/WWPNs are absent and will delete if needed.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "use_proxy": "{'description': ['If C(no), will not use the proxy as defined by system environment variable.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['Username for Cisco UCS Manager authentication.'], 'type': 'str', 'default': 'admin'}",
}
```

## Examples


``` yaml

- name: Configure WWNN/WWPN pools
  ucs_wwn_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: WWNN-Pool
    purpose: node
    first_addr: 20:00:00:25:B5:48:00:00
    last_addr: 20:00:00:25:B5:48:00:0F
- ucs_wwn_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: WWPN-Pool-A
    purpose: port
    order: sequential
    first_addr: 20:00:00:25:B5:48:0A:00
    last_addr: 20:00:00:25:B5:48:0A:0F

- name: Remove WWNN/WWPN pools
  ucs_wwn_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: WWNN-Pool
    state: absent
- ucs_wwn_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: WWPN-Pool-A
    state: absent

```

## License

TODO

## Author Information
  - ['David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
  - ['David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
