# Ansible vars: ansible.vars_host_group_vars


In charge of loading group_vars and host_vars

## Description

Loads YAML vars into corresponding groups/hosts in group_vars/ and host_vars/ directories.
Files are restricted by extension to one of .yaml, .json, .yml or no extension.
Hidden (starting with '.') and backup (ending with '~') files and directories are ignored.
Only applies to inventory sources that are existing paths.

## Requirements

TODO

## Arguments

``` json
{
    "_valid_extensions": "{'default': ['.yml', '.yaml', '.json'], 'description': ["Check all of these extensions when looking for 'variable' files which should be YAML or JSON or vaulted versions of these.", 'This affects vars_files, include_vars, inventory and vars plugins among others.'], 'env': [{'name': 'ANSIBLE_YAML_FILENAME_EXT'}], 'ini': [{'section': 'yaml_valid_extensions', 'key': 'defaults'}], 'type': 'list'}",
}
```

## Examples



## License

TODO

## Author Information
  - ['UNKNOWN']
