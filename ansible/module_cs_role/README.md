# Ansible module: ansible.module_cs_role


Manages user roles on Apache CloudStack based clouds

## Description

Create, update, delete user roles.

## Requirements

TODO

## Arguments

``` json
{
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "description": "{'description': ['Description of the role.']}",
    "id": "{'description': ['ID of the role.', 'If provided, C(id) is used as key.'], 'aliases': ['uuid']}",
    "name": "{'description': ['Name of the role.'], 'required': True}",
    "role_type": "{'description': ['Type of the role.', 'Only considered for creation.'], 'default': 'User', 'choices': ['User', 'DomainAdmin', 'ResourceAdmin', 'Admin']}",
    "state": "{'description': ['State of the role.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

# Ensure an user role is present
- local_action:
    module: cs_role
    name: myrole_user

# Ensure a role having particular ID is named as myrole_user
- local_action:
    module: cs_role
    name: myrole_user
    id: 04589590-ac63-4ffc-93f5-b698b8ac38b6

# Ensure a role is absent
- local_action:
    module: cs_role
    name: myrole_user
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
