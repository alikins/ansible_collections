# Ansible module: ansible.module_fetch


Fetch files from remote nodes

## Description

This module works like M(copy), but in reverse.
It is used for fetching files from remote machines and storing them locally in a file tree, organized by hostname.
This module is also supported for Windows targets.

## Requirements

TODO

## Arguments

``` json
{
    "dest": "{'description': ['A directory to save the file into.', 'For example, if the I(dest) directory is C(/backup) a I(src) file named C(/etc/profile) on host C(host.example.com), would be saved into C(/backup/host.example.com/etc/profile).'], 'required': True}",
    "fail_on_missing": "{'description': ['When set to C(yes), the task will fail if the remote file cannot be read for any reason.', 'Prior to Ansible 2.5, setting this would only fail if the source file was missing.', 'The default was changed to C(yes) in Ansible 2.5.'], 'type': 'bool', 'default': True}",
    "flat": "{'description': ['Allows you to override the default behavior of appending hostname/path/to/file to the destination.', "If C(dest) ends with '/', it will use the basename of the source file, similar to the copy module.", 'Obviously this is only handy if the filenames are unique.'], 'type': 'bool', 'default': False}",
    "src": "{'description': ['The file on the remote system to fetch.', 'This I(must) be a file, not a directory.', 'Recursive fetching may be supported in a later release.'], 'required': True}",
    "validate_checksum": "{'version_added': '1.4', 'description': ['Verify that the source and destination checksums match after the files are fetched.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Store file into /tmp/fetched/host.example.com/tmp/somefile
  fetch:
    src: /tmp/somefile
    dest: /tmp/fetched

- name: Specifying a path directly
  fetch:
    src: /tmp/somefile
    dest: /tmp/prefix-{{ inventory_hostname }}
    flat: yes

- name: Specifying a destination path
  fetch:
    src: /tmp/uniquefile
    dest: /tmp/special/
    flat: yes

- name: Storing in a path relative to the playbook
  fetch:
    src: /tmp/uniquefile
    dest: special/prefix-{{ inventory_hostname }}
    flat: yes

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan']
  - ['Ansible Core Team', 'Michael DeHaan']
