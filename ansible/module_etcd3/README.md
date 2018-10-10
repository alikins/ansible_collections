# Ansible module: ansible.module_etcd3


Set or delete key value pairs from an etcd3 cluster

## Description

Sets or deletes values in etcd3 cluster using its v3 api.
Needs python etcd3 lib to work

## Requirements

TODO

## Arguments

``` json
{
    "host": "{'description': ['the IP address of the cluster'], 'default': 'localhost'}",
    "key": "{'description': ['the key where the information is stored in the cluster'], 'required': True}",
    "port": "{'description': ['the port number used to connect to the cluster'], 'default': 2379}",
    "state": "{'description': ['the state of the value for the key.', 'can be present or absent'], 'required': True}",
    "value": "{'description': ['the information stored'], 'required': True}",
}
```

## Examples


``` yaml

# Store a value "bar" under the key "foo" for a cluster located "http://localhost:2379"
- etcd3:
    key: "foo"
    value: "baz3"
    host: "localhost"
    port: 2379
    state: "present"

```

## License

TODO

## Author Information
  - ['Jean-Philippe Evrard (@evrardjp)']
