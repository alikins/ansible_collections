# Ansible module: ansible.module_clc_aa_policy


Create or Delete Anti Affinity Policies at CenturyLink Cloud

## Description

An Ansible module to Create or Delete Anti Affinity Policies at CenturyLink Cloud.

## Requirements

TODO

## Arguments

``` json
{
    "location": "{'description': ['Datacenter in which the policy lives/should live.'], 'required': True}",
    "name": "{'description': ['The name of the Anti Affinity Policy.'], 'required': True}",
    "state": "{'description': ['Whether to create or delete the policy.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "wait": "{'description': ['Whether to wait for the tasks to finish before returning.'], 'default': True, 'required': False, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Note - You must set the CLC_V2_API_USERNAME And CLC_V2_API_PASSWD Environment variables before running these examples

---
- name: Create AA Policy
  hosts: localhost
  gather_facts: False
  connection: local
  tasks:
    - name: Create an Anti Affinity Policy
      clc_aa_policy:
        name: Hammer Time
        location: UK3
        state: present
      register: policy

    - name: debug
      debug:
        var: policy

---
- name: Delete AA Policy
  hosts: localhost
  gather_facts: False
  connection: local
  tasks:
    - name: Delete an Anti Affinity Policy
      clc_aa_policy:
        name: Hammer Time
        location: UK3
        state: absent
      register: policy

    - name: debug
      debug:
        var: policy

```

## License

TODO

## Author Information
  - ['CLC Runner (@clc-runner)']
