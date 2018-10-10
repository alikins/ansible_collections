# Ansible module: ansible.module_netapp_e_auth


NetApp E-Series set or update the password for a storage array

## Description

Sets or updates the password for a storage array.  When the password is updated on the storage array, it must be updated on the SANtricity Web Services proxy. Note, all storage arrays do not have a Monitor or RO role.

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'description': ['The password used to authenticate against the API', 'This can optionally be set via an environment variable, API_PASSWORD'], 'required': False}",
    "api_url": "{'description': ['The full API url.', 'Example: http://ENDPOINT:8080/devmgr/v2', 'This can optionally be set via an environment variable, API_URL'], 'required': False}",
    "api_username": "{'description': ['The username used to authenticate against the API', 'This can optionally be set via an environment variable, API_USERNAME'], 'required': False}",
    "current_password": "{'description': ["The current admin password. This is not required if the password hasn't been set before."], 'required': False}",
    "name": "{'description': ["The name of the storage array. Note that if more than one storage array with this name is detected, the task will fail and you'll have to use the ID instead."], 'required': False}",
    "new_password": "{'description': ['The password you would like to set. Cannot be more than 30 characters.'], 'required': True}",
    "set_admin": "{'description': ['Boolean value on whether to update the admin password. If set to false then the RO account is updated.'], 'default': False}",
    "ssid": "{'description': ['the identifier of the storage array in the Web Services Proxy.'], 'required': False}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?']}",
}
```

## Examples


``` yaml

- name: Test module
  netapp_e_auth:
    name: trex
    current_password: OldPasswd
    new_password: NewPasswd
    set_admin: yes
    api_url: '{{ netapp_api_url }}'
    api_username: '{{ netapp_api_username }}'
    api_password: '{{ netapp_api_password }}'

```

## License

TODO

## Author Information
  - ['Kevin Hulquest (@hulquest)']
