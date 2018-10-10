# Ansible module: ansible.module_ftd_configuration


Manages configuration on Cisco FTD devices over REST API

## Description

Manages configuration on Cisco FTD devices including creating, updating, removing configuration objects, scheduling and staring jobs, deploying pending changes, etc. All operations are performed over REST API.

## Requirements

TODO

## Arguments

``` json
{
    "data": "{'description': ['Key-value pairs that should be sent as body parameters in a REST API call']}",
    "filters": "{'description': ['Key-value dict that represents equality filters. Every key is a property name and value is its desired value. If multiple filters are present, they are combined with logical operator AND.']}",
    "operation": "{'description': ["The name of the operation to execute. Commonly, the operation starts with 'add', 'edit', 'get' or 'delete' verbs, but can have an arbitrary name too."], 'required': True}",
    "path_params": "{'description': ['Key-value pairs that should be sent as path parameters in a REST API call.']}",
    "query_params": "{'description': ['Key-value pairs that should be sent as query parameters in a REST API call.']}",
    "register_as": "{'description': ['Specifies Ansible fact name that is used to register received response from the FTD device.']}",
}
```

## Examples


``` yaml

- name: Create a network object
  ftd_configuration:
    operation: "addNetworkObject"
    data:
      name: "Ansible-network-host"
      description: "From Ansible with love"
      subType: "HOST"
      value: "192.168.2.0"
      dnsResolution: "IPV4_AND_IPV6"
      type: "networkobject"
      isSystemDefined: false
    register_as: "hostNetwork"

- name: Delete the network object
  ftd_configuration:
    operation: "deleteNetworkObject"
    path_params:
      objId: "{{ hostNetwork['id'] }}"

```

## License

TODO

## Author Information
  - ['Cisco Systems, Inc.']
