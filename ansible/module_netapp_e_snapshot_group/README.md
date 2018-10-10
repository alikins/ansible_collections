# Ansible module: ansible.module_netapp_e_snapshot_group


NetApp E-Series manage snapshot groups

## Description

Create, update, delete snapshot groups for NetApp E-series storage arrays

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity WebServices Proxy or embedded REST API.']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity WebServices Proxy or embedded REST API.']}",
    "base_volume_name": "{'description': ['The name of the base volume or thin volume to use as the base for the new snapshot group.', 'If a snapshot group with an identical C(name) already exists but with a different base volume an error will be returned.'], 'required': True}",
    "delete_limit": "{'description': ['The automatic deletion indicator.', 'If non-zero, the oldest snapshot image will be automatically deleted when creating a new snapshot image to keep the total number of snapshot images limited to the number specified.', 'This value is overridden by the consistency group setting if this snapshot group is associated with a consistency group.'], 'required': False, 'default': 30}",
    "full_policy": "{'description': ['The behavior on when the data repository becomes full.', 'This value is overridden by consistency group setting if this snapshot group is associated with a consistency group'], 'required': False, 'default': 'purgepit', 'choices': ['purgepit', 'unknown', 'failbasewrites', '__UNDEFINED']}",
    "name": "{'description': ['The name to give the snapshot group'], 'required': True}",
    "repo_pct": "{'description': ['The size of the repository in relation to the size of the base volume'], 'required': False, 'default': 20}",
    "rollback_priority": "{'required': False, 'description': ['The importance of the rollback operation.', 'This value is overridden by consistency group setting if this snapshot group is associated with a consistency group'], 'choices': ['highest', 'high', 'medium', 'low', 'lowest', '__UNDEFINED'], 'default': 'medium'}",
    "state": "{'description': ['Whether to ensure the group is present or absent.'], 'required': True, 'choices': ['present', 'absent']}",
    "storage_pool_name": "{'required': True, 'description': ['The name of the storage pool on which to allocate the repository volume.']}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?']}",
    "warning_threshold": "{'description': ['The repository utilization warning threshold, as a percentage of the repository volume capacity.'], 'required': False, 'default': 80}",
}
```

## Examples


``` yaml

    - name: Configure Snapshot group
      netapp_e_snapshot_group:
        ssid: "{{ ssid }}"
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
        validate_certs: "{{ netapp_api_validate_certs }}"
        base_volume_name: SSGroup_test
        name=: OOSS_Group
        repo_pct: 20
        warning_threshold: 85
        delete_limit: 30
        full_policy: purgepit
        storage_pool_name: Disk_Pool_1
        rollback_priority: medium

```

## License

TODO

## Author Information
  - ['Kevin Hulquest (@hulquest)']
