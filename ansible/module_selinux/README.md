# Ansible module: ansible.module_selinux


Change policy and state of SELinux

## Description

Configures the SELinux mode and policy. A reboot may be required after usage. Ansible will not issue this reboot but will let you know when it is required.

## Requirements

TODO

## Arguments

``` json
{
    "conf": "{'description': ['path to the SELinux configuration file, if non-standard'], 'default': '/etc/selinux/config', 'aliases': ['configfile', 'file']}",
    "policy": "{'description': ['name of the SELinux policy to use (example: C(targeted)) will be required if state is not C(disabled)']}",
    "state": "{'description': ['The SELinux mode'], 'required': True, 'choices': ['enforcing', 'permissive', 'disabled']}",
}
```

## Examples


``` yaml

# Enable SELinux
- selinux:
    policy: targeted
    state: enforcing

# Put SELinux in permissive mode, logging actions that would be blocked.
- selinux:
    policy: targeted
    state: permissive

# Disable SELinux
- selinux:
    state: disabled

```

## License

TODO

## Author Information
  - ['Derek Carter (@goozbach) <goozbach@friocorte.com>']
