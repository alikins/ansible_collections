# Ansible module: ansible.module_cs_role_permission


Manages role permissions on Apache CloudStack based clouds

## Description

Create, update and remove CloudStack role permissions.
Managing role permissions only supported in CloudStack >= 4.9.

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
    "description": "{'description': ['The description of the role permission.']}",
    "name": "{'description': ['The API name of the permission.'], 'required': True}",
    "parent": "{'description': ['The parent role permission uuid. use 0 to move this rule at the top of the list.']}",
    "permission": "{'description': ['The rule permission, allow or deny. Defaulted to deny.'], 'choices': ['allow', 'deny'], 'default': 'deny'}",
    "role": "{'description': ['Name or ID of the role.'], 'required': True}",
    "state": "{'description': ['State of the role permission.'], 'choices': ['present', 'absent'], 'default': 'present'}",
}
```

## Examples


``` yaml

# Create a role permission
- local_action:
    module: cs_role_permission
    role: "My_Custom_role"
    name: "createVPC"
    permission: "allow"
    description: "My comments"

# Remove a role permission
- local_action:
    module: cs_role_permission
    state: absent
    role: "My_Custom_role"
    name: "createVPC"

# Update a system role permission
- local_action:
    module: cs_role_permission
    role: "Domain Admin"
    name: "createVPC"
    permission: "deny"

# Update rules order. Move the rule at the top of list
- local_action:
    module: cs_role_permission
    role: "Domain Admin"
    name: "createVPC"
    parent: 0

```

## License

TODO

## Author Information
  - ['David Passante (@dpassante)']
