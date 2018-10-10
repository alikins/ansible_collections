# Ansible module: ansible.module_vmware_category


Manage VMware categories

## Description

This module can be used to create / delete / update VMware categories.
Tag feature is introduced in vSphere 6 version, so this module is not supported in the earlier versions of vSphere.
All variables and VMware object names are case sensitive.

## Requirements

TODO

## Arguments

``` json
{
    "category_cardinality": "{'description': ['The category cardinality.', 'This parameter is ignored, when updating existing category.'], 'choices': ['multiple', 'single'], 'default': 'multiple'}",
    "category_description": "{'description': ['The category description.', 'This is required only if C(state) is set to C(present).', 'This parameter is ignored, when C(state) is set to C(absent).'], 'default': ''}",
    "category_name": "{'description': ['The name of category to manage.'], 'required': True}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.'], 'required': False}",
    "new_category_name": "{'description': ['The new name for an existing category.', 'This value is used while updating an existing category.']}",
    "password": "{'description': ['The password of the vSphere vCenter server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.'], 'required': False, 'aliases': ['pass', 'pwd']}",
    "protocol": "{'description': ['The connection to protocol.'], 'choices': ['https', 'http'], 'default': 'https', 'required': False}",
    "state": "{'description': ['The state of category.', 'If set to C(present) and category does not exists, then category is created.', 'If set to C(present) and category exists, then category is updated.', 'If set to C(absent) and category exists, then category is deleted.', 'If set to C(absent) and category does not exists, no action is taken.', 'Process of updating category only allows name, description change.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "username": "{'description': ['The username of the vSphere vCenter server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.'], 'aliases': ['user', 'admin']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.'], 'default': True, 'type': 'bool', 'required': False}",
}
```

## Examples


``` yaml

- name: Create a category
  vmware_category:
    hostname: "{{ vcenter_server }}"
    username: "{{ vcenter_user }}"
    password: "{{ vcenter_pass }}"
    category_name: Sample_Cat_0001
    category_description: Sample Description
    category_cardinality: 'multiple'
    state: present

- name: Rename category
  vmware_category:
    hostname: "{{ vcenter_server }}"
    username: "{{ vcenter_user }}"
    password: "{{ vcenter_pass }}"
    category_name: Sample_Category_0001
    new_category_name: Sample_Category_0002
    state: present

- name: Update category description
  vmware_category:
    hostname: "{{ vcenter_server }}"
    username: "{{ vcenter_user }}"
    password: "{{ vcenter_pass }}"
    category_name: Sample_Category_0001
    category_description: Some fancy description
    state: present

- name: Delete category
  vmware_category:
    hostname: "{{ vcenter_server }}"
    username: "{{ vcenter_user }}"
    password: "{{ vcenter_pass }}"
    category_name: Sample_Category_0002
    state: absent

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
