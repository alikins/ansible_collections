# Ansible module: ansible.module_xbps


Manage packages with XBPS

## Description

Manage packages with the XBPS package manager.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Name of the package to install, upgrade, or remove.']}",
    "recurse": "{'description': ['When removing a package, also remove its dependencies, provided that they are not required by other packages and were not explicitly installed by a user.'], 'type': 'bool', 'default': False}",
    "state": "{'description': ['Desired state of the package.'], 'default': 'present', 'choices': ['present', 'absent', 'latest']}",
    "update_cache": "{'description': ['Whether or not to refresh the master package lists. This can be run as part of a package installation or as a separate step.'], 'type': 'bool', 'default': True}",
    "upgrade": "{'description': ['Whether or not to upgrade whole system'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

# Install package foo
- xbps: name=foo state=present
# Upgrade package foo
- xbps: name=foo state=latest update_cache=yes
# Remove packages foo and bar
- xbps: name=foo,bar state=absent
# Recursively remove package foo
- xbps: name=foo state=absent recurse=yes
# Update package cache
- xbps: update_cache=yes
# Upgrade packages
- xbps: upgrade=yes

```

## License

TODO

## Author Information
  - ['Dino Occhialini (@dinoocch)', 'Michael Aldridge (@the-maldridge)']
  - ['Dino Occhialini (@dinoocch)', 'Michael Aldridge (@the-maldridge)']
