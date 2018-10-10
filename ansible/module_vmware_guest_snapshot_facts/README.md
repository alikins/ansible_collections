# Ansible module: ansible.module_vmware_guest_snapshot_facts


Gather facts about virtual machine's snapshots in vCenter

## Description

This module can be used to gather facts about virtual machine's snapshots.

## Requirements

TODO

## Arguments

``` json
{
    "datacenter": "{'description': ['Name of the datacenter.'], 'required': True}",
    "folder": "{'description': ['Destination folder, absolute or relative path to find an existing guest.', 'This is required only, if multiple virtual machines with same name are found on given vCenter.', "The folder should include the datacenter. ESX's datacenter is ha-datacenter", 'Examples:', '   folder: /ha-datacenter/vm', '   folder: ha-datacenter/vm', '   folder: /datacenter1/vm', '   folder: datacenter1/vm', '   folder: /datacenter1/vm/folder1', '   folder: datacenter1/vm/folder1', '   folder: /folder1/datacenter1/vm', '   folder: folder1/datacenter1/vm', '   folder: /folder1/datacenter1/vm/folder2']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "name": "{'description': ['Name of the VM to work with.', 'This is required if C(uuid) is not supplied.']}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "uuid": "{'description': ["UUID of the instance to manage if known, this value is VMware's unique identifier.", 'This is required if C(name) is not supplied.', 'The C(folder) is ignored, if C(uuid) is provided.']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

  - name: Gather snapshot facts about the virtual machine in the given vCenter
    vmware_guest_snapshot_facts:
      hostname: "{{ vcenter_hostname }}"
      username: "{{ vcenter_username }}"
      password: "{{ vcenter_password }}"
      datacenter: "{{ datacenter_name }}"
      name: "{{ guest_name }}"
    delegate_to: localhost
    register: snapshot_facts

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>']
