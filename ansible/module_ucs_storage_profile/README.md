# Ansible module: ansible.module_ucs_storage_profile


Configures storage profiles on Cisco UCS Manager

## Description

Configures storage profiles on Cisco UCS Manager.
Examples can be used with the L(UCS Platform Emulator,https://communities.cisco.com/ucspe).

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['The user-defined description of the storage profile.', 'Enter up to 256 characters.', 'You can use any characters or spaces except the following:', '` (accent mark),  (backslash), ^ (carat), " (double quote), = (equal sign), > (greater than), < (less than), or \' (single quote).'], 'aliases': ['descr']}",
    "hostname": "{'description': ['IP address or hostname of Cisco UCS Manager.'], 'type': 'str', 'required': True}",
    "local_luns": "{'description': ['List of Local LUNs used by the storage profile.'], 'suboptions': {'name': {'description': ['The name of the local LUN.'], 'required': True}, 'size': {'description': ['Size of this LUN in GB.', 'The size can range from 1 to 10240 GB.'], 'default': '1'}, 'auto_deploy': {'description': ['Whether the local LUN should be automatically deployed or not.'], 'choices': ['auto-deploy', 'no-auto-deploy'], 'default': 'auto-deploy'}, 'expand_to_avail': {'description': ['Specifies that this LUN can be expanded to use the entire available disk group.', 'For each service profile, only one LUN can use this option.', 'Expand To Available option is not supported for already deployed LUN.'], 'type': 'bool', 'default': 'no'}, 'fractional_size': {'description': ['Fractional size of this LUN in MB.'], 'default': '0'}, 'disk_policy_name': {'description': ['The disk group configuration policy to be applied to this local LUN.']}, 'state': {'description': ['If C(present), will verify local LUN is present on profile. If C(absent), will verify local LUN is absent on profile.'], 'choices': ['absent', 'present'], 'default': 'present'}}}",
    "name": "{'description': ['The name of the storage profile.', 'This name can be between 1 and 16 alphanumeric characters.', 'You cannot use spaces or any special characters other than - (hyphen), "_" (underscore), : (colon), and . (period).', 'You cannot change this name after profile is created.'], 'required': True}",
    "org_dn": "{'description': ['The distinguished name (dn) of the organization where the resource is assigned.'], 'default': 'org-root'}",
    "password": "{'description': ['Password for Cisco UCS Manager authentication.'], 'type': 'str', 'required': True}",
    "port": "{'description': ['Port number to be used during connection (by default uses 443 for https and 80 for http connection).'], 'type': 'int'}",
    "proxy": "{'description': ["If use_proxy is no, specfies proxy to be used for connection. e.g. 'http://proxy.xy.z:8080'"], 'type': 'str'}",
    "state": "{'description': ['If C(present), will verify that the storage profile is present and will create if needed.', 'If C(absent), will verify that the storage profile is absent and will delete if needed.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "use_proxy": "{'description': ['If C(no), will not use the proxy as defined by system environment variable.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['Username for Cisco UCS Manager authentication.'], 'type': 'str', 'default': 'admin'}",
}
```

## Examples


``` yaml

- name: Configure Storage Profile
  ucs_storage_profile:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: DEE-StgProf
    local_luns:
    - name: Boot-LUN
      size: '60'
      disk_policy_name: DEE-DG
    - name: Data-LUN
      size: '200'
      disk_policy_name: DEE-DG

- name: Remove Storage Profile
  ucs_storage_profile:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: DEE-StgProf
    state: absent

- name: Remove Local LUN from Storage Profile
  ucs_storage_profile:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: DEE-StgProf
    local_luns:
    - name: Data-LUN
      state: absent

```

## License

TODO

## Author Information
  - ['Sindhu Sudhir (@sisudhir)', 'David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
  - ['Sindhu Sudhir (@sisudhir)', 'David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
  - ['Sindhu Sudhir (@sisudhir)', 'David Soper (@dsoper2)', 'CiscoUcs (@CiscoUcs)']
