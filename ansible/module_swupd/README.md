# Ansible module: ansible.module_swupd


Manages updates and bundles in ClearLinux systems

## Description

Manages updates and bundles with the swupd bundle manager, which is used by the Clear Linux Project for Intel Architecture.

## Requirements

TODO

## Arguments

``` json
{
    "contenturl": "{'description': ['URL pointing to the contents of available bundles. If not specified, the contents are retrieved from clearlinux.org.']}",
    "format": "{'description': ['The format suffix for version file downloads. For example [1,2,3,staging,etc]. If not specified, the default format is used.']}",
    "manifest": "{'description': ['The manifest contains information about the bundles at certaion version of the OS. Specify a Manifest version to verify against that version or leave unspecified to verify against the current version.'], 'aliases': ['release', 'version']}",
    "name": "{'description': ['Name of the (I)bundle to install or remove.'], 'aliases': ['bundle']}",
    "state": "{'description': ['Indicates the desired (I)bundle state. C(present) ensures the bundle is installed while C(absent) ensures the (I)bundle is not installed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "update": "{'description': ['Updates the OS to the latest version.']}",
    "url": "{'description': ['Overrides both I(contenturl) and I(versionurl).']}",
    "verify": "{'description': ['Verify content for OS version.']}",
    "versionurl": "{'description': ['URL for version string download.']}",
}
```

## Examples


``` yaml

- name: Update the OS to the latest version
  swupd:
    update: yes

- name: Installs the "foo" bundle
  swupd:
    name: foo
    state: present

- name: Removes the "foo" bundle
  swupd:
    name: foo
    state: absent

- name: Check integrity of filesystem
  swupd:
    verify: yes

- name: Downgrade OS to release 12920
  swupd:
    verify: yes
    manifest: 12920

```

## License

TODO

## Author Information
  - ['Alberto Murillo (@albertomurillo)']
