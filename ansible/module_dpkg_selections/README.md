# Ansible module: ansible.module_dpkg_selections


Dpkg package selection selections

## Description

Change dpkg package selection state via --get-selections and --set-selections.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Name of the package'], 'required': True}",
    "selection": "{'description': ['The selection state to set the package to.'], 'choices': ['install', 'hold', 'deinstall', 'purge'], 'required': True}",
}
```

## Examples


``` yaml

# Prevent python from being upgraded.
- dpkg_selections:
    name: python
    selection: hold

```

## License

TODO

## Author Information
  - ['Brian Brazil (@brian-brazil) <brian.brazil@boxever.com>']
