# Ansible inventory: ansible.inventory_script


Executes an inventory script that returns JSON

## Description

The source provided must be an executable that returns Ansible inventory JSON
The source must accept C(--list) and C(--host <hostname>) as arguments. C(--host) will only be used if no C(_meta) key is present. This is a performance optimization as the script would be called per host otherwise.

## Requirements

TODO

## Arguments

``` json
{
    "always_show_stderr": "{'description': ['Toggle display of stderr even when script was successful'], 'version_added': '2.5.1', 'default': True, 'type': 'boolean', 'ini': [{'section': 'inventory_plugin_script', 'key': 'always_show_stderr'}], 'env': [{'name': 'ANSIBLE_INVENTORY_PLUGIN_SCRIPT_STDERR'}]}",
    "cache": "{'description': ['Toggle the usage of the configured Cache plugin.'], 'default': False, 'type': 'boolean', 'ini': [{'section': 'inventory_plugin_script', 'key': 'cache'}], 'env': [{'name': 'ANSIBLE_INVENTORY_PLUGIN_SCRIPT_CACHE'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['UNKNOWN']
