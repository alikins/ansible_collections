# Ansible module: ansible.module_na_ontap_software_update


NetApp ONTAP Update Software

## Description

Update ONTAP software

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "ignore_validation_warning": "{'description': ['Allows the update to continue if warnings are encountered during the validation phase.'], 'default': False, 'type': 'bool'}",
    "node": "{'description': ['List of nodes to be updated, the nodes have to be a part of a HA Pair.']}",
    "package_url": "{'required': True, 'description': ['Specifies the package URL.']}",
    "package_version": "{'required': True, 'description': ['Specifies the package version.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'choices': ['present', 'absent'], 'description': ['Whether the specified ONTAP package should update or not.'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
}
```

## Examples


``` yaml


    - name: ONTAP software update
      na_ontap_software_update:
        state: present
        node: laurentn-vsim1
        package_url: "{{ url }}"
        package_version: "{{ version_name }}"
        ignore_validation_warning: True
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
