# Ansible module: ansible.module_na_elementsw_drive


NetApp Element Software Manage Node Drives

## Description

Add, Erase or Remove drive for nodes on Element Software Cluster.

## Requirements

TODO

## Arguments

``` json
{
    "drive_id": "{'description': ['Drive ID or Serial Name of Node drive.', 'If not specified, add and remove action will be performed on all drives of node_id']}",
    "force_during_bin_sync": "{'description': ['Flag to force during a bin sync operation.'], 'type': 'bool'}",
    "force_during_upgrade": "{'description': ['Flag to force drive operation during upgrade.'], 'type': 'bool'}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "node_id": "{'description': ['ID or Name of cluster node.'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'description': ['Element SW Storage Drive operation state.', 'present - To add drive of node to participate in cluster data storage.', 'absent  - To remove the drive from being part of active cluster.', 'clean   - Clean-up any residual data persistent on a *removed* drive in a secured method.'], 'choices': ['present', 'absent', 'clean'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
}
```

## Examples


``` yaml

   - name: Add drive with status available to cluster
     tags:
     - elementsw_add_drive
     na_element_drive:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: present
       drive_id: scsi-SATA_SAMSUNG_MZ7LM48S2UJNX0J3221807
       force_during_upgrade: false
       force_during_bin_sync: false
       node_id: sf4805-meg-03

   - name: Remove active drive from cluster
     tags:
     - elementsw_remove_drive
     na_element_drive:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: absent
       force_during_upgrade: false
       node_id: sf4805-meg-03
       drive_id: scsi-SATA_SAMSUNG_MZ7LM48S2UJNX0J321208

   - name: Secure Erase drive
     tags:
     - elemensw_clean_drive
     na_elementsw_drive:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: clean
       drive_id: scsi-SATA_SAMSUNG_MZ7LM48S2UJNX0J432109
       node_id: sf4805-meg-03

   - name: Add all the drives of a node to cluster
     tags:
     - elementsw_add_node
     na_elementsw_drive:
       hostname: "{{ elementsw_hostname }}"
       username: "{{ elementsw_username }}"
       password: "{{ elementsw_password }}"
       state: present
       force_during_upgrade: false
       force_during_bin_sync: false
       node_id: sf4805-meg-03


```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
