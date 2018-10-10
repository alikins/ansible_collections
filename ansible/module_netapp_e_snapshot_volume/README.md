# Ansible module: ansible.module_netapp_e_snapshot_volume


NetApp E-Series manage snapshot volumes

## Description

Create, update, remove snapshot volumes for NetApp E/EF-Series storage arrays.

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity WebServices Proxy or embedded REST API.']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "full_threshold": "{'description': ['The repository utilization warning threshold percentage'], 'default': 85}",
    "name": "{'required': True, 'description': ['The name you wish to give the snapshot volume']}",
    "repo_percentage": "{'description': ['The size of the view in relation to the size of the base volume'], 'default': 20}",
    "snapshot_image_id": "{'required': True, 'description': ['The identifier of the snapshot image used to create the new snapshot volume.', "Note: You'll likely want to use the M(netapp_e_facts) module to find the ID of the image you want."]}",
    "ssid": "{'description': ['storage array ID'], 'required': True}",
    "state": "{'description': ['Whether to create or remove the snapshot volume'], 'required': True, 'choices': ['absent', 'present']}",
    "storage_pool_name": "{'description': ['Name of the storage pool on which to allocate the repository volume.'], 'required': True}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?']}",
    "view_mode": "{'required': True, 'description': ['The snapshot volume access mode'], 'choices': ['modeUnknown', 'readWrite', 'readOnly', '__UNDEFINED']}",
}
```

## Examples


``` yaml

    - name: Snapshot volume
      netapp_e_snapshot_volume:
        ssid: "{{ ssid }}"
        api_url: "{{ netapp_api_url }}/"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
        state: present
        storage_pool_name: "{{ snapshot_volume_storage_pool_name }}"
        snapshot_image_id: "{{ snapshot_volume_image_id }}"
        name: "{{ snapshot_volume_name }}"

```

## License

TODO

## Author Information
  - ['Kevin Hulquest (@hulquest)']
