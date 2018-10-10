# Ansible module: ansible.module_pkgng


Package manager for FreeBSD >= 9.0

## Description

Manage binary packages for FreeBSD using 'pkgng' which is available in versions after 9.0.

## Requirements

TODO

## Arguments

``` json
{
    "annotation": "{'description': ['A comma-separated list of keyvalue-pairs of the form C(<+/-/:><key>[=<value>]). A C(+) denotes adding an annotation, a C(-) denotes removing an annotation, and C(:) denotes modifying an annotation. If setting or modifying annotations, a value must be provided.'], 'required': False, 'version_added': '1.6'}",
    "autoremove": "{'version_added': '2.2', 'description': ['Remove automatically installed packages which are no longer needed.'], 'required': False, 'type': 'bool', 'default': False}",
    "cached": "{'description': ['Use local package base instead of fetching an updated one.'], 'type': 'bool', 'required': False, 'default': False}",
    "chroot": "{'version_added': '2.1', 'description': ['Pkg will chroot in the specified environment.', 'Can not be used together with I(rootdir) or I(jail) options.'], 'required': False}",
    "jail": "{'version_added': '2.4', 'description': ['Pkg will execute in the given jail name or id.', 'Can not be used together with I(chroot) or I(rootdir) options.']}",
    "name": "{'description': ['Name or list of names of packages to install/remove.'], 'required': True}",
    "pkgsite": "{'description': ['For pkgng versions before 1.1.4, specify packagesite to use for downloading packages. If not specified, use settings from C(/usr/local/etc/pkg.conf).', 'For newer pkgng versions, specify a the name of a repository configured in C(/usr/local/etc/pkg/repos).'], 'required': False}",
    "rootdir": "{'description': ['For pkgng versions 1.5 and later, pkg will install all packages within the specified root directory.', 'Can not be used together with I(chroot) or I(jail) options.'], 'required': False}",
    "state": "{'description': ['State of the package.', 'Note: "latest" added in 2.7'], 'choices': ['present', 'latest', 'absent'], 'required': False, 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Install package foo
  pkgng:
    name: foo
    state: present

- name: Annotate package foo and bar
  pkgng:
    name: foo,bar
    annotation: '+test1=baz,-test2,:test3=foobar'

- name: Remove packages foo and bar
  pkgng:
    name: foo,bar
    state: absent

# "latest" support added in 2.7
- name: Upgrade package baz
  pkgng:
    name: baz
    state: latest

```

## License

TODO

## Author Information
  - ['bleader (@bleader)']
