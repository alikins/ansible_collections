# Ansible module: ansible.module_unarchive


Unpacks an archive after (optionally) copying it from the local machine

## Description

The C(unarchive) module unpacks an archive.
By default, it will copy the source file from the local system to the target before unpacking.
Set C(remote_src=yes) to unpack an archive which already exists on the target.
For Windows targets, use the M(win_unzip) module instead.
If checksum validation is desired, use M(get_url) or M(uri) instead to fetch the file and set C(remote_src=yes).

## Requirements

TODO

## Arguments

``` json
{
    "attributes": "{'description': ['The attributes the resulting file or directory should have.', 'To get supported flags look at the man page for I(chattr) on the target system.', 'This string should contain the attributes in the same order as the one displayed by I(lsattr).', 'The C(=) operator is assumed as default, otherwise C(+) or C(-) operators need to be included in the string.'], 'aliases': ['attr'], 'version_added': '2.3'}",
    "copy": "{'description': ["If true, the file is copied from local 'master' to the target machine, otherwise, the plugin will look for src archive at the target machine.", 'This option has been deprecated in favor of C(remote_src).', 'This option is mutually exclusive with C(remote_src).'], 'type': 'bool', 'default': True}",
    "creates": "{'description': ['If the specified absolute path (file or directory) already exists, this step will B(not) be run.'], 'version_added': '1.6'}",
    "decrypt": "{'description': ['This option controls the autodecryption of source files using vault.'], 'required': False, 'type': 'bool', 'default': True, 'version_added': '2.4'}",
    "dest": "{'description': ['Remote absolute path where the archive should be unpacked.'], 'required': True}",
    "exclude": "{'description': ['List the directory and file entries that you would like to exclude from the unarchive action.'], 'version_added': '2.1'}",
    "extra_opts": "{'description': ['Specify additional options by passing in an array.'], 'default': '', 'version_added': '2.1'}",
    "group": "{'description': ['Name of the group that should own the file/directory, as would be fed to I(chown).']}",
    "keep_newer": "{'description': ['Do not replace existing files that are newer than files from the archive.'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "list_files": "{'description': ['If set to True, return the list of files that are contained in the tarball.'], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
    "mode": "{'description': ['The permissions the resulting file or directory should have.', "For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like C(0644) or C(01777)) or quote it (like C('644') or C('1777')) so Ansible receives a string and can do its own conversion from string into number.", 'Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.', 'As of version 1.8, the mode may be specified as a symbolic mode (for example, C(u+rwx) or C(u=rw,g=r,o=r)).', 'As of version 2.6, the mode may also be the special string C(preserve).', 'When set to C(preserve) the file will be given the same permissions as the source file.']}",
    "owner": "{'description': ['Name of the user that should own the file/directory, as would be fed to I(chown).']}",
    "remote_src": "{'description': ['Set to C(yes) to indicate the archived file is already on the remote system and not local to the Ansible controller.', 'This option is mutually exclusive with C(copy).'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "selevel": "{'description': ['The level part of the SELinux file context.', 'This is the MLS/MCS attribute, sometimes known as the C(range).', 'When set to C(_default), it will use the C(level) portion of the policy if available.'], 'default': 's0'}",
    "serole": "{'description': ['The role part of the SELinux file context.', 'When set to C(_default), it will use the C(role) portion of the policy if available.']}",
    "setype": "{'description': ['The type part of the SELinux file context.', 'When set to C(_default), it will use the C(type) portion of the policy if available.']}",
    "seuser": "{'description': ['The user part of the SELinux file context.', 'By default it uses the C(system) policy, where applicable.', 'When set to C(_default), it will use the C(user) portion of the policy if available.']}",
    "src": "{'description': ['If C(remote_src=no) (default), local path to archive file to copy to the target server; can be absolute or relative. If C(remote_src=yes), path on the target server to existing archive file to unpack.', 'If C(remote_src=yes) and C(src) contains C(://), the remote machine will download the file from the URL first. (version_added 2.0). This is only for simple cases, for full download support use the M(get_url) module.'], 'required': True}",
    "unsafe_writes": "{'description': ['Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target file.', 'By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted files, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.', "This option allows Ansible to fall back to unsafe methods of updating files when atomic operations fail (however, it doesn't force Ansible to perform unsafe writes).", 'IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "validate_certs": "{'description': ['This only applies if using a https URL as the source of the file.', 'This should only set to C(no) used on personally controlled sites using self-signed certificate.', 'Prior to 2.2 the code worked as if this was set to C(yes).'], 'type': 'bool', 'default': True, 'version_added': '2.2'}",
}
```

## Examples


``` yaml

- name: Extract foo.tgz into /var/lib/foo
  unarchive:
    src: foo.tgz
    dest: /var/lib/foo

- name: Unarchive a file that is already on the remote machine
  unarchive:
    src: /tmp/foo.zip
    dest: /usr/local/bin
    remote_src: yes

- name: Unarchive a file that needs to be downloaded (added in 2.0)
  unarchive:
    src: https://example.com/example.zip
    dest: /usr/local/bin
    remote_src: yes

- name: Unarchive a file with extra options
  unarchive:
    src: /tmp/foo.zip
    dest: /usr/local/bin
    extra_opts:
    - --transform
    - s/^xxx/yyy/

```

## License

TODO

## Author Information
  - ['Michael DeHaan']
