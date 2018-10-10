# Ansible module: ansible.module_slackpkg


Package manager for Slackware >= 12.2

## Description

Manage binary packages for Slackware using 'slackpkg' which is available in versions after 12.2.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['name of package to install/remove'], 'required': True}",
    "state": "{'description': ['state of the package, you can use "installed" as an alias for C(present) and removed as one for C(absent).'], 'choices': ['present', 'absent', 'latest'], 'required': False, 'default': 'present'}",
    "update_cache": "{'description': ['update the package database first'], 'required': False, 'default': False, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Install package foo
- slackpkg:
    name: foo
    state: present

# Remove packages foo and bar
- slackpkg:
    name: foo,bar
    state: absent

# Make sure that it is the most updated package
- slackpkg:
    name: foo
    state: latest

```

## License

TODO

## Author Information
  - ['Kim Nørgaard (@KimNorgaard)']
