# Ansible inventory: ansible.inventory_yaml


Uses a specific YAML file as an inventory source

## Description

YAML based inventory, starts with the 'all' group and has hosts/vars/children entries.
Host entries can have sub-entries defined, which will be treated as variables.
Vars entries are normal group vars.
Children are 'child groups', which can also have their own vars/hosts/children and so on.
File MUST have a valid extension, defined in configuration

## Requirements

TODO

## Arguments

``` json
{
    "yaml_extensions": "{'description': ["list of 'valid' extensions for files containing YAML"], 'type': 'list', 'default': ['.yaml', '.yml', '.json'], 'env': [{'name': 'ANSIBLE_YAML_FILENAME_EXT'}, {'name': 'ANSIBLE_INVENTORY_PLUGIN_EXTS'}], 'ini': [{'key': 'yaml_valid_extensions', 'section': 'defaults'}, {'section': 'inventory_plugin_yaml', 'key': 'yaml_valid_extensions'}]}",
}
```

## Examples


``` yaml

all: # keys must be unique, i.e. only one 'hosts' per group
    hosts:
        test1:
        test2:
            var1: value1
    vars:
        group_var1: value2
    children:   # key order does not matter, indentation does
        other_group:
            children:
                group_x:
                    hosts:
                        test5
            vars:
                g2_var2: value3
            hosts:
                test4:
                    ansible_host: 127.0.0.1
        last_group:
            hosts:
                test1 # same host as above, additional group membership
            vars:
                last_var: MYVALUE

```

## License

TODO

## Author Information
  - ['UNKNOWN']
