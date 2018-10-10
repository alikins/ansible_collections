# Ansible module: ansible.module_lineinfile


Manage lines in text files

## Description

This module ensures a particular line is in a file, or replace an existing line using a back-referenced regular expression.
This is primarily useful when you want to change a single line in a file only. See the M(replace) module if you want to change multiple, similar lines or check M(blockinfile) if you want to insert/update/remove a block of lines in a file. For other cases, see the M(copy) or M(template) modules.

## Requirements

TODO

## Arguments

``` json
{
    "attributes": "{'description': ['The attributes the resulting file or directory should have.', 'To get supported flags look at the man page for I(chattr) on the target system.', 'This string should contain the attributes in the same order as the one displayed by I(lsattr).', 'The C(=) operator is assumed as default, otherwise C(+) or C(-) operators need to be included in the string.'], 'aliases': ['attr'], 'version_added': '2.3'}",
    "backrefs": "{'description': ["Used with C(state=present). If set, C(line) can contain backreferences (both positional and named) that will get populated if the C(regexp) matches. This flag changes the operation of the module slightly; C(insertbefore) and C(insertafter) will be ignored, and if the C(regexp) doesn't match anywhere in the file, the file will be left unchanged. If the C(regexp) does match, the last matching line will be replaced by the expanded line parameter."], 'type': 'bool', 'default': False}",
    "backup": "{'description': ['Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.'], 'type': 'bool', 'default': False}",
    "create": "{'description': ['Used with C(state=present). If specified, the file will be created if it does not already exist. By default it will fail if the file is missing.'], 'type': 'bool', 'default': False}",
    "firstmatch": "{'description': ['Used with C(insertafter) or C(insertbefore). If set, C(insertafter) and C(inserbefore) find a first line has regular expression matches.'], 'type': 'bool', 'default': False, 'version_added': '2.5'}",
    "group": "{'description': ['Name of the group that should own the file/directory, as would be fed to I(chown).']}",
    "insertafter": "{'description': ['Used with C(state=present). If specified, the line will be inserted after the last match of specified regular expression. If the first match is required, use(firstmatch=yes). A special value is available; C(EOF) for inserting the line at the end of the file. If specified regular expression has no matches, EOF will be used instead. If regular expressions are passed to both C(regexp) and C(insertafter), C(insertafter) is only honored if no match for C(regexp) is found. May not be used with C(backrefs).'], 'choices': ['EOF', '*regex*'], 'default': 'EOF'}",
    "insertbefore": "{'description': ['Used with C(state=present). If specified, the line will be inserted before the last match of specified regular expression. If the first match is required, use(firstmatch=yes). A value is available; C(BOF) for inserting the line at the beginning of the file. If specified regular expression has no matches, the line will be inserted at the end of the file. If regular expressions are passed to both C(regexp) and C(insertbefore), C(insertbefore) is only honored if no match for C(regexp) is found. May not be used with C(backrefs).'], 'choices': ['BOF', '*regex*']}",
    "line": "{'description': ['Required for C(state=present). The line to insert/replace into the file. If C(backrefs) is set, may contain backreferences that will get expanded with the C(regexp) capture groups if the regexp matches.']}",
    "mode": "{'description': ['The permissions the resulting file or directory should have.', "For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like C(0644) or C(01777)) or quote it (like C('644') or C('1777')) so Ansible receives a string and can do its own conversion from string into number.", 'Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.', 'As of version 1.8, the mode may be specified as a symbolic mode (for example, C(u+rwx) or C(u=rw,g=r,o=r)).', 'As of version 2.6, the mode may also be the special string C(preserve).', 'When set to C(preserve) the file will be given the same permissions as the source file.']}",
    "others": "{'description': ['All arguments accepted by the M(file) module also work here.']}",
    "owner": "{'description': ['Name of the user that should own the file/directory, as would be fed to I(chown).']}",
    "path": "{'description': ['The file to modify.', 'Before 2.3 this option was only usable as I(dest), I(destfile) and I(name).'], 'aliases': ['dest', 'destfile', 'name'], 'required': True}",
    "regexp": "{'aliases': ['regex'], 'description': ['The regular expression to look for in every line of the file.', 'For C(state=present), the pattern to replace if found. Only the last line found will be replaced.', 'For C(state=absent), the pattern of the line(s) to remove.', 'If the regular expression is not matched, the line will be added to the file in keeping with`insertbefore` or `insertafter` settings.', 'Uses Python regular expressions. See U(http://docs.python.org/2/library/re.html).'], 'version_added': '1.7'}",
    "selevel": "{'description': ['The level part of the SELinux file context.', 'This is the MLS/MCS attribute, sometimes known as the C(range).', 'When set to C(_default), it will use the C(level) portion of the policy if available.'], 'default': 's0'}",
    "serole": "{'description': ['The role part of the SELinux file context.', 'When set to C(_default), it will use the C(role) portion of the policy if available.']}",
    "setype": "{'description': ['The type part of the SELinux file context.', 'When set to C(_default), it will use the C(type) portion of the policy if available.']}",
    "seuser": "{'description': ['The user part of the SELinux file context.', 'By default it uses the C(system) policy, where applicable.', 'When set to C(_default), it will use the C(user) portion of the policy if available.']}",
    "state": "{'description': ['Whether the line should be there or not.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "unsafe_writes": "{'description': ['Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target file.', 'By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted files, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.', "This option allows Ansible to fall back to unsafe methods of updating files when atomic operations fail (however, it doesn't force Ansible to perform unsafe writes).", 'IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "validate": "{'description': ['The validation command to run before copying into place.', "The path to the file to validate is passed in via '%s' which must be present as in the examples below.", 'The command is passed securely so shell features like expansion and pipes will not work.']}",
}
```

