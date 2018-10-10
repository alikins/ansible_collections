# Ansible module: ansible.module_vmware_cluster


Manage VMware vSphere clusters

## Description

Add or remove VMware vSphere clusters.

## Requirements

TODO

## Arguments

``` json
{
    "cluster_name": "{'description': ['The name of the cluster that will be created.'], 'required': True}",
    "datacenter_name": "{'description': ['The name of the datacenter the cluster will be created in.'], 'required': True}",
    "enable_drs": "{'description': ['If set to C(yes) will enable DRS when the cluster is created.'], 'type': 'bool', 'default': False}",
    "enable_ha": "{'description': ['If set to C(yes) will enable HA when the cluster is created.'], 'type': 'bool', 'default': False}",
    "enable_vsan": "{'description': ['If set to C(yes) will enable vSAN when the cluster is created.'], 'type': 'bool', 'default': False}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['Create (C(present)) or remove (C(absent)) a VMware vSphere cluster.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Create Cluster
  vmware_cluster:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter
    cluster_name: cluster
    enable_ha: yes
    enable_drs: yes
    enable_vsan: yes
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Joseph Callen (@jcpowermac)']
