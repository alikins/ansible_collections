# Ansible module: ansible.module_cnos_vlan


Manage VLAN resources and attributes on devices running Lenovo CNOS

## Description

This module allows you to work with VLAN related configurations. The operators used are overloaded to ensure control over switch VLAN configurations. The first level of VLAN configuration allows to set up the VLAN range, the VLAN tag persistence, a VLAN access map and access map filter. After passing this level, there are five VLAN arguments that will perform further configurations. They are vlanArg1, vlanArg2, vlanArg3, vlanArg4, and vlanArg5. The value of vlanArg1 will determine the way following arguments will be evaluated. This module uses SSH to manage network device configuration. The results of the operation will be placed in a directory named 'results' that must be created by the user in their local directory to where the playbook is run. For more information about this module from Lenovo and customizing it usage for your use cases, please visit U(http://systemx.lenovofiles.com/help/index.jsp?topic=%2Fcom.lenovo.switchmgt.ansible.doc%2Fcnos_vlan.html)

## Requirements

TODO

## Arguments

``` json
{
    "deviceType": "{'description': ['This specifies the type of device where the method is executed. The choices NE1072T,NE1032,NE1032T,NE10032, NE2572 are added since version 2.4'], 'required': True, 'choices': ['g8272_cnos', 'g8296_cnos', 'g8332_cnos', 'NE1072T', 'NE1032', 'NE1032T', 'NE10032', 'NE2572'], 'version_added': 2.3}",
    "enablePassword": "{'description': ['Configures the password used to enter Global Configuration command mode on the switch. If the switch does not request this password, the parameter is ignored.While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'version_added': 2.3}",
    "host": "{'description': ['This is the variable used to search the hosts file at /etc/ansible/hosts and identify the IP address of the device on which the template is going to be applied. Usually the Ansible keyword {{ inventory_hostname }} is specified in the playbook as an abstraction of the group of network elements that need to be configured.'], 'required': True, 'version_added': 2.3}",
    "outputfile": "{'description': ['This specifies the file path where the output of each command execution is saved. Each command that is specified in the merged template file and each response from the device are saved here. Usually the location is the results folder, but you can choose another location based on your write permission.'], 'required': True, 'version_added': 2.3}",
    "password": "{'description': ['Configures the password used to authenticate the connection to the remote device. The value of the password parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'required': True, 'version_added': 2.3}",
    "username": "{'description': ['Configures the username used to authenticate the connection to the remote device. The value of the username parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'required': True, 'version_added': 2.3}",
    "vlanArg1": "{'description': ['This is an overloaded vlan first argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': True, 'choices': ['access-map', 'dot1q', 'filter', '<1-3999> VLAN ID 1-3999 or range']}",
    "vlanArg2": "{'description': ['This is an overloaded vlan second argument. Usage of this argument can be found is the User Guide referenced above.'], 'choices': ['VLAN Access Map name', 'egress-only', 'name', 'flood', 'state', 'ip']}",
    "vlanArg3": "{'description': ['This is an overloaded vlan third argument. Usage of this argument can be found is the User Guide referenced above.'], 'choices': ['action', 'match', 'statistics', 'enter VLAN id or range of vlan', 'ascii name for the VLAN', 'ipv4 or ipv6', 'active or suspend', 'fast-leave', 'last-member-query-interval', 'mrouter', 'querier', 'querier-timeout', 'query-interval', 'query-max-response-time', 'report-suppression', 'robustness-variable', 'startup-query-count', 'startup-query-interval', 'static-group']}",
    "vlanArg4": "{'description': ['This is an overloaded vlan fourth argument. Usage of this argument can be found is the User Guide referenced above.'], 'choices': ['drop or forward or redirect', 'ip or mac', 'Interval in seconds', 'ethernet', 'port-aggregation', 'Querier IP address', 'Querier Timeout in seconds', 'Query Interval in seconds', 'Query Max Response Time in seconds', 'Robustness Variable value', 'Number of queries sent at startup', 'Query Interval at startup']}",
    "vlanArg5": "{'description': ['This is an overloaded vlan fifth argument. Usage of this argument can be found is the User Guide referenced above.'], 'choices': ['access-list name', 'Slot/chassis number', 'Port Aggregation Number']}",
}
```

## Examples


``` yaml


Tasks: The following are examples of using the module cnos_vlan. These are
       written in the main.yml file of the tasks directory.
---
- name: Test Vlan - Create a vlan, name it
  cnos_vlan:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_vlan_{{ inventory_hostname }}_output.txt"
      vlanArg1: 13
      vlanArg2: "name"
      vlanArg3: "Anil"

- name: Test Vlan - Create a vlan, Flood configuration
  cnos_vlan:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_vlan_{{ inventory_hostname }}_output.txt"
      vlanArg1: 13
      vlanArg2: "flood"
      vlanArg3: "ipv4"

- name: Test Vlan - Create a vlan, State configuration
  cnos_vlan:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_vlan_{{ inventory_hostname }}_output.txt"
      vlanArg1: 13
      vlanArg2: "state"
      vlanArg3: "active"

- name: Test Vlan - VLAN Access map1
  cnos_vlan:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_vlan_{{ inventory_hostname }}_output.txt"
      vlanArg1: "access-map"
      vlanArg2: "Anil"
      vlanArg3: "statistics"

- name: Test Vlan - VLAN Accep Map2
  cnos_vlan:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_vlan_{{ inventory_hostname }}_output.txt"
      vlanArg1: "access-map"
      vlanArg2: "Anil"
      vlanArg3: "action"
      vlanArg4: "forward"

- name: Test Vlan - ip igmp snooping query interval
  cnos_vlan:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_vlan_{{ inventory_hostname }}_output.txt"
      vlanArg1: 13
      vlanArg2: "ip"
      vlanArg3: "query-interval"
      vlanArg4: 1313

- name: Test Vlan - ip igmp snooping mrouter interface port-aggregation 23
  cnos_vlan:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_vlan_{{ inventory_hostname }}_output.txt"
      vlanArg1: 13
      vlanArg2: "ip"
      vlanArg3: "mrouter"
      vlanArg4: "port-aggregation"
      vlanArg5: 23


```

## License

TODO

## Author Information
  - ['Anil Kumar Muraleedharan (@amuraleedhar)']
