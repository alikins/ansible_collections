# Ansible module: ansible.module_clc_modify_server


modify servers in CenturyLink Cloud

## Description

An Ansible module to modify servers in CenturyLink Cloud.

## Requirements

TODO

## Arguments

``` json
{
    "alert_policy_id": "{'description': ["The alert policy id to be associated to the server. This is mutually exclusive with 'alert_policy_name'"]}",
    "alert_policy_name": "{'description': ["The alert policy name to be associated to the server. This is mutually exclusive with 'alert_policy_id'"]}",
    "anti_affinity_policy_id": "{'description': ["The anti affinity policy id to be set for a hyper scale server. This is mutually exclusive with 'anti_affinity_policy_name'"]}",
    "anti_affinity_policy_name": "{'description': ["The anti affinity policy name to be set for a hyper scale server. This is mutually exclusive with 'anti_affinity_policy_id'"]}",
    "cpu": "{'description': ['How many CPUs to update on the server']}",
    "memory": "{'description': ['Memory (in GB) to set to the server.']}",
    "server_ids": "{'description': ['A list of server Ids to modify.'], 'required': True}",
    "state": "{'description': ['The state to insure that the provided resources are in.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "wait": "{'description': ['Whether to wait for the provisioning tasks to finish before returning.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

# Note - You must set the CLC_V2_API_USERNAME And CLC_V2_API_PASSWD Environment variables before running these examples

- name: set the cpu count to 4 on a server
  clc_modify_server:
    server_ids:
        - UC1TESTSVR01
        - UC1TESTSVR02
    cpu: 4
    state: present

- name: set the memory to 8GB on a server
  clc_modify_server:
    server_ids:
        - UC1TESTSVR01
        - UC1TESTSVR02
    memory: 8
    state: present

- name: set the anti affinity policy on a server
  clc_modify_server:
    server_ids:
        - UC1TESTSVR01
        - UC1TESTSVR02
    anti_affinity_policy_name: 'aa_policy'
    state: present

- name: remove the anti affinity policy on a server
  clc_modify_server:
    server_ids:
        - UC1TESTSVR01
        - UC1TESTSVR02
    anti_affinity_policy_name: 'aa_policy'
    state: absent

- name: add the alert policy on a server
  clc_modify_server:
    server_ids:
        - UC1TESTSVR01
        - UC1TESTSVR02
    alert_policy_name: 'alert_policy'
    state: present

- name: remove the alert policy on a server
  clc_modify_server:
    server_ids:
        - UC1TESTSVR01
        - UC1TESTSVR02
    alert_policy_name: 'alert_policy'
    state: absent

- name: set the memory to 16GB and cpu to 8 core on a lust if servers
  clc_modify_server:
    server_ids:
        - UC1TESTSVR01
        - UC1TESTSVR02
    cpu: 8
    memory: 16
    state: present

```

## License

TODO

## Author Information
  - ['CLC Runner (@clc-runner)']
