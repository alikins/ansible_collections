# Ansible module: ansible.module_pam_limits


Modify Linux PAM limits

## Description

The C(pam_limits) module modifies PAM limits. The default file is C(/etc/security/limits.conf). For the full documentation, see C(man 5 limits.conf).

## Requirements

TODO

## Arguments

``` json
{
    "backup": "{'description': ['Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.'], 'required': False, 'type': 'bool', 'default': False}",
    "comment": "{'description': ['Comment associated with the limit.'], 'required': False, 'default': ''}",
    "dest": "{'description': ['Modify the limits.conf path.'], 'required': False, 'default': '/etc/security/limits.conf'}",
    "domain": "{'description': ['A username, @groupname, wildcard, uid/gid range.'], 'required': True}",
    "limit_item": "{'description': ['The limit to be set'], 'required': True, 'choices': ['core', 'data', 'fsize', 'memlock', 'nofile', 'rss', 'stack', 'cpu', 'nproc', 'as', 'maxlogins', 'maxsyslogins', 'priority', 'locks', 'sigpending', 'msgqueue', 'nice', 'rtprio', 'chroot']}",
    "limit_type": "{'description': ['Limit type, see C(man 5 limits.conf) for an explanation'], 'required': True, 'choices': ['hard', 'soft', '-']}",
    "use_max": "{'description': ['If set to C(yes), the maximal value will be used or conserved. If the specified value is superior to the value in the file, file content is replaced with the new value, else content is not modified.'], 'required': False, 'type': 'bool', 'default': False}",
    "use_min": "{'description': ['If set to C(yes), the minimal value will be used or conserved. If the specified value is inferior to the value in the file, file content is replaced with the new value, else content is not modified.'], 'required': False, 'type': 'bool', 'default': False}",
    "value": "{'description': ['The value of the limit.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Add or modify nofile soft limit for the user joe
  pam_limits:
    domain: joe
    limit_type: soft
    limit_item: nofile
    value: 64000

- name: Add or modify fsize hard limit for the user smith. Keep or set the maximal value.
  pam_limits:
    domain: smith
    limit_type: hard
    limit_item: fsize
    value: 1000000
    use_max: yes

- name: Add or modify memlock, both soft and hard, limit for the user james with a comment.
  pam_limits:
    domain: james
    limit_type: '-'
    limit_item: memlock
    value: unlimited
    comment: unlimited memory lock for james

- name: Add or modify hard nofile limits for wildcard domain
  pam_limits:
    domain: '*'
    limit_type: hard
    limit_item: nofile
    value: 39693561

```

## License

TODO

## Author Information
  - ['Sebastien Rohaut (@usawa)']
