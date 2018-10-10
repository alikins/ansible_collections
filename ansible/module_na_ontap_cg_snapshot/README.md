# Ansible module: ansible.module_na_ontap_cg_snapshot


NetApp ONTAP manage consistency group snapshot

## Description

Create consistency group snapshot for ONTAP volumes.

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "snapmirror_label": "{'description': ['A human readable SnapMirror label to be attached with the consistency group snapshot copies.']}",
    "snapshot": "{'required': True, 'description': ['The provided name of the snapshot that is created in each volume.']}",
    "state": "{'description': ['If you want to create a snapshot.'], 'default': 'present'}",
    "timeout": "{'description': ['Timeout selector.'], 'choices': ['urgent', 'medium', 'relaxed'], 'default': 'medium'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "volumes": "{'required': True, 'description': ['A list of volumes in this filer that is part of this CG operation.']}",
    "vserver": "{'required': True, 'description': ['Name of the vserver.']}",
}
```

## Examples


``` yaml

    - name:
      na_ontap_cg_snapshot:
        state: present
        vserver: vserver_name
        snapshot: snapshot name
        volume: vol_name
        username: "{{ netapp username }}"
        password: "{{ netapp password }}"
        hostname: "{{ netapp hostname }}"

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
