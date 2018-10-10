# Ansible module: ansible.module_ucs_san_connectivity


Configures SAN Connectivity Policies on Cisco UCS Manager

## Description

Configures SAN Connectivity Policies on Cisco UCS Manager.
Examples can be used with the UCS Platform Emulator U(https://communities.cisco.com/ucspe).

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['A description of the policy.', 'Cisco recommends including information about where and when to use the policy.', 'Enter up to 256 characters.', 'You can use any characters or spaces except the following:', '` (accent mark),  (backslash), ^ (carat), " (double quote), = (equal sign), > (greater than), < (less than), or \' (single quote).'], 'aliases': ['descr']}",
    "hostname": "{'description': ['IP address or hostname of Cisco UCS Manager.'], 'type': 'str', 'required': True}",
    "name": "{'description': ['The name of the SAN Connectivity Policy.', 'This name can be between 1 and 16 alphanumeric characters.', 'You cannot use spaces or any special characters other than - (hyphen), "_" (underscore), : (colon), and . (period).', 'You cannot change this name after the policy is created.'], 'required': True}",
    "org_dn": "{'description': ['Org dn (distinguished name)'], 'default': 'org-root'}",
    "password": "{'description': ['Password for Cisco UCS Manager authentication.'], 'type': 'str', 'required': True}",
    "port": "{'description': ['Port number to be used during connection (by default uses 443 for https and 80 for http connection).'], 'type': 'int'}",
    "proxy": "{'description': ["If use_proxy is no, specfies proxy to be used for connection. e.g. 'http://proxy.xy.z:8080'"], 'type': 'str'}",
    "state": "{'description': ['If C(present), will verify SAN Connectivity Policies are present and will create if needed.', 'If C(absent), will verify SAN Connectivity Policies are absent and will delete if needed.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "use_proxy": "{'description': ['If C(no), will not use the proxy as defined by system environment variable.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['Username for Cisco UCS Manager authentication.'], 'type': 'str', 'default': 'admin'}",
    "vhba_list": "{'description': ['List of vHBAs used by the SAN Connectivity Policy.', 'vHBAs used by the SAN Connectivity Policy must be created from a vHBA template.', 'Each list element has the following suboptions:', '= name', '  The name of the virtual HBA (required).', '= vhba_template', '  The name of the virtual HBA template (required).', '- adapter_policy', '  The name of the Fibre Channel adapter policy.', '  A user defined policy can be used, or one of the system defined policies (default, Linux, Solaris, VMware, Windows, WindowsBoot)', '  [Default: default]', '- order', "  String specifying the vHBA assignment order (e.g., '1', '2').", '  [Default: unspecified]']}",
    "wwnn_pool": "{'description': ['Name of the WWNN pool to use for WWNN assignment.'], 'default': 'default'}",
}
```

## Examples


``` yaml

- name: Configure SAN Connectivity Policy
  ucs_san_connectivity:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: Cntr-FC-Boot
    wwnn_pool: WWNN-Pool
    vhba_list:
    - name: Fabric-A
      vhba_template: vHBA-Template-A
      adapter_policy: Linux
    - name: Fabric-B
      vhba_template: vHBA-Template-B
      adapter_policy: Linux

- name: Remove SAN Connectivity Policy
  ucs_san_connectivity:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: Cntr-FC-Boot
    state: absent

```

## License

TODO

## Author Information
  - ['David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
  - ['David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
