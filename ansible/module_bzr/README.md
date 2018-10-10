# Ansible module: ansible.module_bzr


Deploy software (or files) from bzr branches

## Description

Manage I(bzr) branches to deploy files or software.

## Requirements

TODO

## Arguments

``` json
{
    "dest": "{'description': ['Absolute path of where the branch should be cloned to.'], 'required': True}",
    "executable": "{'description': ['Path to bzr executable to use. If not supplied, the normal mechanism for resolving binary paths will be used.'], 'version_added': '1.4'}",
    "force": "{'description': ['If C(yes), any modified files in the working tree will be discarded.  Before 1.9 the default value was C(yes).'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['SSH or HTTP protocol address of the parent branch.'], 'aliases': ['parent'], 'required': True}",
    "version": "{'description': ['What version of the branch to clone.  This can be the bzr revno or revid.'], 'default': 'head'}",
}
```

## Examples


``` yaml

# Example bzr checkout from Ansible Playbooks
- bzr:
    name: bzr+ssh://foosball.example.org/path/to/branch
    dest: /srv/checkout
    version: 22

```

## License

TODO

## Author Information
  - ['André Paramés (@andreparames)']
