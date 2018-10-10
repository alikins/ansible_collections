# Ansible module: ansible.module_na_elementsw_cluster_pair


NetApp Element Software Manage Cluster Pair

## Description

Create, delete cluster pair

## Requirements

TODO

## Arguments

``` json
{
    "dest_mvip": "{'description': ['Destination IP address of the cluster to be paired.'], 'required': True}",
    "dest_password": "{'description': ['Destination password for the cluster to be paired.', 'Optional if this is same as source cluster password.']}",
    "dest_username": "{'description': ['Destination username for the cluster to be paired.', 'Optional if this is same as source cluster username.']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'description': ['Whether the specified cluster pair should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
}
```

## Examples


``` yaml

   - name: Create cluster pair
     na_elementsw_cluster_pair:
       hostname: "{{ src_hostname }}"
       username: "{{ src_username }}"
       password: "{{ src_password }}"
       state: present
       dest_mvip: "{{ dest_hostname }}"

   - name: Delete cluster pair
     na_elementsw_cluster_pair:
       hostname: "{{ src_hostname }}"
       username: "{{ src_username }}"
       password: "{{ src_password }}"
       state: absent
       ddest_mvip: "{{ dest_hostname }}"
       dest_username: "{{ dest_username }}"
       dest_password: "{{ dest_password }}"


```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
