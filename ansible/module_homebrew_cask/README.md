# Ansible module: ansible.module_homebrew_cask


Install/uninstall homebrew casks

## Description

Manages Homebrew casks.

## Requirements

TODO

## Arguments

``` json
{
    "accept_external_apps": "{'description': ['allow external apps'], 'type': 'bool', 'default': False, 'version_added': '2.5.0'}",
    "greedy": "{'description': ['upgrade casks that auto update; passes --greedy to brew cask outdated when checking if an installed cask has a newer version available'], 'type': 'bool', 'default': False, 'version_added': '2.7.0'}",
    "install_options": "{'description': ['options flags to install a package'], 'aliases': ['options'], 'version_added': '2.2'}",
    "name": "{'description': ['name of cask to install/remove'], 'required': True, 'aliases': ['pkg', 'package', 'cask']}",
    "path": "{'description': ["':' separated list of paths to search for 'brew' executable."], 'default': '/usr/local/bin'}",
    "state": "{'description': ['state of the cask'], 'choices': ['present', 'absent', 'upgraded'], 'default': 'present'}",
    "update_homebrew": "{'description': ['update homebrew itself first. Note that C(brew cask update) is a synonym for C(brew update).'], 'type': 'bool', 'default': False, 'aliases': ['update-brew'], 'version_added': '2.2'}",
    "upgrade": "{'description': ['upgrade all casks (mutually exclusive with `upgrade_all`)'], 'type': 'bool', 'default': False, 'version_added': '2.5.0'}",
    "upgrade_all": "{'description': ['upgrade all casks (mutually exclusive with `upgrade`)'], 'type': 'bool', 'default': False, 'version_added': '2.5.0'}",
}
```

## Examples


``` yaml

- homebrew_cask:
    name: alfred
    state: present

- homebrew_cask:
    name: alfred
    state: absent

- homebrew_cask:
    name: alfred
    state: present
    install_options: 'appdir=/Applications'

- homebrew_cask:
    name: alfred
    state: present
    install_options: 'debug,appdir=/Applications'

- homebrew_cask:
    name: alfred
    state: present
    allow_external_apps: True

- homebrew_cask:
    name: alfred
    state: absent
    install_options: force

- homebrew_cask:
    upgrade_all: true

- homebrew_cask:
    name: alfred
    state: upgraded
    install_options: force

- homebrew_cask:
    name: 1password
    state: upgraded
    greedy: True


```

## License

TODO

## Author Information
  - ['Indrajit Raychaudhuri (@indrajitr)', 'Daniel Jaouen (@danieljaouen)', 'Enric Lluelles (@enriclluelles)']
  - ['Indrajit Raychaudhuri (@indrajitr)', 'Daniel Jaouen (@danieljaouen)', 'Enric Lluelles (@enriclluelles)']
  - ['Indrajit Raychaudhuri (@indrajitr)', 'Daniel Jaouen (@danieljaouen)', 'Enric Lluelles (@enriclluelles)']
