# Ansible module: ansible.module_profitbricks_datacenter


Create or destroy a ProfitBricks Virtual Datacenter

## Description

This is a simple module that supports creating or removing vDCs. A vDC is required before you can create servers. This module has a dependency on profitbricks >= 1.0.0

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['The description of the virtual datacenter.'], 'required': False}",
    "location": "{'description': ['The datacenter location.'], 'required': False, 'default': 'us/las', 'choices': ['us/las', 'de/fra', 'de/fkb']}",
    "name": "{'description': ['The name of the virtual datacenter.'], 'required': True}",
    "state": "{'description': ['create or terminate datacenters'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "subscription_password": "{'description': ['THe ProfitBricks password. Overrides the PB_PASSWORD environment variable.'], 'required': False}",
    "subscription_user": "{'description': ['The ProfitBricks username. Overrides the PB_SUBSCRIPTION_ID environment variable.'], 'required': False}",
    "wait": "{'description': ['wait for the datacenter to be created before returning'], 'required': False, 'default': True, 'type': 'bool'}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 600}",
}
```

## Examples


``` yaml


# Create a Datacenter
- profitbricks_datacenter:
    datacenter: Tardis One
    wait_timeout: 500

# Destroy a Datacenter. This will remove all servers, volumes, and other objects in the datacenter.
- profitbricks_datacenter:
    datacenter: Tardis One
    wait_timeout: 500
    state: absent


```

## License

TODO

## Author Information
  - ['Matt Baldwin (baldwin@stackpointcloud.com)']
