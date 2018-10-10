# Ansible module: ansible.module_sf_volume_access_group_manager


Manage SolidFire Volume Access Groups

## Description

Create, destroy, or update volume access groups on SolidFire

## Requirements

TODO

## Arguments

``` json
{
    "attributes": "{'description': ['List of Name/Value pairs in JSON object format.']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "initiators": "{'description': ['List of initiators to include in the volume access group. If unspecified, the access group will start out without configured initiators.']}",
    "name": "{'description': ['Name of the volume access group. It is not required to be unique, but recommended.'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'description': ['Whether the specified volume access group should exist or not.'], 'required': True, 'choices': ['present', 'absent']}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
    "virtual_network_id": "{'description': ['The ID of the SolidFire Virtual Network ID to associate the volume access group with.']}",
    "virtual_network_tags": "{'description': ['The ID of the VLAN Virtual Network Tag to associate the volume access group with.']}",
    "volume_access_group_id": "{'description': ['The ID of the volume access group to modify or delete.']}",
    "volumes": "{'description': ['List of volumes to initially include in the volume access group. If unspecified, the access group will start without any volumes.']}",
}
```

## Examples


``` yaml

   - name: Create Volume Access Group
     sf_volume_access_group_manager:
       hostname: "{{ solidfire_hostname }}"
       username: "{{ solidfire_username }}"
       password: "{{ solidfire_password }}"
       state: present
       name: AnsibleVolumeAccessGroup
       volumes: [7,8]

   - name: Modify Volume Access Group
     sf_volume_access_group_manager:
       hostname: "{{ solidfire_hostname }}"
       username: "{{ solidfire_username }}"
       password: "{{ solidfire_password }}"
       state: present
       volume_access_group_id: 1
       name: AnsibleVolumeAccessGroup-Renamed
       attributes: {"volumes": [1,2,3], "virtual_network_id": 12345}

   - name: Delete Volume Access Group
     sf_volume_access_group_manager:
       hostname: "{{ solidfire_hostname }}"
       username: "{{ solidfire_username }}"
       password: "{{ solidfire_password }}"
       state: absent
       volume_access_group_id: 1

```

## License

TODO

## Author Information
  - ['Sumit Kumar (sumit4@netapp.com)']
