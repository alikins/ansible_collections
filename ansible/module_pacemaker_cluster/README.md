# Ansible module: ansible.module_pacemaker_cluster


Manage pacemaker clusters

## Description

This module can manage a pacemaker cluster and nodes from Ansible using the pacemaker cli.

## Requirements

TODO

## Arguments

``` json
{
    "force": "{'description': ['Force the change of the cluster state'], 'type': 'bool', 'default': True}",
    "node": "{'description': ["Specify which node of the cluster you want to manage. None == the cluster status itself, 'all' == check the status of all nodes."]}",
    "state": "{'description': ['Indicate desired state of the cluster'], 'choices': ['cleanup', 'offline', 'online', 'restart'], 'required': True}",
    "timeout": "{'description': ['Timeout when the module should considered that the action has failed'], 'default': 300}",
}
```

## Examples


``` yaml

---
- name: Set cluster Online
  hosts: localhost
  gather_facts: no
  tasks:
  - name: Get cluster state
    pacemaker_cluster:
      state: online

```

## License

TODO

## Author Information
  - ['Mathieu Bultel (@matbu)']
