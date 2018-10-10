# Ansible module: ansible.module_vmware_drs_rule_facts


Gathers facts about DRS rule on the given cluster

## Description

This module can be used to gather facts about DRS VM-VM and VM-HOST rules from the given cluster.

## Requirements

TODO

## Arguments

``` json
{
    "cluster_name": "{'description': ['Name of the cluster.', 'DRS facts for the given cluster will be returned.', 'This is required parameter if C(datacenter) parameter is not provided.']}",
    "datacenter": "{'description': ['Name of the datacenter.', 'DRS facts for all the clusters from the given datacenter will be returned.', 'This is required parameter if C(cluster_name) parameter is not provided.']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Gather DRS facts about given Cluster
  vmware_drs_rule_facts:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost
  register: cluster_drs_facts

- name: Gather DRS facts about all Clusters in given datacenter
  vmware_drs_rule_facts:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: '{{ datacenter_name }}'
  delegate_to: localhost
  register: datacenter_drs_facts

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
