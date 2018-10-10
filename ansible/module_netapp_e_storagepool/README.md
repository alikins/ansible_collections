# Ansible module: ansible.module_netapp_e_storagepool


NetApp E-Series manage disk groups and disk pools

## Description

Create or remove disk groups and disk pools for NetApp E-series storage arrays.

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity Web Services Proxy or Embedded Web Services API.'], 'example': ['https://prod-1.wahoo.acme.com/devmgr/v2']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "criteria_drive_count": "{'description': ['The number of disks to use for building the storage pool. The pool will be expanded if this number exceeds the number of disks already in place']}",
    "criteria_drive_interface_type": "{'description': ['The interface type to use when selecting drives for the storage pool (no value means all interface types will be considered)'], 'choices': ['sas', 'sas4k', 'fibre', 'fibre520b', 'scsi', 'sata', 'pata']}",
    "criteria_drive_min_size": "{'description': ['The minimum individual drive size (in size_unit) to consider when choosing drives for the storage pool.']}",
    "criteria_drive_require_fde": "{'description': ['Whether full disk encryption ability is required for drives to be added to the storage pool']}",
    "criteria_drive_type": "{'description': ['The type of disk (hdd or ssd) to use when searching for candidates to use.'], 'choices': ['hdd', 'ssd']}",
    "criteria_min_usable_capacity": "{'description': ['The minimum size of the storage pool (in size_unit). The pool will be expanded if this value exceeds itscurrent size.']}",
    "criteria_size_unit": "{'description': ['The unit used to interpret size parameters'], 'choices': ['bytes', 'b', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb'], 'default': 'gb'}",
    "erase_secured_drives": "{'required': False, 'type': 'bool', 'description': ['Whether to erase secured disks before adding to storage pool']}",
    "name": "{'required': True, 'description': ['The name of the storage pool to manage']}",
    "raid_level": "{'required': True, 'choices': ['raidAll', 'raid0', 'raid1', 'raid3', 'raid5', 'raid6', 'raidDiskPool'], 'description': ["Only required when the requested state is 'present'.  The RAID level of the storage pool to be created."]}",
    "remove_volumes": "{'required': False, 'default': False, 'description': ['Prior to removing a storage pool, delete all volumes in the pool.']}",
    "reserve_drive_count": "{'required': False, 'description': ['Set the number of drives reserved by the storage pool for reconstruction operations. Only valide on raid disk pools.']}",
    "secure_pool": "{'required': False, 'type': 'bool', 'description': ['Whether to convert to a secure storage pool. Will only work if all drives in the pool are security capable.']}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage. This value must be unique for each array.']}",
    "state": "{'required': True, 'description': ['Whether the specified storage pool should exist or not.', 'Note that removing a storage pool currently requires the removal of all defined volumes first.'], 'choices': ['present', 'absent']}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?'], 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: No disk groups
      netapp_e_storagepool:
        ssid: "{{ ssid }}"
        name: "{{ item }}"
        state: absent
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
        validate_certs: "{{ netapp_api_validate_certs }}"

```

## License

TODO

## Author Information
  - ['Kevin Hulquest (@hulquest)']
