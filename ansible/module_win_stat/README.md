# Ansible module: ansible.module_win_stat


Get information about Windows files

## Description

Returns information about a Windows file.
For non-Windows targets, use the M(stat) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "checksum_algorithm": "{'description': ['Algorithm to determine checksum of file. Will throw an error if the host is unable to use specified algorithm.'], 'default': 'sha1', 'choices': ['md5', 'sha1', 'sha256', 'sha384', 'sha512'], 'version_added': '2.3'}",
    "get_checksum": "{'description': ['Whether to return a checksum of the file (default sha1)'], 'type': 'bool', 'default': True, 'version_added': '2.1'}",
    "get_md5": "{'description': ['Whether to return the checksum sum of the file. Between Ansible 1.9 and 2.2 this is no longer an MD5, but a SHA1 instead. As of Ansible 2.3 this is back to an MD5. Will return None if host is unable to use specified algorithm.', 'The default of this option changed from C(yes) to C(no) in Ansible 2.5 and will be removed altogether in Ansible 2.9.', 'Use C(get_checksum=true) with C(checksum_algorithm=md5) to return an md5 hash under the C(checksum) return value.'], 'type': 'bool', 'default': False}",
    "path": "{'description': ['The full path of the file/object to get the facts of; both forward and back slashes are accepted.'], 'required': True, 'type': 'path'}",
}
```

## Examples


``` yaml

- name: Obtain information about a file
  win_stat:
    path: C:\foo.ini
  register: file_info

- name: Obtain information about a folder
  win_stat:
    path: C:\bar
  register: folder_info

- name: Get MD5 checksum of a file
  win_stat:
    path: C:\foo.ini
    get_checksum: yes
    checksum_algorithm: md5
  register: md5_checksum

- debug:
    var: md5_checksum.stat.checksum

- name: Get SHA1 checksum of file
  win_stat:
    path: C:\foo.ini
    get_checksum: yes
  register: sha1_checksum

- debug:
    var: sha1_checksum.stat.checksum

- name: Get SHA256 checksum of file
  win_stat:
    path: C:\foo.ini
    get_checksum: yes
    checksum_algorithm: sha256
  register: sha256_checksum

- debug:
    var: sha256_checksum.stat.checksum

```

## License

TODO

## Author Information
  - ['Chris Church (@cchurch)']
