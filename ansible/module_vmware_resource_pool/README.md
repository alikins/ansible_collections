# Ansible module: ansible.module_vmware_resource_pool


Add/remove resource pools to/from vCenter

## Description

This module can be used to add/remove a resource pool to/from vCenter

## Requirements

TODO

## Arguments

``` json
{
    "cluster": "{'description': ['Name of the cluster to add the host.'], 'required': True}",
    "cpu_expandable_reservations": "{'description': ['In a resource pool with an expandable reservation, the reservation on a resource pool can grow beyond the specified value.'], 'default': True, 'type': 'bool'}",
    "cpu_limit": "{'description': ['The utilization of a virtual machine/resource pool will not exceed this limit, even if there are available resources.', 'The default value -1 indicates no limit.'], 'default': -1}",
    "cpu_reservation": "{'description': ['Amount of resource that is guaranteed available to the virtual machine or resource pool.'], 'default': 0}",
    "cpu_shares": "{'description': ['Memory shares are used in case of resource contention.'], 'choices': ['high', 'custom', 'low', 'normal'], 'default': 'normal'}",
    "datacenter": "{'description': ['Name of the datacenter to add the host.'], 'required': True}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "mem_expandable_reservations": "{'description': ['In a resource pool with an expandable reservation, the reservation on a resource pool can grow beyond the specified value.'], 'default': True, 'type': 'bool'}",
    "mem_limit": "{'description': ['The utilization of a virtual machine/resource pool will not exceed this limit, even if there are available resources.', 'The default value -1 indicates no limit.'], 'default': -1}",
    "mem_reservation": "{'description': ['Amount of resource that is guaranteed available to the virtual machine or resource pool.'], 'default': 0}",
    "mem_shares": "{'description': ['Memory shares are used in case of resource contention.'], 'choices': ['high', 'custom', 'low', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "resource_pool": "{'description': ['Resource pool name to manage.'], 'required': True}",
    "state": "{'description': ['Add or remove the resource pool'], 'default': 'present', 'choices': ['present', 'absent']}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Add resource pool to vCenter
  vmware_resource_pool:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: '{{ datacenter_name }}'
    cluster: '{{ cluster_name }}'
    resource_pool: '{{ resource_pool_name }}'
    mem_shares: normal
    mem_limit: -1
    mem_reservation: 0
    mem_expandable_reservations: yes
    cpu_shares: normal
    cpu_limit: -1
    cpu_reservation: 0
    cpu_expandable_reservations: yes
    state: present
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Davis Phillips (@dav1x)']
