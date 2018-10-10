# Ansible module: ansible.module_vmware_dvswitch


Create or remove a distributed vSwitch

## Description

Create or remove a distributed vSwitch

## Requirements

TODO

## Arguments

``` json
{
    "datacenter_name": "{'description': ['The name of the datacenter that will contain the dvSwitch'], 'required': True}",
    "discovery_operation": "{'description': ['Select the discovery operation'], 'choices': ['both', 'none', 'advertise', 'listen']}",
    "discovery_proto": "{'description': ['Link discovery protocol between Cisco and Link Layer discovery'], 'choices': ['cdp', 'lldp'], 'required': True}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "mtu": "{'description': ['The switch maximum transmission unit'], 'required': True}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['Create or remove dvSwitch'], 'default': 'present', 'choices': ['present', 'absent'], 'required': False}",
    "switch_name": "{'description': ['The name of the switch to create or remove'], 'required': True}",
    "switch_version": "{'description': ['The version of the switch to create. Can be 6.5.0, 6.0.0, 5.5.0, 5.1.0, 5.0.0 with a vcenter running vSphere 6.5', 'Needed if you have a vcenter version > ESXi version to join DVS. If not specified version=version of vcenter'], 'required': False, 'version_added': 2.5}",
    "uplink_quantity": "{'description': ['Quantity of uplink per ESXi host added to the switch'], 'required': True}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Create dvswitch
  vmware_dvswitch:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter
    switch_name: dvSwitch
    switch_version: 6.0.0
    mtu: 9000
    uplink_quantity: 2
    discovery_proto: lldp
    discovery_operation: both
    state: present
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Joseph Callen (@jcpowermac)']
