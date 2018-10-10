# Ansible module: ansible.module_panos_admpwd


change admin password of PAN-OS device using SSH with SSH key

## Description

Change the admin password of PAN-OS via SSH using a SSH key for authentication.
Useful for AWS instances where the first login should be done via SSH.

## Requirements

TODO

## Arguments

``` json
{
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device'], 'required': True}",
    "key_filename": "{'description': ['filename of the SSH Key to use for authentication'], 'required': True}",
    "newpassword": "{'description': ['password to configure for admin on the PAN-OS device'], 'required': True}",
    "username": "{'description': ['username for initial authentication'], 'required': False, 'default': 'admin'}",
}
```

## Examples


``` yaml

# Tries for 10 times to set the admin password of 192.168.1.1 to "badpassword"
# via SSH, authenticating using key /tmp/ssh.key
- name: set admin password
  panos_admpwd:
    ip_address: "192.168.1.1"
    username: "admin"
    key_filename: "/tmp/ssh.key"
    newpassword: "badpassword"
  register: result
  until: result is not failed
  retries: 10
  delay: 30

```

## License

TODO

## Author Information
  - ['Luigi Mori (@jtschichold), Ivan Bojer (@ivanbojer)']
