# Ansible lookup: ansible.lookup_fileglob


list files matching a pattern

## Description

Matches all files in a single directory, non-recursively, that match a pattern. It calls Python's "glob" library.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['path(s) of files to read'], 'required': True}",
}
```

## Examples


``` yaml

- name: display content of all .txt files in dir
  debug: msg={{lookup('fileglob', '/my/path/*.txt')}}

- name: Copy each file over that matches the given pattern
  copy:
    src: "{{ item }}"
    dest: "/etc/fooapp/"
    owner: "root"
    mode: 0600
  with_fileglob:
    - "/playbooks/files/fooapp/*"

```

## License

TODO

## Author Information
  - ['Michael DeHaan <michael.dehaan@gmail.com>']
