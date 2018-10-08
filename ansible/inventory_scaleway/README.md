# Ansible inventory: ansible.inventory_scaleway


Scaleway inventory source

## Description

Get inventory hosts from Scaleway

## Requirements

TODO

## Arguments

``` json
{
    "hostnames": "{'description': ['List of preference about what to use as an hostname.'], 'type': 'list', 'default': ['public_ipv4'], 'choices': ['public_ipv4', 'private_ipv4', 'public_ipv6', 'hostname', 'id']}",
    "oauth_token": "{'required': True, 'description': ['Scaleway OAuth token.'], 'env': [{'name': 'SCW_TOKEN'}, {'name': 'SCW_API_KEY'}, {'name': 'SCW_OAUTH_TOKEN'}]}",
    "plugin": "{'description': ["token that ensures this is a source file for the 'scaleway' plugin."], 'required': True, 'choices': ['scaleway']}",
    "regions": "{'description': ['Filter results on a specific Scaleway region'], 'type': 'list', 'default': ['ams1', 'par1']}",
    "tags": "{'description': ['Filter results on a specific tag'], 'type': 'list'}",
    "variables": "{'description': ['set individual variables: keys are variable names and values are templates. Any value returned by the L(Scaleway API, https://developer.scaleway.com/#servers-server-get) can be used.'], 'type': 'dict'}",
}
```

## Examples


``` yaml

# scaleway_inventory.yml file in YAML format
# Example command line: ansible-inventory --list -i scaleway_inventory.yml

# use hostname as inventory_hostname
# use the private IP address to connect to the host
plugin: scaleway
regions:
  - ams1
  - par1
tags:
  - foobar
hostnames:
  - hostname
variables:
  ansible_host: private_ip
  state: state

# use hostname as inventory_hostname and public IP address to connect to the host
plugin: scaleway
hostnames:
  - hostname
regions:
  - par1
variables:
  ansible_host: public_ip.address

```

## License

TODO

## Author Information
  - ['Remy Leone (@sieben)']
