# Ansible lookup: ansible.lookup_file


read file contents

## Description

This lookup returns the contents from a file on the Ansible controller's file system.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['path(s) of files to read'], 'required': True}",
    "lstrip": "{'description': ['whether or not to remove whitespace from the beginning of the looked-up file'], 'type': 'bool', 'required': False, 'default': False}",
    "rstrip": "{'description': ['whether or not to remove whitespace from the ending of the looked-up file'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

- debug: msg="the value of foo.txt is {{lookup('file', '/etc/foo.txt') }}"

- name: display multiple file contents
  debug: var=item
  with_file:
    - "/path/to/foo.txt"
    - "bar.txt"  # will be looked in files/ dir relative to play or in role
    - "/path/to/biz.txt"

```

## License

TODO

## Author Information
  - ['Daniel Hokka Zakrisson <daniel@hozac.com>']
