# Ansible module: ansible.module_win_whoami


Get information about the current user and process

## Description

Designed to return the same information as the C(whoami /all) command.
Also includes information missing from C(whoami) such as logon metadata like logon rights, id, type.

## Requirements

TODO

## Arguments

}
```

## Examples


``` yaml

- name: get whoami information
  win_whoami:

```

## License

TODO

## Author Information
  - ['Jordan Borean (@jborean93)']
