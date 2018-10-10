# Ansible module: ansible.module_na_ontap_license


NetApp ONTAP protocol and feature licenses

## Description

Add or remove licenses on NetApp ONTAP.

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "license_codes": "{'description': ['List of license codes to be added.']}",
    "license_names": "{'description': ['List of license-names to delete.'], 'suboptions': {'base': {'description': ['Cluster Base License']}, 'nfs': {'description': ['NFS License']}, 'cifs': {'description': ['CIFS License']}, 'iscsi': {'description': ['iSCSI License']}, 'fcp': {'description': ['FCP License']}, 'cdmi': {'description': ['CDMI License']}, 'snaprestore': {'description': ['SnapRestore License']}, 'snapmirror': {'description': ['SnapMirror License']}, 'flexclone': {'description': ['FlexClone License']}, 'snapvault': {'description': ['SnapVault License']}, 'snaplock': {'description': ['SnapLock License']}, 'snapmanagersuite': {'description': ['SnapManagerSuite License']}, 'snapprotectapps': {'description': ['SnapProtectApp License']}, 'v_storageattach': {'description': ['Virtual Attached Storage License']}}}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "remove_expired": "{'description': ['Remove licenses that have expired in the cluster.'], 'type': 'bool'}",
    "remove_unused": "{'description': ['Remove licenses that have no controller affiliation in the cluster.'], 'type': 'bool'}",
    "serial_number": "{'description': ['Serial number of the node associated with the license. This parameter is used primarily when removing license for a specific service.']}",
    "state": "{'description': ['Whether the specified license should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Add licenses
  na_ontap_license:
    state: present
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    serial_number: #################
    license_codes: CODE1,CODE2

- name: Remove licenses
  na_ontap_license:
    state: absent
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    remove_unused: false
    remove_expired: true
    serial_number: #################
    license_names: nfs,cifs

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
