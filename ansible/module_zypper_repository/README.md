# Ansible module: ansible.module_zypper_repository


Add and remove Zypper repositories

## Description

Add or remove Zypper repositories on SUSE and openSUSE

## Requirements

TODO

## Arguments

``` json
{
    "auto_import_keys": "{'description': ['Automatically import the gpg signing key of the new or changed repository.', 'Has an effect only if state is I(present). Has no effect on existing (unchanged) repositories or in combination with I(absent).', 'Implies runrefresh.', 'Only works with C(.repo) files if `name` is given explicitly.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "autorefresh": "{'description': ['Enable autorefresh of the repository.'], 'type': 'bool', 'default': True, 'aliases': ['refresh']}",
    "description": "{'description': ['A description of the repository']}",
    "disable_gpg_check": "{'description': ['Whether to disable GPG signature checking of all packages. Has an effect only if state is I(present).', 'Needs zypper version >= 1.6.2.'], 'type': 'bool', 'default': False}",
    "enabled": "{'description': ['Set repository to enabled (or disabled).'], 'type': 'bool', 'default': True, 'version_added': '2.2'}",
    "name": "{'description': ['A name for the repository. Not required when adding repofiles.']}",
    "overwrite_multiple": "{'description': ['Overwrite multiple repository entries, if repositories with both name and URL already exist.'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "priority": "{'description': ['Set priority of repository. Packages will always be installed from the repository with the smallest priority number.', 'Needs zypper version >= 1.12.25.'], 'version_added': '2.1'}",
    "repo": "{'description': ['URI of the repository or .repo file. Required when state=present.']}",
    "runrefresh": "{'description': ['Refresh the package list of the given repository.', 'Can be used with repo=* to refresh all repositories.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "state": "{'description': ['A source string state.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

# Add NVIDIA repository for graphics drivers
- zypper_repository:
    name: nvidia-repo
    repo: 'ftp://download.nvidia.com/opensuse/12.2'
    state: present

# Remove NVIDIA repository
- zypper_repository:
    name: nvidia-repo
    repo: 'ftp://download.nvidia.com/opensuse/12.2'
    state: absent

# Add python development repository
- zypper_repository:
    repo: 'http://download.opensuse.org/repositories/devel:/languages:/python/SLE_11_SP3/devel:languages:python.repo'

# Refresh all repos
- zypper_repository:
    repo: '*'
    runrefresh: yes

# Add a repo and add it's gpg key
- zypper_repository:
    repo: 'http://download.opensuse.org/repositories/systemsmanagement/openSUSE_Leap_42.1/'
    auto_import_keys: yes

# Force refresh of a repository
- zypper_repository:
    repo: 'http://my_internal_ci_repo/repo'
    name: my_ci_repo
    state: present
    runrefresh: yes

```

## License

TODO

## Author Information
  - ['Matthias Vogelgesang (@matze)']
