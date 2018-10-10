# Ansible module: ansible.module_cyberark_authentication


Module for CyberArk Vault Authentication using PAS Web Services SDK

## Description

Authenticates to CyberArk Vault using Privileged Account Security Web Services SDK and creates a session fact that can be used by other modules. It returns an Ansible fact called I(cyberark_session). Every module can use this fact as C(cyberark_session) parameter.

## Requirements

TODO

## Arguments

``` json
{
    "api_base_url": "{'description': ["A string containing the base URL of the server hosting CyberArk's Privileged Account Security Web Services SDK."]}",
    "cyberark_session": "{'description': ['Dictionary set by a CyberArk authentication containing the different values to perform actions on a logged-on CyberArk session.']}",
    "new_password": "{'description': ['The new password of the user. This parameter is optional, and enables you to change a password.']}",
    "password": "{'description': ['The password of the user.']}",
    "state": "{'default': 'present', 'choices': ['present', 'absent'], 'description': ['Specifies if an authentication logon/logoff and a cyberark_session should be added/removed.']}",
    "use_radius_authentication": "{'type': 'bool', 'default': False, 'description': ['Whether or not users will be authenticated via a RADIUS server. Valid values are true/false.']}",
    "use_shared_logon_authentication": "{'type': 'bool', 'default': False, 'description': ['Whether or not Shared Logon Authentication will be used.']}",
    "username": "{'description': ['The name of the user who will logon to the Vault.']}",
    "validate_certs": "{'type': 'bool', 'default': True, 'description': ['If C(false), SSL certificates will not be validated.  This should only set to C(false) used on personally controlled sites using self-signed certificates.']}",
}
```

## Examples


``` yaml

- name: Logon to CyberArk Vault using PAS Web Services SDK - use_shared_logon_authentication
  cyberark_authentication:
    api_base_url: "{{ web_services_base_url }}"
    use_shared_logon_authentication: yes

- name: Logon to CyberArk Vault using PAS Web Services SDK - Not use_shared_logon_authentication
  cyberark_authentication:
    api_base_url: "{{ web_services_base_url }}"
    username: "{{ password_object.password }}"
    password: "{{ password_object.passprops.username }}"
    use_shared_logon_authentication: no

- name: Logoff from CyberArk Vault
  cyberark_authentication:
    state: absent
    cyberark_session: "{{ cyberark_session }}"

```

## License

TODO

## Author Information
  - ['Edward Nunez @ CyberArk BizDev (@enunez-cyberark, @cyberark-bizdev, @erasmix)']
