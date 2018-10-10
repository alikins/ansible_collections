# Ansible module: ansible.module_vmware_vm_facts


Return basic facts pertaining to a vSphere virtual machine guest

## Description

Return basic facts pertaining to a vSphere virtual machine guest.
Cluster name as fact is added in version 2.7.

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
    "vm_type": "{'description': ['If set to C(vm), then facts are gathered for virtual machines only.', 'If set to C(template), then facts are gathered for virtual machine templates only.', 'If set to C(all), then facts are gathered for all virtual machines and virtual machine templates.'], 'required': False, 'default': 'all', 'choices': ['all', 'vm', 'template'], 'version_added': 2.5}",
}
```

## Examples


``` yaml

- name: Gather all registered virtual machines
  vmware_vm_facts:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
  delegate_to: localhost
  register: vmfacts

- debug:
    var: vmfacts.virtual_machines

- name: Gather only registered virtual machine templates
  vmware_vm_facts:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    vm_type: template
  delegate_to: localhost
  register: template_facts

- debug:
    var: template_facts.virtual_machines

- name: Gather only registered virtual machines
  vmware_vm_facts:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    vm_type: vm
  delegate_to: localhost
  register: vm_facts

- debug:
    var: vm_facts.virtual_machines

```

## License

TODO

## Author Information
  - ['Joseph Callen (@jcpowermac)', 'Abhijeet Kasurde (@Akasurde)']
  - ['Joseph Callen (@jcpowermac)', 'Abhijeet Kasurde (@Akasurde)']
