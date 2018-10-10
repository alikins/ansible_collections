# Ansible module: ansible.module_ucs_vsans


Configures VSANs on Cisco UCS Manager

## Description

Configures VSANs on Cisco UCS Manager.
Examples can be used with the UCS Platform Emulator U(https://communities.cisco.com/ucspe).

## Requirements

TODO

## Arguments

``` json
{
    "fabric": "{'description': ['The fabric configuration of the VSAN.  This can be one of the following:', 'common - The VSAN maps to the same VSAN ID in all available fabrics.', 'A - The VSAN maps to the a VSAN ID that exists only in fabric A.', 'B - The VSAN maps to the a VSAN ID that exists only in fabric B.'], 'choices': ['common', 'A', 'B'], 'default': 'common'}",
    "fc_zoning": "{'description': ['Fibre Channel zoning configuration for the Cisco UCS domain.', 'Fibre Channel zoning can be set to one of the following values:', 'disabled — The upstream switch handles Fibre Channel zoning, or Fibre Channel zoning is not implemented for the Cisco UCS domain.', 'enabled — Cisco UCS Manager configures and controls Fibre Channel zoning for the Cisco UCS domain.', 'If you enable Fibre Channel zoning, do not configure the upstream switch with any VSANs that are being used for Fibre Channel zoning.'], 'choices': ['disabled', 'enabled'], 'default': 'disabled'}",
    "hostname": "{'description': ['IP address or hostname of Cisco UCS Manager.'], 'type': 'str', 'required': True}",
    "name": "{'description': ['The name assigned to the VSAN.', 'This name can be between 1 and 32 alphanumeric characters.', 'You cannot use spaces or any special characters other than - (hyphen), "_" (underscore), : (colon), and . (period).', 'You cannot change this name after the VSAN is created.'], 'required': True}",
    "password": "{'description': ['Password for Cisco UCS Manager authentication.'], 'type': 'str', 'required': True}",
    "port": "{'description': ['Port number to be used during connection (by default uses 443 for https and 80 for http connection).'], 'type': 'int'}",
    "proxy": "{'description': ["If use_proxy is no, specfies proxy to be used for connection. e.g. 'http://proxy.xy.z:8080'"], 'type': 'str'}",
    "state": "{'description': ['If C(present), will verify VSANs are present and will create if needed.', 'If C(absent), will verify VSANs are absent and will delete if needed.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "use_proxy": "{'description': ['If C(no), will not use the proxy as defined by system environment variable.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['Username for Cisco UCS Manager authentication.'], 'type': 'str', 'default': 'admin'}",
    "vlan_id": "{'description': ['The unique string identifier assigned to the VLAN used for Fibre Channel connections.', "Note that Cisco UCS Manager uses VLAN '4048'.  See the UCS Manager configuration guide if you want to assign '4048' to a VLAN.", 'Optional if state is absent.'], 'required': True}",
    "vsan_id": "{'description': ['The unique identifier assigned to the VSAN.', "The ID can be a string between '1' and '4078', or between '4080' and '4093'. '4079' is a reserved VSAN ID.", "In addition, if you plan to use FC end-host mode, the range between '3840' to '4079' is also a reserved VSAN ID range.", 'Optional if state is absent.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Configure VSAN
  ucs_vsans:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: vsan110
    vsan_id: '110'
    vlan_id: '110'

- name: Remove VSAN
  ucs_vsans:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: vsan110

```

## License

TODO

## Author Information
  - ['David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
  - ['David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
