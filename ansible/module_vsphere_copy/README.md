# Ansible module: ansible.module_vsphere_copy


Copy a file to a vCenter datastore

## Description

Upload files to a vCenter datastore

## Requirements

TODO

## Arguments

``` json
{
    "datacenter": "{'description': ['The datacenter on the vCenter server that holds the datastore.'], 'required': True}",
    "datastore": "{'description': ['The datastore on the vCenter server to push files to.'], 'required': True}",
    "host": "{'description': ['The vCenter server on which the datastore is available.'], 'required': True, 'aliases': ['hostname']}",
    "login": "{'description': ['The login name to authenticate on the vCenter server.'], 'required': True, 'aliases': ['username']}",
    "password": "{'description': ['The password to authenticate on the vCenter server.'], 'required': True}",
    "path": "{'description': ['The file to push to the datastore on the vCenter server.'], 'required': True}",
    "src": "{'description': ['The file to push to vCenter'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be set to C(no) when no other option exists.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- vsphere_copy:
    host: '{{ vhost }}'
    login: '{{ vuser }}'
    password: '{{ vpass }}'
    src: /some/local/file
    datacenter: DC1 Someplace
    datastore: datastore1
    path: some/remote/file
  delegate_to: localhost

- vsphere_copy:
    host: '{{ vhost }}'
    login: '{{ vuser }}'
    password: '{{ vpass }}'
    src: /other/local/file
    datacenter: DC2 Someplace
    datastore: datastore2
    path: other/remote/file
  delegate_to: other_system

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
