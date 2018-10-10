# Ansible module: ansible.module_panos_lic


apply authcode to a device/instance

## Description

Apply an authcode to a device.
The authcode should have been previously registered on the Palo Alto Networks support portal.
The device should have Internet access.

## Requirements

TODO

## Arguments

``` json
{
    "auth_code": "{'description': ['authcode to be applied'], 'required': True}",
    "force": "{'description': ['whether to apply authcode even if device is already licensed'], 'required': False, 'default': 'false'}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device.'], 'required': True}",
    "password": "{'description': ['Password for authentication.'], 'required': True}",
    "username": "{'description': ['Username for authentication.'], 'default': 'admin'}",
}
```

## Examples


``` yaml

    - hosts: localhost
      connection: local
      tasks:
        - name: fetch license
          panos_lic:
            ip_address: "192.168.1.1"
            password: "paloalto"
            auth_code: "IBADCODE"
          register: result
    - name: Display serialnumber (if already registered)
      debug:
        var: "{{result.serialnumber}}"

```

## License

TODO

## Author Information
  - ['Luigi Mori (@jtschichold), Ivan Bojer (@ivanbojer)']
