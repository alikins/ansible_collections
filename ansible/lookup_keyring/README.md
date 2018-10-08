# Ansible lookup: ansible.lookup_keyring


grab secrets from the OS keyring

## Description

Allows you to access data stored in the OS provided keyring/keychain.

## Requirements

TODO

## Arguments

}
```

## Examples


``` yaml

- name : output secrets to screen (BAD IDEA)
  debug:
    msg: "Password: {{item}}"
  with_keyring:
    - 'servicename username'

- name: access mysql with password from keyring
  mysql_db: login_password={{lookup('keyring','mysql joe')}} login_user=joe

```

## License

TODO

## Author Information
  - ['Samuel Boucher <boucher.samuel.c@gmail.com>']
