# Ansible module: ansible.module_vmware_vm_shell


Run commands in a VMware guest operating system

## Description

Module allows user to run common system administration commands in the guest operating system.

## Requirements

TODO

## Arguments

``` json
{
    "cluster": "{'description': ['The cluster hosting the virtual machine.', 'If set, it will help to speed up virtual machine search.']}",
    "datacenter": "{'description': ['The datacenter hosting the virtual machine.', 'If set, it will help to speed up virtual machine search.']}",
    "folder": "{'description': ['Destination folder, absolute or relative path to find an existing guest or create the new guest.', "The folder should include the datacenter. ESX's datacenter is ha-datacenter.", 'Examples:', '   folder: /ha-datacenter/vm', '   folder: ha-datacenter/vm', '   folder: /datacenter1/vm', '   folder: datacenter1/vm', '   folder: /datacenter1/vm/folder1', '   folder: datacenter1/vm/folder1', '   folder: /folder1/datacenter1/vm', '   folder: folder1/datacenter1/vm', '   folder: /folder1/datacenter1/vm/folder2'], 'version_added': '2.4'}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "timeout": "{'description': ['Timeout in seconds.', 'If set to positive integers, then C(wait_for_process) will honor this parameter and will exit after this timeout.'], 'default': 3600, 'version_added': 2.7}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
    "vm_id": "{'description': ['Name of the virtual machine to work with.'], 'required': True}",
    "vm_id_type": "{'description': ['The VMware identification method by which the virtual machine will be identified.'], 'default': 'vm_name', 'choices': ['uuid', 'dns_name', 'inventory_path', 'vm_name']}",
    "vm_password": "{'description': ['The password used to login-in to the virtual machine.'], 'required': True}",
    "vm_shell": "{'description': ['The absolute path to the program to start.', 'On Linux, shell is executed via bash.'], 'required': True}",
    "vm_shell_args": "{'description': ['The argument to the program.', 'The characters which must be escaped to the shell also be escaped on the command line provided.'], 'default': ' '}",
    "vm_shell_cwd": "{'description': ['The current working directory of the application from which it will be run.']}",
    "vm_shell_env": "{'description': ['Comma separated list of environment variable, specified in the guest OS notation.']}",
    "vm_username": "{'description': ['The user to login-in to the virtual machine.'], 'required': True}",
    "wait_for_process": "{'description': ['If set to C(True), module will wait for process to complete in the given virtual machine.'], 'default': False, 'type': 'bool', 'version_added': 2.7}",
}
```

## Examples


``` yaml

- name: Run command inside a virtual machine
  vmware_vm_shell:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    folder: /"{{datacenter}}"/vm
    vm_id: "{{ vm_name }}"
    vm_username: root
    vm_password: superSecret
    vm_shell: /bin/echo
    vm_shell_args: " $var >> myFile "
    vm_shell_env:
      - "PATH=/bin"
      - "VAR=test"
    vm_shell_cwd: "/tmp"
  delegate_to: localhost
  register: shell_command_output

- name: Run command inside a virtual machine with wait and timeout
  vmware_vm_shell:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    folder: /"{{datacenter}}"/vm
    vm_id: NameOfVM
    vm_username: root
    vm_password: superSecret
    vm_shell: /bin/sleep
    vm_shell_args: 100
    wait_for_process: True
    timeout: 2000
  delegate_to: localhost
  register: shell_command_with_wait_timeout

- name: Change user password in the guest machine
  vmware_vm_shell:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    folder: /"{{datacenter}}"/vm
    vm_id: "{{ vm_name }}"
    vm_username: sample
    vm_password: old_password
    vm_shell: "/bin/echo"
    vm_shell_args: "-e 'old_password\nnew_password\nnew_password' | passwd sample > /tmp/$$.txt 2>&1"
  delegate_to: localhost

- name: Change hostname of guest machine
  vmware_vm_shell:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: no
    datacenter: "{{ datacenter }}"
    folder: /"{{datacenter}}"/vm
    vm_id: "{{ vm_name }}"
    vm_username: testUser
    vm_password: SuperSecretPassword
    vm_shell: "/usr/bin/hostnamectl"
    vm_shell_args: "set-hostname new_hostname > /tmp/$$.txt 2>&1"
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Ritesh Khadgaray (@ritzk)', 'Abhijeet Kasurde (@Akasurde)']
  - ['Ritesh Khadgaray (@ritzk)', 'Abhijeet Kasurde (@Akasurde)']
