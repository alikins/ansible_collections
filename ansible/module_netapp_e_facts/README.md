# Ansible module: ansible.module_netapp_e_facts


NetApp E-Series retrieve facts about NetApp E-Series storage arrays

## Description

Return various information about NetApp E-Series storage arrays (eg, configuration, disks)

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity WebServices Proxy or embedded REST API.']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage. This value must be unique for each array.']}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?']}",
}
```

## Examples


``` yaml

---
    - name: Get array facts
      netapp_e_facts:
        array_id: "{{ netapp_array_id }}"
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
        validate_certs: "{{ netapp_api_validate_certs }}"

```

## License

TODO

## Author Information
  - ['Kevin Hulquest (@hulquest)']
