# Ansible module: ansible.module_ucs_lan_connectivity


Configures LAN Connectivity Policies on Cisco UCS Manager

## Description

Configures LAN Connectivity Policies on Cisco UCS Manager.
Examples can be used with the UCS Platform Emulator U(https://communities.cisco.com/ucspe).

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['A description of the LAN Connectivity Policy.', 'Cisco recommends including information about where and when to use the policy.', 'Enter up to 256 characters.', 'You can use any characters or spaces except the following:', '` (accent mark),  (backslash), ^ (carat), " (double quote), = (equal sign), > (greater than), < (less than), or \' (single quote).'], 'aliases': ['descr']}",
    "hostname": "{'description': ['IP address or hostname of Cisco UCS Manager.'], 'type': 'str', 'required': True}",
    "name": "{'description': ['The name of the LAN Connectivity Policy.', 'This name can be between 1 and 16 alphanumeric characters.', 'You cannot use spaces or any special characters other than - (hyphen), "_" (underscore), : (colon), and . (period).', 'You cannot change this name after the policy is created.'], 'required': True}",
    "org_dn": "{'description': ['Org dn (distinguished name)'], 'default': 'org-root'}",
    "password": "{'description': ['Password for Cisco UCS Manager authentication.'], 'type': 'str', 'required': True}",
    "port": "{'description': ['Port number to be used during connection (by default uses 443 for https and 80 for http connection).'], 'type': 'int'}",
    "proxy": "{'description': ["If use_proxy is no, specfies proxy to be used for connection. e.g. 'http://proxy.xy.z:8080'"], 'type': 'str'}",
    "state": "{'description': ['If C(present), will verify LAN Connectivity Policies are present and will create if needed.', 'If C(absent), will verify LAN Connectivity Policies are absent and will delete if needed.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "use_proxy": "{'description': ['If C(no), will not use the proxy as defined by system environment variable.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['Username for Cisco UCS Manager authentication.'], 'type': 'str', 'default': 'admin'}",
    "vnic_list": "{'description': ['List of vNICs used by the LAN Connectivity Policy.', 'vNICs used by the LAN Connectivity Policy must be created from a vNIC template.', 'Each list element has the following suboptions:', '= name', '  The name of the vNIC (required).', '= vnic_template', '  The name of the vNIC template (required).', '- adapter_policy', '  The name of the Ethernet adapter policy.', '  A user defined policy can be used, or one of the system defined policies.', '- order', "  String specifying the vNIC assignment order (e.g., '1', '2').", '  [Default: unspecified]']}",
}
```

## Examples


``` yaml

- name: Configure LAN Connectivity Policy
  ucs_lan_connectivity:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: Cntr-LAN-Boot
    vnic_list:
    - name: Fabric-A
      vnic_template: vNIC-Template-A
      adapter_policy: Linux
    - name: Fabric-B
      vnic_template: vNIC-Template-B
      adapter_policy: Linux

- name: Remove LAN Connectivity Policy
  ucs_lan_connectivity:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: Cntr-LAN-Boot
    state: absent

```

## License

TODO

## Author Information
  - ['David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
  - ['David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
