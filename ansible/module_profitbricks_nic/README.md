# Ansible module: ansible.module_profitbricks_nic


Create or Remove a NIC

## Description

This module allows you to create or restore a volume snapshot. This module has a dependency on profitbricks >= 1.0.0

## Requirements

TODO

## Arguments

``` json
{
    "datacenter": "{'description': ['The datacenter in which to operate.'], 'required': True}",
    "lan": "{'description': ["The LAN to place the NIC on. You can pass a LAN that doesn't exist and it will be created. Required on create."], 'required': True}",
    "name": "{'description': ['The name or ID of the NIC. This is only required on deletes, but not on create.'], 'required': True}",
    "server": "{'description': ['The server name or ID.'], 'required': True}",
    "state": "{'description': ['Indicate desired state of the resource'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "subscription_password": "{'description': ['THe ProfitBricks password. Overrides the PB_PASSWORD environment variable.'], 'required': False}",
    "subscription_user": "{'description': ['The ProfitBricks username. Overrides the PB_SUBSCRIPTION_ID environment variable.'], 'required': False}",
    "wait": "{'description': ['wait for the operation to complete before returning'], 'required': False, 'default': True, 'type': 'bool'}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 600}",
}
```

## Examples


``` yaml


# Create a NIC
- profitbricks_nic:
    datacenter: Tardis One
    server: node002
    lan: 2
    wait_timeout: 500
    state: present

# Remove a NIC
- profitbricks_nic:
    datacenter: Tardis One
    server: node002
    name: 7341c2454f
    wait_timeout: 500
    state: absent


```

## License

TODO

## Author Information
  - ['Matt Baldwin (baldwin@stackpointcloud.com)']