## Examples


``` yaml

# Before 2.3, option 'dest', 'destfile' or 'name' was used instead of 'path'
- lineinfile:
    path: /etc/selinux/config
    regexp: '^SELINUX='
    line: 'SELINUX=enforcing'

- lineinfile:
    path: /etc/sudoers
    state: absent
    regexp: '^%wheel'

# Searches for a line that begins with 127.0.0.1 and replaces it with the value of the 'line' parameter
- lineinfile:
    path: /etc/hosts
    regexp: '^127\.0\.0\.1'
    line: '127.0.0.1 localhost'
    owner: root
    group: root
    mode: 0644

- lineinfile:
    path: /etc/httpd/conf/httpd.conf
    regexp: '^Listen '
    insertafter: '^#Listen '
    line: 'Listen 8080'

- lineinfile:
    path: /etc/services
    regexp: '^# port for http'
    insertbefore: '^www.*80/tcp'
    line: '# port for http by default'

# Add a line to a file if the file does not exist, without passing regexp
- lineinfile:
    path: /tmp/testfile
    line: '192.168.1.99 foo.lab.net foo'
    create: yes

# Fully quoted because of the ': ' on the line. See the Gotchas in the YAML docs.
- lineinfile:
    path: /etc/sudoers
    state: present
    regexp: '^%wheel\s'
    line: '%wheel ALL=(ALL) NOPASSWD: ALL'

# Yaml requires escaping backslashes in double quotes but not in single quotes
- lineinfile:
    path: /opt/jboss-as/bin/standalone.conf
    regexp: '^(.*)Xms(\\d+)m(.*)$'
    line: '\1Xms${xms}m\3'
    backrefs: yes

# Validate the sudoers file before saving
- lineinfile:
    path: /etc/sudoers
    state: present
    regexp: '^%ADMIN ALL='
    line: '%ADMIN ALL=(ALL) NOPASSWD: ALL'
    validate: '/usr/sbin/visudo -cf %s'

```

## License

TODO

## Author Information
  - ['Daniel Hokka Zakrissoni (@dhozac)', 'Ahti Kitsik (@ahtik)']
  - ['Daniel Hokka Zakrissoni (@dhozac)', 'Ahti Kitsik (@ahtik)']
