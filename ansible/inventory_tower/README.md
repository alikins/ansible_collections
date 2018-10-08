# Ansible inventory: ansible.inventory_tower


Ansible dynamic inventory plugin for Ansible Tower

## Description

Reads inventories from Ansible Tower.
Supports reading configuration from both YAML config file and environment variables.
If reading from the YAML file, the file name must end with tower_inventory.(yml|yaml), the path in the command would be /path/to/tower_inventory.(yml|yaml). If some arguments in the config file are missing, this plugin will try to fill in missing arguments by reading from environment variables.
If reading configurations from environment variables, the path in the command must be @tower_inventory.

## Requirements

TODO

## Arguments

``` json
{
    "host": "{'description': ['The network address of your Ansible Tower host.'], 'type': 'string', 'env': [{'name': 'TOWER_HOST'}], 'required': True}",
    "inventory_id": "{'description': ['The ID of the Ansible Tower inventory that you wish to import.'], 'type': 'string', 'env': [{'name': 'TOWER_INVENTORY'}], 'required': True}",
    "password": "{'description': ['The password for your Ansible Tower user.'], 'type': 'string', 'env': [{'name': 'TOWER_PASSWORD'}], 'required': True}",
    "plugin": "{'description': ["the name of this plugin, it should always be set to 'tower' for this plugin to recognize it as it's own."], 'env': [{'name': 'ANSIBLE_INVENTORY_ENABLED'}], 'required': True, 'choices': ['tower']}",
    "username": "{'description': ['The user that you plan to use to access inventories on Ansible Tower.'], 'type': 'string', 'env': [{'name': 'TOWER_USERNAME'}], 'required': True}",
    "verify_ssl": "{'description': ['Specify whether Ansible should verify the SSL certificate of Ansible Tower host.'], 'type': 'bool', 'default': True, 'env': [{'name': 'TOWER_VERIFY_SSL'}], 'required': False}",
}
```

## Examples


``` yaml

# Before you execute the following commands, you should make sure this file is in your plugin path,
# and you enabled this plugin.

# Example for using tower_inventory.yml file

plugin: tower
host: your_ansible_tower_server_network_address
username: your_ansible_tower_username
password: your_ansible_tower_password
inventory_id: the_ID_of_targeted_ansible_tower_inventory
# Then you can run the following command.
# If some of the arguments are missing, Ansible will attempt to read them from environment variables.
# ansible-inventory -i /path/to/tower_inventory.yml --list

# Example for reading from environment variables:

# Set environment variables:
# export TOWER_HOST=YOUR_TOWER_HOST_ADDRESS
# export TOWER_USERNAME=YOUR_TOWER_USERNAME
# export TOWER_PASSWORD=YOUR_TOWER_PASSWORD
# export TOWER_INVENTORY=THE_ID_OF_TARGETED_INVENTORY
# Read the inventory specified in TOWER_INVENTORY from Ansible Tower, and list them.
# The inventory path must always be @tower_inventory if you are reading all settings from environment variables.
# ansible-inventory -i @tower_inventory --list

```

## License

TODO

## Author Information
  - ['Matthew Jones (@matburt)', 'Yunfan Zhang (@YunfanZhang42)']
  - ['Matthew Jones (@matburt)', 'Yunfan Zhang (@YunfanZhang42)']
