# Ansible module: ansible.module_win_hostname


Manages local Windows computer name

## Description

Manages local Windows computer name.
A reboot is required for the computer name to take effect.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['The hostname to set for the computer.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Change the hostname to sample-hostname
  win_hostname:
    name: sample-hostname
  register: res

- name: Reboot
  win_reboot:
  when: res.reboot_required

```

## License

TODO

## Author Information
  - ['Ripon Banik (@riponbanik)']
