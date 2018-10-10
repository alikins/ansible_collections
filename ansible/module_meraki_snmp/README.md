# Ansible module: ansible.module_meraki_snmp


Manage organizations in the Meraki cloud

## Description

Allows for management of SNMP settings for Meraki.

## Requirements

TODO

## Arguments

``` json
{
    "auth_key": "{'description': ['Authentication key provided by the dashboard. Required if environmental variable MERAKI_KEY is not set.']}",
    "host": "{'description': ['Hostname for Meraki dashboard', 'Only useful for internal Meraki developers'], 'type': 'string', 'default': 'api.meraki.com'}",
    "org_id": "{'description': ['ID of organization.']}",
    "org_name": "{'description': ['Name of organization.'], 'aliases': ['organization']}",
    "output_level": "{'description': ['Set amount of debug output during module execution'], 'choices': ['normal', 'debug'], 'default': 'normal'}",
    "peer_ips": "{'description': ['Semi-colon delimited IP addresses which can perform SNMP queries.']}",
    "state": "{'description': ['Specifies whether SNMP information should be queried or modified.'], 'choices': ['query', 'present'], 'default': 'present'}",
    "timeout": "{'description': ['Time to timeout for HTTP requests.'], 'type': 'int', 'default': 30}",
    "use_https": "{'description': ['If C(no), it will use HTTP. Otherwise it will use HTTPS.', 'Only useful for internal Meraki developers'], 'type': 'bool', 'default': True}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool'}",
    "v2c_enabled": "{'description': ['Specifies whether SNMPv2c is enabled.'], 'type': 'bool'}",
    "v3_auth_mode": "{'description': ['Sets authentication mode for SNMPv3.'], 'choices': ['MD5', 'SHA']}",
    "v3_auth_pass": "{'description': ['Authentication password for SNMPv3.', 'Must be at least 8 characters long.']}",
    "v3_enabled": "{'description': ['Specifies whether SNMPv3 is enabled.'], 'type': 'bool'}",
    "v3_priv_mode": "{'description': ['Specifies privacy mode for SNMPv3.'], 'choices': ['DES', 'AES128']}",
    "v3_priv_pass": "{'description': ['Privacy password for SNMPv3.', 'Must be at least 8 characters long.']}",
    "validate_certs": "{'description': ['Whether to validate HTTP certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Query SNMP values
  meraki_snmp:
    auth_key: abc12345
    org_name: YourOrg
    state: query
  delegate_to: localhost

- name: Enable SNMPv2
  meraki_snmp:
    auth_key: abc12345
    org_name: YourOrg
    state: present
    v2c_enabled: yes
  delegate_to: localhost

- name: Disable SNMPv2
  meraki_snmp:
    auth_key: abc12345
    org_name: YourOrg
    state: present
    v2c_enabled: no
  delegate_to: localhost

- name: Enable SNMPv3
  meraki_snmp:
    auth_key: abc12345
    org_name: YourOrg
    state: present
    v3_enabled: true
    v3_auth_mode: SHA
    v3_auth_pass: ansiblepass
    v3_priv_mode: AES128
    v3_priv_pass: ansiblepass
    peer_ips: 192.0.1.1;192.0.1.2
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Kevin Breit (@kbreit)']
