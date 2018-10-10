# Ansible module: ansible.module_replace


Replace all instances of a particular string in a file using a back-referenced regular expression

## Description

This module will replace all instances of a pattern within a file.
It is up to the user to maintain idempotence by ensuring that the same pattern would never match any replacements made.

## Requirements

TODO

## Arguments

``` json
{
    "after": "{'description': ['If specified, the line after the replace/remove will start. Can be used in combination with C(before). Uses Python regular expressions; see U(http://docs.python.org/2/library/re.html).'], 'version_added': '2.4'}",
    "attributes": "{'description': ['The attributes the resulting file or directory should have.', 'To get supported flags look at the man page for I(chattr) on the target system.', 'This string should contain the attributes in the same order as the one displayed by I(lsattr).', 'The C(=) operator is assumed as default, otherwise C(+) or C(-) operators need to be included in the string.'], 'aliases': ['attr'], 'version_added': '2.3'}",
    "backup": "{'description': ['Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.'], 'type': 'bool', 'default': False}",
    "before": "{'description': ['If specified, the line before the replace/remove will occur. Can be used in combination with C(after). Uses Python regular expressions; see U(http://docs.python.org/2/library/re.html).'], 'version_added': '2.4'}",
    "encoding": "{'description': ['The character encoding for reading and writing the file.'], 'default': 'utf-8', 'version_added': '2.4'}",
    "group": "{'description': ['Name of the group that should own the file/directory, as would be fed to I(chown).']}",
    "mode": "{'description': ['The permissions the resulting file or directory should have.', "For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like C(0644) or C(01777)) or quote it (like C('644') or C('1777')) so Ansible receives a string and can do its own conversion from string into number.", 'Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.', 'As of version 1.8, the mode may be specified as a symbolic mode (for example, C(u+rwx) or C(u=rw,g=r,o=r)).', 'As of version 2.6, the mode may also be the special string C(preserve).', 'When set to C(preserve) the file will be given the same permissions as the source file.']}",
    "others": "{'description': ['All arguments accepted by the M(file) module also work here.']}",
    "owner": "{'description': ['Name of the user that should own the file/directory, as would be fed to I(chown).']}",
    "path": "{'description': ['The file to modify.', 'Before 2.3 this option was only usable as I(dest), I(destfile) and I(name).'], 'aliases': ['dest', 'destfile', 'name'], 'required': True}",
    "regexp": "{'description': ['The regular expression to look for in the contents of the file. Uses Python regular expressions; see U(http://docs.python.org/2/library/re.html). Uses MULTILINE mode, which means C(^) and C($) match the beginning and end of the file, as well as the beginning and end respectively of I(each line) of the file.', 'Does not use DOTALL, which means the C(.) special character matches any character I(except newlines). A common mistake is to assume that a negated character set like C([^#]) will also not match newlines. In order to exclude newlines, they must be added to the set like C([^#\\n]).', 'Note that, as of ansible 2, short form tasks should have any escape sequences backslash-escaped in order to prevent them being parsed as string literal escapes. See the examples.'], 'required': True}",
    "replace": "{'description': ['The string to replace regexp matches. May contain backreferences that will get expanded with the regexp capture groups if the regexp matches. If not set, matches are removed entirely.']}",
    "selevel": "{'description': ['The level part of the SELinux file context.', 'This is the MLS/MCS attribute, sometimes known as the C(range).', 'When set to C(_default), it will use the C(level) portion of the policy if available.'], 'default': 's0'}",
    "serole": "{'description': ['The role part of the SELinux file context.', 'When set to C(_default), it will use the C(role) portion of the policy if available.']}",
    "setype": "{'description': ['The type part of the SELinux file context.', 'When set to C(_default), it will use the C(type) portion of the policy if available.']}",
    "seuser": "{'description': ['The user part of the SELinux file context.', 'By default it uses the C(system) policy, where applicable.', 'When set to C(_default), it will use the C(user) portion of the policy if available.']}",
    "unsafe_writes": "{'description': ['Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target file.', 'By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted files, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.', "This option allows Ansible to fall back to unsafe methods of updating files when atomic operations fail (however, it doesn't force Ansible to perform unsafe writes).", 'IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "validate": "{'description': ['The validation command to run before copying into place.', "The path to the file to validate is passed in via '%s' which must be present as in the examples below.", 'The command is passed securely so shell features like expansion and pipes will not work.']}",
}
```

## Examples


``` yaml

# Before 2.3, option 'dest', 'destfile' or 'name' was used instead of 'path'
- replace:
    path: /etc/hosts
    regexp: '(\s+)old\.host\.name(\s+.*)?$'
    replace: '\1new.host.name\2'
    backup: yes

# Replace after the expression till the end of the file (requires >=2.4)
- replace:
    path: /etc/hosts
    regexp: '(\s+)old\.host\.name(\s+.*)?$'
    replace: '\1new.host.name\2'
    after: 'Start after line.*'
    backup: yes

# Replace before the expression till the begin of the file (requires >=2.4)
- replace:
    path: /etc/hosts
    regexp: '(\s+)old\.host\.name(\s+.*)?$'
    replace: '\1new.host.name\2'
    before: 'Start before line.*'
    backup: yes

# Replace between the expressions (requires >=2.4)
- replace:
    path: /etc/hosts
    regexp: '(\s+)old\.host\.name(\s+.*)?$'
    replace: '\1new.host.name\2'
    after: 'Start after line.*'
    before: 'Start before line.*'
    backup: yes

- replace:
    path: /home/jdoe/.ssh/known_hosts
    regexp: '^old\.host\.name[^\n]*\n'
    owner: jdoe
    group: jdoe
    mode: 0644

- replace:
    path: /etc/apache/ports
    regexp: '^(NameVirtualHost|Listen)\s+80\s*$'
    replace: '\1 127.0.0.1:8080'
    validate: '/usr/sbin/apache2ctl -f %s -t'

- name: short form task (in ansible 2+) necessitates backslash-escaped sequences
  replace: dest=/etc/hosts regexp='\\b(localhost)(\\d*)\\b' replace='\\1\\2.localdomain\\2 \\1\\2'

- name: long form task does not
  replace:
    dest: /etc/hosts
    regexp: '\b(localhost)(\d*)\b'
    replace: '\1\2.localdomain\2 \1\2'

```

## License

TODO

## Author Information
  - ['Evan Kaufman (@EvanK)']
