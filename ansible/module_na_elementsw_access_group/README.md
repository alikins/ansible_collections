# Ansible module: ansible.module_na_elementsw_access_group


NetApp Element Software Manage Access Groups

## Description

Create, destroy, or update access groups on Element Software Cluster.

## Requirements

TODO

## Arguments

``` json
{
    "attributes": "{'description': ['List of Name/Value pairs in JSON object format.']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "initiators": "{'description': ['List of initiators to include in the access group. If unspecified, the access group will start out without configured initiators.'], 'required': False}",
    "new_name": "{'description': ['New name for the access group for create and modify operation.', 'Required for create operation.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "src_access_group_id": "{'description': ['ID or Name of the access group to modify or delete.', 'Required for delete and modify operations.']}",
    "state": "{'description': ['Whether the specified access group should exist or not.'], 'required': True, 'choices': ['present', 'absent']}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
    "virtual_network_id": "{'description': ['The ID of the Element SW Software Cluster Virtual Network ID to associate the access group with.']}",
    "virtual_network_tags": "{'description': ['The ID of the VLAN Virtual Network Tag to associate the access group with.']}",
    "volumes": "{'description': ['List of volumes to initially include in the volume access group. If unspecified, the access group will start without any volumes.']}",
}
```

## Examples


``` yaml

   - name: Create Access Group
     na_elementsw_access_group:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: present
       new_name: AnsibleAccessGroup
       volumes: [7,8]

   - name: Modify Access Group
     na_elementsw_access_group:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: present
       src_access_group_id: AnsibleAccessGroup
       new_name: AnsibleAccessGroup-Renamed
       attributes: {"volumes": [1,2,3], "virtual_network_id": 12345}

   - name: Delete Access Group
     na_elementsw_access_group:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: absent
       src_access_group_id: 1

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
