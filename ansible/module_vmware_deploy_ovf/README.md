# Ansible module: ansible.module_vmware_deploy_ovf


Deploys a VMware virtual machine from an OVF or OVA file

## Description

This module can be used to deploy a VMware VM from an OVF or OVA file

## Requirements

TODO

## Arguments

``` json
{
    "allow_duplicates": "{'default': True, 'description': ['Whether or not to allow duplicate VM names. ESXi allows duplicates, vCenter may not.'], 'type': 'bool'}",
    "cluster": "{'description': ['Cluster to deploy to.']}",
    "datacenter": "{'default': 'ha-datacenter', 'description': ['Datacenter to deploy to.']}",
    "datastore": "{'default': 'datastore1', 'description': ['Datastore to deploy to.']}",
    "deployment_option": "{'description': ['The key of the chosen deployment option.']}",
    "disk_provisioning": "{'choices': ['flat', 'eagerZeroedThick', 'monolithicSparse', 'twoGbMaxExtentSparse', 'twoGbMaxExtentFlat', 'thin', 'sparse', 'thick', 'seSparse', 'monolithicFlat'], 'default': 'thin', 'description': ['Disk provisioning type.']}",
    "fail_on_spec_warnings": "{'description': ['Cause the module to treat OVF Import Spec warnings as errors.'], 'default': False, 'type': 'bool'}",
    "folder": "{'description': ['Absolute path of folder to place the virtual machine.', 'If not specified, defaults to the value of C(datacenter.vmFolder).']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "name": "{'description': ['Name of the VM to work with.', 'Virtual machine names in vCenter are not necessarily unique, which may be problematic.']}",
    "networks": "{'default': {'VM Network': 'VM Network'}, 'description': ['C(key: value) mapping of OVF network name, to the vCenter network name.']}",
    "ovf": "{'description': ['Path to OVF or OVA file to deploy.'], 'aliases': ['ova']}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "power_on": "{'default': True, 'description': ['Whether or not to power on the virtual machine after creation.'], 'type': 'bool'}",
    "properties": "{'description': ['The assignment of values to the properties found in the OVF as key value pairs.']}",
    "resource_pool": "{'default': 'Resources', 'description': ['Resource Pool to deploy to.']}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
    "wait": "{'default': True, 'description': ['Wait for the host to power on.'], 'type': 'bool'}",
    "wait_for_ip_address": "{'default': False, 'description': ['Wait until vCenter detects an IP address for the VM.', 'This requires vmware-tools (vmtoolsd) to properly work after creation.'], 'type': 'bool'}",
}
```

## Examples


``` yaml

- vmware_deploy_ovf:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    ovf: /path/to/ubuntu-16.04-amd64.ovf
    wait_for_ip_address: true
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Matt Martz (@sivel)']
