# Ansible module: ansible.module_vmware_vmkernel


Manage a VMware VMkernel Interface aka. Virtual NICs of host system

## Description

This module can be used to manage the VMWare VMKernel interface (also known as Virtual NICs) of host system.
This module assumes that the host is already configured with Portgroup and vSwitch.

## Requirements

TODO

## Arguments

``` json
{
    "enable_ft": "{'description': ['Enable the VMKernel interface for Fault Tolerance traffic.'], 'type': 'bool'}",
    "enable_mgmt": "{'description': ['Enable the VMKernel interface for Management traffic.'], 'type': 'bool'}",
    "enable_provisioning": "{'description': ['Enable the VMKernel interface for provisioning service.'], 'type': 'bool', 'version_added': 2.8}",
    "enable_replication": "{'description': ['Enable the VMKernel interface for vSphere replication service.'], 'type': 'bool', 'version_added': 2.8}",
    "enable_replication_nfc": "{'description': ['Enable the VMKernel interface for vSphere replication NFC service.'], 'type': 'bool', 'version_added': 2.8}",
    "enable_vmotion": "{'description': ['Enable the VMKernel interface for vMotion traffic.'], 'type': 'bool'}",
    "enable_vsan": "{'description': ['Enable the VMKernel interface for VSAN traffic.'], 'type': 'bool'}",
    "esxi_hostname": "{'description': ['Name of ESXi host to which VMKernel is to be managed.', 'From version 2.5 onwards, this parameter is required.'], 'required': True, 'version_added': 2.5}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "ip_address": "{'description': ['The IP Address for the VMKernel interface.', 'Use C(network) parameter with C(ip_address) instead.', 'Deprecated option, will be removed in version 2.9.']}",
    "mtu": "{'description': ['The MTU for the VMKernel interface.', 'The default value of 1500 is valid from version 2.5 and onwards.'], 'default': 1500}",
    "network": "{'description': ['A dictionary of network details.', 'Following parameter is required:', ' - C(type) (string): Type of IP assignment (either C(dhcp) or C(static)).', 'Following parameters are required in case of C(type) is set to C(static)', ' - C(ip_address) (string): Static IP address (implies C(type: static)).', ' - C(subnet_mask) (string): Static netmask required for C(ip).'], 'version_added': 2.5}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "portgroup_name": "{'description': ['The name of the port group for the VMKernel interface.'], 'required': True}",
    "state": "{'description': ['If set to C(present), VMKernel is created with the given specifications.', 'If set to C(absent), VMKernel is removed from the given configurations.', 'If set to C(present) and VMKernel exists then VMKernel configurations are updated.'], 'choices': ['present', 'absent'], 'default': 'present', 'version_added': 2.5}",
    "subnet_mask": "{'description': ['The Subnet Mask for the VMKernel interface.', 'Use C(network) parameter with C(subnet_mask) instead.', 'Deprecated option, will be removed in version 2.9.']}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
    "vlan_id": "{'description': ['The VLAN ID for the VMKernel interface.', 'Required parameter only if C(state) is set to C(present).', 'Optional parameter from version 2.5 and onwards.'], 'version_added': 2.0}",
    "vswitch_name": "{'description': ['The name of the vSwitch where to add the VMKernel interface.', 'Required parameter only if C(state) is set to C(present).', 'Optional parameter from version 2.5 and onwards.']}",
}
```

## Examples


``` yaml

-  name: Add Management vmkernel port using static network type
   vmware_vmkernel:
      hostname: '{{ esxi_hostname }}'
      username: '{{ esxi_username }}'
      password: '{{ esxi_password }}'
      vswitch_name: vSwitch0
      portgroup_name: PG_0001
      vlan_id: '{{ vlan_id }}'
      network:
        type: 'static'
        ip_address: 192.168.127.10
        subnet_mask: 255.255.255.0
      state: present
      enable_mgmt: True
   delegate_to: localhost

-  name: Add Management vmkernel port using DHCP network type
   vmware_vmkernel:
      hostname: '{{ esxi_hostname }}'
      username: '{{ esxi_username }}'
      password: '{{ esxi_password }}'
      vswitch_name: vSwitch0
      portgroup_name: PG_0002
      vlan_id: '{{ vlan_id }}'
      state: present
      network:
        type: 'dhcp'
      enable_mgmt: True
   delegate_to: localhost

-  name: Delete VMkernel port using DHCP network type
   vmware_vmkernel:
      hostname: '{{ esxi_hostname }}'
      username: '{{ esxi_username }}'
      password: '{{ esxi_password }}'
      vswitch_name: vSwitch0
      portgroup_name: PG_0002
      vlan_id: '{{ vlan_id }}'
      state: absent
   delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Joseph Callen (@jcpowermac)', 'Russell Teague (@mtnbikenc)', 'Abhijeet Kasurde (@Akasurde)']
  - ['Joseph Callen (@jcpowermac)', 'Russell Teague (@mtnbikenc)', 'Abhijeet Kasurde (@Akasurde)']
  - ['Joseph Callen (@jcpowermac)', 'Russell Teague (@mtnbikenc)', 'Abhijeet Kasurde (@Akasurde)']
