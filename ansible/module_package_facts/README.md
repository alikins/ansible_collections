# Ansible module: ansible.module_package_facts


package information as facts

## Description

Return information about installed packages as facts

## Requirements

TODO

## Arguments

``` json
{
    "manager": "{'description': ['The package manager used by the system so we can query the package information'], 'default': 'auto', 'choices': ['auto', 'rpm', 'apt'], 'required': False}",
}
```

## Examples


``` yaml

- name: get the rpm package facts
  package_facts:
    manager: "auto"

- name: show them
  debug: var=ansible_facts.packages


```

## License

TODO

## Author Information
  - ['Matthew Jones', 'Brian Coca', 'Adam Miller']
  - ['Matthew Jones', 'Brian Coca', 'Adam Miller']
  - ['Matthew Jones', 'Brian Coca', 'Adam Miller']
