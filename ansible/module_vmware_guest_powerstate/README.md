# Ansible module: ansible.module_vmware_guest_powerstate


Manages power states of virtual machines in vCenter

## Description

Power on / Power off / Restart a virtual machine.

## Requirements

TODO

## Arguments

``` json
{
    "folder": "{'description': ['Destination folder, absolute or relative path to find an existing guest or create the new guest.', "The folder should include the datacenter. ESX's datacenter is ha-datacenter", 'Examples:', '   folder: /ha-datacenter/vm', '   folder: ha-datacenter/vm', '   folder: /datacenter1/vm', '   folder: datacenter1/vm', '   folder: /datacenter1/vm/folder1', '   folder: datacenter1/vm/folder1', '   folder: /folder1/datacenter1/vm', '   folder: folder1/datacenter1/vm', '   folder: /folder1/datacenter1/vm/folder2', '   folder: vm/folder2', '   folder: folder2'], 'default': '/vm'}",
    "force": "{'description': ['Ignore warnings and complete the actions.', 'This parameter is useful while forcing virtual machine state.'], 'default': False, 'type': 'bool', 'version_added': 2.5}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "name": "{'description': ['Name of the virtual machine to work with.', 'Virtual machine names in vCenter are not necessarily unique, which may be problematic, see C(name_match).']}",
    "name_match": "{'description': ['If multiple virtual machines matching the name, use the first or last found.'], 'default': 'first', 'choices': ['first', 'last']}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "scheduled_at": "{'description': ['Date and time in string format at which specificed task needs to be performed.', "The required format for date and time - 'dd/mm/yyyy hh:mm'.", 'Scheduling task requires vCenter server. A standalone ESXi server does not support this option.']}",
    "state": "{'description': ['Set the state of the virtual machine.'], 'choices': ['powered-off', 'powered-on', 'reboot-guest', 'restarted', 'shutdown-guest', 'suspended', 'present'], 'default': 'present'}",
    "state_change_timeout": "{'description': ['If the C(state) is set to C(shutdown-guest), by default the module will return immediately after sending the shutdown signal.', 'If this argument is set to a positive integer, the module will instead wait for the VM to reach the poweredoff state.', 'The value sets a timeout in seconds for the module to wait for the state change.'], 'default': 0, 'version_added': '2.6'}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "uuid": "{'description': ["UUID of the instance to manage if known, this is VMware's unique identifier.", 'This is required if name is not supplied.']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Set the state of a virtual machine to poweroff
  vmware_guest_powerstate:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: no
    folder: /"{{ datacenter_name }}"/vm/my_folder
    name: "{{ guest_name }}"
    state: powered-off
  delegate_to: localhost
  register: deploy

- name: Set the state of a virtual machine to poweroff at given scheduled time
  vmware_guest_powerstate:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    folder: /"{{ datacenter_name }}"/vm/my_folder
    name: "{{ guest_name }}"
    state: powered-off
    scheduled_at: "09/01/2018 10:18"
  delegate_to: localhost
  register: deploy_at_schedule_datetime

- name: Wait for the virtual machine to shutdown
  vmware_guest_powerstate:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: "{{ guest_name }}"
    state: shutdown-guest
    state_change_timeout: 200
  delegate_to: localhost
  register: deploy

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>']
