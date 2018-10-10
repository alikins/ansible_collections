# Ansible module: ansible.module_cnos_showrun


Collect the current running configuration on devices running on CNOS

## Description

This module allows you to view the switch running configuration. It executes the display running-config CLI command on a switch and returns a file containing the current running configuration of the target network device. This module uses SSH to manage network device configuration. The results of the operation will be placed in a directory named 'results' that must be created by the user in their local directory to where the playbook is run. For more information about this module from Lenovo and customizing it usage for your use cases, please visit U(http://systemx.lenovofiles.com/help/index.jsp?topic=%2Fcom.lenovo.switchmgt.ansible.doc%2Fcnos_showrun.html)

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
}
```

## Examples


``` yaml

Tasks : The following are examples of using the module cnos_showrun. These are
 written in the main.yml file of the tasks directory.
---
- name: Run show running-config
  cnos_showrun:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_showrun_{{ inventory_hostname }}_output.txt"


```

## License

TODO

## Author Information
  - ['Anil Kumar Muraleedharan (@amuraleedhar)']
