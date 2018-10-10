# Ansible module: ansible.module_homebrew


Package manager for Homebrew

## Description

Manages Homebrew packages

## Requirements

TODO

## Arguments

``` json
{
    "install_options": "{'description': ['options flags to install a package'], 'aliases': ['options'], 'version_added': '1.4'}",
    "name": "{'description': ['list of names of packages to install/remove'], 'aliases': ['pkg', 'package', 'formula']}",
    "path": "{'description': ["A ':' separated list of paths to search for 'brew' executable. Since a package (I(formula) in homebrew parlance) location is prefixed relative to the actual path of I(brew) command, providing an alternative I(brew) path enables managing different set of packages in an alternative location in the system."], 'default': '/usr/local/bin'}",
    "state": "{'description': ['state of the package'], 'choices': ['head', 'latest', 'present', 'absent', 'linked', 'unlinked'], 'default': 'present'}",
    "update_homebrew": "{'description': ['update homebrew itself first'], 'type': 'bool', 'default': False, 'aliases': ['update-brew']}",
    "upgrade_all": "{'description': ['upgrade all homebrew packages'], 'type': 'bool', 'default': False, 'aliases': ['upgrade']}",
}
```

## Examples


``` yaml

# Install formula foo with 'brew' in default path (C(/usr/local/bin))
- homebrew:
    name: foo
    state: present

# Install formula foo with 'brew' in alternate path C(/my/other/location/bin)
- homebrew:
    name: foo
    path: /my/other/location/bin
    state: present

# Update homebrew first and install formula foo with 'brew' in default path
- homebrew:
    name: foo
    state: present
    update_homebrew: yes

# Update homebrew first and upgrade formula foo to latest available with 'brew' in default path
- homebrew:
    name: foo
    state: latest
    update_homebrew: yes

# Update homebrew and upgrade all packages
- homebrew:
    update_homebrew: yes
    upgrade_all: yes

# Miscellaneous other examples
- homebrew:
    name: foo
    state: head

- homebrew:
    name: foo
    state: linked

- homebrew:
    name: foo
    state: absent

- homebrew:
    name: foo,bar
    state: absent

- homebrew:
    name: foo
    state: present
    install_options: with-baz,enable-debug

```

## License

TODO

## Author Information
  - ['Indrajit Raychaudhuri (@indrajitr)', 'Daniel Jaouen (@danieljaouen)', 'Andrew Dunham (@andrew-d)']
  - ['Indrajit Raychaudhuri (@indrajitr)', 'Daniel Jaouen (@danieljaouen)', 'Andrew Dunham (@andrew-d)']
  - ['Indrajit Raychaudhuri (@indrajitr)', 'Daniel Jaouen (@danieljaouen)', 'Andrew Dunham (@andrew-d)']
