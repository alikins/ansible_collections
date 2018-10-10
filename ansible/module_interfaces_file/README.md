# Ansible module: ansible.module_interfaces_file


Tweak settings in /etc/network/interfaces files

## Description

Manage (add, remove, change) individual interface options in an interfaces-style file without having to manage the file as a whole with, say, M(template) or M(assemble). Interface has to be presented in a file.
Read information about interfaces from interfaces-styled files

## Requirements

TODO

## Arguments

``` json
{
    "attributes": "{'description': ['The attributes the resulting file or directory should have.', 'To get supported flags look at the man page for I(chattr) on the target system.', 'This string should contain the attributes in the same order as the one displayed by I(lsattr).', 'The C(=) operator is assumed as default, otherwise C(+) or C(-) operators need to be included in the string.'], 'aliases': ['attr'], 'version_added': '2.3'}",
    "backup": "{'description': ['Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.'], 'type': 'bool', 'default': False}",
    "dest": "{'description': ['Path to the interfaces file'], 'default': '/etc/network/interfaces'}",
    "group": "{'description': ['Name of the group that should own the file/directory, as would be fed to I(chown).']}",
    "iface": "{'description': ['Name of the interface, required for value changes or option remove']}",
    "mode": "{'description': ['The permissions the resulting file or directory should have.', "For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like C(0644) or C(01777)) or quote it (like C('644') or C('1777')) so Ansible receives a string and can do its own conversion from string into number.", 'Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.', 'As of version 1.8, the mode may be specified as a symbolic mode (for example, C(u+rwx) or C(u=rw,g=r,o=r)).', 'As of version 2.6, the mode may also be the special string C(preserve).', 'When set to C(preserve) the file will be given the same permissions as the source file.']}",
    "option": "{'description': ['Name of the option, required for value changes or option remove']}",
    "owner": "{'description': ['Name of the user that should own the file/directory, as would be fed to I(chown).']}",
    "selevel": "{'description': ['The level part of the SELinux file context.', 'This is the MLS/MCS attribute, sometimes known as the C(range).', 'When set to C(_default), it will use the C(level) portion of the policy if available.'], 'default': 's0'}",
    "serole": "{'description': ['The role part of the SELinux file context.', 'When set to C(_default), it will use the C(role) portion of the policy if available.']}",
    "setype": "{'description': ['The type part of the SELinux file context.', 'When set to C(_default), it will use the C(type) portion of the policy if available.']}",
    "seuser": "{'description': ['The user part of the SELinux file context.', 'By default it uses the C(system) policy, where applicable.', 'When set to C(_default), it will use the C(user) portion of the policy if available.']}",
    "state": "{'description': ['If set to C(absent) the option or section will be removed if present instead of created.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "unsafe_writes": "{'description': ['Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target file.', 'By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted files, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.', "This option allows Ansible to fall back to unsafe methods of updating files when atomic operations fail (however, it doesn't force Ansible to perform unsafe writes).", 'IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "value": "{'description': ["If I(option) is not presented for the I(interface) and I(state) is C(present) option will be added. If I(option) already exists and is not C(pre-up), C(up), C(post-up) or C(down), it's value will be updated. C(pre-up), C(up), C(post-up) and C(down) options can't be updated, only adding new options, removing existing ones or cleaning the whole option set are supported"]}",
}
```

## Examples


``` yaml

# Set eth1 mtu configuration value to 8000
- interfaces_file:
    dest: /etc/network/interfaces.d/eth1.cfg
    iface: eth1
    option: mtu
    value: 8000
    backup: yes
    state: present
  register: eth1_cfg

```

## License

TODO

## Author Information
  - ['Roman Belyakovsky (@hryamzik)']
