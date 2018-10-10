# Ansible module: ansible.module_open_iscsi


Manage iscsi targets with open-iscsi

## Description

Discover targets on given portal, (dis)connect targets, mark targets to manually or auto start, return device nodes of connected targets.

## Requirements

TODO

## Arguments

``` json
{
    "auto_node_startup": "{'aliases': ['automatic'], 'required': False, 'type': 'bool', 'description': ['whether the target node should be automatically connected at startup']}",
    "discover": "{'required': False, 'type': 'bool', 'description': ['whether the list of target nodes on the portal should be (re)discovered and added to the persistent iscsi database. Keep in mind that iscsiadm discovery resets configurtion, like node.startup to manual, hence combined with auto_node_startup=yes will always return a changed state.']}",
    "login": "{'required': False, 'type': 'bool', 'description': ['whether the target node should be connected']}",
    "node_auth": "{'required': False, 'default': 'CHAP', 'description': ['discovery.sendtargets.auth.authmethod']}",
    "node_pass": "{'required': False, 'description': ['discovery.sendtargets.auth.password']}",
    "node_user": "{'required': False, 'description': ['discovery.sendtargets.auth.username']}",
    "port": "{'required': False, 'default': 3260, 'description': ['the port on which the iscsi target process listens']}",
    "portal": "{'required': False, 'aliases': ['ip'], 'description': ['the ip address of the iscsi target']}",
    "show_nodes": "{'required': False, 'type': 'bool', 'description': ['whether the list of nodes in the persistent iscsi database should be returned by the module']}",
    "target": "{'required': False, 'aliases': ['name', 'targetname'], 'description': ['the iscsi target name']}",
}
```

## Examples


``` yaml

# perform a discovery on 10.1.2.3 and show available target nodes
- open_iscsi:
    show_nodes: yes
    discover: yes
    portal: 10.1.2.3

# discover targets on portal and login to the one available
# (only works if exactly one target is exported to the initiator)
- open_iscsi:
    portal: '{{ iscsi_target }}'
    login: yes
    discover: yes

# description: connect to the named target, after updating the local
# persistent database (cache)
- open_iscsi:
    login: yes
    target: 'iqn.1986-03.com.sun:02:f8c1f9e0-c3ec-ec84-c9c9-8bfb0cd5de3d'

# description: discconnect from the cached named target
- open_iscsi:
    login: no
    target: 'iqn.1986-03.com.sun:02:f8c1f9e0-c3ec-ec84-c9c9-8bfb0cd5de3d'

```

## License

TODO

## Author Information
  - ['Serge van Ginderachter (@srvg)']
