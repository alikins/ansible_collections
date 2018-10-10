# Ansible module: ansible.module_vmware_vsan_cluster


Configure VSAN clustering on an ESXi host

## Description

This module can be used to configure VSAN clustering on an ESXi host

## Requirements

TODO

## Arguments

``` json
{
    "cluster_uuid": "{'description': ['Desired cluster UUID'], 'required': False}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Configure VMware VSAN Cluster
  hosts: deploy_node
  tags:
    - vsan
  tasks:
    - name: Configure VSAN on first host
      vmware_vsan_cluster:
         hostname: "{{ groups['esxi'][0] }}"
         username: "{{ esxi_username }}"
         password: "{{ site_password }}"
      delegate_to: localhost
      register: vsan_cluster

    - name: Configure VSAN on remaining hosts
      vmware_vsan_cluster:
         hostname: "{{ item }}"
         username: "{{ esxi_username }}"
         password: "{{ site_password }}"
         cluster_uuid: "{{ vsan_cluster.cluster_uuid }}"
      delegate_to: localhost
      with_items: "{{ groups['esxi'][1:] }}"

```

## License

TODO

## Author Information
  - ['Russell Teague (@mtnbikenc)']
