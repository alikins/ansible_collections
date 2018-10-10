# Ansible module: ansible.module_tower_credential_type


Create, update, or destroy custom Ansible Tower credential type

## Description

Create, update, or destroy Ansible Tower credential type. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['The description of the credential type to give more detail about it.'], 'required': False}",
    "injectors": "{'description': ['Enter injectors using either JSON or YAML syntax. Refer to the Ansible Tower documentation for example syntax.'], 'required': False}",
    "inputs": "{'description': ['Enter inputs using either JSON or YAML syntax. Refer to the Ansible Tower documentation for example syntax.'], 'required': False}",
    "kind": "{'description': ['The type of credential type being added. Note that only cloud and net can be used for creating credential types. Refer to the Ansible for more information.'], 'choices': ['ssh', 'vault', 'net', 'scm', 'cloud', 'insights'], 'required': False}",
    "name": "{'description': ['The name of the credential type.'], 'required': True}",
    "state": "{'description': ['Desired state of the resource.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Tower option to avoid certificates check.'], 'type': 'bool', 'default': True, 'required': False}",
}
```

## Examples


``` yaml

- tower_credential_type:
    name: Nexus
    description: Credentials type for Nexus
    kind: cloud
    inputs: "{{ lookup('file', 'tower_credential_inputs_nexus.json') }}"
    injectors: {'extra_vars': {'nexus_credential': 'test' }}
    state: present
    tower_verify_ssl: false

- tower_credential_type:
    name: Nexus
    state: absent

```

## License

TODO

## Author Information
  - ['Adrien Fleury (@fleu42)']
