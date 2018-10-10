# Ansible module: ansible.module_apk


Manages apk packages

## Description

Manages I(apk) packages for Alpine Linux.

## Requirements

TODO

## Arguments

``` json
{
    "available": "{'description': ['During upgrade, reset versioned world dependencies and change logic to prefer replacing or downgrading packages (instead of holding them) if the currently installed package is no longer available from any repository.'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "name": "{'description': ['A package name, like C(foo), or multiple packages, like C(foo, bar).']}",
    "repository": "{'description': ['A package repository or multiple repositories. Unlike with the underlying apk command, this list will override the system repositories rather than supplement them.'], 'version_added': '2.4'}",
    "state": "{'description': ['Indicates the desired package(s) state.', 'C(present) ensures the package(s) is/are present.', 'C(absent) ensures the package(s) is/are absent.', 'C(latest) ensures the package(s) is/are present and the latest version(s).'], 'default': 'present', 'choices': ['present', 'absent', 'latest']}",
    "update_cache": "{'description': ["Update repository indexes. Can be run with other steps or on it's own."], 'type': 'bool', 'default': False}",
    "upgrade": "{'description': ['Upgrade all installed packages to their latest version.'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

# Update repositories and install "foo" package
- apk:
    name: foo
    update_cache: yes

# Update repositories and install "foo" and "bar" packages
- apk:
    name: foo,bar
    update_cache: yes

# Remove "foo" package
- apk:
    name: foo
    state: absent

# Remove "foo" and "bar" packages
- apk:
    name: foo,bar
    state: absent

# Install the package "foo"
- apk:
    name: foo
    state: present

# Install the packages "foo" and "bar"
- apk:
    name: foo,bar
    state: present

# Update repositories and update package "foo" to latest version
- apk:
    name: foo
    state: latest
    update_cache: yes

# Update repositories and update packages "foo" and "bar" to latest versions
- apk:
    name: foo,bar
    state: latest
    update_cache: yes

# Update all installed packages to the latest versions
- apk:
    upgrade: yes

# Upgrade / replace / downgrade / uninstall all installed packages to the latest versions available
- apk:
    available: yes
    upgrade: yes

# Update repositories as a separate step
- apk:
    update_cache: yes

# Install package from a specific repository
- apk:
    name: foo
    state: latest
    update_cache: yes
    repository: http://dl-3.alpinelinux.org/alpine/edge/main

```

## License

TODO

## Author Information
  - ['Kevin Brebanov (@kbrebanov)']
