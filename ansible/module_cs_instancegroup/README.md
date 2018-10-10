# Ansible module: ansible.module_cs_instancegroup


Manages instance groups on Apache CloudStack based clouds

## Description

Create and remove instance groups.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the instance group is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "domain": "{'description': ['Domain the instance group is related to.']}",
    "name": "{'description': ['Name of the instance group.'], 'required': True}",
    "project": "{'description': ['Project the instance group is related to.']}",
    "state": "{'description': ['State of the instance group.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

# Create an instance group
- local_action:
    module: cs_instancegroup
    name: loadbalancers

# Remove an instance group
- local_action:
    module: cs_instancegroup
    name: loadbalancers
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
