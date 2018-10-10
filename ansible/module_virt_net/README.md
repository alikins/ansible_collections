# Ansible module: ansible.module_virt_net


Manage libvirt network configuration

## Description

Manage I(libvirt) networks.

## Requirements

TODO

## Arguments

``` json
{
    "autostart": "{'required': False, 'type': 'bool', 'description': ['Specify if a given network should be started automatically on system boot.']}",
    "command": "{'required': False, 'choices': ['define', 'create', 'start', 'stop', 'destroy', 'undefine', 'get_xml', 'list_nets', 'facts', 'info', 'status', 'modify'], 'description': ['in addition to state management, various non-idempotent commands are available. See examples. Modify was added in version 2.1']}",
    "name": "{'required': True, 'aliases': ['network'], 'description': ['name of the network being managed. Note that network must be previously defined with xml.']}",
    "state": "{'required': False, 'choices': ['active', 'inactive', 'present', 'absent'], 'description': ["specify which state you want a network to be in. If 'active', network will be started. If 'present', ensure that network is present but do not change its state; if it's missing, you need to specify xml argument. If 'inactive', network will be stopped. If 'undefined' or 'absent', network will be removed from I(libvirt) configuration."]}",
    "uri": "{'required': False, 'default': 'qemu:///system', 'description': ['libvirt connection uri.']}",
    "xml": "{'required': False, 'description': ['XML document used with the define command.']}",
}
```

## Examples


``` yaml

# Define a new network
- virt_net:
    command: define
    name: br_nat
    xml: '{{ lookup("template", "network/bridge.xml.j2") }}'

# Start a network
- virt_net:
    command: create
    name: br_nat

# List available networks
- virt_net:
    command: list_nets

# Get XML data of a specified network
- virt_net:
    command: get_xml
    name: br_nat

# Stop a network
- virt_net:
    command: destroy
    name: br_nat

# Undefine a network
- virt_net:
    command: undefine
    name: br_nat

# Gather facts about networks
# Facts will be available as 'ansible_libvirt_networks'
- virt_net:
    command: facts

# Gather information about network managed by 'libvirt' remotely using uri
- virt_net:
    command: info
    uri: '{{ item }}'
  with_items: '{{ libvirt_uris }}'
  register: networks

# Ensure that a network is active (needs to be defined and built first)
- virt_net:
    state: active
    name: br_nat

# Ensure that a network is inactive
- virt_net:
    state: inactive
    name: br_nat

# Ensure that a given network will be started at boot
- virt_net:
    autostart: yes
    name: br_nat

# Disable autostart for a given network
- virt_net:
    autostart: no
    name: br_nat

# Add a new host in the dhcp pool
- virt_net:
    name: br_nat
    xml: "<host mac='FC:C2:33:00:6c:3c' name='my_vm' ip='192.168.122.30'/>"

```

## License

TODO

## Author Information
  - ['Maciej Delmanowski (@drybjed)']
