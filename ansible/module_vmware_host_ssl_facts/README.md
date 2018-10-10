# Ansible module: ansible.module_vmware_host_ssl_facts


Gather facts of ESXi host system about SSL

## Description

This module can be used to gather facts of the SSL thumbprint information for a host.

## Requirements

TODO

## Arguments

``` json
{
    "cluster_name": "{'description': ['Name of the cluster.', 'SSL thumbprint information about all ESXi host system in the given cluster will be reported.', 'If C(esxi_hostname) is not given, this parameter is required.']}",
    "esxi_hostname": "{'description': ['ESXi hostname.', 'SSL thumbprint information of this ESXi host system will be reported.', 'If C(cluster_name) is not given, this parameter is required.']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Gather SSL thumbprint information about all ESXi Hosts in given Cluster
  vmware_host_ssl_facts:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost
  register: all_host_ssl_facts

- name: Get SSL Thumbprint info about "{{ esxi_hostname }}"
  vmware_host_ssl_facts:
    hostname: "{{ vcenter_server }}"
    username: "{{ vcenter_user }}"
    password: "{{ vcenter_pass }}"
    esxi_hostname: '{{ esxi_hostname }}'
  register: ssl_facts
- set_fact:
    ssl_thumbprint: "{{ ssl_facts['host_ssl_facts'][esxi_hostname]['ssl_thumbprints'][0] }}"
- debug:
    msg: "{{ ssl_thumbprint }}"
- name: Add ESXi Host to vCenter
  vmware_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: '{{ datacenter_name }}'
    cluster_name: '{{ cluster_name }}'
    esxi_hostname: '{{ esxi_hostname }}'
    esxi_username: '{{ esxi_username }}'
    esxi_password: '{{ esxi_password }}'
    esxi_ssl_thumbprint: '{{ ssl_thumbprint }}'
    state: present

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
