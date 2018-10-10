# Ansible module: ansible.module_vmware_category_facts


Gather facts about VMware tag categories

## Description

This module can be used to gather facts about VMware tag categories.
Tag feature is introduced in vSphere 6 version, so this module is not supported in earlier versions of vSphere.
All variables and VMware object names are case sensitive.

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.'], 'required': False}",
    "password": "{'description': ['The password of the vSphere vCenter server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.'], 'required': False, 'aliases': ['pass', 'pwd']}",
    "protocol": "{'description': ['The connection to protocol.'], 'choices': ['https', 'http'], 'default': 'https', 'required': False}",
    "username": "{'description': ['The username of the vSphere vCenter server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.'], 'aliases': ['user', 'admin']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.'], 'default': True, 'type': 'bool', 'required': False}",
}
```

## Examples


``` yaml

- name: Gather facts about tag categories
  vmware_category_facts:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
  delegate_to: localhost
  register: all_tag_category_facts

- name: Gather category id from given tag category
  vmware_category_facts:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
  delegate_to: localhost
  register: tag_category_results

- set_fact:
    category_id: "{{ item.category_id }}"
  with_items: "{{ tag_category_results.tag_category_facts|json_query(query) }}"
  vars:
    query: "[?category_name==`Category0001`]"
- debug: var=category_id


```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
