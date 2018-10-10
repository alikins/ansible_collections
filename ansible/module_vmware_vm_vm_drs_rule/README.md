# Ansible module: ansible.module_vmware_vm_vm_drs_rule


Configure VMware DRS Affinity rule for virtual machine in given cluster

## Description

This module can be used to configure VMware DRS Affinity rule for virtual machine in given cluster.

## Requirements

TODO

## Arguments

``` json
{
    "affinity_rule": "{'description': ['If set to C(True), the DRS rule will be an Affinity rule.', 'If set to C(False), the DRS rule will be an Anti-Affinity rule.', 'Effective only if C(state) is set to C(present).'], 'default': True, 'type': 'bool'}",
    "cluster_name": "{'description': ['Desired cluster name where virtual machines are present for the DRS rule.'], 'required': True}",
    "drs_rule_name": "{'description': ['The name of the DRS rule to manage.'], 'required': True}",
    "enabled": "{'description': ['If set to C(True), the DRS rule will be enabled.', 'Effective only if C(state) is set to C(present).'], 'default': False, 'type': 'bool'}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "mandatory": "{'description': ['If set to C(True), the DRS rule will be mandatory.', 'Effective only if C(state) is set to C(present).'], 'default': False, 'type': 'bool'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['If set to C(present), then the DRS rule is created if not present.', 'If set to C(present), then the DRS rule is deleted and created if present already.', 'If set to C(absent), then the DRS rule is deleted if present.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
    "vms": "{'description': ['List of virtual machines name for which DRS rule needs to be applied.', 'Required if C(state) is set to C(present).']}",
}
```

## Examples


``` yaml

- name: Create DRS Affinity Rule for VM-VM
  vmware_vm_vm_drs_rule:
    hostname: "{{ esxi_server }}"
    username: "{{ esxi_username }}"
    password: "{{ esxi_password }}"
    cluster_name: "{{ cluster_name }}"
    validate_certs: no
    vms:
        - vm1
        - vm2
    drs_rule_name: vm1-vm2-affinity-rule-001
    enabled: True
    mandatory: True
    affinity_rule: True
  delegate_to: localhost

- name: Create DRS Anti-Affinity Rule for VM-VM
  vmware_vm_vm_drs_rule:
    hostname: "{{ esxi_server }}"
    username: "{{ esxi_username }}"
    password: "{{ esxi_password }}"
    cluster_name: "{{ cluster_name }}"
    validate_certs: no
    vms:
        - vm1
        - vm2
    drs_rule_name: vm1-vm2-affinity-rule-001
    enabled: True
    mandatory: True
    affinity_rule: False
  delegate_to: localhost

- name: Delete DRS Affinity Rule for VM-VM
  vmware_vm_vm_drs_rule:
    hostname: "{{ esxi_server }}"
    username: "{{ esxi_username }}"
    password: "{{ esxi_password }}"
    cluster_name: "{{ cluster_name }}"
    validate_certs: no
    drs_rule_name: vm1-vm2-affinity-rule-001
    state: absent
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
