# Ansible module: ansible.module_profitbricks_volume_attachments


Attach or detach a volume

## Description

Allows you to attach or detach a volume from a ProfitBricks server. This module has a dependency on profitbricks >= 1.0.0

## Requirements

TODO

## Arguments

``` json
{
    "datacenter": "{'description': ['The datacenter in which to operate.'], 'required': True}",
    "server": "{'description': ['The name of the server you wish to detach or attach the volume.'], 'required': True}",
    "state": "{'description': ['Indicate desired state of the resource'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "subscription_password": "{'description': ['THe ProfitBricks password. Overrides the PB_PASSWORD environment variable.'], 'required': False}",
    "subscription_user": "{'description': ['The ProfitBricks username. Overrides the PB_SUBSCRIPTION_ID environment variable.'], 'required': False}",
    "volume": "{'description': ['The volume name or ID.'], 'required': True}",
    "wait": "{'description': ['wait for the operation to complete before returning'], 'required': False, 'default': True, 'type': 'bool'}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 600}",
}
```

## Examples


``` yaml


# Attach a Volume

- profitbricks_volume_attachments:
    datacenter: Tardis One
    server: node002
    volume: vol01
    wait_timeout: 500
    state: present

# Detach a Volume

- profitbricks_volume_attachments:
    datacenter: Tardis One
    server: node002
    volume: vol01
    wait_timeout: 500
    state: absent


```

## License

TODO

## Author Information
  - ['Matt Baldwin (baldwin@stackpointcloud.com)']
