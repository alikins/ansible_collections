# Ansible module: ansible.module_beadm


Manage ZFS boot environments on FreeBSD/Solaris/illumos systems

## Description

Create, delete or activate ZFS boot environments.
Mount and unmount ZFS boot environments.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['Associate a description with a new boot environment. This option is available only on Solarish platforms.'], 'required': False, 'default': False}",
    "force": "{'description': ['Specifies if the unmount should be forced.'], 'required': False, 'default': False, 'type': 'bool'}",
    "mountpoint": "{'description': ['Path where to mount the ZFS boot environment'], 'required': False, 'default': False}",
    "name": "{'description': ['ZFS boot environment name.'], 'aliases': ['be'], 'required': True}",
    "options": "{'description': ['Create the datasets for new BE with specific ZFS properties. Multiple options can be specified. This option is available only on Solarish platforms.'], 'required': False, 'default': False}",
    "snapshot": "{'description': ['If specified, the new boot environment will be cloned from the given snapshot or inactive boot environment.'], 'required': False, 'default': False}",
    "state": "{'description': ['Create or delete ZFS boot environment.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent', 'activated', 'mounted', 'unmounted']}",
}
```

## Examples


``` yaml

- name: Create ZFS boot environment
  beadm:
    name: upgrade-be
    state: present

- name: Create ZFS boot environment from existing inactive boot environment
  beadm:
    name: upgrade-be
    snapshot: be@old
    state: present

- name: Create ZFS boot environment with compression enabled and description "upgrade"
  beadm:
    name: upgrade-be
    options: "compression=on"
    description: upgrade
    state: present

- name: Delete ZFS boot environment
  beadm:
    name: old-be
    state: absent

- name: Mount ZFS boot environment on /tmp/be
  beadm:
    name: BE
    mountpoint: /tmp/be
    state: mounted

- name: Unmount ZFS boot environment
  beadm:
    name: BE
    state: unmounted

- name: Activate ZFS boot environment
  beadm:
    name: upgrade-be
    state: activated

```

## License

TODO

## Author Information
  - ['Adam Števko (@xen0l)']
