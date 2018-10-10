# Ansible module: ansible.module_sysctl


Manage entries in sysctl.conf

## Description

This module manipulates sysctl entries and optionally performs a C(/sbin/sysctl -p) after changing them.

## Requirements

TODO

## Arguments

``` json
{
    "ignoreerrors": "{'description': ['Use this option to ignore errors about unknown keys.'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['The dot-separated path (aka I(key)) specifying the sysctl variable.'], 'required': True, 'aliases': ['key']}",
    "reload": "{'description': ['If C(yes), performs a I(/sbin/sysctl -p) if the C(sysctl_file) is updated. If C(no), does not reload I(sysctl) even if the C(sysctl_file) is updated.'], 'type': 'bool', 'default': True}",
    "state": "{'description': ['Whether the entry should be present or absent in the sysctl file.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "sysctl_file": "{'description': ['Specifies the absolute path to C(sysctl.conf), if not C(/etc/sysctl.conf).'], 'default': '/etc/sysctl.conf'}",
    "sysctl_set": "{'description': ['Verify token value with the sysctl command and set with -w if necessary'], 'type': 'bool', 'default': False, 'version_added': 1.5}",
    "value": "{'description': ['Desired value of the sysctl key.'], 'aliases': ['val']}",
}
```

## Examples


``` yaml

# Set vm.swappiness to 5 in /etc/sysctl.conf
- sysctl:
    name: vm.swappiness
    value: 5
    state: present

# Remove kernel.panic entry from /etc/sysctl.conf
- sysctl:
    name: kernel.panic
    state: absent
    sysctl_file: /etc/sysctl.conf

# Set kernel.panic to 3 in /tmp/test_sysctl.conf
- sysctl:
    name: kernel.panic
    value: 3
    sysctl_file: /tmp/test_sysctl.conf
    reload: no

# Set ip forwarding on in /proc and do not reload the sysctl file
- sysctl:
    name: net.ipv4.ip_forward
    value: 1
    sysctl_set: yes

# Set ip forwarding on in /proc and in the sysctl file and reload if necessary
- sysctl:
    name: net.ipv4.ip_forward
    value: 1
    sysctl_set: yes
    state: present
    reload: yes

```

## License

TODO

## Author Information
  - ['David CHANIAL (@davixx) <david.chanial@gmail.com>']
