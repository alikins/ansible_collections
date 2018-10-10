# Ansible module: ansible.module_cnos_vlag


Manage VLAG resources and attributes on devices running Lenovo CNOS

## Description

This module allows you to work with virtual Link Aggregation Groups (vLAG) related configurations. The operators used are overloaded to ensure control over switch vLAG configurations. Apart from the regular device connection related attributes, there are four vLAG arguments which are overloaded variables that will perform further configurations. They are vlagArg1, vlagArg2, vlagArg3, and vlagArg4. For more details on how to use these arguments, see [Overloaded Variables]. This module uses SSH to manage network device configuration. The results of the operation will be placed in a directory named 'results' that must be created by the user in their local directory to where the playbook is run. For more information about this module from Lenovo and customizing it usage for your use cases, please visit U(http://systemx.lenovofiles.com/help/index.jsp?topic=%2Fcom.lenovo.switchmgt.ansible.doc%2Fcnos_vlag.html)

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
    "vlagArg1": "{'description': ['This is an overloaded vlag first argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': True, 'default': None, 'choices': ['enable', 'auto-recovery', 'config-consistency', 'isl', 'mac-address-table', 'peer-gateway', 'priority', 'startup-delay', 'tier-id', 'vrrp', 'instance', 'hlthchk']}",
    "vlagArg2": "{'description': ['This is an overloaded vlag second argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': False, 'default': None, 'choices': ['Interval in seconds', 'disable or strict', 'Port Aggregation Number', 'VLAG priority', 'Delay time in seconds', 'VLAG tier-id value', 'VLAG instance number', 'keepalive-attempts', 'keepalive-interval', 'retry-interval', 'peer-ip']}",
    "vlagArg3": "{'description': ['This is an overloaded vlag third argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': False, 'default': None, 'choices': ['enable or port-aggregation', 'Number of keepalive attempts', 'Interval in seconds', 'Interval in seconds', 'VLAG health check peer IP4 address']}",
    "vlagArg4": "{'description': ['This is an overloaded vlag fourth argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': False, 'default': None, 'choices': ['Port Aggregation Number', 'default or management']}",
}
```

## Examples


``` yaml


Tasks : The following are examples of using the module cnos_vlag. These are
        written in the main.yml file of the tasks directory.
---
- name: Test Vlag  - enable
  cnos_vlag:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user']}}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass']}}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "enable"

- name: Test Vlag - autorecovery
  cnos_vlag:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user']}}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass']}}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "auto-recovery"
      vlagArg2: 266

- name: Test Vlag - config-consistency
  cnos_vlag:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user']}}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass']}}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "config-consistency"
      vlagArg2: "strict"

- name: Test Vlag - isl
  cnos_vlag:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user']}}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass']}}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "isl"
      vlagArg2: 23

- name: Test Vlag  - mac-address-table
  cnos_vlag:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user']}}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass']}}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "mac-address-table"

- name: Test Vlag - peer-gateway
  cnos_vlag:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user']}}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass']}}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "peer-gateway"

- name: Test Vlag - priority
  cnos_vlag:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user']}}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass']}}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "priority"
      vlagArg2: 1313

- name: Test Vlag - startup-delay
  cnos_vlag:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user']}}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass']}}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "startup-delay"
      vlagArg2: 323

- name: Test Vlag  - tier-id
  cnos_vlag:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user']}}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass']}}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "tier-id"
      vlagArg2: 313

- name: Test Vlag - vrrp
  cnos_vlag:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user']}}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass']}}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "vrrp"

- name: Test Vlag - instance
  cnos_vlag:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user']}}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass']}}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "instance"
      vlagArg2: 33
      vlagArg3: 333

- name: Test Vlag - instance2
  cnos_vlag:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user']}}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass']}}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "instance"
      vlagArg2: "33"

- name: Test Vlag  - keepalive-attempts
  cnos_vlag:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user']}}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass']}}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "hlthchk"
      vlagArg2: "keepalive-attempts"
      vlagArg3: 13

- name: Test Vlag - keepalive-interval
  cnos_vlag:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user']}}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass']}}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "hlthchk"
      vlagArg2: "keepalive-interval"
      vlagArg3: 131

- name: Test Vlag - retry-interval
  cnos_vlag:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user']}}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass']}}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "hlthchk"
      vlagArg2: "retry-interval"
      vlagArg3: 133

- name: Test Vlag - peer ip
  cnos_vlag:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user']}}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass']}}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType']}}"
      outputfile: "./results/cnos_vlag_{{ inventory_hostname }}_output.txt"
      vlagArg1: "hlthchk"
      vlagArg2: "peer-ip"
      vlagArg3: "1.2.3.4"


```

## License

TODO

## Author Information
  - ['Anil Kumar Muraleedharan (@amuraleedhar)']
