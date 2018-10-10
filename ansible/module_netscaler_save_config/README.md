# Ansible module: ansible.module_netscaler_save_config


Save Netscaler configuration

## Description

This module uncoditionally saves the configuration on the target netscaler node.
This module does not support check mode.
This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance.

## Requirements

TODO

## Arguments

``` json
{
    "nitro_pass": "{'description': ['The password with which to authenticate to the netscaler node.'], 'required': True}",
    "nitro_protocol": "{'choices': ['http', 'https'], 'default': 'http', 'description': ['Which protocol to use when accessing the nitro API objects.']}",
    "nitro_timeout": "{'description': ['Time in seconds until a timeout error is thrown when establishing a new session with Netscaler.'], 'default': 310}",
    "nitro_user": "{'description': ['The username with which to authenticate to the netscaler node.'], 'required': True}",
    "nsip": "{'description': ['The ip address of the netscaler appliance where the nitro API calls will be made.', 'The port can be specified with the colon (:). E.g. C(192.168.1.1:555).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'required': False, 'default': 'yes'}",
}
```

## Examples


``` yaml

---
- name: Save netscaler configuration
  delegate_to: localhost
  netscaler_save_config:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot

- name: Setup server without saving  configuration
  delegate_to: localhost
  notify: Save configuration
  netscaler_server:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot

    save_config: no

    name: server-1
    ipaddress: 192.168.1.1

# Under playbook's handlers

- name: Save configuration
  delegate_to: localhost
  netscaler_save_config:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot

```

## License

TODO

## Author Information
  - ['George Nikolopoulos (@giorgos-nikolopoulos)']
