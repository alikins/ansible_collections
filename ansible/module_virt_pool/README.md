# Ansible module: ansible.module_virt_pool


Manage libvirt storage pools

## Description

Manage I(libvirt) storage pools.

## Requirements

TODO

## Arguments

``` json
{
    "autostart": "{'required': False, 'type': 'bool', 'description': ['Specify if a given storage pool should be started automatically on system boot.']}",
    "command": "{'required': False, 'choices': ['define', 'build', 'create', 'start', 'stop', 'destroy', 'delete', 'undefine', 'get_xml', 'list_pools', 'facts', 'info', 'status'], 'description': ['in addition to state management, various non-idempotent commands are available. See examples.']}",
    "mode": "{'required': False, 'choices': ['new', 'repair', 'resize', 'no_overwrite', 'overwrite', 'normal', 'zeroed'], 'description': ["Pass additional parameters to 'build' or 'delete' commands."]}",
    "name": "{'required': False, 'aliases': ['pool'], 'description': ['name of the storage pool being managed. Note that pool must be previously defined with xml.']}",
    "state": "{'required': False, 'choices': ['active', 'inactive', 'present', 'absent', 'undefined', 'deleted'], 'description': ["specify which state you want a storage pool to be in. If 'active', pool will be started. If 'present', ensure that pool is present but do not change its state; if it's missing, you need to specify xml argument. If 'inactive', pool will be stopped. If 'undefined' or 'absent', pool will be removed from I(libvirt) configuration. If 'deleted', pool contents will be deleted and then pool undefined."]}",
    "uri": "{'required': False, 'default': 'qemu:///system', 'description': ['I(libvirt) connection uri.']}",
    "xml": "{'required': False, 'description': ['XML document used with the define command.']}",
}
```

## Examples


``` yaml

# Define a new storage pool
- virt_pool:
    command: define
    name: vms
    xml: '{{ lookup("template", "pool/dir.xml.j2") }}'

# Build a storage pool if it does not exist
- virt_pool:
    command: build
    name: vms

# Start a storage pool
- virt_pool:
    command: create
    name: vms

# List available pools
- virt_pool:
    command: list_pools

# Get XML data of a specified pool
- virt_pool:
    command: get_xml
    name: vms

# Stop a storage pool
- virt_pool:
    command: destroy
    name: vms

# Delete a storage pool (destroys contents)
- virt_pool:
    command: delete
    name: vms

# Undefine a storage pool
- virt_pool:
    command: undefine
    name: vms

# Gather facts about storage pools
# Facts will be available as 'ansible_libvirt_pools'
- virt_pool:
    command: facts

# Gather information about pools managed by 'libvirt' remotely using uri
- virt_pool:
    command: info
    uri: '{{ item }}'
  with_items: '{{ libvirt_uris }}'
  register: storage_pools

# Ensure that a pool is active (needs to be defined and built first)
- virt_pool:
    state: active
    name: vms

# Ensure that a pool is inactive
- virt_pool:
    state: inactive
    name: vms

# Ensure that a given pool will be started at boot
- virt_pool:
    autostart: yes
    name: vms

# Disable autostart for a given pool
- virt_pool:
    autostart: no
    name: vms

```

## License

TODO

## Author Information
  - ['Maciej Delmanowski (@drybjed)']
