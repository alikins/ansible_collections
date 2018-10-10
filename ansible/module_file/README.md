# Ansible module: ansible.module_file


Manage files and file properties

## Description

Set attributes of files, symlinks or directories.
Alternatively, remove files, symlinks or directories.
Many other modules support the same options as the C(file) module - including M(copy), M(template), and M(assemble).
For Windows targets, use the M(win_file) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "access_time": "{'description': ["This parameter indicates the time the file's access time should be set to.", 'Should be C(preserve) when no modification is required, C(YYYYMMDDHHMM.SS) when using default time format, or C(now).', 'Default is C(None) meaning that C(preserve) is the default for C(state=[file,directory,link,hard]) and C(now) is default for C(state=touch).'], 'version_added': '2.7'}",
    "access_time_format": "{'description': ['When used with C(access_time), indicates the time format that must be used.', 'Based on default Python format (see time.strftime doc).'], 'default': '%Y%m%d%H%M.%S', 'version_added': '2.7'}",
    "attributes": "{'description': ['The attributes the resulting file or directory should have.', 'To get supported flags look at the man page for I(chattr) on the target system.', 'This string should contain the attributes in the same order as the one displayed by I(lsattr).', 'The C(=) operator is assumed as default, otherwise C(+) or C(-) operators need to be included in the string.'], 'aliases': ['attr'], 'version_added': '2.3'}",
    "follow": "{'description': ['This flag indicates that filesystem links, if they exist, should be followed.', 'Previous to Ansible 2.5, this was C(no) by default.'], 'type': 'bool', 'default': True, 'version_added': '1.8'}",
    "force": "{'description': ['Force the creation of the symlinks in two cases: the source file does not exist (but will appear later); the destination exists and is a file (so, we need to unlink the C(path) file and create symlink to the C(src) file in place of it).\n'], 'type': 'bool', 'default': False}",
    "group": "{'description': ['Name of the group that should own the file/directory, as would be fed to I(chown).']}",
    "mode": "{'description': ['The permissions the resulting file or directory should have.', "For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like C(0644) or C(01777)) or quote it (like C('644') or C('1777')) so Ansible receives a string and can do its own conversion from string into number.", 'Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.', 'As of version 1.8, the mode may be specified as a symbolic mode (for example, C(u+rwx) or C(u=rw,g=r,o=r)).', 'As of version 2.6, the mode may also be the special string C(preserve).', 'When set to C(preserve) the file will be given the same permissions as the source file.']}",
    "modification_time": "{'description': ["This parameter indicates the time the file's modification time should be set to.", 'Should be C(preserve) when no modification is required, C(YYYYMMDDHHMM.SS) when using default time format, or C(now).', 'Default is None meaning that C(preserve) is the default for C(state=[file,directory,link,hard]) and C(now) is default for C(state=touch).'], 'version_added': '2.7'}",
    "modification_time_format": "{'description': ['When used with C(modification_time), indicates the time format that must be used.', 'Based on default Python format (see time.strftime doc).'], 'default': '%Y%m%d%H%M.%S', 'version_added': '2.7'}",
    "owner": "{'description': ['Name of the user that should own the file/directory, as would be fed to I(chown).']}",
    "path": "{'description': ['Path to the file being managed.'], 'required': True, 'aliases': ['dest', 'name']}",
    "recurse": "{'description': ['Recursively set the specified file attributes.', 'This applies only to C(state=directory).'], 'type': 'bool', 'default': False}",
    "selevel": "{'description': ['The level part of the SELinux file context.', 'This is the MLS/MCS attribute, sometimes known as the C(range).', 'When set to C(_default), it will use the C(level) portion of the policy if available.'], 'default': 's0'}",
    "serole": "{'description': ['The role part of the SELinux file context.', 'When set to C(_default), it will use the C(role) portion of the policy if available.']}",
    "setype": "{'description': ['The type part of the SELinux file context.', 'When set to C(_default), it will use the C(type) portion of the policy if available.']}",
    "seuser": "{'description': ['The user part of the SELinux file context.', 'By default it uses the C(system) policy, where applicable.', 'When set to C(_default), it will use the C(user) portion of the policy if available.']}",
    "src": "{'description': ['Path of the file to link to.', 'This applies only to C(state=link) and C(state=hard).', 'Will accept absolute, relative and non-existing paths.', 'Relative paths are relative to the file being created (C(path)) which is how the Unix command C(ln -s SRC DEST) treats relative paths.']}",
    "state": "{'description': ['If C(absent), directories will be recursively deleted, and files or symlinks will be unlinked. Note that C(absent) will not cause C(file) to fail if the C(path) does not exist as the state did not change.', 'If C(directory), all intermediate subdirectories will be created if they do not exist. Since Ansible 1.7 they will be created with the supplied permissions.', 'If C(file), the file will NOT be created if it does not exist; see the C(touch) value or the M(copy) or M(template) module if you want that behavior.', 'If C(hard), the hard link will be created or changed.', 'If C(link), the symbolic link will be created or changed.', 'If C(touch) (new in 1.4), an empty file will be created if the C(path) does not exist, while an existing file or directory will receive updated file access and modification times (similar to the way C(touch) works from the command line).'], 'default': 'file', 'choices': ['absent', 'directory', 'file', 'hard', 'link', 'touch']}",
    "unsafe_writes": "{'description': ['Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target file.', 'By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted files, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.', "This option allows Ansible to fall back to unsafe methods of updating files when atomic operations fail (however, it doesn't force Ansible to perform unsafe writes).", 'IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
}
```

## Examples


``` yaml

- name: Change file ownership, group and permissions
  file:
    path: /etc/foo.conf
    owner: foo
    group: foo
    # When specifying mode using octal numbers, add a leading 0
    mode: 0644

- name: Create an insecure file
  file:
    path: /work
    owner: root
    group: root
    # Or use quotes instead
    mode: '1777'

- name: Create a symbolic link
  file:
    src: /file/to/link/to
    dest: /path/to/symlink
    owner: foo
    group: foo
    state: link

- name: Create two hard links
  file:
    src: '/tmp/{{ item.src }}'
    dest: '{{ item.dest }}'
    state: link
  with_items:
    - { src: x, dest: y }
    - { src: z, dest: k }

- name: Touch a file, using symbolic modes to set the permissions (equivalent to 0644)
  file:
    path: /etc/foo.conf
    state: touch
    mode: u=rw,g=r,o=r

- name: Touch the same file, but add/remove some permissions
  file:
    path: /etc/foo.conf
    state: touch
    mode: u+rw,g-wx,o-rwx

- name: Touch again the same file, but dont change times this makes the task idempotent
  file:
    path: /etc/foo.conf
    state: touch
    mode: u+rw,g-wx,o-rwx
    modification_time: preserve
    access_time: preserve

- name: Create a directory if it does not exist
  file:
    path: /etc/some_directory
    state: directory
    mode: 0755

- name: Update modification and access time of given file
  file:
    path: /etc/some_file
    state: file
    modification_time: now
    access_time: now

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan']
  - ['Ansible Core Team', 'Michael DeHaan']
