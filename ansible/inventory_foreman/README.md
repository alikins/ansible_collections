# Ansible inventory: ansible.inventory_foreman


foreman inventory source

## Description

Get inventory hosts from the foreman service.
Uses a configuration file as an inventory source, it must end in foreman.yml or foreman.yaml and has a ``plugin: foreman`` entry.

## Requirements

TODO

## Arguments

``` json
{
    "cache": "{'description': ["Toggle to enable/disable the caching of the inventory's source data, requires a cache plugin setup to work."], 'type': 'boolean', 'default': False, 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE'}], 'ini': [{'section': 'inventory', 'key': 'cache'}]}",
    "cache_connection": "{'description': ['Cache connection data or path, read cache plugin documentation for specifics.'], 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_CONNECTION'}], 'ini': [{'section': 'inventory', 'key': 'cache_connection'}]}",
    "cache_plugin": "{'description': ["Cache plugin to use for the inventory's source data."], 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_PLUGIN'}], 'ini': [{'section': 'inventory', 'key': 'cache_plugin'}]}",
    "cache_timeout": "{'description': ['Cache duration in seconds'], 'default': 3600, 'type': 'integer', 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_TIMEOUT'}], 'ini': [{'section': 'inventory', 'key': 'cache_timeout'}]}",
    "group_prefix": "{'description': ['prefix to apply to foreman groups'], 'default': 'foreman_'}",
    "password": "{'description': ['forman authentication password'], 'required': True}",
    "plugin": "{'description': ["the name of this plugin, it should alwys be set to 'foreman' for this plugin to recognize it as it's own."], 'required': True, 'choices': ['foreman']}",
    "url": "{'description': ['url to foreman'], 'default': 'http://localhost:300'}",
    "user": "{'description': ['foreman authentication user'], 'required': True}",
    "validate_certs": "{'description': ['verify SSL certificate if using https'], 'type': 'boolean', 'default': False}",
    "vars_prefix": "{'description': ['prefix to apply to host variables, does not include facts nor params'], 'default': 'foreman_'}",
    "want_facts": "{'description': ['Toggle, if True the plugin will retrieve host facts from the server'], 'type': 'boolean', 'default': False}",
    "want_params": "{'description': ["Toggle, if true the inventory will retrieve 'all_parameters' information as host vars"], 'type': 'boolean', 'default': False}",
}
```

## Examples


``` yaml

# my.foreman.yml
plugin: foreman
url: http://localhost:2222
user: ansible-tester
password: secure
validate_certs: False

```

## License

TODO

## Author Information
  - ['UNKNOWN']
