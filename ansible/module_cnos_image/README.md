# Ansible module: ansible.module_cnos_image


Perform firmware upgrade/download from a remote server on devices running Lenovo CNOS

## Description

This module allows you to work with switch firmware images. It provides a way to download a firmware image to a network device from a remote server using FTP, SFTP, TFTP, or SCP. The first step is to create a directory from where the remote server can be reached. The next step is to provide the full file path of the image's location. Authentication details required by the remote server must be provided as well. By default, this method makes the newly downloaded firmware image the active image, which will be used by the switch during the next restart. This module uses SSH to manage network device configuration. The results of the operation will be placed in a directory named 'results' that must be created by the user in their local directory to where the playbook is run. For more information about this module from Lenovo and customizing it usage for your use cases, please visit U(http://systemx.lenovofiles.com/help/index.jsp?topic=%2Fcom.lenovo.switchmgt.ansible.doc%2Fcnos_image.html)

## Requirements

TODO

## Arguments

``` json
{
    "deviceType": "{'description': ['This specifies the type of device where the method is executed. The choices NE1072T,NE1032,NE1032T,NE10032, NE2572 are added since version 2.4'], 'required': True, 'choices': ['g8272_cnos', 'g8296_cnos', 'g8332_cnos', 'NE1072T', 'NE1032', 'NE1032T', 'NE10032', 'NE2572'], 'version_added': 2.3}",
    "enablePassword": "{'description': ['Configures the password used to enter Global Configuration command mode on the switch. If the switch does not request this password, the parameter is ignored.While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'version_added': 2.3}",
    "host": "{'description': ['This is the variable used to search the hosts file at /etc/ansible/hosts and identify the IP address of the device on which the template is going to be applied. Usually the Ansible keyword {{ inventory_hostname }} is specified in the playbook as an abstraction of the group of network elements that need to be configured.'], 'required': True, 'version_added': 2.3}",
    "imgpath": "{'description': ['This specifies the full file path of the image located on the remote server. In case the relative path is used as the variable value, the root folder for the user of the server needs to be specified.'], 'required': True}",
    "imgtype": "{'description': ['This specifies the firmware image type to be downloaded'], 'required': True, 'choices': ['all', 'boot', 'os', 'onie']}",
    "outputfile": "{'description': ['This specifies the file path where the output of each command execution is saved. Each command that is specified in the merged template file and each response from the device are saved here. Usually the location is the results folder, but you can choose another location based on your write permission.'], 'required': True, 'version_added': 2.3}",
    "password": "{'description': ['Configures the password used to authenticate the connection to the remote device. The value of the password parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'required': True, 'version_added': 2.3}",
    "protocol": "{'description': ['This refers to the protocol used by the network device to interact with the remote server from where to download the firmware image. The choices are FTP, SFTP, TFTP, or SCP. Any other protocols will result in error. If this parameter is not specified there is no default value to be used.'], 'required': True, 'choices': ['SFTP', 'SCP', 'FTP', 'TFTP']}",
    "serverip": "{'description': ['This specifies the IP Address of the remote server from where the software image will be downloaded.'], 'required': True}",
    "serverpassword": "{'description': ['Specify the password for the server relating to the protocol used']}",
    "serverusername": "{'description': ['Specify the username for the server relating to the protocol used'], 'required': True}",
    "username": "{'description': ['Configures the username used to authenticate the connection to the remote device. The value of the username parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'required': True, 'version_added': 2.3}",
}
```

## Examples


``` yaml

Tasks : The following are examples of using the module cnos_image. These are
  written in the main.yml file of the tasks directory.
---
- name: Test Image transfer
  cnos_image:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_image_{{ inventory_hostname }}_output.txt"
      protocol: "sftp"
      serverip: "10.241.106.118"
      imgpath: "/root/cnos_images/G8272-10.1.0.112.img"
      imgtype: "os"
      serverusername: "root"
      serverpassword: "root123"

- name: Test Image tftp
  cnos_image:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_image_{{ inventory_hostname }}_output.txt"
      protocol: "tftp"
      serverip: "10.241.106.118"
      imgpath: "/anil/G8272-10.2.0.34.img"
      imgtype: "os"
      serverusername: "root"
      serverpassword: "root123"

```

## License

TODO

## Author Information
  - ['Anil Kumar Muraleedharan (@amuraleedhar)']
