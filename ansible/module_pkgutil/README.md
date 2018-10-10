# Ansible module: ansible.module_pkgutil


Manage CSW-Packages on Solaris

## Description

Manages CSW packages (SVR4 format) on Solaris 10 and 11.
These were the native packages on Solaris <= 10 and are available as a legacy feature in Solaris 11.
Pkgutil is an advanced packaging system, which resolves dependency on installation. It is designed for CSW packages.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Package name, e.g. (C(CSWnrpe))'], 'required': True}",
    "site": "{'description': ['Specifies the repository path to install the package from.', 'Its global definition is done in C(/etc/opt/csw/pkgutil.conf).'], 'required': False}",
    "state": "{'description': ['Whether to install (C(present)), or remove (C(absent)) a package.', 'The upgrade (C(latest)) operation will update/install the package to the latest version available.', 'Note: The module has a limitation that (C(latest)) only works for one package, not lists of them.'], 'required': True, 'choices': ['present', 'absent', 'latest']}",
    "update_catalog": "{'description': ['If you want to refresh your catalog from the mirror, set this to (C(yes)).'], 'required': False, 'default': False, 'version_added': '2.1'}",
}
```

## Examples


``` yaml

# Install a package
- pkgutil:
    name: CSWcommon
    state: present

# Install a package from a specific repository
- pkgutil:
    name: CSWnrpe
    site: 'ftp://myinternal.repo/opencsw/kiel'
    state: latest

```

## License

TODO

## Author Information
  - ['Alexander Winkler (@dermute)']
