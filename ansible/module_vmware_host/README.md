# Ansible module: ansible.module_vmware_host


Add / Remove ESXi host to / from vCenter

## Description

This module can be used to add / remove / reconnect an ESXi host to / from vCenter.

## Requirements

TODO

## Arguments

``` json
{
    "add_connected": "{'description': ['If set to C(True), then the host should be connected as soon as it is added.', 'This parameter is ignored if state is set to a value other than C(present).'], 'default': True, 'type': 'bool', 'version_added': '2.6'}",
    "cluster_name": "{'description': ['Name of the cluster to add the host.', 'If C(folder) is not set, then this parameter is required.', 'Aliases added in version 2.6.'], 'aliases': ['cluster']}",
    "datacenter_name": "{'description': ['Name of the datacenter to add the host.', 'Aliases added in version 2.6.'], 'required': True, 'aliases': ['datacenter']}",
    "esxi_hostname": "{'description': ['ESXi hostname to manage.'], 'required': True}",
    "esxi_password": "{'description': ['ESXi password.', 'Required for adding a host.', 'Optional for reconnect.', 'Unused for removing.', 'No longer a required parameter from version 2.5.']}",
    "esxi_ssl_thumbprint": "{'description': ["Specifying the hostsystem certificate's thumbprint.", "Use following command to get hostsystem certificate's thumbprint - ", '# openssl x509 -in /etc/vmware/ssl/rui.crt -fingerprint -sha1 -noout'], 'version_added': 2.5, 'default': ''}",
    "esxi_username": "{'description': ['ESXi username.', 'Required for adding a host.', 'Optional for reconnect.', 'Unused for removing.', 'No longer a required parameter from version 2.5.']}",
    "folder": "{'description': ['Name of the folder under which host to add.', 'If C(cluster_name) is not set, then this parameter is required.', "For example, if there is a datacenter 'dc1' under folder called 'Site1' then, this value will be '/Site1/dc1/host'.", "Here 'host' is an invisible folder under VMware Web Client.", "Another example, if there is a nested folder structure like '/myhosts/india/pune' under datacenter 'dc2', then C(folder) value will be '/dc2/host/myhosts/india/pune'.", 'Other Examples: ', "  - '/Site2/dc2/Asia-Cluster/host'", "  - '/dc3/Asia-Cluster/host'"], 'version_added': '2.6'}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['If set to C(present), then add the host if host is absent.', 'If set to C(present), then do nothing if host already exists.', 'If set to C(absent), then remove the host if host is present.', 'If set to C(absent), then do nothing if host already does not exists.', "If set to C(add_or_reconnect), then add the host if it's absent else reconnect it.", "If set to C(reconnect), then reconnect the host if it's present else fail."], 'default': 'present', 'choices': ['present', 'absent', 'add_or_reconnect', 'reconnect']}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Add ESXi Host to vCenter
  vmware_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter_name
    cluster_name: cluster_name
    esxi_hostname: '{{ esxi_hostname }}'
    esxi_username: '{{ esxi_username }}'
    esxi_password: '{{ esxi_password }}'
    state: present
  delegate_to: localhost

- name: Add ESXi Host to vCenter under a specific folder
  vmware_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter_name
    folder: '/Site2/Asia-Cluster/host'
    esxi_hostname: '{{ esxi_hostname }}'
    esxi_username: '{{ esxi_username }}'
    esxi_password: '{{ esxi_password }}'
    state: present
    add_connected: True
  delegate_to: localhost

- name: Reconnect ESXi Host (with username/password set)
  vmware_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter_name
    cluster_name: cluster_name
    esxi_hostname: '{{ esxi_hostname }}'
    esxi_username: '{{ esxi_username }}'
    esxi_password: '{{ esxi_password }}'
    state: reconnect
  delegate_to: localhost

- name: Reconnect ESXi Host (with default username/password)
  vmware_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter_name
    cluster_name: cluster_name
    esxi_hostname: '{{ esxi_hostname }}'
    state: reconnect
  delegate_to: localhost

- name: Add ESXi Host with SSL Thumbprint to vCenter
  vmware_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter_name
    cluster_name: cluster_name
    esxi_hostname: '{{ esxi_hostname }}'
    esxi_username: '{{ esxi_username }}'
    esxi_password: '{{ esxi_password }}'
    esxi_ssl_thumbprint: "3C:A5:60:6F:7A:B7:C4:6C:48:28:3D:2F:A5:EC:A3:58:13:88:F6:DD"
    state: present
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Joseph Callen (@jcpowermac)', 'Russell Teague (@mtnbikenc)', 'Maxime de Roucy (@tchernomax)']
  - ['Joseph Callen (@jcpowermac)', 'Russell Teague (@mtnbikenc)', 'Maxime de Roucy (@tchernomax)']
  - ['Joseph Callen (@jcpowermac)', 'Russell Teague (@mtnbikenc)', 'Maxime de Roucy (@tchernomax)']
