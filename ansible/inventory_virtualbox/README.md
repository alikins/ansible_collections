# Ansible inventory: ansible.inventory_virtualbox


virtualbox inventory source

## Description

Get inventory hosts from the local virtualbox installation.
Uses a <name>.vbox.yaml (or .vbox.yml) YAML configuration file.
The inventory_hostname is always the 'Name' of the virtualbox instance.

## Requirements

TODO

## Arguments

``` json
{
    "cache": "{'description': ["Toggle to enable/disable the caching of the inventory's source data, requires a cache plugin setup to work."], 'type': 'boolean', 'default': False, 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE'}], 'ini': [{'section': 'inventory', 'key': 'cache'}]}",
    "cache_connection": "{'description': ['Cache connection data or path, read cache plugin documentation for specifics.'], 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_CONNECTION'}], 'ini': [{'section': 'inventory', 'key': 'cache_connection'}]}",
    "cache_plugin": "{'description': ["Cache plugin to use for the inventory's source data."], 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_PLUGIN'}], 'ini': [{'section': 'inventory', 'key': 'cache_plugin'}]}",
    "cache_timeout": "{'description': ['Cache duration in seconds'], 'default': 3600, 'type': 'integer', 'env': [{'name': 'ANSIBLE_INVENTORY_CACHE_TIMEOUT'}], 'ini': [{'section': 'inventory', 'key': 'cache_timeout'}]}",
    "compose": "{'description': ['create vars from jinja2 expressions'], 'type': 'dictionary', 'default': {}}",
    "groups": "{'description': ['add hosts to group based on Jinja2 conditionals'], 'type': 'dictionary', 'default': {}}",
    "keyed_groups": "{'description': ['add hosts to group based on the values of a variable'], 'type': 'list', 'default': []}",
    "network_info_path": "{'description': ['property path to query for network information (ansible_host)'], 'default': '/VirtualBox/GuestInfo/Net/0/V4/IP'}",
    "plugin": "{'description': ["token that ensures this is a source file for the 'virtualbox' plugin"], 'required': True, 'choices': ['virtualbox']}",
    "query": "{'description': ['create vars from virtualbox properties'], 'type': 'dictionary', 'default': {}}",
    "running_only": "{'description': ['toggles showing all vms vs only those currently running'], 'type': 'boolean', 'default': False}",
    "settings_password_file": "{'description': ['provide a file containing the settings password (equivalent to --settingspwfile)']}",
    "strict": "{'description': ['If true make invalid entries a fatal error, otherwise skip and continue', 'Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.'], 'type': 'boolean', 'default': False}",
}
```

## Examples


``` yaml

# file must be named vbox.yaml or vbox.yml
simple_config_file:
    plugin: virtualbox
    settings_password_file: /etc/virtulbox/secrets
    query:
      logged_in_users: /VirtualBox/GuestInfo/OS/LoggedInUsersList
    compose:
      ansible_connection: ('indows' in vbox_Guest_OS)|ternary('winrm', 'ssh')

```

## License

TODO

## Author Information
  - ['UNKNOWN']
