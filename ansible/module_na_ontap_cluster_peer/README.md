# Ansible module: ansible.module_na_ontap_cluster_peer


NetApp ONTAP Manage Cluster peering

## Description

Create/Delete cluster peer relations on ONTAP

## Requirements

TODO

## Arguments

``` json
{
    "dest_cluster_name": "{'description': ['The name of the destination cluster name in the peer relation to be deleted.']}",
    "dest_hostname": "{'description': ['Destination cluster IP or hostname which needs to be peered.'], 'required': True}",
    "dest_intercluster_lif": "{'description': ['Intercluster address of the destination cluster.', 'Used as peer-address in source cluster.']}",
    "dest_password": "{'description': ['Destination password.', 'Optional if this is same as source password.']}",
    "dest_username": "{'description': ['Destination username.', 'Optional if this is same as source username.']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "passphrase": "{'description': ['The arbitrary passphrase that matches the one given to the peer cluster.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "source_cluster_name": "{'description': ['The name of the source cluster name in the peer relation to be deleted.']}",
    "source_intercluster_lif": "{'description': ['Intercluster address of the source cluster.', 'Used as peer-address in destination cluster.']}",
    "state": "{'choices': ['present', 'absent'], 'description': ['Whether the specified cluster peer should exist or not.'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
}
```

## Examples


``` yaml


    - name: Create cluster peer
      na_ontap_cluster_peer:
        state: present
        source_intercluster_lif: 1.2.3.4
        dest_intercluster_lif: 5.6.7.8
        passphrase: XXXX
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"
        dest_hostname: "{{ dest_netapp_hostname }}"

    - name: Delete cluster peer
      na_ontap_cluster_peer:
        state: absent
        source_cluster_name: test-source-cluster
        dest_cluster_name: test-dest-cluster
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"
        dest_hostname: "{{ dest_netapp_hostname }}"

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
