# Ansible module: ansible.module_na_elementsw_cluster


NetApp Element Software Create Cluster

## Description

Initialize Element Software node ownership to form a cluster.

## Requirements

TODO

## Arguments

``` json
{
    "accept_eula": "{'description': ['Required to indicate your acceptance of the End User License Agreement when creating this cluster.', 'To accept the EULA, set this parameter to true.'], 'type': 'bool'}",
    "attributes": "{'description': ['List of name-value pairs in JSON object format.']}",
    "cluster_admin_password": "{'description': ['Initial password for the cluster admin account.', 'If not provided, default to login password.']}",
    "cluster_admin_username": "{'description': ['Username for the cluster admin.', 'If not provided, default to login username.']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "management_virtual_ip": "{'description': ['Floating (virtual) IP address for the cluster on the management network.'], 'required': True}",
    "nodes": "{'description': ['Storage IP (SIP) addresses of the initial set of nodes making up the cluster.', 'nodes IP must be in the list.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "replica_count": "{'description': ['Number of replicas of each piece of data to store in the cluster.'], 'default': '2'}",
    "storage_virtual_ip": "{'description': ['Floating (virtual) IP address for the cluster on the storage (iSCSI) network.'], 'required': True}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
}
```

## Examples


``` yaml


  - name: Initialize new cluster
    tags:
    - elementsw_cluster
    na_elementsw_cluster:
      hostname: "{{ elementsw_hostname }}"
      username: "{{ elementsw_username }}"
      password: "{{ elementsw_password }}"
      management_virtual_ip: 10.226.108.32
      storage_virtual_ip: 10.226.109.68
      replica_count: 2
      cluster_admin_username: admin
      cluster_admin_password: netapp123
      accept_eula: true
      nodes:
      - 10.226.109.72
      - 10.226.109.74

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
