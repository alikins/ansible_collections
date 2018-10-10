# Ansible module: ansible.module_template


Template a file out to a remote server

## Description

Templates are processed by the L(Jinja2 templating language,http://jinja.pocoo.org/docs/).
Documentation on the template formatting can be found in the L(Template Designer Documentation,http://jinja.pocoo.org/docs/templates/).
The six additional variables, listed below, can be used in template.
C(ansible_managed) (configurable via the C(defaults) section of C(ansible.cfg)) contains a string which can be used to describe the template name, host, modification time of the template file and the owner uid.
C(template_host) contains the node name of the template's machine.
C(template_uid) is the numeric user id of the owner.
C(template_path) is the path of the template.
C(template_fullpath) is the absolute path of the template.
C(template_run_date) is the date that the template was rendered.

## Requirements

TODO

## Arguments

``` json
{
    "attributes": "{'description': ['The attributes the resulting file or directory should have.', 'To get supported flags look at the man page for I(chattr) on the target system.', 'This string should contain the attributes in the same order as the one displayed by I(lsattr).', 'The C(=) operator is assumed as default, otherwise C(+) or C(-) operators need to be included in the string.'], 'aliases': ['attr'], 'version_added': '2.3'}",
    "backup": "{'description': ['Determine whether a backup should be created.', 'When set to C(yes), create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.'], 'type': 'bool', 'default': False}",
    "block_end_string": "{'description': ['The string marking the end of a block.'], 'default': '%}', 'version_added': '2.4'}",
    "block_start_string": "{'description': ['The string marking the beginning of a block.'], 'default': '{%', 'version_added': '2.4'}",
    "dest": "{'description': ['Location to render the template to on the remote machine.'], 'required': True}",
    "follow": "{'description': ['Determine whether symbolic links should be followed.', 'When set to C(yes) symbolic links will be followed, if they exist.', 'When set to C(no) symbolic links will not be followed.', 'Previous to Ansible 2.4, this was hardcoded as C(yes).'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "force": "{'description': ['Determine when the file is being transferred if the destination already exists.', 'When set to C(yes), replace the remote file when contents are different than the source.', 'When set to C(no), the file will only be transferred if the destination does not exist.'], 'type': 'bool', 'default': True}",
    "group": "{'description': ['Name of the group that should own the file/directory, as would be fed to I(chown).']}",
    "lstrip_blocks": "{'description': ['Determine when leading spaces and tabs should be stripped.', 'When set to C(yes) leading spaces and tabs are stripped from the start of a line to a block.', 'This functionality requires Jinja v2.7 or newer.'], 'type': 'bool', 'default': False, 'version_added': '2.6'}",
    "mode": "{'description': ['The permissions the resulting file or directory should have.', "For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like C(0644) or C(01777)) or quote it (like C('644') or C('1777')) so Ansible receives a string and can do its own conversion from string into number.", 'Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.', 'As of version 1.8, the mode may be specified as a symbolic mode (for example, C(u+rwx) or C(u=rw,g=r,o=r)).', 'As of version 2.6, the mode may also be the special string C(preserve).', 'When set to C(preserve) the file will be given the same permissions as the source file.']}",
    "newline_sequence": "{'description': ['Specify the newline sequence to use for templating files.'], 'choices': ['\\n', '\\r', '\\r\\n'], 'default': '\\n', 'version_added': '2.4'}",
    "output_encoding": "{'description': ['Overrides the encoding used to write the template file defined by C(dest).', 'It defaults to C(utf-8), but any encoding supported by python can be used.', 'The source template file must always be encoded using C(utf-8), for homogeneity.'], 'default': 'utf-8', 'version_added': '2.7'}",
    "owner": "{'description': ['Name of the user that should own the file/directory, as would be fed to I(chown).']}",
    "selevel": "{'description': ['The level part of the SELinux file context.', 'This is the MLS/MCS attribute, sometimes known as the C(range).', 'When set to C(_default), it will use the C(level) portion of the policy if available.'], 'default': 's0'}",
    "serole": "{'description': ['The role part of the SELinux file context.', 'When set to C(_default), it will use the C(role) portion of the policy if available.']}",
    "setype": "{'description': ['The type part of the SELinux file context.', 'When set to C(_default), it will use the C(type) portion of the policy if available.']}",
    "seuser": "{'description': ['The user part of the SELinux file context.', 'By default it uses the C(system) policy, where applicable.', 'When set to C(_default), it will use the C(user) portion of the policy if available.']}",
    "src": "{'description': ['Path of a Jinja2 formatted template on the Ansible controller.', 'This can be a relative or an absolute path.'], 'required': True}",
    "trim_blocks": "{'description': ['Determine when newlines should be removed from blocks.', 'When set to C(yes) the first newline after a block is removed (block, not variable tag!).'], 'type': 'bool', 'default': True, 'version_added': '2.4'}",
    "unsafe_writes": "{'description': ['Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target file.', 'By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted files, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.', "This option allows Ansible to fall back to unsafe methods of updating files when atomic operations fail (however, it doesn't force Ansible to perform unsafe writes).", 'IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "validate": "{'description': ['The validation command to run before copying into place.', "The path to the file to validate is passed in via '%s' which must be present as in the examples below.", 'The command is passed securely so shell features like expansion and pipes will not work.']}",
    "variable_end_string": "{'description': ['The string marking the end of a print statement.'], 'default': '}}', 'version_added': '2.4'}",
    "variable_start_string": "{'description': ['The string marking the beginning of a print statement.'], 'default': '{{', 'version_added': '2.4'}",
}
```

## Examples


``` yaml

- name: Template a file to /etc/files.conf
  template:
    src: /mytemplates/foo.j2
    dest: /etc/file.conf
    owner: bin
    group: wheel
    mode: '0644'

- name: Template a file, using symbolic modes (equivalent to 0644)
  template:
    src: /mytemplates/foo.j2
    dest: /etc/file.conf
    owner: bin
    group: wheel
    mode: "u=rw,g=r,o=r"

- name: Create a DOS-style text file from a template
  template:
    src: config.ini.j2
    dest: /share/windows/config.ini
    newline_sequence: '\r\n'

- name: Copy a new sudoers file into place, after passing validation with visudo
  template:
    src: /mine/sudoers
    dest: /etc/sudoers
    validate: '/usr/sbin/visudo -cf %s'

- name: Update sshd configuration safely, avoid locking yourself out
  template:
    src: etc/ssh/sshd_config.j2
    dest: /etc/ssh/sshd_config
    owner: root
    group: root
    mode: '0600'
    validate: /usr/sbin/sshd -t -f %s
    backup: yes

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan']
  - ['Ansible Core Team', 'Michael DeHaan']
