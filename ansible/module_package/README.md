# Ansible module: ansible.module_package


Generic OS package manager

## Description

Installs, upgrade and removes packages using the underlying OS package manager.
For Windows targets, use the M(win_package) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Package name, or package specifier with version, like C(name-1.0).', "Be aware that packages are not always named the same and this module will not 'translate' them per distro."], 'required': True}",
    "state": "{'description': ['Whether to install (C(present)), or remove (C(absent)) a package. Other states depend on the underlying package module, i.e C(latest).'], 'required': True}",
    "use": "{'description': ["The required package manager module to use (yum, apt, etc). The default 'auto' will use existing facts or try to autodetect it.", 'You should only use this field if the automatic selection is not working for some reason.'], 'required': False, 'default': 'auto'}",
}
```

## Examples


``` yaml

- name: install ntpdate
  package:
    name: ntpdate
    state: present

# This uses a variable as this changes per distribution.
- name: remove the apache package
  package:
    name: "{{ apache }}"
    state: absent

```

## License

TODO

## Author Information
  - ['Ansible Inc']
