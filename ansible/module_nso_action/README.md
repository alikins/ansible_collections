# Ansible module: ansible.module_nso_action


Executes Cisco NSO actions and verifies output

## Description

This module provices support for executing Cisco NSO actions and then verifying that the output is as expected.

## Requirements

TODO

## Arguments

``` json
{
    "input": "{'description': ['NSO action parameters.\n']}",
    "output_invalid": "{'description': ['List of result parameter names that will cause the task to fail if they are present.\n']}",
    "output_required": "{'description': ['Required output parameters.\n']}",
    "password": "{'description': ['NSO password'], 'required': True}",
    "path": "{'description': ['Path to NSO action.'], 'required': True}",
    "timeout": "{'description': ['JSON-RPC request timeout in seconds'], 'default': 300, 'version_added': '2.6'}",
    "url": "{'description': ['NSO JSON-RPC URL, http://localhost:8080/jsonrpc'], 'required': True}",
    "username": "{'description': ['NSO username'], 'required': True}",
    "validate_strict": "{'description': ['If set to true, the task will fail if any output parameters not in output_required is present in the output.\n']}",
}
```

## Examples


``` yaml

- name: Sync NSO device
  nso_config:
    url: http://localhost:8080/jsonrpc
    username: username
    password: password
    path: /ncs:devices/device{ce0}/sync-from
    output_required:
      result: true

```

## License

TODO

## Author Information
  - ['Claes Nästén (@cnasten)']
