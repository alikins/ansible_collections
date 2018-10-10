# Ansible module: ansible.module_na_elementsw_node


NetApp Element Software Node Operation

## Description

Add, remove cluster node on Element Software Cluster.

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "node_id": "{'description': ['List of IDs or Names or IP Address of nodes from cluster used for operation.'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'description': ['Element Software Storage Node operation state.', 'present - To add pending node to participate in cluster data storage.', 'absent  - To remove node from active cluster.  A node cannot be removed if active drives are present.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
}
```

## Examples


``` yaml

   - name: Add node from pending to active cluster
     tags:
     - elementsw_add_node
     na_elementsw_node:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: present
       node_id: sf4805-meg-03

   - name: Remove active node from cluster
     tags:
     - elementsw_remove_node
     na_elementsw_node:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: absent
       node_id: 13

   - name: Add node from pending to active cluster using node IP
     tags:
     - elementsw_add_node_ip
     na_elementsw_node:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: present
       node_id: 10.109.48.65

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
