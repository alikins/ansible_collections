# Ansible module: ansible.module_netapp_e_lun_mapping


NetApp E-Series create, delete, or modify lun mappings

## Description

Create, delete, or modify mappings between a volume and a targeted host/host+ group.

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity Web Services Proxy or Embedded Web Services API.'], 'example': ['https://prod-1.wahoo.acme.com/devmgr/v2']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "lun": "{'description': ['The LUN value you wish to give the mapping.', 'If the supplied I(volume_name) is associated with a different LUN, it will be updated to what is supplied here.', 'LUN value will be determine by the storage-system when not specified.'], 'version_added': 2.7, 'required': False}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage. This value must be unique for each array.']}",
    "state": "{'description': ['Present will ensure the mapping exists, absent will remove the mapping.'], 'required': True, 'choices': ['present', 'absent']}",
    "target": "{'description': ['The name of host or hostgroup you wish to assign to the mapping', 'If omitted, the default hostgroup is used.', 'If the supplied I(volume_name) is associated with a different target, it will be updated to what is supplied here.'], 'required': False}",
    "target_type": "{'description': ['This option specifies the whether the target should be a host or a group of hosts', 'Only necessary when the target name is used for both a host and a group of hosts'], 'choices': ['host', 'group'], 'version_added': 2.7, 'required': False}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?'], 'type': 'bool'}",
    "volume_name": "{'description': ['The name of the volume you wish to include in the mapping.'], 'required': True, 'aliases': ['volume']}",
}
```

## Examples


``` yaml

---
    - name: Map volume1 to the host target host1
      netapp_e_lun_mapping:
        ssid: 1
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
        validate_certs: no
        state: present
        target: host1
        volume: volume1
    - name: Delete the lun mapping between volume1 and host1
      netapp_e_lun_mapping:
        ssid: 1
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
        validate_certs: yes
        state: absent
        target: host1
        volume: volume1

```

## License

TODO

## Author Information
  - ['Kevin Hulquest (@hulquest)', 'Nathan Swartz (@ndswartz)']
  - ['Kevin Hulquest (@hulquest)', 'Nathan Swartz (@ndswartz)']
