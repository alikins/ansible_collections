# Ansible module: ansible.module_netapp_e_volume


NetApp E-Series manage storage volumes (standard and thin)

## Description

Create or remove volumes (standard and thin) for NetApp E/EF-series storage arrays.

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity Web Services Proxy or Embedded Web Services API.'], 'example': ['https://prod-1.wahoo.acme.com/devmgr/v2']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "data_assurance_enabled": "{'description': ['If data assurance should be enabled for the volume'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['The name of the volume to manage'], 'required': True}",
    "segment_size_kb": "{'description': ['The segment size of the new volume'], 'default': 512}",
    "size": "{'description': ["Required only when state = 'present'.  The size of the volume in (size_unit)."], 'required': True}",
    "size_unit": "{'description': ['The unit used to interpret the size parameter'], 'choices': ['bytes', 'b', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb'], 'default': 'gb'}",
    "ssd_cache_enabled": "{'description': ['Whether an existing SSD cache should be enabled on the volume (fails if no SSD cache defined)', 'The default value is to ignore existing SSD cache setting.'], 'type': 'bool'}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage. This value must be unique for each array.']}",
    "state": "{'description': ['Whether the specified volume should exist or not.'], 'required': True, 'choices': ['present', 'absent']}",
    "storage_pool_name": "{'description': ["Required only when requested state is 'present'.  The name of the storage pool the volume should exist on."], 'required': True}",
    "thin_provision": "{'description': ['Whether the volume should be thin provisioned.  Thin volumes can only be created on disk pools (raidDiskPool).'], 'type': 'bool', 'default': False}",
    "thin_volume_max_repo_size": "{'description': ['Maximum size that the thin volume repository volume will automatically expand to'], 'default': 'same as size (in size_unit)'}",
    "thin_volume_repo_size": "{'description': ['Initial size of the thin volume repository volume (in size_unit)'], 'required': True}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?'], 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: No thin volume
      netapp_e_volume:
        ssid: "{{ ssid }}"
        name: NewThinVolumeByAnsible
        state: absent
        log_path: /tmp/volume.log
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
        validate_certs: "{{ netapp_api_validate_certs }}"
      when: check_volume


    - name: No fat volume
      netapp_e_volume:
        ssid: "{{ ssid }}"
        name: NewVolumeByAnsible
        state: absent
        log_path: /tmp/volume.log
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
        validate_certs: "{{ netapp_api_validate_certs }}"
      when: check_volume

```

## License

TODO

## Author Information
  - ['Kevin Hulquest (@hulquest)']
