# Ansible inventory: ansible.inventory_nmap


Uses nmap to find hosts to target

## Description

Uses a YAML configuration file with a valid YAML extension.

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['Network IP or range of IPs to scan, you can use a simple range (10.2.2.15-25) or CIDR notation.'], 'required': True}",
    "cache": "{'description': ["Toggle to enable/disable the caching of the inventory's source data, requires a cache plugin setup to work."], 'type': 'boolean', 'default': False, 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE'}], 'ini': [{'section': 'inventory', 'key': 'cache'}]}",
    "cache_connection": "{'description': ['Cache connection data or path, read cache plugin documentation for specifics.'], 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_CONNECTION'}], 'ini': [{'section': 'inventory', 'key': 'cache_connection'}]}",
    "cache_plugin": "{'description': ["Cache plugin to use for the inventory's source data."], 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_PLUGIN'}], 'ini': [{'section': 'inventory', 'key': 'cache_plugin'}]}",
    "cache_timeout": "{'description': ['Cache duration in seconds'], 'default': 3600, 'type': 'integer', 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_TIMEOUT'}], 'ini': [{'section': 'inventory', 'key': 'cache_timeout'}]}",
    "compose": "{'description': ['create vars from jinja2 expressions'], 'type': 'dictionary', 'default': {}}",
    "exclude": "{'description': ['list of addresses to exclude'], 'type': 'list'}",
    "groups": "{'description': ['add hosts to group based on Jinja2 conditionals'], 'type': 'dictionary', 'default': {}}",
    "ipv4": "{'description': ['use IPv4 type addresses'], 'type': 'boolean', 'default': True}",
    "ipv6": "{'description': ['use IPv6 type addresses'], 'type': 'boolean', 'default': True}",
    "keyed_groups": "{'description': ['add hosts to group based on the values of a variable'], 'type': 'list', 'default': []}",
    "plugin": "{'description': ["token that ensures this is a source file for the 'nmap' plugin."], 'required': True, 'choices': ['nmap']}",
    "ports": "{'description': ['Enable/disable scanning for open ports'], 'type': 'boolean', 'default': True}",
    "strict": "{'description': ['If true make invalid entries a fatal error, otherwise skip and continue', 'Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.'], 'type': 'boolean', 'default': False}",
}
```

## Examples


``` yaml

    # inventory.config file in YAML format
    plugin: nmap
    strict: False
    address: 192.168.0.0/24

```

## License

TODO

## Author Information
  - ['UNKNOWN']
