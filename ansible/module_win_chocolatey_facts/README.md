# Ansible module: ansible.module_win_chocolatey_facts


Create a facts collection for Chocolatey

## Description

This module shows information from Chocolatey, such as installed packages, configuration, feature and sources.

## Requirements

TODO

## Arguments

}
```

## Examples


``` yaml

- name: Gather facts from chocolatey
  win_chocolatey_facts:

- name: Displays the Configuration
  debug:
    var: ansible_chocolatey.config

- name: Displays the Feature
  debug:
    var: ansible_chocolatey.feature

- name: Displays the Sources
  debug:
    var: ansible_chocolatey.sources

- name: Displays the Packages
  debug:
    var: ansible_chocolatey.packages

```

## License

TODO

## Author Information
  - ['Simon Bärlocher (@sbaerlocher)', 'ITIGO AG (@itigoag)']
  - ['Simon Bärlocher (@sbaerlocher)', 'ITIGO AG (@itigoag)']
