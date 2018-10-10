# Ansible module: ansible.module_cnos_template


Manage switch configuration using templates on devices running Lenovo CNOS

## Description

This module allows you to work with the running configuration of a switch. It provides a way to execute a set of CNOS commands on a switch by evaluating the current running configuration and executing the commands only if the specific settings have not been already configured. The configuration source can be a set of commands or a template written in the Jinja2 templating language. This module uses SSH to manage network device configuration. The results of the operation will be placed in a directory named 'results' that must be created by the user in their local directory to where the playbook is run. For more information about this module from Lenovo and customizing it usage for your use cases, please visit U(http://systemx.lenovofiles.com/help/index.jsp?topic=%2Fcom.lenovo.switchmgt.ansible.doc%2Fcnos_template.html)

## Requirements

TODO

## Arguments

``` json
{
    "commandfile": "{'description': ['This specifies the path to the CNOS command file which needs to be applied. This usually comes from the commands folder. Generally this file is the output of the variables applied on a template file. So this command is preceded by a template module. Note The command file must contain the Ansible keyword {{ inventory_hostname }} in its filename to ensure that the command file is unique for each switch and condition. If this is omitted, the command file will be overwritten during iteration. For example, commandfile=./commands/clos_leaf_bgp_{{ inventory_hostname }}_commands.txt'], 'required': True, 'default': None}",
    "deviceType": "{'description': ['This specifies the type of device where the method is executed. The choices NE1072T,NE1032,NE1032T,NE10032, NE2572 are added since version 2.4'], 'required': True, 'choices': ['g8272_cnos', 'g8296_cnos', 'g8332_cnos', 'NE1072T', 'NE1032', 'NE1032T', 'NE10032', 'NE2572'], 'version_added': 2.3}",
    "enablePassword": "{'description': ['Configures the password used to enter Global Configuration command mode on the switch. If the switch does not request this password, the parameter is ignored.While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'version_added': 2.3}",
    "host": "{'description': ['This is the variable used to search the hosts file at /etc/ansible/hosts and identify the IP address of the device on which the template is going to be applied. Usually the Ansible keyword {{ inventory_hostname }} is specified in the playbook as an abstraction of the group of network elements that need to be configured.'], 'required': True, 'version_added': 2.3}",
    "outputfile": "{'description': ['This specifies the file path where the output of each command execution is saved. Each command that is specified in the merged template file and each response from the device are saved here. Usually the location is the results folder, but you can choose another location based on your write permission.'], 'required': True, 'version_added': 2.3}",
    "password": "{'description': ['Configures the password used to authenticate the connection to the remote device. The value of the password parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'required': True, 'version_added': 2.3}",
    "username": "{'description': ['Configures the username used to authenticate the connection to the remote device. The value of the username parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'required': True, 'version_added': 2.3}",
}
```

## Examples


``` yaml

Tasks : The following are examples of using the module cnos_template. These are written in the main.yml file of the tasks directory.
---
- name: Replace Config CLI command template with values
  template:
      src: demo_template.j2
      dest: "./commands/demo_template_{{ inventory_hostname }}_commands.txt"
      vlanid1: 13
      slot_chassis_number1: "1/2"
      portchannel_interface_number1: 100
      portchannel_mode1: "active"

- name: Applying CLI commands on Switches
  cnos_template:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      commandfile: "./commands/demo_template_{{ inventory_hostname }}_commands.txt"
      outputfile: "./results/demo_template_command_{{ inventory_hostname }}_output.txt"


```

## License

TODO

## Author Information
  - ['Anil Kumar Muraleedharan (@amuraleedhar)']
