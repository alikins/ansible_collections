# Ansible module: ansible.module_win_pagefile


Query or change pagefile configuration

## Description

Query current pagefile configuration.
Enable/Disable AutomaticManagedPagefile.
Create new or override pagefile configuration.

## Requirements

TODO

## Arguments

``` json
{
    "automatic": "{'description': ['Configures AutomaticManagedPagefile for the entire system.'], 'type': 'bool'}",
    "drive": "{'description': ['The drive of the pagefile.']}",
    "initial_size": "{'description': ['The initial size of the pagefile in megabytes.'], 'type': 'int'}",
    "maximum_size": "{'description': ['The maximum size of the pagefile in megabytes.'], 'type': 'int'}",
    "override": "{'description': ['Override the current pagefile on the drive.'], 'type': 'bool', 'default': True}",
    "remove_all": "{'description': ['Remove all pagefiles in the system, not including automatic managed.'], 'type': 'bool', 'default': False}",
    "state": "{'description': ['State of the pagefile.'], 'choices': ['absent', 'present', 'query'], 'default': 'query'}",
    "system_managed": "{'description': ['Configures current pagefile to be managed by the system.'], 'type': 'bool', 'default': False}",
    "test_path": "{'description': ['Use Test-Path on the drive to make sure the drive is accessible before creating the pagefile.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Query pagefiles configuration
  win_pagefile:

- name: Query C pagefile
  win_pagefile:
    drive: C

- name: Set C pagefile, don't override if exists
  win_pagefile:
    drive: C
    initial_size: 1024
    maximum_size: 1024
    override: no
    state: present

- name: Set C pagefile, override if exists
  win_pagefile:
    drive: C
    initial_size: 1024
    maximum_size: 1024
    state: present

- name: Remove C pagefile
  win_pagefile:
    drive: C
    state: absent

- name: Remove all current pagefiles, enable AutomaticManagedPagefile and query at the end
  win_pagefile:
    remove_all: yes
    automatic: yes

- name: Remove all pagefiles disable AutomaticManagedPagefile and set C pagefile
  win_pagefile:
    drive: C
    initial_size: 2048
    maximum_size: 2048
    remove_all: yes
    automatic: no
    state: present

- name: Set D pagefile, override if exists
  win_pagefile:
    drive: d
    initial_size: 1024
    maximum_size: 1024
    state: present

```

## License

TODO

## Author Information
  - ['Liran Nisanov (@LiranNis)']
