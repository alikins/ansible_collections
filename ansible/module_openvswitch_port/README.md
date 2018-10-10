# Ansible module: ansible.module_openvswitch_port


Manage Open vSwitch ports

## Description

Manage Open vSwitch ports

## Requirements

TODO

## Arguments

``` json
{
    "bridge": "{'required': True, 'description': ['Name of bridge to manage']}",
    "external_ids": "{'version_added': 2.0, 'default': {}, 'description': ['Dictionary of external_ids applied to a port.']}",
    "port": "{'required': True, 'description': ['Name of port to manage on the bridge']}",
    "set": "{'version_added': 2.0, 'description': ['Set a single property on a port.']}",
    "state": "{'default': 'present', 'choices': ['present', 'absent'], 'description': ['Whether the port should exist']}",
    "tag": "{'version_added': 2.2, 'description': ['VLAN tag for this port. Must be a value between 0 and 4095.']}",
    "timeout": "{'default': 5, 'description': ['How long to wait for ovs-vswitchd to respond']}",
}
```

## Examples


``` yaml

# Creates port eth2 on bridge br-ex
- openvswitch_port:
    bridge: br-ex
    port: eth2
    state: present

# Creates port eth6
- openvswitch_port:
    bridge: bridge-loop
    port: eth6
    state: present
    set: Interface eth6

# Creates port vlan10 with tag 10 on bridge br-ex
- openvswitch_port:
    bridge: br-ex
    port: vlan10
    tag: 10
    state: present
    set: Interface vlan10

# Assign interface id server1-vifeth6 and mac address 00:00:5E:00:53:23
# to port vifeth6 and setup port to be managed by a controller.
- openvswitch_port:
    bridge: br-int
    port: vifeth6
    state: present
  args:
    external_ids:
      iface-id: '{{ inventory_hostname }}-vifeth6'
      attached-mac: '00:00:5E:00:53:23'
      vm-id: '{{ inventory_hostname }}'
      iface-status: active

```

## License

TODO

## Author Information
  - ['David Stygstra (@stygstra)']
