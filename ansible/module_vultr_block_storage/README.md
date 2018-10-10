# Ansible module: ansible.module_vultr_block_storage


Manages block storage volumes on Vultr

## Description

Manage block storage volumes on Vultr.

## Requirements

TODO

## Arguments

``` json
{
    "api_account": "{'description': ['Name of the ini section in the C(vultr.ini) file.', 'The ENV variable C(VULTR_API_ACCOUNT) is used as default, when defined.'], 'default': 'default'}",
    "api_endpoint": "{'description': ['URL to API endpint (without trailing slash).', 'The ENV variable C(VULTR_API_ENDPOINT) is used as default, when defined.', 'Fallback value is U(https://api.vultr.com) if not specified.']}",
    "api_key": "{'description': ['API key of the Vultr API.', 'The ENV variable C(VULTR_API_KEY) is used as default, when defined.']}",
    "api_retries": "{'description': ['Amount of retries in case of the Vultr API retuns an HTTP 503 code.', 'The ENV variable C(VULTR_API_RETRIES) is used as default, when defined.', 'Fallback value is 5 retries if not specified.']}",
    "api_timeout": "{'description': ['HTTP timeout to Vultr API.', 'The ENV variable C(VULTR_API_TIMEOUT) is used as default, when defined.', 'Fallback value is 60 seconds if not specified.']}",
    "name": "{'description': ['Name of the block storage volume.'], 'required': True, 'aliases': ['description', 'label']}",
    "region": "{'description': ['Region the block storage volume is deployed into.'], 'required': True}",
    "size": "{'description': ['Size of the block storage volume in GB.'], 'required': True}",
    "state": "{'description': ['State of the block storage volume.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['Validate SSL certs of the Vultr API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Ensure a block storage volume is present
  local_action:
    module: vultr_block_storage
    name: myvolume
    size: 10
    region: Amsterdam

- name: Ensure a block storage volume is absent
  local_action:
    module: vultr_block_storage
    name: myvolume
    state: absent

```

## License

TODO

## Author Information
  - ['Yanis Guenane (@Spredzy)']
