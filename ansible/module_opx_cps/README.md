# Ansible module: ansible.module_opx_cps


CPS operations on networking device running Openswitch (OPX)

## Description

Executes the given operation on the YANG object, using CPS API in the networking device running OpenSwitch (OPX). It uses the YANG models provided in https://github.com/open-switch/opx-base-model.

## Requirements

TODO

## Arguments

``` json
{
    "attr_data": "{'description': ['Attribute Yang path and their corresponding data.']}",
    "attr_type": "{'description': ['Attribute Yang type.']}",
    "commit_event": "{'description': ['Attempts to force the auto-commit event to the specified yang object.'], 'type': 'bool', 'default': False}",
    "db": "{'description': ['Queries/Writes the specified yang path from/to the db.'], 'type': 'bool', 'default': False}",
    "module_name": "{'description': ['Yang path to be configured.']}",
    "operation": "{'description': ['Operation to be performed on the object.'], 'default': 'create', 'choices': ['delete', 'create', 'set', 'action', 'get']}",
    "qualifier": "{'description': ['A qualifier provides the type of object data to retrieve or act on.'], 'default': 'target', 'choices': ['target', 'observed', 'proposed', 'realtime', 'registration', 'running', 'startup']}",
}
```

## Examples


``` yaml

- name: Create VLAN
  opx_cps:
    module_name: "dell-base-if-cmn/if/interfaces/interface"
    attr_data: {
         "base-if-vlan/if/interfaces/interface/id": 230,
         "if/interfaces/interface/name": "br230",
         "if/interfaces/interface/type": "ianaift:l2vlan"
    }
    operation: "create"
- name: Get VLAN
  opx_cps:
    module_name: "dell-base-if-cmn/if/interfaces/interface"
    attr_data: {
         "if/interfaces/interface/name": "br230",
    }
    operation: "get"
- name: Modify some attributes in VLAN
  opx_cps:
    module_name: "dell-base-if-cmn/if/interfaces/interface"
    attr_data: {
         "cps/key_data":
            { "if/interfaces/interface/name": "br230" },
         "dell-if/if/interfaces/interface/untagged-ports": ["e101-008-0"],
    }
    operation: "set"
- name: Delete VLAN
  opx_cps:
    module_name: "dell-base-if-cmn/if/interfaces/interface"
    attr_data: {
         "if/interfaces/interface/name": "br230",
    }
    operation: "delete"

```

## License

TODO

## Author Information
  - ['Senthil Kumar Ganesan (@skg-net)']
