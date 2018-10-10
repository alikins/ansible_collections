# Ansible module: ansible.module_vmware_guest_vnc


Manages VNC remote display on virtual machines in vCenter

## Description

This module can be used to enable and disable VNC remote display on virtual machine.

## Requirements

TODO

## Arguments

``` json
{
    "datacenter": "{'description': ['Destination datacenter for the deploy operation.', 'This parameter is case sensitive.'], 'default': 'ha-datacenter'}",
    "folder": "{'description': ['Destination folder, absolute or relative path to find an existing guest.', "The folder should include the datacenter. ESX's datacenter is ha-datacenter"], 'required': False}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "name": "{'description': ['Name of the virtual machine to work with.', 'Virtual machine names in vCenter are not necessarily unique, which may be problematic, see C(name_match).'], 'required': False}",
    "name_match": "{'description': ['If multiple virtual machines matching the name, use the first or last found.'], 'default': 'first', 'choices': ['first', 'last'], 'required': False}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "state": "{'description': ['Set the state of VNC on virtual machine.'], 'choices': ['present', 'absent'], 'default': 'present', 'required': False}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "uuid": "{'description': ["UUID of the instance to manage if known, this is VMware's unique identifier.", 'This is required, if C(name) is not supplied.'], 'required': False}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
    "vnc_ip": "{'description': ['Sets an IP for VNC on virtual machine.', 'This is required only when I(state) is set to present and will be ignored if I(state) is absent.'], 'default': '0.0.0.0', 'required': False}",
    "vnc_password": "{'description': ['Sets a password for VNC on virtual machine.', 'This is required only when I(state) is set to present and will be ignored if I(state) is absent.'], 'default': '', 'required': False}",
    "vnc_port": "{'description': ['The port that VNC listens on. Usually a number between 5900 and 7000 depending on your config.', 'This is required only when I(state) is set to present and will be ignored if I(state) is absent.'], 'default': 0, 'required': False}",
}
```

## Examples


``` yaml

- name: Enable VNC remote display on the VM
  vmware_guest_vnc:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: no
    folder: /mydatacenter/vm
    name: testvm1
    vnc_port: 5990
    vnc_password: vNc5ecr3t
    datacenter: "{{ datacenter_name }}"
    state: present
  delegate_to: localhost
  register: vnc_result

- name: Disable VNC remote display on the VM
  vmware_guest_vnc:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: no
    datacenter: "{{ datacenter_name }}"
    uuid: 32074771-7d6b-699a-66a8-2d9cf8236fff
    state: absent
  delegate_to: localhost
  register: vnc_result

```

## License

TODO

## Author Information
  - ['Armin Ranjbar Daemi (@rmin)']
