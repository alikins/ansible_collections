# Ansible module: ansible.module_na_ontap_vserver_peer


NetApp ONTAP Vserver peering

## Description

Create/Delete vserver peer

## Requirements

TODO

## Arguments

``` json
{
    "applications": "{'choices': ['snapmirror', 'file_copy', 'lun_copy'], 'description': ['List of applications which can make use of the peering relationship.']}",
    "dest_hostname": "{'description': ['Destination hostname or IP address.', 'Required for creating the vserver peer relationship']}",
    "dest_password": "{'description': ['Destination password.', 'Optional if this is same as source password.']}",
    "dest_username": "{'description': ['Destination username.', 'Optional if this is same as source username.']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "peer_cluster": "{'description': ['Specifies name of the peer Cluster.', 'If peer Cluster is not given, it considers local Cluster.']}",
    "peer_vserver": "{'description': ['Specifies name of the peer Vserver in the relationship.']}",
    "state": "{'choices': ['present', 'absent'], 'description': ['Whether the specified vserver peer should exist or not.'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "vserver": "{'description': ['Specifies name of the source Vserver in the relationship.']}",
}
```

## Examples


``` yaml


    - name: Source vserver peer create
      na_ontap_vserver_peer:
        state: present
        peer_vserver: ansible2
        peer_cluster: ansibleCluster
        vserver: ansible
        applications: snapmirror
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"
        dest_hostname: "{{ netapp_dest_hostname }}"

    - name: vserver peer delete
      na_ontap_vserver_peer:
        state: absent
        peer_vserver: ansible2
        vserver: ansible
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
