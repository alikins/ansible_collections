# Ansible module: ansible.module_netapp_e_amg_role


NetApp E-Series update the role of a storage array within an Asynchronous Mirror Group (AMG)

## Description

Update a storage array to become the primary or secondary instance in an asynchronous mirror group

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity WebServices Proxy or embedded REST API.']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "force": "{'description': ['Whether to force the role reversal regardless of the online-state of the primary'], 'required': False, 'default': False}",
    "noSync": "{'description': ['Whether to avoid synchronization prior to role reversal'], 'required': False, 'default': False, 'type': 'bool'}",
    "role": "{'description': ['Whether the array should be the primary or secondary array for the AMG'], 'required': True, 'choices': ['primary', 'secondary']}",
    "ssid": "{'description': ['The ID of the primary storage array for the async mirror action'], 'required': True}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?']}",
}
```

## Examples


``` yaml

    - name: Update the role of a storage array
      netapp_e_amg_role:
        name: updating amg role
        role: primary
        ssid: "{{ ssid }}"
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
        validate_certs: "{{ netapp_api_validate_certs }}"

```

## License

TODO

## Author Information
  - ['Kevin Hulquest (@hulquest)']
