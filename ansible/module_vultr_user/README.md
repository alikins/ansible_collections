# Ansible module: ansible.module_vultr_user


Manages users on Vultr

## Description

Create, update and remove users.

## Requirements

TODO

## Arguments

``` json
{
    "acls": "{'description': ['List of ACLs this users should have, see U(https://www.vultr.com/api/#user_user_list).', 'Required if C(state=present).', 'One or more of the choices list, some depend on each other.'], 'choices': ['manage_users', 'subscriptions', 'provisioning', 'billing', 'support', 'abuse', 'dns', 'upgrade'], 'aliases': ['acl']}",
    "api_account": "{'description': ['Name of the ini section in the C(vultr.ini) file.', 'The ENV variable C(VULTR_API_ACCOUNT) is used as default, when defined.'], 'default': 'default'}",
    "api_enabled": "{'description': ['Whether the API is enabled or not.'], 'default': True, 'type': 'bool'}",
    "api_endpoint": "{'description': ['URL to API endpint (without trailing slash).', 'The ENV variable C(VULTR_API_ENDPOINT) is used as default, when defined.', 'Fallback value is U(https://api.vultr.com) if not specified.']}",
    "api_key": "{'description': ['API key of the Vultr API.', 'The ENV variable C(VULTR_API_KEY) is used as default, when defined.']}",
    "api_retries": "{'description': ['Amount of retries in case of the Vultr API retuns an HTTP 503 code.', 'The ENV variable C(VULTR_API_RETRIES) is used as default, when defined.', 'Fallback value is 5 retries if not specified.']}",
    "api_timeout": "{'description': ['HTTP timeout to Vultr API.', 'The ENV variable C(VULTR_API_TIMEOUT) is used as default, when defined.', 'Fallback value is 60 seconds if not specified.']}",
    "email": "{'description': ['Email of the user.', 'Required if C(state=present).']}",
    "force": "{'description': ['Password will only be changed with enforcement.'], 'default': False, 'type': 'bool'}",
    "name": "{'description': ['Name of the user'], 'required': True}",
    "password": "{'description': ['Password of the user.', 'Only considered while creating a user or when C(force=yes).']}",
    "state": "{'description': ['State of the user.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['Validate SSL certs of the Vultr API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Ensure a user exists
  local_action:
    module: vultr_user
    name: john
    email: john.doe@example.com
    password: s3cr3t
    acls:
      - upgrade
      - dns
      - manage_users
      - subscriptions
      - upgrade

- name: Remove a user
  local_action:
    module: vultr_user
    name: john
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
