# Ansible module: ansible.module_na_ontap_aggregate


NetApp ONTAP manage aggregates

## Description

Create, delete, or manage aggregates on ONTAP.

## Requirements

TODO

## Arguments

``` json
{
    "disk_count": "{'description': ['Number of disks to place into the aggregate, including parity disks.', 'The disks in this newly-created aggregate come from the spare disk pool.', 'The smallest disks in this pool join the aggregate first, unless the C(disk-size) argument is provided.', 'Either C(disk-count) or C(disks) must be supplied. Range [0..2^31-1].', 'Required when C(state=present).']}",
    "disk_size": "{'description': ['Disk size to use in 4K block size.  Disks within 10% of specified size will be used.'], 'version_added': '2.7'}",
    "disk_type": "{'description': ['Type of disk to use to build aggregate'], 'choices': ['ATA', 'BSAS', 'FCAL', 'FSAS', 'LUN', 'MSATA', 'SAS', 'SSD', 'VMDISK'], 'version_added': '2.7'}",
    "from_name": "{'description': ['Name of the aggregate to be renamed.'], 'version_added': '2.7'}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "name": "{'required': True, 'description': ['The name of the aggregate to manage.']}",
    "nodes": "{'description': ['Node(s) for the aggregate to be created on.  If no node specified, mgmt lif home will be used.', 'If multiple nodes specified an aggr stripe will be made.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "raid_size": "{'description': ['Sets the maximum number of drives per raid group.'], 'version_added': '2.7'}",
    "raid_type": "{'description': ['Specifies the type of RAID groups to use in the new aggregate.', 'The default value is raid4 on most platforms.'], 'version_added': '2.7'}",
    "service_state": "{'description': ['Whether the specified aggregate should be enabled or disabled. Creates aggregate if doesnt exist.'], 'choices': ['online', 'offline']}",
    "state": "{'description': ['Whether the specified aggregate should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "unmount_volumes": "{'type': 'bool', 'description': ['If set to "TRUE", this option specifies that all of the volumes hosted by the given aggregate are to be unmounted', 'before the offline operation is executed.', 'By default, the system will reject any attempt to offline an aggregate that hosts one or more online volumes.']}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Create Aggregates
  na_ontap_aggregate:
    state: present
    service_state: online
    name: ansibleAggr
    disk_count: 1
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Manage Aggregates
  na_ontap_aggregate:
    state: present
    service_state: offline
    unmount_volumes: true
    name: ansibleAggr
    disk_count: 1
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Rename Aggregates
  na_ontap_aggregate:
    state: present
    service_state: online
    name: ansibleAggr
    rename: ansibleAggr2
    disk_count: 1
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Delete Aggregates
  na_ontap_aggregate:
    state: absent
    service_state: offline
    unmount_volumes: true
    name: ansibleAggr
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
