# Ansible module: ansible.module_vmware_host_powerstate


Manages power states of host systems in vCenter

## Description

This module can be used to manage power states of host systems in given vCenter infrastructure.
User can set power state to 'power-down-to-standby', 'power-up-from-standby', 'shutdown-host' and 'reboot-host'.
State 'reboot-host', 'shutdown-host' and 'power-down-to-standby' are not supported by all the host systems.

## Requirements

TODO

## Arguments

``` json
{
    "cluster_name": "{'description': ['Name of the cluster from which all host systems will be used.', 'This is required parameter if C(esxi_hostname) is not specified.']}",
    "esxi_hostname": "{'description': ['Name of the host system to work with.', 'This is required parameter if C(cluster_name) is not specified.']}",
    "force": "{'description': ['This parameter specify if the host should be proceeding with user defined powerstate regardless of whether it is in maintenance mode.', 'If C(state) set to C(reboot-host) and C(force) as C(true), then host system is rebooted regardless of whether it is in maintenance mode.', 'If C(state) set to C(shutdown-host) and C(force) as C(true), then host system is shutdown regardless of whether it is in maintenance mode.', 'If C(state) set to C(power-down-to-standby) and C(force) to C(true), then all powered off VMs will evacuated.', 'Not applicable if C(state) set to C(power-up-from-standby).'], 'type': 'bool', 'default': False}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['Set the state of the host system.'], 'choices': ['power-down-to-standby', 'power-up-from-standby', 'shutdown-host', 'reboot-host'], 'default': 'shutdown-host'}",
    "timeout": "{'description': ['This parameter defines timeout for C(state) set to C(power-down-to-standby) or C(power-up-from-standby).', 'Ignored if C(state) set to C(reboot-host) or C(shutdown-host).', 'This parameter is defined in seconds.'], 'default': 600}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Set the state of a host system to reboot
  vmware_host_powerstate:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    validate_certs: no
    esxi_hostname: '{{ esxi_hostname }}'
    state: reboot-host
  delegate_to: localhost
  register: reboot_host

- name: Set the state of a host system to power down to standby
  vmware_host_powerstate:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    validate_certs: no
    esxi_hostname: '{{ esxi_hostname }}'
    state: power-down-to-standby
  delegate_to: localhost
  register: power_down

- name: Set the state of all host systems from cluster to reboot
  vmware_host_powerstate:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    validate_certs: no
    cluster_name: '{{ cluster_name }}'
    state: reboot-host
  delegate_to: localhost
  register: reboot_host

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>']
