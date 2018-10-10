# Ansible module: ansible.module_blockinfile


Insert/update/remove a text block surrounded by marker lines

## Description

This module will insert/update/remove a block of multi-line text surrounded by customizable marker lines.

## Requirements

TODO

## Arguments

``` json
{
    "attributes": "{'description': ['The attributes the resulting file or directory should have.', 'To get supported flags look at the man page for I(chattr) on the target system.', 'This string should contain the attributes in the same order as the one displayed by I(lsattr).', 'The C(=) operator is assumed as default, otherwise C(+) or C(-) operators need to be included in the string.'], 'aliases': ['attr'], 'version_added': '2.3'}",
    "backup": "{'description': ['Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.'], 'type': 'bool', 'default': False}",
    "block": "{'description': ['The text to insert inside the marker lines.', 'If it is missing or an empty string, the block will be removed as if C(state) were specified to C(absent).'], 'type': 'str', 'aliases': ['content'], 'default': ''}",
    "create": "{'description': ['Create a new file if it does not exist.'], 'type': 'bool', 'default': False}",
    "group": "{'description': ['Name of the group that should own the file/directory, as would be fed to I(chown).']}",
    "insertafter": "{'description': ['If specified, the block will be inserted after the last match of specified regular expression.', 'A special value is available; C(EOF) for inserting the block at the end of the file.', 'If specified regular expression has no matches, C(EOF) will be used instead.'], 'type': 'str', 'default': 'EOF', 'choices': ['EOF', '*regex*']}",
    "insertbefore": "{'description': ['If specified, the block will be inserted before the last match of specified regular expression.', 'A special value is available; C(BOF) for inserting the block at the beginning of the file.', 'If specified regular expression has no matches, the block will be inserted at the end of the file.'], 'type': 'str', 'choices': ['BOF', '*regex*']}",
    "marker": "{'description': ['The marker line template.', 'C({mark}) will be replaced with the values C(in marker_begin) (default="BEGIN") and C(marker_end) (default="END").'], 'type': 'str', 'default': '# {mark} ANSIBLE MANAGED BLOCK'}",
    "marker_begin": "{'description': ['This will be inserted at C({mark}) in the opening ansible block marker.'], 'type': 'str', 'default': 'BEGIN', 'version_added': '2.5'}",
    "marker_end": "{'required': False, 'description': ['This will be inserted at C({mark}) in the closing ansible block marker.'], 'type': 'str', 'default': 'END', 'version_added': '2.5'}",
    "mode": "{'description': ['The permissions the resulting file or directory should have.', "For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like C(0644) or C(01777)) or quote it (like C('644') or C('1777')) so Ansible receives a string and can do its own conversion from string into number.", 'Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.', 'As of version 1.8, the mode may be specified as a symbolic mode (for example, C(u+rwx) or C(u=rw,g=r,o=r)).', 'As of version 2.6, the mode may also be the special string C(preserve).', 'When set to C(preserve) the file will be given the same permissions as the source file.']}",
    "owner": "{'description': ['Name of the user that should own the file/directory, as would be fed to I(chown).']}",
    "path": "{'description': ['The file to modify.', 'Before Ansible 2.3 this option was only usable as I(dest), I(destfile) and I(name).'], 'required': True, 'type': 'path', 'aliases': ['dest', 'destfile', 'name']}",
    "selevel": "{'description': ['The level part of the SELinux file context.', 'This is the MLS/MCS attribute, sometimes known as the C(range).', 'When set to C(_default), it will use the C(level) portion of the policy if available.'], 'default': 's0'}",
    "serole": "{'description': ['The role part of the SELinux file context.', 'When set to C(_default), it will use the C(role) portion of the policy if available.']}",
    "setype": "{'description': ['The type part of the SELinux file context.', 'When set to C(_default), it will use the C(type) portion of the policy if available.']}",
    "seuser": "{'description': ['The user part of the SELinux file context.', 'By default it uses the C(system) policy, where applicable.', 'When set to C(_default), it will use the C(user) portion of the policy if available.']}",
    "state": "{'description': ['Whether the block should be there or not.'], 'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'}",
    "unsafe_writes": "{'description': ['Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target file.', 'By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted files, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.', "This option allows Ansible to fall back to unsafe methods of updating files when atomic operations fail (however, it doesn't force Ansible to perform unsafe writes).", 'IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "validate": "{'description': ['The validation command to run before copying into place.', "The path to the file to validate is passed in via '%s' which must be present as in the examples below.", 'The command is passed securely so shell features like expansion and pipes will not work.']}",
}
```

## Examples


``` yaml

# Before Ansible 2.3, option 'dest' or 'name' was used instead of 'path'
- name: Insert/Update "Match User" configuration block in /etc/ssh/sshd_config
  blockinfile:
    path: /etc/ssh/sshd_config
    block: |
      Match User ansible-agent
      PasswordAuthentication no

- name: Insert/Update eth0 configuration stanza in /etc/network/interfaces
        (it might be better to copy files into /etc/network/interfaces.d/)
  blockinfile:
    path: /etc/network/interfaces
    block: |
      iface eth0 inet static
          address 192.0.2.23
          netmask 255.255.255.0

- name: Insert/Update configuration using a local file and validate it
  blockinfile:
    block: "{{ lookup('file', './local/ssh_config') }}"
    dest: /etc/ssh/ssh_config
    backup: yes
    validate: /usr/sbin/sshd -T -f %s

- name: Insert/Update HTML surrounded by custom markers after <body> line
  blockinfile:
    path: /var/www/html/index.html
    marker: "<!-- {mark} ANSIBLE MANAGED BLOCK -->"
    insertafter: "<body>"
    content: |
      <h1>Welcome to {{ ansible_hostname }}</h1>
      <p>Last updated on {{ ansible_date_time.iso8601 }}</p>

- name: Remove HTML as well as surrounding markers
  blockinfile:
    path: /var/www/html/index.html
    marker: "<!-- {mark} ANSIBLE MANAGED BLOCK -->"
    content: ""

- name: Add mappings to /etc/hosts
  blockinfile:
    path: /etc/hosts
    block: |
      {{ item.ip }} {{ item.name }}
    marker: "# {mark} ANSIBLE MANAGED BLOCK {{ item.name }}"
  with_items:
  - { name: host1, ip: 10.10.1.10 }
  - { name: host2, ip: 10.10.1.11 }
  - { name: host3, ip: 10.10.1.12 }

```

## License

TODO

## Author Information
  - ['Yaegashi Takeshi (@yaegashi)']
