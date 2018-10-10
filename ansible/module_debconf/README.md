# Ansible module: ansible.module_debconf


Configure a .deb package

## Description

Configure a .deb package using debconf-set-selections. Or just query existing selections.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Name of package to configure.'], 'required': True, 'aliases': ['pkg']}",
    "question": "{'description': ['A debconf configuration setting.'], 'aliases': ['selection', 'setting']}",
    "unseen": "{'description': ["Do not set 'seen' flag when pre-seeding."], 'type': 'bool', 'default': False}",
    "value": "{'description': ['Value to set the configuration to.'], 'aliases': ['answer']}",
    "vtype": "{'description': ['The type of the value supplied.', 'C(seen) was added in 2.2.'], 'choices': ['boolean', 'error', 'multiselect', 'note', 'password', 'seen', 'select', 'string', 'text', 'title', 'text']}",
}
```

## Examples


``` yaml

- name: Set default locale to fr_FR.UTF-8
  debconf:
    name: locales
    question: locales/default_environment_locale
    value: fr_FR.UTF-8
    vtype: select

- name: set to generate locales
  debconf:
    name: locales
    question: locales/locales_to_be_generated
    value: en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8
    vtype: multiselect

- name: Accept oracle license
  debconf:
    name: oracle-java7-installer
    question: shared/accepted-oracle-license-v1-1
    value: 'true'
    vtype: select

- name: Specifying package you can register/return the list of questions and current values
  debconf:
    name: tzdata

```

## License

TODO

## Author Information
  - ['Brian Coca (@bcoca)']
