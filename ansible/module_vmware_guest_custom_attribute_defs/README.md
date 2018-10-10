# Ansible module: ansible.module_vmware_guest_custom_attribute_defs


Manage custom attributes definitions for virtual machine from VMWare

## Description

This module can be used to add and remove custom attributes definitions for the given virtual machine from VMWare.

## Requirements

TODO

## Arguments

``` json
{
    "attribute_key": "{'description': ['Name of the custom attribute definition.', 'This is required parameter, if C(state) is set to C(present) or C(absent).'], 'required': False}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['Manage definition of custom attributes.', 'If set to C(present) and definition not present, then custom attribute definition is created.', 'If set to C(present) and definition is present, then no action taken.', 'If set to C(absent) and definition is present, then custom attribute definition is removed.', 'If set to C(absent) and definition is absent, then no action taken.'], 'default': 'present', 'choices': ['present', 'absent'], 'required': True}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Add VMWare Attribute Definition
  vmware_guest_custom_attribute_defs:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    state: present
    attribute_key: custom_attr_def_1
  delegate_to: localhost
  register: defs

- name: Remove VMWare Attribute Definition
  vmware_guest_custom_attribute_defs:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    state: absent
    attribute_key: custom_attr_def_1
  delegate_to: localhost
  register: defs

```

## License

TODO

## Author Information
  - ['Jimmy Conner', 'Abhijeet Kasurde (@Akasurde)']
  - ['Jimmy Conner', 'Abhijeet Kasurde (@Akasurde)']
