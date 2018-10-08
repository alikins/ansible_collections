# Ansible lookup: ansible.lookup_lines


read lines from command

## Description

Run one or more commands and split the output into lines, returning them as a list

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['command(s) to run'], 'required': True}",
}
```

## Examples


``` yaml

- name: We could read the file directly, but this shows output from command
  debug: msg="{{ item }} is an output line from running cat on /etc/motd"
  with_lines: cat /etc/motd

- name: More useful example of looping over a command result
  shell: "/usr/bin/frobnicate {{ item }}"
  with_lines:
    - "/usr/bin/frobnications_per_host --param {{ inventory_hostname }}"

```

## License

TODO

## Author Information
  - ['Daniel Hokka Zakrisson <daniel@hozac.com>']
