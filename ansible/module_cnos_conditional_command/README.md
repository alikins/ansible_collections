# Ansible module: ansible.module_cnos_conditional_command


Execute a single command based on condition on devices running Lenovo CNOS

## Description

This module allows you to modify the running configuration of a switch. It provides a way to execute a single CNOS command on a network device by evaluating the current running configuration and executing the command only if the specific settings have not been already configured. The CNOS command is passed as an argument of the method. This module functions the same as the cnos_command module. The only exception is that following inventory variable can be specified ["condition = <flag string>"] When this inventory variable is specified as the variable of a task, the command is executed for the network element that matches the flag string. Usually, commands are executed across a group of network devices. When there is a requirement to skip the execution of the command on one or more devices, it is recommended to use this module. This module uses SSH to manage network device configuration. For more information about this module from Lenovo and customizing it usage for your use cases, please visit U(http://systemx.lenovofiles.com/help/index.jsp?topic=%2Fcom.lenovo.switchmgt.ansible.doc%2Fcnos_conditional_command.html)

## Requirements

TODO

## Arguments

``` json
{
    "clicommand": "{'description': ['This specifies the CLI command as an attribute to this method. The command is passed using double quotes. The variables can be placed directly on to the CLI commands or can be invoked from the vars directory.'], 'required': True, 'default': None}",
    "condition": "{'description': ['If you specify condition=false in the inventory file against any device, the command execution is skipped for that device.'], 'required': True, 'default': None}",
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
 cnos_conditional_command. These are written in the main.yml file of the tasks
 directory.
---
- name: Applying CLI template on VLAG Tier1 Leaf Switch1
  cnos_conditional_command:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_conditional_command_
                  {{ inventory_hostname }}_output.txt"
      condition: "{{ hostvars[inventory_hostname]['condition']}}"
      flag: leaf_switch2
      command: "spanning-tree mode enable"


```

## License

TODO

## Author Information
  - ['Anil Kumar Muraleedharan (@amuraleedhar)']
