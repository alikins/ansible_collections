# Ansible module: ansible.module_na_elementsw_volume_pair


NetApp Element Software Volume Pair

## Description

Create, delete volume pair

## Requirements

TODO

## Arguments

``` json
{
    "dest_account": "{'description': ['Destination account name or ID'], 'required': True}",
    "dest_mvip": "{'description': ['Destination IP address of the paired cluster.'], 'required': True}",
    "dest_password": "{'description': ['Destination password for the paired cluster', 'Optional if this is same as source cluster password.']}",
    "dest_username": "{'description': ['Destination username for the paired cluster', 'Optional if this is same as source cluster username.']}",
    "dest_volume": "{'description': ['Destination volume name or volume ID'], 'required': True}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "mode": "{'description': ['Mode to start the volume pairing'], 'choices': ['async', 'sync', 'snapshotsonly'], 'default': 'async'}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "src_account": "{'description': ['Source account name or ID'], 'required': True}",
    "src_volume": "{'description': ['Source volume name or volume ID'], 'required': True}",
    "state": "{'description': ['Whether the specified volume pair should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
}
```

## Examples


``` yaml

   - name: Create volume pair
     na_elementsw_volume_pair:
       hostname: "{{ src_cluster_hostname }}"
       username: "{{ src_cluster_username }}"
       password: "{{ src_cluster_password }}"
       state: present
       src_volume: test1
       src_account: test2
       dest_volume: test3
       dest_account: test4
       mode: sync
       dest_mvip: "{{ dest_cluster_hostname }}"

   - name: Delete volume pair
     na_elementsw_volume_pair:
       hostname: "{{ src_cluster_hostname }}"
       username: "{{ src_cluster_username }}"
       password: "{{ src_cluster_password }}"
       state: absent
       src_volume: 3
       src_account: 1
       dest_volume: 2
       dest_account: 1
       dest_mvip: "{{ dest_cluster_hostname }}"
       dest_username: "{{ dest_cluster_username }}"
       dest_password: "{{ dest_cluster_password }}"


```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
