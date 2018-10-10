# Ansible module: ansible.module_na_ontap_snapmirror


NetApp ONTAP Manage SnapMirror

## Description

Create/Delete/Initialize/Modify SnapMirror volume/vserver relationships

## Requirements

TODO

## Arguments

``` json
{
    "destination_path": "{'description': ['Specifies the destination endpoint of the SnapMirror relationship.']}",
    "destination_volume": "{'description': ['Specifies the name of the destination volume for the SnapMirror.']}",
    "destination_vserver": "{'description': ['Name of the destination vserver for the SnapMirror.']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "relationship_type": "{'choices': ['data_protection', 'load_sharing', 'vault', 'restore', 'transition_data_protection', 'extended_data_protection'], 'description': ['Specify the type of SnapMirror relationship.']}",
    "schedule": "{'description': ['Specify the name of the current schedule, which is used to update the SnapMirror relationship.', 'Optional for create, modifiable.']}",
    "source_hostname": "{'description': ['Source hostname or IP address.', 'Required for SnapMirror delete']}",
    "source_password": "{'description': ['Source password.', 'Optional if this is same as destination password.']}",
    "source_path": "{'description': ['Specifies the source endpoint of the SnapMirror relationship.']}",
    "source_username": "{'description': ['Source username.', 'Optional if this is same as destination username.']}",
    "source_volume": "{'description': ['Specifies the name of the source volume for the SnapMirror.']}",
    "source_vserver": "{'description': ['Name of the source vserver for the SnapMirror.']}",
    "state": "{'choices': ['present', 'absent'], 'description': ['Whether the specified relationship should exist or not.'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
}
```

## Examples


``` yaml


    - name: Create SnapMirror
      na_ontap_snapmirror:
        state: present
        source_volume: test_src
        destination_volume: test_dest
        source_vserver: ansible_src
        destination_vserver: ansible_dest
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

    - name: Delete SnapMirror
      na_ontap_snapmirror:
        state: absent
        destination_path: <path>
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

    - name: Set schedule to NULL
      na_ontap_snapmirror:
        state: present
        destination_path: <path>
        schedule: ""
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

    - name: Release SnapMirror
      na_ontap_snapmirror:
        state: release
        destination_path: <path>
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
