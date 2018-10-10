# Ansible module: ansible.module_vultr_ssh_key


Manages ssh keys on Vultr

## Description

Create, update and remove ssh keys.

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
    "name": "{'description': ['Name of the ssh key.'], 'required': True}",
    "ssh_key": "{'description': ['SSH public key.', 'Required if C(state=present).'], 'required': False}",
    "state": "{'description': ['State of the ssh key.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['Validate SSL certs of the Vultr API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: ensure an SSH key is present
  local_action:
    module: vultr_ssh_key
    name: my ssh key
    ssh_key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"

- name: ensure an SSH key is absent
  local_action:
    module: vultr_ssh_key
    name: my ssh key
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
