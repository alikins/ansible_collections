# Ansible module: ansible.module_vca_vapp


Manages vCloud Air vApp instances

## Description

This module will actively managed vCloud Air vApp instances.  Instances can be created and deleted as well as both deployed and undeployed.

## Requirements

TODO

## Arguments

``` json
{
    "api_version": "{'description': ['The api version to be used with the vca'], 'default': '5.7'}",
    "gateway_name": "{'description': ['The name of the gateway of the vdc where the rule should be added.'], 'default': 'gateway'}",
    "host": "{'description': ['The authentication host to be used when service type  is vcd.']}",
    "instance_id": "{'description': ['The instance id in a vchs environment to be used for creating the vapp']}",
    "network_mode": "{'description': ['Configures the mode of the network connection.'], 'default': 'pool', 'choices': ['pool', 'dhcp', 'static']}",
    "network_name": "{'description': ["The name of the network that should be attached to the virtual machine in the vApp.  The virtual network specified must already be created in the vCloud Air VDC.  If the I(state) is not 'absent' then the I(network_name) argument must be provided."]}",
    "operation": "{'description': ['Specifies an operation to be performed on the vApp.'], 'default': 'noop', 'choices': ['noop', 'poweron', 'poweroff', 'suspend', 'shutdown', 'reboot', 'reset']}",
    "org": "{'description': ['The org to login to for creating vapp, mostly set when the service_type is vdc.']}",
    "password": "{'description': ['The vCloud Air password to use during authentication'], 'aliases': ['pass', 'passwd']}",
    "service_type": "{'description': ['The type of service we are authenticating against'], 'default': 'vca', 'choices': ['vca', 'vchs', 'vcd']}",
    "state": "{'description': ['Configures the state of the vApp.'], 'default': 'present', 'choices': ['present', 'absent', 'deployed', 'undeployed']}",
    "template_name": "{'description': ['The name of the vApp template to use to create the vApp instance.  If the I(state) is not `absent` then the I(template_name) value must be provided.  The I(template_name) must be previously uploaded to the catalog specified by I(catalog_name)']}",
    "username": "{'description': ['The vCloud Air username to use during authentication'], 'aliases': ['user']}",
    "vapp_name": "{'description': ['The name of the vCloud Air vApp instance'], 'required': True}",
    "vdc_name": "{'description': ['The name of the virtual data center (VDC) where the vm should be created or contains the vAPP.']}",
    "verify_certs": "{'description': ['If the certificates of the authentication is to be verified.'], 'type': 'bool', 'default': True}",
    "vm_cpus": "{'description': ['The number of vCPUs to configure for the VM in the vApp.   If the I(vm_name) argument is provided, then this becomes a per VM setting otherwise it is applied to all VMs in the vApp.']}",
    "vm_memory": "{'description': ['The amount of memory in MB to allocate to VMs in the vApp.  If the I(vm_name) argument is provided, then this becomes a per VM setting otherise it is applied to all VMs in the vApp.']}",
    "vm_name": "{'description': ['The name of the virtual machine instance in the vApp to manage.']}",
}
```

## Examples


``` yaml

- name: Creates a new vApp in a VCA instance
  vca_vapp:
    vapp_name: tower
    state: present
    template_name: 'Ubuntu Server 12.04 LTS (amd64 20150127)'
    vdc_name: VDC1
    instance_id: '<your instance id here>'
    username: '<your username here>'
    password: '<your password here>'
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip)']
