# Ansible module: ansible.module_vmware_host_ntp


Manage NTP configurations about an ESXi host

## Description

This module can be used to manage NTP configuration information about an ESXi host.
User can specify an ESXi hostname or Cluster name. In case of cluster name, all ESXi hosts are updated.

## Requirements

TODO

## Arguments

``` json
{
    "cluster_name": "{'description': ['Name of the cluster.', 'NTP settings are applied to every ESXi host system in the given cluster.', 'If C(esxi_hostname) is not given, this parameter is required.']}",
    "esxi_hostname": "{'description': ['ESXi hostname.', 'NTP settings are applied to this ESXi host system.', 'If C(cluster_name) is not given, this parameter is required.']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "ntp_servers": "{'description': ['IP or FQDN of NTP server/s.', 'This accepts a list of NTP servers. For multiple servers, please look at the examples.'], 'required': True}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['present: Add NTP server/s, if it specified server/s are absent else do nothing.', 'absent: Remove NTP server/s, if specified server/s are present else do nothing.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Set NTP setting for all ESXi Host in given Cluster
  vmware_host_ntp:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: cluster_name
    state: present
    ntp_servers:
        - 0.pool.ntp.org
        - 1.pool.ntp.org
  delegate_to: localhost

- name: Set NTP setting for an ESXi Host
  vmware_host_ntp:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    state: present
    ntp_servers:
        - 0.pool.ntp.org
        - 1.pool.ntp.org
  delegate_to: localhost

- name: Remove NTP setting for an ESXi Host
  vmware_host_ntp:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    state: absent
    ntp_servers:
        - bad.server.ntp.org
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
