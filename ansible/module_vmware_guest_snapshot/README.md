# Ansible module: ansible.module_vmware_guest_snapshot


Manages virtual machines snapshots in vCenter

## Description

This module can be used to create, delete and update snapshot(s) of the given virtual machine.
All parameters and VMware object names are case sensitive.

## Requirements

TODO

## Arguments

``` json
{
    "datacenter": "{'description': ['Destination datacenter for the deploy operation.'], 'required': True}",
    "description": "{'description': ['Define an arbitrary description to attach to snapshot.'], 'default': ''}",
    "folder": "{'description': ['Destination folder, absolute or relative path to find an existing guest.', 'This is required parameter, if C(name) is supplied.', "The folder should include the datacenter. ESX's datacenter is ha-datacenter.", 'Examples:', '   folder: /ha-datacenter/vm', '   folder: ha-datacenter/vm', '   folder: /datacenter1/vm', '   folder: datacenter1/vm', '   folder: /datacenter1/vm/folder1', '   folder: datacenter1/vm/folder1', '   folder: /folder1/datacenter1/vm', '   folder: folder1/datacenter1/vm', '   folder: /folder1/datacenter1/vm/folder2', '   folder: vm/folder2', '   folder: folder2']}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "memory_dump": "{'description': ['If set to C(true), memory dump of virtual machine is also included in snapshot.', 'Note that memory snapshots take time and resources, this will take longer time to create.', 'If virtual machine does not provide capability to take memory snapshot, then this flag is set to C(false).'], 'required': False, 'version_added': '2.4', 'type': 'bool', 'default': False}",
    "name": "{'description': ['Name of the virtual machine to work with.', 'This is required parameter, if C(uuid) is not supplied.']}",
    "name_match": "{'description': ['If multiple VMs matching the name, use the first or last found.'], 'default': 'first', 'choices': ['first', 'last']}",
    "new_description": "{'description': ['Value to change the description of an existing snapshot to.'], 'version_added': '2.5'}",
    "new_snapshot_name": "{'description': ['Value to rename the existing snapshot to.'], 'version_added': '2.5'}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "quiesce": "{'description': ['If set to C(true) and virtual machine is powered on, it will quiesce the file system in virtual machine.', 'Note that VMWare Tools are required for this flag.', 'If virtual machine is powered off or VMware Tools are not available, then this flag is set to C(false).', 'If virtual machine does not provide capability to take quiesce snapshot, then this flag is set to C(false).'], 'required': False, 'version_added': '2.4', 'type': 'bool', 'default': False}",
    "remove_children": "{'description': ['If set to C(true) and state is set to C(absent), then entire snapshot subtree is set for removal.'], 'required': False, 'version_added': '2.4', 'type': 'bool', 'default': False}",
    "snapshot_name": "{'description': ['Sets the snapshot name to manage.', 'This param is required only if state is not C(remove_all)']}",
    "state": "{'description': ['Manage snapshot(s) attached to a specific virtual machine.', 'If set to C(present) and snapshot absent, then will create a new snapshot with the given name.', 'If set to C(present) and snapshot present, then no changes are made.', 'If set to C(absent) and snapshot present, then snapshot with the given name is removed.', 'If set to C(absent) and snapshot absent, then no changes are made.', 'If set to C(revert) and snapshot present, then virtual machine state is reverted to the given snapshot.', 'If set to C(revert) and snapshot absent, then no changes are made.', 'If set to C(remove_all) and snapshot(s) present, then all snapshot(s) will be removed.', 'If set to C(remove_all) and snapshot(s) absent, then no changes are made.'], 'required': True, 'choices': ['present', 'absent', 'revert', 'remove_all'], 'default': 'present'}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "uuid": "{'description': ["UUID of the instance to manage if known, this is VMware's unique identifier.", 'This is required parameter, if C(name) is not supplied.']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

  - name: Create a snapshot
    vmware_guest_snapshot:
      hostname: "{{ vcenter_hostname }}"
      username: "{{ vcenter_username }}"
      password: "{{ vcenter_password }}"
      datacenter: "{{ datacenter_name }}"
      folder: /"{{ datacenter_name }}"/vm/
      name: "{{ guest_name }}"
      state: present
      snapshot_name: snap1
      description: snap1_description
    delegate_to: localhost

  - name: Remove a snapshot
    vmware_guest_snapshot:
      hostname: "{{ vcenter_hostname }}"
      username: "{{ vcenter_username }}"
      password: "{{ vcenter_password }}"
      datacenter: "{{ datacenter_name }}"
      folder: /"{{ datacenter_name }}"/vm/
      name: "{{ guest_name }}"
      state: absent
      snapshot_name: snap1
    delegate_to: localhost

  - name: Revert to a snapshot
    vmware_guest_snapshot:
      hostname: "{{ vcenter_hostname }}"
      username: "{{ vcenter_username }}"
      password: "{{ vcenter_password }}"
      datacenter: "{{ datacenter_name }}"
      folder: /"{{ datacenter_name }}"/vm/
      name: "{{ guest_name }}"
      state: revert
      snapshot_name: snap1
    delegate_to: localhost

  - name: Remove all snapshots of a VM
    vmware_guest_snapshot:
      hostname: "{{ vcenter_hostname }}"
      username: "{{ vcenter_username }}"
      password: "{{ vcenter_password }}"
      datacenter: "{{ datacenter_name }}"
      folder: /"{{ datacenter_name }}"/vm/
      name: "{{ guest_name }}"
      state: remove_all
    delegate_to: localhost

  - name: Take snapshot of a VM using quiesce and memory flag on
    vmware_guest_snapshot:
      hostname: "{{ vcenter_hostname }}"
      username: "{{ vcenter_username }}"
      password: "{{ vcenter_password }}"
      datacenter: "{{ datacenter_name }}"
      folder: /"{{ datacenter_name }}"/vm/
      name: "{{ guest_name }}"
      state: present
      snapshot_name: dummy_vm_snap_0001
      quiesce: yes
      memory_dump: yes
    delegate_to: localhost

  - name: Remove a snapshot and snapshot subtree
    vmware_guest_snapshot:
      hostname: "{{ vcenter_hostname }}"
      username: "{{ vcenter_username }}"
      password: "{{ vcenter_password }}"
      datacenter: "{{ datacenter_name }}"
      folder: /"{{ datacenter_name }}"/vm/
      name: "{{ guest_name }}"
      state: absent
      remove_children: yes
      snapshot_name: snap1
    delegate_to: localhost

  - name: Rename a snapshot
    vmware_guest_snapshot:
      hostname: "{{ vcenter_hostname }}"
      username: "{{ vcenter_username }}"
      password: "{{ vcenter_password }}"
      datacenter: "{{ datacenter_name }}"
      folder: /"{{ datacenter_name }}"/vm/
      name: "{{ guest_name }}"
      state: present
      snapshot_name: current_snap_name
      new_snapshot_name: im_renamed
      new_description: "{{ new_snapshot_description }}"
    delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Loic Blot (@nerzhul) <loic.blot@unix-experience.fr>']
