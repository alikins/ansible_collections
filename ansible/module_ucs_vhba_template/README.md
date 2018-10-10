# Ansible module: ansible.module_ucs_vhba_template


Configures vHBA templates on Cisco UCS Manager

## Description

Configures vHBA templates on Cisco UCS Manager.
Examples can be used with the UCS Platform Emulator U(https://communities.cisco.com/ucspe).

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['A user-defined description of the template.', 'Enter up to 256 characters.', 'You can use any characters or spaces except the following:', '` (accent mark),  (backslash), ^ (carat), " (double quote), = (equal sign), > (greater than), < (less than), or \' (single quote).'], 'aliases': ['descr']}",
    "fabric": "{'description': ['The Fabric ID field.', 'The name of the fabric interconnect that vHBAs created with this template are associated with.'], 'choices': ['A', 'B'], 'default': 'A'}",
    "hostname": "{'description': ['IP address or hostname of Cisco UCS Manager.'], 'type': 'str', 'required': True}",
    "max_data": "{'description': ['The Max Data Field Size field.', 'The maximum size of the Fibre Channel frame payload bytes that the vHBA supports.', "Enter an string between '256' and '2112'."], 'default': '2048'}",
    "name": "{'description': ['The name of the virtual HBA template.', 'This name can be between 1 and 16 alphanumeric characters.', 'You cannot use spaces or any special characters other than - (hyphen), "_" (underscore), : (colon), and . (period).', 'You cannot change this name after the template is created.'], 'required': True}",
    "org_dn": "{'description': ['Org dn (distinguished name)'], 'default': 'org-root'}",
    "password": "{'description': ['Password for Cisco UCS Manager authentication.'], 'type': 'str', 'required': True}",
    "pin_group": "{'description': ['The SAN pin group that is associated with vHBAs created from this template.']}",
    "port": "{'description': ['Port number to be used during connection (by default uses 443 for https and 80 for http connection).'], 'type': 'int'}",
    "proxy": "{'description': ["If use_proxy is no, specfies proxy to be used for connection. e.g. 'http://proxy.xy.z:8080'"], 'type': 'str'}",
    "qos_policy": "{'description': ['The QoS policy that is associated with vHBAs created from this template.']}",
    "redundancy_type": "{'description': ['The Redundancy Type used for template pairing from the Primary or Secondary redundancy template.', 'primary — Creates configurations that can be shared with the Secondary template.', 'Any other shared changes on the Primary template are automatically synchronized to the Secondary template.', 'secondary — All shared configurations are inherited from the Primary template.', 'none - Legacy vHBA template behavior. Select this option if you do not want to use redundancy.'], 'choices': ['none', 'primary', 'secondary'], 'default': 'none'}",
    "state": "{'description': ['If C(present), will verify vHBA templates are present and will create if needed.', 'If C(absent), will verify vHBA templates are absent and will delete if needed.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "stats_policy": "{'description': ['The statistics collection policy that is associated with vHBAs created from this template.'], 'default': 'default'}",
    "template_type": "{'description': ['The Template Type field.', 'This can be one of the following:', 'initial-template — vHBAs created from this template are not updated if the template changes.', 'updating-template - vHBAs created from this template are updated if the template changes.'], 'choices': ['initial-template', 'updating-template'], 'default': 'initial-template'}",
    "use_proxy": "{'description': ['If C(no), will not use the proxy as defined by system environment variable.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['Username for Cisco UCS Manager authentication.'], 'type': 'str', 'default': 'admin'}",
    "vsan": "{'description': ['The VSAN to associate with vHBAs created from this template.'], 'default': 'default'}",
    "wwpn_pool": "{'description': ['The WWPN pool that a vHBA created from this template uses to derive its WWPN address.'], 'default': 'default'}",
}
```

## Examples


``` yaml

- name: Configure vHBA template
  ucs_vhba_template:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: vHBA-A
    fabric: A
    vsan: VSAN-A
    wwpn_pool: WWPN-Pool-A

- name: Remote vHBA template
  ucs_vhba_template:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: vHBA-A
    state: absent

```

## License

TODO

## Author Information
  - ['David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
  - ['David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
