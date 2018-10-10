# Ansible module: ansible.module_subversion


Deploys a subversion repository

## Description

Deploy given repository URL / revision to dest. If dest exists, update to the specified revision, otherwise perform a checkout.

## Requirements

TODO

## Arguments

``` json
{
    "checkout": "{'description': ['If C(no), do not check out the repository if it does not exist locally.'], 'type': 'bool', 'default': True, 'version_added': '2.3'}",
    "dest": "{'description': ['Absolute path where the repository should be deployed.'], 'required': True}",
    "executable": "{'description': ['Path to svn executable to use. If not supplied, the normal mechanism for resolving binary paths will be used.'], 'version_added': '1.4'}",
    "export": "{'description': ['If C(yes), do export instead of checkout/update.'], 'type': 'bool', 'default': False, 'version_added': '1.6'}",
    "force": "{'description': ['If C(yes), modified files will be discarded. If C(no), module will fail if it encounters modified files. Prior to 1.9 the default was C(yes).'], 'type': 'bool', 'default': False}",
    "in_place": "{'description': ['If the directory exists, then the working copy will be checked-out over-the-top using svn checkout --force; if force is specified then existing files with different content are reverted'], 'type': 'bool', 'default': False, 'version_added': '2.6'}",
    "password": "{'description': ['C(--password) parameter passed to svn.']}",
    "repo": "{'description': ['The subversion URL to the repository.'], 'required': True, 'aliases': ['name', 'repository']}",
    "revision": "{'description': ['Specific revision to checkout.'], 'default': 'HEAD', 'aliases': ['version']}",
    "switch": "{'description': ['If C(no), do not call svn switch before update.'], 'default': True, 'version_added': '2.0', 'type': 'bool'}",
    "update": "{'description': ['If C(no), do not retrieve new revisions from the origin repository.'], 'type': 'bool', 'default': True, 'version_added': '2.3'}",
    "username": "{'description': ['C(--username) parameter passed to svn.']}",
}
```

## Examples


``` yaml

- name: Checkout subversion repository to specified folder
  subversion:
    repo: svn+ssh://an.example.org/path/to/repo
    dest: /src/checkout

- name: Export subversion directory to folder
  subversion:
    repo: svn+ssh://an.example.org/path/to/repo
    dest: /src/export

- name: Get information about the repository whether or not it has already been cloned locally
- subversion:
    repo: svn+ssh://an.example.org/path/to/repo
    dest: /srv/checkout
    checkout: no
    update: no

```

## License

TODO

## Author Information
  - ['Dane Summers (@dsummersl) <njharman@gmail.com>']
