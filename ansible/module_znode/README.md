# Ansible module: ansible.module_znode


Create, delete, retrieve, and update znodes using ZooKeeper

## Description

Create, delete, retrieve, and update znodes using ZooKeeper.

## Requirements

TODO

## Arguments

``` json
{
    "hosts": "{'description': ["A list of ZooKeeper servers (format '[server]:[port]')."], 'required': True}",
    "name": "{'description': ['The path of the znode.'], 'required': True}",
    "op": "{'description': ['An operation to perform. Mutually exclusive with state.']}",
    "recursive": "{'description': ['Recursively delete node and all its children.'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "state": "{'description': ['The state to enforce. Mutually exclusive with op.']}",
    "timeout": "{'description': ['The amount of time to wait for a node to appear.'], 'default': 300}",
    "value": "{'description': ['The value assigned to the znode.']}",
}
```

## Examples


``` yaml

# Creating or updating a znode with a given value
- znode:
    hosts: 'localhost:2181'
    name: /mypath
    value: myvalue
    state: present

# Getting the value and stat structure for a znode
- znode:
    hosts: 'localhost:2181'
    name: /mypath
    op: get

# Listing a particular znode's children
- znode:
    hosts: 'localhost:2181'
    name: /zookeeper
    op: list

# Waiting 20 seconds for a znode to appear at path /mypath
- znode:
    hosts: 'localhost:2181'
    name: /mypath
    op: wait
    timeout: 20

# Deleting a znode at path /mypath
- znode:
    hosts: 'localhost:2181'
    name: /mypath
    state: absent

# Creating or updating a znode with a given value on a remote Zookeeper
- znode:
    hosts: 'my-zookeeper-node:2181'
    name: /mypath
    value: myvalue
    state: present
  delegate_to: 127.0.0.1

```

## License

TODO

## Author Information
  - ['Trey Perry (@treyperry)']
