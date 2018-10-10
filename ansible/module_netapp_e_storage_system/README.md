# Ansible module: ansible.module_netapp_e_storage_system


NetApp E-Series Web Services Proxy manage storage arrays

## Description

Manage the arrays accessible via a NetApp Web Services Proxy for NetApp E-series storage arrays.

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'description': ['The password to authenticate with the SANtricity WebServices Proxy or embedded REST API.'], 'required': True}",
    "api_url": "{'description': ['The url to the SANtricity WebServices Proxy or embedded REST API.'], 'required': True}",
    "api_username": "{'description': ['The username to authenticate with the SANtricity WebServices Proxy or embedded REST API.'], 'required': True}",
    "array_password": "{'description': ['The management password of the array to manage, if set.']}",
    "array_wwn": "{'description': ['The WWN of the array to manage. Only necessary if in-band managing multiple arrays on the same agent host.  Mutually exclusive of controller_addresses parameter.']}",
    "controller_addresses": "{'description': ['The list addresses for the out-of-band management adapter or the agent host. Mutually exclusive of array_wwn parameter.'], 'required': True}",
    "enable_trace": "{'description': ['Enable trace logging for SYMbol calls to the storage system.'], 'type': 'bool', 'default': False}",
    "meta_tags": "{'description': ['Optional meta tags to associate to this storage system']}",
    "ssid": "{'description': ['The ID of the array to manage. This value must be unique for each array.'], 'required': True}",
    "state": "{'description': ['Whether the specified array should be configured on the Web Services Proxy or not.'], 'required': True, 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['Should https certificates be validated?'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

---
    - name:  Presence of storage system
      netapp_e_storage_system:
        ssid: "{{ item.key }}"
        state: present
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
        validate_certs: "{{ netapp_api_validate_certs }}"
        controller_addresses:
          - "{{ item.value.address1 }}"
          - "{{ item.value.address2 }}"
      with_dict: "{{ storage_systems }}"
      when: check_storage_system

```

## License

TODO

## Author Information
  - ['Kevin Hulquest (@hulquest)']
