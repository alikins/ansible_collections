# Ansible inventory: ansible.inventory_vultr


Vultr inventory source

## Description

Get inventory hosts from Vultr public cloud.
Uses C(api_config), C(~/.vultr.ini), C(./vultr.ini) or VULTR_API_CONFIG path to config file.

## Requirements

TODO

## Arguments

``` json
{
    "api_account": "{'description': ['Specify the account to be used.'], 'default': 'default'}",
    "api_config": "{'description': ['Path to the vultr configuration file. If not specified will be taken from regular Vultr configuration.'], 'env': [{'name': 'VULTR_API_CONFIG'}]}",
    "api_key": "{'description': ['Vultr API key. If not specified will be taken from regular Vultr configuration.'], 'env': [{'name': 'VULTR_API_KEY'}]}",
    "hostname": "{'description': ['Field to match the hostname. Note v4_main_ip corresponds to the main_ip field returned from the API and name to label.'], 'type': 'string', 'default': 'v4_main_ip', 'choices': ['v4_main_ip', 'v6_main_ip', 'name']}",
    "plugin": "{'description': ["token that ensures this is a source file for the 'vultr' plugin."], 'required': True, 'choices': ['vultr']}",
}
```

## Examples


``` yaml

# vultr_inventory.yml file in YAML format
# Example command line: ansible-inventory --list -i vultr_inventory.yml

plugin: vultr

```

## License

TODO

## Author Information
  - ['Yanis Guenane (@Spredzy)']
