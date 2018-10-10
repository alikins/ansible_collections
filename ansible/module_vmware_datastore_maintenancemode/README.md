# Ansible module: ansible.module_vmware_datastore_maintenancemode


Place a datastore into maintenance mode

## Description

This module can be used to manage maintenance mode of a datastore.

## Requirements

TODO

## Arguments

``` json
{
    "cluster_name": "{'description': ['Name of the cluster where datastore is connected to.', 'If multiple datastores are connected to the given cluster, then all datastores will be managed by C(state).', 'If C(datastore) or C(datastore_cluster) are not set, this parameter is required.']}",
    "datastore": "{'description': ['Name of datastore to manage.', 'If C(datastore_cluster) or C(cluster_name) are not set, this parameter is required.']}",
    "datastore_cluster": "{'description': ['Name of the datastore cluster from all child datastores to be managed.', 'If C(datastore) or C(cluster_name) are not set, this parameter is required.']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['If set to C(present), then enter datastore into maintenance mode.', 'If set to C(present) and datastore is already in maintenance mode, then no action will be taken.', 'If set to C(absent) and datastore is in maintenance mode, then exit maintenance mode.', 'If set to C(absent) and datastore is not in maintenance mode, then no action will be taken.'], 'choices': ['present', 'absent'], 'default': 'present', 'required': False}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Enter datastore into Maintenance Mode
  vmware_datastore_maintenancemode:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datastore: '{{ datastore_name }}'
    state: present
  delegate_to: localhost

- name: Enter all datastores under cluster into Maintenance Mode
  vmware_datastore_maintenancemode:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
    state: present
  delegate_to: localhost

- name: Enter all datastores under datastore cluster into Maintenance Mode
  vmware_datastore_maintenancemode:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datastore_cluster: '{{ datastore_cluster_name }}'
    state: present
  delegate_to: localhost

- name: Exit datastore into Maintenance Mode
  vmware_datastore_maintenancemode:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datastore: '{{ datastore_name }}'
    state: absent
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
