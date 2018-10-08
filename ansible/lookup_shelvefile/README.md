# Ansible lookup: ansible.lookup_shelvefile


read keys from Python shelve file

## Description

Read keys from Python shelve file.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['sets of key value pairs of parameters']}",
    "file": "{'description': ['path to shelve file'], 'required': True}",
    "key": "{'description': ['key to query'], 'required': True}",
}
```

## Examples


``` yaml

- name: retrieve a string value corresponding to a key inside a Python shelve file
  debug: msg="{{ lookup('shelvefile', 'file=path_to_some_shelve_file.db key=key_to_retrieve') }}

```

## License

TODO

## Author Information
  - ['Alejandro Guirao <lekumberri@gmail.com>']
