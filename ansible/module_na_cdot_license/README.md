# Ansible module: ansible.module_na_cdot_license


Manage NetApp cDOT protocol and feature licenses

## Description

Add or remove licenses on NetApp ONTAP.

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "licenses": "{'description': ['List of licenses to add or remove.', 'Please note that trying to remove a non-existent license will throw an error.'], 'suboptions': {'base': {'description': ['Cluster Base License']}, 'nfs': {'description': ['NFS License']}, 'cifs': {'description': ['CIFS License']}, 'iscsi': {'description': ['iSCSI License']}, 'fcp': {'description': ['FCP License']}, 'cdmi': {'description': ['CDMI License']}, 'snaprestore': {'description': ['SnapRestore License']}, 'snapmirror': {'description': ['SnapMirror License']}, 'flexclone': {'description': ['FlexClone License']}, 'snapvault': {'description': ['SnapVault License']}, 'snaplock': {'description': ['SnapLock License']}, 'snapmanagersuite': {'description': ['SnapManagerSuite License']}, 'snapprotectapps': {'description': ['SnapProtectApp License']}, 'v_storageattach': {'description': ['Virtual Attached Storage License']}}}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "remove_expired": "{'description': ['Remove licenses that have expired in the cluster.'], 'type': 'bool'}",
    "remove_unused": "{'description': ['Remove licenses that have no controller affiliation in the cluster.'], 'type': 'bool'}",
    "serial_number": "{'description': ['Serial number of the node associated with the license.', 'This parameter is used primarily when removing license for a specific service.', 'If this parameter is not provided, the cluster serial number is used by default.']}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
}
```

## Examples


``` yaml

- name: Add licenses
  na_cdot_license:
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    serial_number: #################
    licenses:
      nfs: #################
      cifs: #################
      iscsi: #################
      fcp: #################
      snaprestore: #################
      flexclone: #################

- name: Remove licenses
  na_cdot_license:
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    remove_unused: false
    remove_expired: true
    serial_number: #################
    licenses:
      nfs: remove

```

## License

TODO

## Author Information
  - ['Sumit Kumar (sumit4@netapp.com)']
