# Ansible module: ansible.module_pear


Manage pear/pecl packages

## Description

Manage PHP packages with the pear package manager.

## Requirements

TODO

## Arguments

``` json
{
    "executable": "{'description': ['Path to the pear executable'], 'version_added': '2.4'}",
    "name": "{'description': ['Name of the package to install, upgrade, or remove.'], 'required': True}",
    "state": "{'description': ['Desired state of the package.'], 'default': 'present', 'choices': ['present', 'absent', 'latest']}",
}
```

## Examples


``` yaml

# Install pear package
- pear:
    name: Net_URL2
    state: present

# Install pecl package
- pear:
    name: pecl/json_post
    state: present

# Upgrade package
- pear:
    name: Net_URL2
    state: latest

# Remove packages
- pear:
    name: Net_URL2,pecl/json_post
    state: absent

```

## License

TODO

## Author Information
  - ["'jonathan.lestrelin' <jonathan.lestrelin@gmail.com>"]
