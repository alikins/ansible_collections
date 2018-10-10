# Ansible module: ansible.module_netapp_e_volume_copy


NetApp E-Series create volume copy pairs

## Description

Create and delete snapshots images on volume groups for NetApp E-series storage arrays.

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity WebServices Proxy or embedded REST API, for example C(https://prod-1.wahoo.acme.com/devmgr/v2).'], 'example': ['https://prod-1.wahoo.acme.com/devmgr/v2']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "create_copy_pair_if_does_not_exist": "{'description': ['Defines if a copy pair will be created if it does not exist.', 'If set to True destination_volume_id and source_volume_id are required.'], 'type': 'bool', 'default': True}",
    "destination_volume_id": "{'description': ['The id of the volume copy destination.', 'If used, must be paired with source_volume_id', 'Mutually exclusive with volume_copy_pair_id, and search_volume_id']}",
    "search_volume_id": "{'description': ['Searches for all valid potential target and source volumes that could be used in a copy_pair', 'Mutually exclusive with volume_copy_pair_id, destination_volume_id and source_volume_id']}",
    "source_volume_id": "{'description': ['The id of the volume copy source.', 'If used, must be paired with destination_volume_id', 'Mutually exclusive with volume_copy_pair_id, and search_volume_id']}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage. This value must be unique for each array.']}",
    "start_stop_copy": "{'description': ['starts a re-copy or stops a copy in progress', 'Note: If you stop the initial file copy before it it done the copy pair will be destroyed', 'Requires volume_copy_pair_id']}",
    "state": "{'description': ['Whether the specified volume copy pair should exist or not.'], 'required': True, 'choices': ['present', 'absent']}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?'], 'type': 'bool'}",
    "volume_copy_pair_id": "{'description': ['The id of a given volume copy pair', 'Mutually exclusive with destination_volume_id, source_volume_id, and search_volume_id', 'Can use to delete or check presence of volume pairs', 'Must specify this or (destination_volume_id and source_volume_id)']}",
}
```

## Examples


``` yaml

---
msg:
    description: Success message
    returned: success
    type: string
    sample: Json facts for the volume copy that was created.

```

## License

TODO

## Author Information
  - ['Kevin Hulquest (@hulquest)']
