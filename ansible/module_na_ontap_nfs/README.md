# Ansible module: ansible.module_na_ontap_nfs


NetApp ONTAP NFS status

## Description

Enable or disable NFS on ONTAP

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "nfsv3": "{'description': ['status of NFSv3.'], 'choices': ['enabled', 'disabled']}",
    "nfsv3_fsid_change": "{'description': ['status of if NFSv3 clients see change in FSID as they traverse filesystems.'], 'choices': ['enabled', 'disabled'], 'version_added': '2.7'}",
    "nfsv4": "{'description': ['status of NFSv4.'], 'choices': ['enabled', 'disabled']}",
    "nfsv40_acl": "{'description': ['status of NFS v4.0 ACL feature'], 'choices': ['enabled', 'disabled'], 'version_added': '2.7'}",
    "nfsv40_read_delegation": "{'description': ['status for NFS v4.0 read delegation feature.'], 'choices': ['enabled', 'disabled'], 'version_added': '2.7'}",
    "nfsv40_write_delegation": "{'description': ['status for NFS v4.0 write delegation feature.'], 'choices': ['enabled', 'disabled'], 'version_added': '2.7'}",
    "nfsv41": "{'description': ['status of NFSv41.'], 'aliases': ['nfsv4.1'], 'choices': ['enabled', 'disabled']}",
    "nfsv41_acl": "{'description': ['status of NFS v4.1 ACL feature'], 'choices': ['enabled', 'disabled'], 'version_added': '2.7'}",
    "nfsv41_read_delegation": "{'description': ['status for NFS v4.1 read delegation feature.'], 'choices': ['enabled', 'disabled'], 'version_added': '2.7'}",
    "nfsv41_write_delegation": "{'description': ['status for NFS v4.1 write delegation feature.'], 'choices': ['enabled', 'disabled'], 'version_added': '2.7'}",
    "nfsv4_id_domain": "{'description': ['Name of the nfsv4_id_domain to use.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "service_state": "{'description': ['Whether the specified NFS should be enabled or disabled. Creates NFS service if doesnt exist.'], 'choices': ['started', 'stopped']}",
    "showmount": "{'description': ['Whether SVM allows showmount'], 'choices': ['enabled', 'disabled'], 'version_added': '2.7'}",
    "state": "{'description': ['Whether NFS should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tcp": "{'description': ['Enable TCP (support from ONTAP 9.3 onward).'], 'choices': ['enabled', 'disabled']}",
    "udp": "{'description': ['Enable UDP (support from ONTAP 9.3 onward).'], 'choices': ['enabled', 'disabled']}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "vserver": "{'description': ['Name of the vserver to use.'], 'required': True}",
    "vstorage_state": "{'description': ['status of vstorage_state.'], 'choices': ['enabled', 'disabled']}",
}
```

## Examples


``` yaml

    - name: change nfs status
      na_ontap_nfs:
        state: present
        service_state: stopped
        vserver: vs_hack
        nfsv3: disabled
        nfsv4: disabled
        nfsv41: enabled
        tcp: disabled
        udp: disabled
        vstorage_state: disabled
        nfsv4_id_domain: example.com
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
