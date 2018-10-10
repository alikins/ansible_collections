# Ansible module: ansible.module_make


Run targets in a Makefile

## Description

Run targets in a Makefile.

## Requirements

TODO

## Arguments

``` json
{
    "chdir": "{'description': ['Change to this directory before running make'], 'required': True}",
    "file": "{'description': ['Use a custom Makefile'], 'version_added': 2.5}",
    "params": "{'description': ['Any extra parameters to pass to make']}",
    "target": "{'description': ['The target to run.', 'Examples: C(install) or C(test)']}",
}
```

## Examples


``` yaml

- name: Build the default target
  make:
    chdir: /home/ubuntu/cool-project

- name: Run 'install' target as root
  make:
    chdir: /home/ubuntu/cool-project
    target: install
  become: yes

- name: Build 'all' target with extra arguments
  make:
    chdir: /home/ubuntu/cool-project
    target: all
    params:
      NUM_THREADS: 4
      BACKEND: lapack

- name: Build 'all' target with a custom Makefile
  make:
    chdir: /home/ubuntu/cool-project
    target: all
    file: /some-project/Makefile

```

## License

TODO

## Author Information
  - ['Linus Unnebäck (@LinusU) <linus@folkdatorn.se>']
