# Ansible module: ansible.module_cnos_conditional_template


Manage switch configuration using templates based on condition on devices running Lenovo CNOS

## Description

This module allows you to work with the running configuration of a switch. It provides a way to execute a set of CNOS commands on a switch by evaluating the current running configuration and executing the commands only if the specific settings have not been already configured. The configuration source can be a set of commands or a template written in the Jinja2 templating language. This module functions the same as the cnos_template module. The only exception is that the following inventory variable can be specified. ["condition = <flag string>"] When this inventory variable is specified as the variable of a task, the template is executed for the network element that matches the flag string. Usually, templates are used when commands are the same across a group of network devices. When there is a requirement to skip the execution of the template on one or more devices, it is recommended to use this module. This module uses SSH to manage network device configuration. For more information about this module and customizing it usage for your use cases, please visit U(http://systemx.lenovofiles.com/help/index.jsp?topic= %2Fcom.lenovo.switchmgt.ansible.doc%2Fcnos_conditional_template.html)

## Requirements

TODO

## Arguments

``` json
{
    "commandfile": "{'description': ['This specifies the path to the CNOS command file which needs to be applied. This usually comes from the commands folder. Generally this file is the output of the variables applied on a template file. So this command is preceded by a template module. The command file must contain the Ansible keyword {{ inventory_hostname }} and the condition flag in its filename to ensure that the command file is unique for each switch and condition. If this is omitted, the command file will be overwritten during iteration. For example, commandfile=./commands/clos_leaf_bgp_ {{ inventory_hostname }}_LP21_commands.txt'], 'required': True, 'default': None}",
    "condition": "{'description': ['If you specify condition=<flag string> in the inventory file against any device, the template execution is done for that device in case it matches the flag setting for that task.'], 'required': True, 'default': None}",
    "deviceType": "{'description': ['This specifies the type of device where the method is executed. The choices NE1072T,NE1032,NE1032T,NE10032, NE2572 are added since version 2.4'], 'required': True, 'choices': ['g8272_cnos', 'g8296_cnos', 'g8332_cnos', 'NE1072T', 'NE1032', 'NE1032T', 'NE10032', 'NE2572'], 'version_added': 2.3}",
    "enablePassword": "{'description': ['Configures the password used to enter Global Configuration command mode on the switch. If the switch does not request this password, the parameter is ignored.While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'version_added': 2.3}",
    "flag": "{'description': ['If a task needs to be executed, you have to set the flag the same as it is specified in the inventory for that device.'], 'required': True, 'default': None}",
    "host": "{'description': ['This is the variable used to search the hosts file at /etc/ansible/hosts and identify the IP address of the device on which the template is going to be applied. Usually the Ansible keyword {{ inventory_hostname }} is specified in the playbook as an abstraction of the group of network elements that need to be configured.'], 'required': True, 'version_added': 2.3}",
    "outputfile": "{'description': ['This specifies the file path where the output of each command execution is saved. Each command that is specified in the merged template file and each response from the device are saved here. Usually the location is the results folder, but you can choose another location based on your write permission.'], 'required': True, 'version_added': 2.3}",
    "password": "{'description': ['Configures the password used to authenticate the connection to the remote device. The value of the password parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'required': True, 'version_added': 2.3}",
    "username": "{'description': ['Configures the username used to authenticate the connection to the remote device. The value of the username parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'required': True, 'version_added': 2.3}",
}
```

## Examples


``` yaml

Tasks : The following are examples of using the module
 cnos_conditional_template. These are written in the main.yml file of the
 tasks directory.
---
- name: Applying CLI template on VLAG Tier1 Leaf Switch1
  cnos_conditional_template:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      outputfile: "./results/vlag_1tier_leaf_switch1_
                  {{ inventory_hostname }}_output.txt"
      condition: "{{ hostvars[inventory_hostname]['condition']}}"
      flag: "leaf_switch1"
      commandfile: "./commands/vlag_1tier_leaf_switch1_
                    {{ inventory_hostname }}_commands.txt"
      enablePassword: "anil"
      stp_mode1: "disable"
      port_range1: "17,18,29,30"
      portchannel_interface_number1: 1001
      portchannel_mode1: active
      slot_chassis_number1: 1/48
      switchport_mode1: trunk

```

## License

TODO

## Author Information
  - ['Anil Kumar Muraleedharan (@amuraleedhar)']
