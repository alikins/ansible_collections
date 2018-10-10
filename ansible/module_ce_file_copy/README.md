# Ansible module: ansible.module_ce_file_copy


Copy a file to a remote cloudengine device over SCP on HUAWEI CloudEngine switches

## Description

Copy a file to a remote cloudengine device over SCP on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "file_system": "{'description': ['The remote file system of the device. If omitted, devices that support a I(file_system) parameter will use their default values. File system indicates the storage medium and can be set to as follows, 1) C(flash) is root directory of the flash memory on the master MPU. 2) C(slave#flash) is root directory of the flash memory on the slave MPU. If no slave MPU exists, this drive is unavailable. 3) C(chassis ID/slot number#flash) is root directory of the flash memory on a device in a stack. For example, C(1/5#flash) indicates the flash memory whose chassis ID is 1 and slot number is 5.'], 'default': 'flash:'}",
    "local_file": "{'description': ['Path to local file. Local directory must exist. The maximum length of I(local_file) is C(4096).'], 'required': True}",
    "remote_file": "{'description': ['Remote file path of the copy. Remote directories must exist. If omitted, the name of the local file will be used. The maximum length of I(remote_file) is C(4096).']}",
}
```

## Examples


``` yaml

- name: File copy test
  hosts: cloudengine
  connection: local
  gather_facts: no
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

  - name: "Copy a local file to remote device"
    ce_file_copy:
      local_file: /usr/vrpcfg.cfg
      remote_file: /vrpcfg.cfg
      file_system: 'flash:'
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Zhou Zhijin (@CloudEngine-Ansible)']
