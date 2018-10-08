# Ansible lookup: ansible.lookup_vars


Lookup templated value of variables

## Description

Retrieves the value of an Ansible variable.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['The variable names to look up.'], 'required': True}",
    "default": "{'description': ['What to return if a variable is undefined.', 'If no default is set, it will result in an error if any of the variables is undefined.']}",
}
```

## Examples


``` yaml

- name: Show value of 'variablename'
  debug: msg="{{ lookup('vars', 'variabl' + myvar)}}"
  vars:
    variablename: hello
    myvar: ename

- name: Show default empty since i dont have 'variablnotename'
  debug: msg="{{ lookup('vars', 'variabl' + myvar, default='')}}"
  vars:
    variablename: hello
    myvar: notename

- name: Produce an error since i dont have 'variablnotename'
  debug: msg="{{ lookup('vars', 'variabl' + myvar)}}"
  ignore_errors: True
  vars:
    variablename: hello
    myvar: notename

- name: find several related variables
  debug: msg="{{ lookup('vars', 'ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all') }}"

- name: alternate way to find some 'prefixed vars' in loop
  debug: msg="{{ lookup('vars', 'ansible_play_' + item) }}"
  loop:
    - hosts
    - batch
    - hosts_all

```

## License

TODO

## Author Information
  - ['Ansible Core']
