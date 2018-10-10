# Ansible module: ansible.module_netapp_e_snapshot_images


NetApp E-Series create and delete snapshot images

## Description

Create and delete snapshots images on snapshot groups for NetApp E-series storage arrays.
Only the oldest snapshot image can be deleted so consistency is preserved.
Related: Snapshot volumes are created from snapshot images.

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity WebServices Proxy or embedded REST API.']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "snapshot_group": "{'description': ['The name of the snapshot group in which you want to create a snapshot image.'], 'required': True}",
    "state": "{'description': ['Whether a new snapshot image should be created or oldest be deleted.'], 'required': True, 'choices': ['create', 'remove']}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?']}",
}
```

## Examples


``` yaml

    - name: Create Snapshot
      netapp_e_snapshot_images:
        ssid: "{{ ssid }}"
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
        validate_certs: "{{ validate_certs }}"
        snapshot_group: "3300000060080E5000299C24000005B656D9F394"
        state: 'create'

```

## License

TODO

## Author Information
  - ['Kevin Hulquest (@hulquest)']
