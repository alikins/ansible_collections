# Ansible module: ansible.module_copy


Copies files to remote locations

## Description

The C(copy) module copies a file from the local or remote machine to a location on the remote machine. Use the M(fetch) module to copy files from remote locations to the local box. If you need variable interpolation in copied files, use the M(template) module.
For Windows targets, use the M(win_copy) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "attributes": "{'description': ['The attributes the resulting file or directory should have.', 'To get supported flags look at the man page for I(chattr) on the target system.', 'This string should contain the attributes in the same order as the one displayed by I(lsattr).', 'The C(=) operator is assumed as default, otherwise C(+) or C(-) operators need to be included in the string.'], 'aliases': ['attr'], 'version_added': '2.3'}",
    "backup": "{'description': ['Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.'], 'type': 'bool', 'default': False}",
    "checksum": "{'description': ['SHA1 checksum of the file being transferred. Used to validate that the copy of the file was successful.', 'If this is not provided, ansible will use the local calculated checksum of the src file.'], 'version_added': '2.5'}",
    "content": "{'description': ['When used instead of I(src), sets the contents of a file directly to the specified value. For anything advanced or with formatting also look at the template module.']}",
    "decrypt": "{'description': ['This option controls the autodecryption of source files using vault.'], 'required': False, 'type': 'bool', 'default': True, 'version_added': '2.4'}",
    "dest": "{'description': ['Remote absolute path where the file should be copied to. If I(src) is a directory, this must be a directory too. If I(dest) is a nonexistent path and if either I(dest) ends with "/" or I(src) is a directory, I(dest) is created. If I(src) and I(dest) are files, the parent directory of I(dest) isn\'t created: the task fails if it doesn\'t already exist.'], 'required': True}",
    "directory_mode": "{'description': ['When doing a recursive copy set the mode for the directories. If this is not set we will use the system defaults. The mode is only set on directories which are newly created, and will not affect those that already existed.'], 'version_added': '1.5'}",
    "follow": "{'description': ['This flag indicates that filesystem links in the destination, if they exist, should be followed.'], 'type': 'bool', 'default': False, 'version_added': '1.8'}",
    "force": "{'description': ['the default is C(yes), which will replace the remote file when contents are different than the source. If C(no), the file will only be transferred if the destination does not exist.'], 'type': 'bool', 'default': True, 'aliases': ['thirsty']}",
    "group": "{'description': ['Name of the group that should own the file/directory, as would be fed to I(chown).']}",
    "local_follow": "{'description': ['This flag indicates that filesystem links in the source tree, if they exist, should be followed.'], 'type': 'bool', 'default': True, 'version_added': '2.4'}",
    "mode": "{'description': ["Mode the file or directory should be. For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like C(0644) or C(01777)) or quote it (like C('644') or C('1777')) so Ansible receives a string and can do its own conversion from string into number.  Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.  As of version 1.8, the mode may be specified as a symbolic mode (for example, C(u+rwx) or C(u=rw,g=r,o=r)).  As of version 2.3, the mode may also be the special string C(preserve).  C(preserve) means that the file will be given the same permissions as the source file."]}",
    "owner": "{'description': ['Name of the user that should own the file/directory, as would be fed to I(chown).']}",
    "remote_src": "{'description': ['If C(no), it will search for I(src) at originating/master machine.', 'If C(yes) it will go to the remote/target machine for the I(src). Default is C(no).', 'Currently I(remote_src) does not support recursive copying.', 'I(remote_src) only works with C(mode=preserve) as of version 2.6.'], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
    "selevel": "{'description': ['The level part of the SELinux file context.', 'This is the MLS/MCS attribute, sometimes known as the C(range).', 'When set to C(_default), it will use the C(level) portion of the policy if available.'], 'default': 's0'}",
    "serole": "{'description': ['The role part of the SELinux file context.', 'When set to C(_default), it will use the C(role) portion of the policy if available.']}",
    "setype": "{'description': ['The type part of the SELinux file context.', 'When set to C(_default), it will use the C(type) portion of the policy if available.']}",
    "seuser": "{'description': ['The user part of the SELinux file context.', 'By default it uses the C(system) policy, where applicable.', 'When set to C(_default), it will use the C(user) portion of the policy if available.']}",
    "src": "{'description': ['Local path to a file to copy to the remote server; can be absolute or relative. If path is a directory, it is copied recursively. In this case, if path ends with "/", only inside contents of that directory are copied to destination. Otherwise, if it does not end with "/", the directory itself with all contents is copied. This behavior is similar to Rsync.']}",
    "unsafe_writes": "{'description': ['Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target file.', 'By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted files, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.', "This option allows Ansible to fall back to unsafe methods of updating files when atomic operations fail (however, it doesn't force Ansible to perform unsafe writes).", 'IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "validate": "{'description': ['The validation command to run before copying into place.', "The path to the file to validate is passed in via '%s' which must be present as in the examples below.", 'The command is passed securely so shell features like expansion and pipes will not work.']}",
}
```

## Examples


``` yaml

- name: example copying file with owner and permissions
  copy:
    src: /srv/myfiles/foo.conf
    dest: /etc/foo.conf
    owner: foo
    group: foo
    mode: 0644

- name: The same example as above, but using a symbolic mode equivalent to 0644
  copy:
    src: /srv/myfiles/foo.conf
    dest: /etc/foo.conf
    owner: foo
    group: foo
    mode: u=rw,g=r,o=r

- name: Another symbolic mode example, adding some permissions and removing others
  copy:
    src: /srv/myfiles/foo.conf
    dest: /etc/foo.conf
    owner: foo
    group: foo
    mode: u+rw,g-wx,o-rwx

- name: Copy a new "ntp.conf file into place, backing up the original if it differs from the copied version
  copy:
    src: /mine/ntp.conf
    dest: /etc/ntp.conf
    owner: root
    group: root
    mode: 0644
    backup: yes

- name: Copy a new "sudoers" file into place, after passing validation with visudo
  copy:
    src: /mine/sudoers
    dest: /etc/sudoers
    validate: /usr/sbin/visudo -cf %s

- name: Copy a "sudoers" file on the remote machine for editing
  copy:
    src: /etc/sudoers
    dest: /etc/sudoers.edit
    remote_src: yes
    validate: /usr/sbin/visudo -cf %s

- name: Copy using the 'content' for inline data
  copy:
    content: '# This file was moved to /etc/other.conf'
    dest: /etc/mine.conf

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan']
  - ['Ansible Core Team', 'Michael DeHaan']
