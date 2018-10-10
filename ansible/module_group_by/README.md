# Ansible module: ansible.module_group_by


Create Ansible groups based on facts

## Description

Use facts to create ad-hoc groups that can be used later in a playbook.
This module is also supported for Windows targets.

## Requirements

TODO

## Arguments

``` json
{
    "key": "{'description': ['The variables whose values will be used as groups'], 'required': True}",
    "parents": "{'description': ['The list of the parent groups'], 'required': False, 'default': 'all', 'version_added': '2.4'}",
}
```

## Examples


``` yaml

# Create groups based on the machine architecture
- group_by:
    key: machine_{{ ansible_machine }}

# Create groups like 'virt_kvm_host'
- group_by:
    key: virt_{{ ansible_virtualization_type }}_{{ ansible_virtualization_role }}

# Create nested groups
- group_by:
    key: el{{ ansible_distribution_major_version }}-{{ ansible_architecture }}
    parents:
      - el{{ ansible_distribution_major_version }}


```

## License

TODO

## Author Information
  - ['Jeroen Hoekx (@jhoekx)']
