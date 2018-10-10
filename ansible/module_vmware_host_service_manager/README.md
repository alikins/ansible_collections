# Ansible module: ansible.module_vmware_host_service_manager


Manage services on a given ESXi host

## Description

This module can be used to manage (start, stop, restart) services on a given ESXi host.
If cluster_name is provided, specified service will be managed on all ESXi host belonging to that cluster.
If specific esxi_hostname is provided, then specified service will be managed on given ESXi host only.

## Requirements

TODO

## Arguments

``` json
{
    "cluster_name": "{'description': ['Name of the cluster.', 'Service settings are applied to every ESXi host system/s in given cluster.', 'If C(esxi_hostname) is not given, this parameter is required.']}",
    "esxi_hostname": "{'description': ['ESXi hostname.', 'Service settings are applied to this ESXi host system.', 'If C(cluster_name) is not given, this parameter is required.']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "service_name": "{'description': ['Name of Service to be managed. This is brief identifier for the service, for example, ntpd, vxsyslogd etc.', 'This value should be a valid ESXi service name.'], 'required': True}",
    "service_policy": "{'description': ['Set of valid service policy strings.', 'If set C(on), then service should be started when the host starts up.', 'If set C(automatic), then service should run if and only if it has open firewall ports.', 'If set C(off), then Service should not be started when the host starts up.'], 'choices': ['automatic', 'off', 'on']}",
    "state": "{'description': ['Desired state of service.', "State value 'start' and 'present' has same effect.", "State value 'stop' and 'absent' has same effect."], 'choices': ['absent', 'present', 'restart', 'start', 'stop'], 'default': 'start'}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Start ntpd service setting for all ESXi Host in given Cluster
  vmware_host_service_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
    service_name: ntpd
    state: present
  delegate_to: localhost

- name: Start ntpd setting for an ESXi Host
  vmware_host_service_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    service_name: ntpd
    state: present
  delegate_to: localhost

- name: Start ntpd setting for an ESXi Host with Service policy
  vmware_host_service_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    service_name: ntpd
    service_policy: on
    state: present
  delegate_to: localhost

- name: Stop ntpd setting for an ESXi Host
  vmware_host_service_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    service_name: ntpd
    state: absent
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
