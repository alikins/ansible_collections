# Ansible module: ansible.module_clc_firewall_policy


Create/delete/update firewall policies

## Description

Create or delete or update firewall polices on Centurylink Cloud

## Requirements

TODO

## Arguments

``` json
{
    "destination": "{'description': ["The list of destination addresses for traffic on the terminating firewall. This is required when state is 'present'"]}",
    "destination_account_alias": "{'description': ['CLC alias for the destination account']}",
    "enabled": "{'description': ['Whether the firewall policy is enabled or disabled'], 'choices': [True, False], 'default': 'yes'}",
    "firewall_policy_id": "{'description': ['Id of the firewall policy. This is required to update or delete an existing firewall policy']}",
    "location": "{'description': ['Target datacenter for the firewall policy'], 'required': True}",
    "ports": "{'description': ['The list of ports associated with the policy. TCP and UDP can take in single ports or port ranges.'], 'choices': ['any', 'icmp', 'TCP/123', 'UDP/123', 'TCP/123-456', 'UDP/123-456']}",
    "source": "{'description': ["The list  of source addresses for traffic on the originating firewall. This is required when state is 'present'"]}",
    "source_account_alias": "{'description': ['CLC alias for the source account'], 'required': True}",
    "state": "{'description': ['Whether to create or delete the firewall policy'], 'default': 'present', 'choices': ['present', 'absent']}",
    "wait": "{'description': ['Whether to wait for the provisioning tasks to finish before returning.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

---
- name: Create Firewall Policy
  hosts: localhost
  gather_facts: False
  connection: local
  tasks:
    - name: Create / Verify an Firewall Policy at CenturyLink Cloud
      clc_firewall:
        source_account_alias: WFAD
        location: VA1
        state: present
        source: 10.128.216.0/24
        destination: 10.128.216.0/24
        ports: Any
        destination_account_alias: WFAD

---
- name: Delete Firewall Policy
  hosts: localhost
  gather_facts: False
  connection: local
  tasks:
    - name: Delete an Firewall Policy at CenturyLink Cloud
      clc_firewall:
        source_account_alias: WFAD
        location: VA1
        state: absent
        firewall_policy_id: c62105233d7a4231bd2e91b9c791e43e1

```

## License

TODO

## Author Information
  - ['CLC Runner (@clc-runner)']
