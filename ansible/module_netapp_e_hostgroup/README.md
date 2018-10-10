# Ansible module: ansible.module_netapp_e_hostgroup


NetApp E-Series manage array host groups

## Description

Create, update or destroy host groups on a NetApp E-Series storage array.

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity WebServices Proxy or embedded REST API.']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "hosts": "{'required': False, 'description': ['a list of host names/labels to add to the group']}",
    "id": "{'required': False, 'description': ['The id number of the host group to manage. Either this or C(name) must be supplied.']}",
    "name": "{'required': False, 'description': ['The name of the host group to manage. Either this or C(id_num) must be supplied.']}",
    "new_name": "{'required': False, 'description': ['specify this when you need to update the name of a host group']}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage (as configured on the web services proxy).']}",
    "state": "{'required': True, 'description': ['Whether the specified host group should exist or not.'], 'choices': ['present', 'absent']}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?']}",
}
```

## Examples


``` yaml

    - name: Configure Hostgroup
      netapp_e_hostgroup:
        ssid: "{{ ssid }}"
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
        validate_certs: "{{ netapp_api_validate_certs }}"
        state: present

```

## License

TODO

## Author Information
  - ['Kevin Hulquest (@hulquest)']
