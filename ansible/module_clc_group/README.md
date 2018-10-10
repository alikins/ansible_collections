# Ansible module: ansible.module_clc_group


Create/delete Server Groups at Centurylink Cloud

## Description

Create or delete Server Groups at Centurylink Centurylink Cloud

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['A description of the Server Group'], 'required': False}",
    "location": "{'description': ['Datacenter to create the group in. If location is not provided, the group gets created in the default datacenter associated with the account'], 'required': False}",
    "name": "{'description': ['The name of the Server Group'], 'required': True}",
    "parent": "{'description': ['The parent group of the server group. If parent is not provided, it creates the group at top level.'], 'required': False}",
    "state": "{'description': ['Whether to create or delete the group'], 'default': 'present', 'choices': ['present', 'absent']}",
    "wait": "{'description': ['Whether to wait for the tasks to finish before returning.'], 'type': 'bool', 'default': True, 'required': False}",
}
```

## Examples


``` yaml


# Create a Server Group

---
- name: Create Server Group
  hosts: localhost
  gather_facts: False
  connection: local
  tasks:
    - name: Create / Verify a Server Group at CenturyLink Cloud
      clc_group:
        name: My Cool Server Group
        parent: Default Group
        state: present
      register: clc

    - name: debug
      debug:
        var: clc

# Delete a Server Group

---
- name: Delete Server Group
  hosts: localhost
  gather_facts: False
  connection: local
  tasks:
    - name: Delete / Verify Absent a Server Group at CenturyLink Cloud
      clc_group:
        name: My Cool Server Group
        parent: Default Group
        state: absent
      register: clc

    - name: debug
      debug:
        var: clc

```

## License

TODO

## Author Information
  - ['CLC Runner (@clc-runner)']
