# Ansible module: ansible.module_netapp_e_amg_sync


NetApp E-Series conduct synchronization actions on asynchronous mirror groups

## Description

Allows for the initialization, suspension and resumption of an asynchronous mirror group's synchronization for NetApp E-series storage arrays.

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity WebServices Proxy or embedded REST API.']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "delete_recovery_point": "{'description': ['Indicates whether the failures point can be deleted on the secondary if necessary to achieve the synchronization.', 'If true, and if the amount of unsynchronized data exceeds the CoW repository capacity on the secondary for any member volume, the last failures point will be deleted and synchronization will continue.', 'If false, the synchronization will be suspended if the amount of unsynchronized data exceeds the CoW Repository capacity on the secondary and the failures point will be preserved.', 'NOTE: This only has impact for newly launched syncs.'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['The name of the async mirror group you wish to target'], 'required': True}",
    "ssid": "{'description': ['The ID of the storage array containing the AMG you wish to target']}",
    "state": "{'description': ["The synchronization action you'd like to take.", 'If C(running) then it will begin syncing if there is no active sync or will resume a suspended sync. If there is already a sync in progress, it will return with an OK status.', 'If C(suspended) it will suspend any ongoing sync action, but return OK if there is no active sync or if the sync is already suspended'], 'choices': ['running', 'suspended'], 'required': True}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?']}",
}
```

## Examples


``` yaml

    - name: start AMG async
      netapp_e_amg_sync:
        name: "{{ amg_sync_name }}"
        state: running
        ssid: "{{ ssid }}"
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"

```

## License

TODO

## Author Information
  - ['Kevin Hulquest (@hulquest)']
