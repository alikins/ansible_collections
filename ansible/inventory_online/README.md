# Ansible inventory: ansible.inventory_online


Online inventory source

## Description

Get inventory hosts from Online

## Requirements

TODO

## Arguments

``` json
{
    "groups": "{'description': ['List of groups.'], 'type': 'list', 'choices': ['location', 'offer', 'rpn']}",
    "hostnames": "{'description': ['List of preference about what to use as an hostname.'], 'type': 'list', 'default': ['public_ipv4'], 'choices': ['public_ipv4', 'private_ipv4', 'hostname']}",
    "oauth_token": "{'required': True, 'description': ['Online OAuth token.'], 'env': [{'name': 'ONLINE_TOKEN'}, {'name': 'ONLINE_API_KEY'}, {'name': 'ONLINE_OAUTH_TOKEN'}]}",
    "plugin": "{'description': ["token that ensures this is a source file for the 'online' plugin."], 'required': True, 'choices': ['online']}",
}
```

## Examples


``` yaml

# online_inventory.yml file in YAML format
# Example command line: ansible-inventory --list -i online_inventory.yml

plugin: online
hostnames:
  - public_ipv4
groups:
  - location
  - offer
  - rpn

```

## License

TODO

## Author Information
  - ['Remy Leone (@sieben)']
