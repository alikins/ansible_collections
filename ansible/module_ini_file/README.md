# Ansible module: ansible.module_ini_file


Tweak settings in INI files

## Description

Manage (add, remove, change) individual settings in an INI-style file without having to manage the file as a whole with, say, M(template) or M(assemble). Adds missing sections if they don't exist.
Before version 2.0, comments are discarded when the source file is read, and therefore will not show up in the destination file.
Since version 2.3, this module adds missing ending newlines to files to keep in line with the POSIX standard, even when no other modifications need to be applied.

## Requirements

TODO

## Arguments

``` json
{
    "allow_no_value": "{'description': ["allow option without value and without '=' symbol"], 'type': 'bool', 'required': False, 'default': False, 'version_added': '2.6'}",
    "attributes": "{'description': ['The attributes the resulting file or directory should have.', 'To get supported flags look at the man page for I(chattr) on the target system.', 'This string should contain the attributes in the same order as the one displayed by I(lsattr).', 'The C(=) operator is assumed as default, otherwise C(+) or C(-) operators need to be included in the string.'], 'aliases': ['attr'], 'version_added': '2.3'}",
    "backup": "{'description': ['Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.'], 'type': 'bool', 'default': False}",
    "create": "{'description': ["If set to 'no', the module will fail if the file does not already exist. By default it will create the file if it is missing."], 'type': 'bool', 'default': True, 'version_added': '2.2'}",
    "group": "{'description': ['Name of the group that should own the file/directory, as would be fed to I(chown).']}",
    "mode": "{'description': ['The permissions the resulting file or directory should have.', "For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like C(0644) or C(01777)) or quote it (like C('644') or C('1777')) so Ansible receives a string and can do its own conversion from string into number.", 'Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.', 'As of version 1.8, the mode may be specified as a symbolic mode (for example, C(u+rwx) or C(u=rw,g=r,o=r)).', 'As of version 2.6, the mode may also be the special string C(preserve).', 'When set to C(preserve) the file will be given the same permissions as the source file.']}",
    "no_extra_spaces": "{'description': ["Do not insert spaces before and after '=' symbol"], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "option": "{'description': ['If set (required for changing a I(value)), this is the name of the option.', 'May be omitted if adding/removing a whole I(section).']}",
    "others": "{'description': ['All arguments accepted by the M(file) module also work here']}",
    "owner": "{'description': ['Name of the user that should own the file/directory, as would be fed to I(chown).']}",
    "path": "{'description': ['Path to the INI-style file; this file is created if required.', 'Before 2.3 this option was only usable as I(dest).'], 'aliases': ['dest'], 'required': True}",
    "section": "{'description': ['Section name in INI file. This is added if C(state=present) automatically when a single value is being set.', 'If left empty or set to `null`, the I(option) will be placed before the first I(section). Using `null` is also required if the config format does not support sections.'], 'required': True}",
    "selevel": "{'description': ['The level part of the SELinux file context.', 'This is the MLS/MCS attribute, sometimes known as the C(range).', 'When set to C(_default), it will use the C(level) portion of the policy if available.'], 'default': 's0'}",
    "serole": "{'description': ['The role part of the SELinux file context.', 'When set to C(_default), it will use the C(role) portion of the policy if available.']}",
    "setype": "{'description': ['The type part of the SELinux file context.', 'When set to C(_default), it will use the C(type) portion of the policy if available.']}",
    "seuser": "{'description': ['The user part of the SELinux file context.', 'By default it uses the C(system) policy, where applicable.', 'When set to C(_default), it will use the C(user) portion of the policy if available.']}",
    "state": "{'description': ['If set to C(absent) the option or section will be removed if present instead of created.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "unsafe_writes": "{'description': ['Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target file.', 'By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted files, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.', "This option allows Ansible to fall back to unsafe methods of updating files when atomic operations fail (however, it doesn't force Ansible to perform unsafe writes).", 'IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "value": "{'description': ['The string value to be associated with an I(option). May be omitted when removing an I(option).']}",
}
```

## Examples


``` yaml

# Before 2.3, option 'dest' was used instead of 'path'
- name: Ensure "fav=lemonade is in section "[drinks]" in specified file
  ini_file:
    path: /etc/conf
    section: drinks
    option: fav
    value: lemonade
    mode: 0600
    backup: yes

- name: Ensure "temperature=cold is in section "[drinks]" in specified file
  ini_file:
    path: /etc/anotherconf
    section: drinks
    option: temperature
    value: cold
    backup: yes

```

## License

TODO

## Author Information
  - ['Jan-Piet Mens (@jpmens)', 'Ales Nosek (@noseka1)']
  - ['Jan-Piet Mens (@jpmens)', 'Ales Nosek (@noseka1)']
