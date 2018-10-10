# Ansible module: ansible.module_assemble


Assemble configuration files from fragments

## Description

Assembles a configuration file from fragments.
Often a particular program will take a single configuration file and does not support a C(conf.d) style structure where it is easy to build up the configuration from multiple sources. C(assemble) will take a directory of files that can be local or have already been transferred to the system, and concatenate them together to produce a destination file.
Files are assembled in string sorting order.
Puppet calls this idea I(fragments).
This module is also supported for Windows targets.

## Requirements

TODO

## Arguments

``` json
{
    "attributes": "{'description': ['The attributes the resulting file or directory should have.', 'To get supported flags look at the man page for I(chattr) on the target system.', 'This string should contain the attributes in the same order as the one displayed by I(lsattr).', 'The C(=) operator is assumed as default, otherwise C(+) or C(-) operators need to be included in the string.'], 'aliases': ['attr'], 'version_added': '2.3'}",
    "backup": "{'description': ['Create a backup file (if C(yes)), including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.'], 'type': 'bool', 'default': False}",
    "decrypt": "{'description': ['This option controls the autodecryption of source files using vault.'], 'required': False, 'type': 'bool', 'default': True, 'version_added': '2.4'}",
    "delimiter": "{'description': ['A delimiter to separate the file contents.'], 'version_added': '1.4'}",
    "dest": "{'description': ['A file to create using the concatenation of all of the source files.'], 'required': True}",
    "group": "{'description': ['Name of the group that should own the file/directory, as would be fed to I(chown).']}",
    "ignore_hidden": "{'description': ["A boolean that controls if files that start with a '.' will be included or not."], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
    "mode": "{'description': ['The permissions the resulting file or directory should have.', "For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like C(0644) or C(01777)) or quote it (like C('644') or C('1777')) so Ansible receives a string and can do its own conversion from string into number.", 'Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.', 'As of version 1.8, the mode may be specified as a symbolic mode (for example, C(u+rwx) or C(u=rw,g=r,o=r)).', 'As of version 2.6, the mode may also be the special string C(preserve).', 'When set to C(preserve) the file will be given the same permissions as the source file.']}",
    "owner": "{'description': ['Name of the user that should own the file/directory, as would be fed to I(chown).']}",
    "regexp": "{'description': ['Assemble files only if C(regex) matches the filename.', 'If not set, all files are assembled.', 'Every "\\" (backslash) must be escaped as "\\\\" to comply to YAML syntax.', 'Uses L(Python regular expressions,http://docs.python.org/2/library/re.html).']}",
    "remote_src": "{'description': ['If C(no), it will search for src at originating/master machine.', 'If C(yes), it will go to the remote/target machine for the src.'], 'type': 'bool', 'default': True, 'version_added': '1.4'}",
    "selevel": "{'description': ['The level part of the SELinux file context.', 'This is the MLS/MCS attribute, sometimes known as the C(range).', 'When set to C(_default), it will use the C(level) portion of the policy if available.'], 'default': 's0'}",
    "serole": "{'description': ['The role part of the SELinux file context.', 'When set to C(_default), it will use the C(role) portion of the policy if available.']}",
    "setype": "{'description': ['The type part of the SELinux file context.', 'When set to C(_default), it will use the C(type) portion of the policy if available.']}",
    "seuser": "{'description': ['The user part of the SELinux file context.', 'By default it uses the C(system) policy, where applicable.', 'When set to C(_default), it will use the C(user) portion of the policy if available.']}",
    "src": "{'description': ['An already existing directory full of source files.'], 'required': True}",
    "unsafe_writes": "{'description': ['Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target file.', 'By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted files, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.', "This option allows Ansible to fall back to unsafe methods of updating files when atomic operations fail (however, it doesn't force Ansible to perform unsafe writes).", 'IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "validate": "{'description': ['The validation command to run before copying into place.', "The path to the file to validate is passed in via '%s' which must be present as in the sshd example below.", "The command is passed securely so shell features like expansion and pipes won't work."], 'version_added': '2.0'}",
}
```

## Examples


``` yaml

- name: Assemble from fragments from a directory
  assemble:
    src: /etc/someapp/fragments
    dest: /etc/someapp/someapp.conf

- name: Inserted provided delimiter in between each fragment
  assemble:
    src: /etc/someapp/fragments
    dest: /etc/someapp/someapp.conf
    delimiter: '### START FRAGMENT ###'

- name: Assemble a new "sshd_config" file into place, after passing validation with sshd
  assemble:
    src: /etc/ssh/conf.d/
    dest: /etc/ssh/sshd_config
    validate: '/usr/sbin/sshd -t -f %s'

```

## License

TODO

## Author Information
  - ['Stephen Fromm (@sfromm)']
