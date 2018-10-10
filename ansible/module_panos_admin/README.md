# Ansible module: ansible.module_panos_admin


Add or modify PAN-OS user accounts password

## Description

PanOS module that allows changes to the user account passwords by doing API calls to the Firewall using pan-api as the protocol.

## Requirements

TODO

## Arguments

``` json
{
    "admin_password": "{'description': ['password for admin user'], 'required': True}",
    "admin_username": "{'description': ['username for admin user'], 'default': 'admin'}",
    "commit": "{'description': ['commit if changed'], 'type': 'bool', 'default': True}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device.'], 'required': True}",
    "password": "{'description': ['Password for authentication.'], 'required': True}",
    "role": "{'description': ['role for admin user']}",
    "username": "{'description': ['Username for authentication.'], 'default': 'admin'}",
}
```

## Examples


``` yaml

# Set the password of user admin to "badpassword"
# Doesn't commit the candidate config
  - name: set admin password
    panos_admin:
      ip_address: "192.168.1.1"
      password: "admin"
      admin_username: admin
      admin_password: "badpassword"
      commit: False

```

## License

TODO

## Author Information
  - ['Luigi Mori (@jtschichold), Ivan Bojer (@ivanbojer)']
