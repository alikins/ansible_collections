# Ansible module: ansible.module_meraki_switchport


Manage switchports on a switch in the Meraki cloud

## Description

Allows for management of switchports settings for Meraki MS switches.

## Requirements

TODO

## Arguments

``` json
{
    "access_policy_number": "{'description': ['Number of the access policy to apply.', 'Only applicable to access port types.']}",
    "allowed_vlans": "{'description': ['List of VLAN numbers to be allowed on switchport.'], 'default': 'all'}",
    "auth_key": "{'description': ['Authentication key provided by the dashboard. Required if environmental variable MERAKI_KEY is not set.']}",
    "enabled": "{'description': ['Whether a switchport should be enabled or disabled.'], 'type': 'bool', 'default': True}",
    "host": "{'description': ['Hostname for Meraki dashboard', 'Only useful for internal Meraki developers'], 'type': 'string', 'default': 'api.meraki.com'}",
    "isolation_enabled": "{'description': ['Isolation status of switchport.'], 'default': False, 'type': 'bool'}",
    "link_negotiation": "{'description': ['Link speed for the switchport.'], 'default': 'Auto negotiate', 'choices': ['Auto negotiate', '100Megabit (auto)', '100 Megabit full duplex (forced)']}",
    "name": "{'description': ['Switchport description.'], 'aliases': ['description']}",
    "number": "{'description': ['Port number.']}",
    "org_id": "{'description': ['ID of organization.']}",
    "org_name": "{'description': ['Name of organization.'], 'aliases': ['organization']}",
    "output_level": "{'description': ['Set amount of debug output during module execution'], 'choices': ['normal', 'debug'], 'default': 'normal'}",
    "poe_enabled": "{'description': ['Enable or disable Power Over Ethernet on a port.'], 'type': 'bool', 'default': True}",
    "rstp_enabled": "{'description': ['Enable or disable Rapid Spanning Tree Protocol on a port.'], 'type': 'bool', 'default': True}",
    "serial": "{'description': ['Serial nubmer of the switch.']}",
    "state": "{'description': ['Specifies whether a switchport should be queried or modified.'], 'choices': ['query', 'present'], 'default': 'query'}",
    "stp_guard": "{'description': ['Set state of STP guard.'], 'choices': ['disabled', 'root guard', 'bpdu guard', 'loop guard'], 'default': 'disabled'}",
    "tags": "{'description': ['Space delimited list of tags to assign to a port.']}",
    "timeout": "{'description': ['Time to timeout for HTTP requests.'], 'type': 'int', 'default': 30}",
    "type": "{'description': ['Set port type.'], 'choices': ['access', 'trunk'], 'default': 'access'}",
    "use_https": "{'description': ['If C(no), it will use HTTP. Otherwise it will use HTTPS.', 'Only useful for internal Meraki developers'], 'type': 'bool', 'default': True}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool'}",
    "validate_certs": "{'description': ['Whether to validate HTTP certificates.'], 'type': 'bool', 'default': True}",
    "vlan": "{'description': ['VLAN number assigned to port.', 'If a port is of type trunk, the specified VLAN is the native VLAN.']}",
    "voice_vlan": "{'description': ['VLAN number assigned to a port for voice traffic.', 'Only applicable to access port type.']}",
}
```

## Examples


``` yaml

- name: Query information about all switchports on a switch
  meraki_switchport:
    auth_key: abc12345
    state: query
    serial: ABC-123
  delegate_to: localhost

- name: Query information about all switchports on a switch
  meraki_switchport:
    auth_key: abc12345
    state: query
    serial: ABC-123
    number: 2
  delegate_to: localhost

- name: Name switchport
  meraki_switchport:
    auth_key: abc12345
    state: present
    serial: ABC-123
    number: 7
    name: Test Port
  delegate_to: localhost

- name: Configure access port with voice VLAN
  meraki_switchport:
    auth_key: abc12345
    state: present
    serial: ABC-123
    number: 7
    enabled: true
    name: Test Port
    tags: desktop
    type: access
    vlan: 10
    voice_vlan: 11
  delegate_to: localhost

- name: Check access port for idempotenty
  meraki_switchport:
    auth_key: abc12345
    state: present
    serial: ABC-123
    number: 7
    enabled: true
    name: Test Port
    tags: desktop
    type: access
    vlan: 10
    voice_vlan: 11
  delegate_to: localhost

- name: Configure trunk port with specific VLANs
  meraki_switchport:
    auth_key: abc12345
    state: present
    serial: ABC-123
    number: 7
    enabled: true
    name: Server port
    tags: server
    type: trunk
    allowed_vlans:
      - 10
      - 15
      - 20
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Kevin Breit (@kbreit)']
