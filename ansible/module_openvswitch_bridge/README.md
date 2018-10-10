# Ansible module: ansible.module_openvswitch_bridge


Manage Open vSwitch bridges

## Description

Manage Open vSwitch bridges

## Requirements

TODO

## Arguments

``` json
{
    "bridge": "{'required': True, 'description': ['Name of bridge or fake bridge to manage']}",
    "external_ids": "{'version_added': 2.0, 'description': ['A dictionary of external-ids. Omitting this parameter is a No-op. To  clear all external-ids pass an empty value.']}",
    "fail_mode": "{'version_added': 2.0, 'choices': ['secure', 'standalone'], 'description': ['Set bridge fail-mode. The default value (None) is a No-op.']}",
    "parent": "{'version_added': '2.3', 'description': ['Bridge parent of the fake bridge to manage']}",
    "set": "{'version_added': 2.3, 'description': ['Run set command after bridge configuration. This parameter is non-idempotent, play will always return I(changed) state if present']}",
    "state": "{'default': 'present', 'choices': ['present', 'absent'], 'description': ['Whether the bridge should exist']}",
    "timeout": "{'default': 5, 'description': ['How long to wait for ovs-vswitchd to respond']}",
    "vlan": "{'version_added': '2.3', 'description': ['The VLAN id of the fake bridge to manage (must be between 0 and 4095). This parameter is required if I(parent) parameter is set.']}",
}
```

## Examples


``` yaml

# Create a bridge named br-int
- openvswitch_bridge:
    bridge: br-int
    state: present

# Create a fake bridge named br-int within br-parent on the VLAN 405
- openvswitch_bridge:
    bridge: br-int
    parent: br-parent
    vlan: 405
    state: present

# Create an integration bridge
- openvswitch_bridge:
    bridge: br-int
    state: present
    fail_mode: secure
  args:
    external_ids:
      bridge-id: br-int

```

## License

TODO

## Author Information
  - ['David Stygstra (@stygstra)']
