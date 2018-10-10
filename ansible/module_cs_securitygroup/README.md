# Ansible module: ansible.module_cs_securitygroup


Manages security groups on Apache CloudStack based clouds

## Description

Create and remove security groups.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the security group is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "description": "{'description': ['Description of the security group.']}",
    "domain": "{'description': ['Domain the security group is related to.']}",
    "name": "{'description': ['Name of the security group.'], 'required': True}",
    "project": "{'description': ['Name of the project the security group to be created in.']}",
    "state": "{'description': ['State of the security group.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: create a security group
  local_action:
    module: cs_securitygroup
    name: default
    description: default security group

- name: remove a security group
  local_action:
    module: cs_securitygroup
    name: default
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
