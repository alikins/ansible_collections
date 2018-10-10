# Ansible module: ansible.module_sefcontext


Manages SELinux file context mapping definitions

## Description

Manages SELinux file context mapping definitions.
Similar to the C(semanage fcontext) command.

## Requirements

TODO

## Arguments

``` json
{
    "ftype": "{'description': ['The file type that should have SELinux contexts applied.', 'The following file type options are available:', 'C(a) for all files,', 'C(b) for block devices,', 'C(c) for character devices,', 'C(d) for directories,', 'C(f) for regular files,', 'C(l) for symbolic links,', 'C(p) for named pipes,', 'C(s) for socket files.'], 'type': 'str', 'default': 'a'}",
    "reload": "{'description': ['Reload SELinux policy after commit.', 'Note that this does not apply SELinux file contexts to existing files.'], 'type': 'bool', 'default': True}",
    "selevel": "{'description': ['SELinux range for the specified target.'], 'type': 'str', 'aliases': ['serange']}",
    "setype": "{'description': ['SELinux type for the specified target.'], 'required': True}",
    "seuser": "{'description': ['SELinux user for the specified target.'], 'type': 'str'}",
    "state": "{'description': ['Whether the SELinux file context must be C(absent) or C(present).'], 'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'}",
    "target": "{'description': ['Target path (expression).'], 'type': 'str', 'required': True, 'aliases': ['path']}",
}
```

## Examples


``` yaml

- name: Allow apache to modify files in /srv/git_repos
  sefcontext:
    target: '/srv/git_repos(/.*)?'
    setype: httpd_git_rw_content_t
    state: present

- name: Apply new SELinux file context to filesystem
  command: restorecon -irv /srv/git_repos

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
