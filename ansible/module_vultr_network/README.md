# Ansible module: ansible.module_vultr_network


Manages networks on Vultr

## Description

Manage networks on Vultr. A network cannot be updated. It needs to be deleted and re-created.

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
    "cidr": "{'description': ['The CIDR IPv4 network block to be used when attaching servers to this network. Required if I(state=present).']}",
    "name": "{'description': ['Name of the network.'], 'required': True, 'aliases': ['description', 'label']}",
    "region": "{'description': ['Region the network is deployed into. Required if I(state=present).']}",
    "state": "{'description': ['State of the network.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['Validate SSL certs of the Vultr API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Ensure a network is present
  local_action:
    module: vultr_network
    name: mynet
    cidr: 192.168.42.0/24
    region: Amsterdam

- name: Ensure a network is absent
  local_action:
    module: vultr_network
    name: mynet
    state: absent

```

## License

TODO

## Author Information
  - ['Yanis Guenane (@Spredzy)']
