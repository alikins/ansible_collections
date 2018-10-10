# Ansible module: ansible.module_hg


Manages Mercurial (hg) repositories

## Description

Manages Mercurial (hg) repositories. Supports SSH, HTTP/S and local address.

## Requirements

TODO

## Arguments

``` json
{
    "clone": "{'description': ['If C(no), do not clone the repository if it does not exist locally.'], 'type': 'bool', 'default': True, 'version_added': '2.3'}",
    "dest": "{'description': ['Absolute path of where the repository should be cloned to. This parameter is required, unless clone and update are set to no'], 'required': True}",
    "executable": "{'description': ['Path to hg executable to use. If not supplied, the normal mechanism for resolving binary paths will be used.'], 'version_added': '1.4'}",
    "force": "{'description': ['Discards uncommitted changes. Runs C(hg update -C).  Prior to 1.9, the default was `yes`.'], 'type': 'bool', 'default': False}",
    "purge": "{'description': ['Deletes untracked files. Runs C(hg purge).'], 'type': 'bool', 'default': False}",
    "repo": "{'description': ['The repository address.'], 'required': True, 'aliases': ['name']}",
    "revision": "{'description': ['Equivalent C(-r) option in hg command which could be the changeset, revision number, branch name or even tag.'], 'aliases': ['version']}",
    "update": "{'description': ['If C(no), do not retrieve new revisions from the origin repository'], 'type': 'bool', 'default': True, 'version_added': '2.0'}",
}
```

## Examples


``` yaml

- name: Ensure the current working copy is inside the stable branch and deletes untracked files if any.
  hg:
    repo: https://bitbucket.org/user/repo1
    dest: /home/user/repo1
    revision: stable
    purge: yes

- name: Get information about the repository whether or not it has already been cloned locally.
  hg:
    repo: git://bitbucket.org/user/repo
    dest: /srv/checkout
    clone: no
    update: no

```

## License

TODO

## Author Information
  - ['Yeukhon Wong (@yeukhon)']
