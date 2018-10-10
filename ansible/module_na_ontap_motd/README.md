# Ansible module: ansible.module_na_ontap_motd


Setup motd on cDOT

## Description

This module allows you to manipulate motd on cDOT

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "message": "{'description': ['MOTD Text message, required when C(state=present).']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "show_cluster_motd": "{'description': ['Set to I(false) if Cluster-level Message of the Day should not be shown'], 'type': 'bool', 'default': True}",
    "state": "{'description': ['If C(state=present) sets MOTD given in I(message) C(state=absent) removes it.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "vserver": "{'description': ['The name of the SVM motd should be set for.'], 'required': True}",
}
```

## Examples


``` yaml


- name: Set Cluster-Level MOTD
  na_ontap_motd:
    vserver: my_ontap_cluster
    message: "Cluster wide MOTD"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    state: present
    https: true

- name: Set MOTD for I(rhev_nfs_krb) SVM, do not show Cluster-Level MOTD
  na_ontap_motd:
    vserver: rhev_nfs_krb
    message: "Access to rhev_nfs_krb is also restricted"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    state: present
    show_cluster_motd: False
    https: true


```

## License

TODO

## Author Information
  - ['Piotr Olczak (polczak@redhat.com)']
