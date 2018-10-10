# Ansible module: ansible.module_na_cdot_aggregate


Manage NetApp cDOT aggregates

## Description

Create or destroy aggregates on NetApp cDOT.

## Requirements

TODO

## Arguments

``` json
{
    "disk_count": "{'description': ['Number of disks to place into the aggregate, including parity disks.', 'The disks in this newly-created aggregate come from the spare disk pool.', 'The smallest disks in this pool join the aggregate first, unless the C(disk-size) argument is provided.', 'Either C(disk-count) or C(disks) must be supplied. Range [0..2^31-1].', 'Required when C(state=present).']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "name": "{'required': True, 'description': ['The name of the aggregate to manage.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'required': True, 'description': ['Whether the specified aggregate should exist or not.'], 'choices': ['present', 'absent']}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
}
```

## Examples


``` yaml

- name: Manage Aggregates
  na_cdot_aggregate:
    state: present
    name: ansibleAggr
    disk_count: 1
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Manage Aggregates
  na_cdot_aggregate:
    state: present
    name: ansibleAggr
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

```

## License

TODO

## Author Information
  - ['Sumit Kumar (sumit4@netapp.com)']
