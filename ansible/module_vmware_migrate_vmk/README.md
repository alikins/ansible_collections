# Ansible module: ansible.module_vmware_migrate_vmk


Migrate a VMK interface from VSS to VDS

## Description

Migrate a VMK interface from VSS to VDS

## Requirements

TODO

## Arguments

``` json
{
    "current_portgroup_name": "{'description': ['Portgroup name VMK interface is currently on'], 'required': True}",
    "current_switch_name": "{'description': ['Switch VMK interface is currently on'], 'required': True}",
    "device": "{'description': ['VMK interface name'], 'required': True}",
    "esxi_hostname": "{'description': ['ESXi hostname to be managed'], 'required': True}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "migrate_portgroup_name": "{'description': ['Portgroup name to migrate VMK interface to'], 'required': True}",
    "migrate_switch_name": "{'description': ['Switch name to migrate VMK interface to'], 'required': True}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Migrate Management vmk
  vmware_migrate_vmk:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    device: vmk1
    current_switch_name: temp_vswitch
    current_portgroup_name: esx-mgmt
    migrate_switch_name: dvSwitch
    migrate_portgroup_name: Management
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Joseph Callen (@jcpowermac)', 'Russell Teague (@mtnbikenc)']
  - ['Joseph Callen (@jcpowermac)', 'Russell Teague (@mtnbikenc)']
