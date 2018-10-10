# Ansible module: ansible.module_cs_affinitygroup


Manages affinity groups on Apache CloudStack based clouds

## Description

Create and remove affinity groups.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the affinity group is related to.']}",
    "affinity_type": "{'description': ['Type of the affinity group. If not specified, first found affinity type is used.'], 'aliases': ['affinty_type']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "description": "{'description': ['Description of the affinity group.']}",
    "domain": "{'description': ['Domain the affinity group is related to.']}",
    "name": "{'description': ['Name of the affinity group.'], 'required': True}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'type': 'bool', 'default': True}",
    "project": "{'description': ['Name of the project the affinity group is related to.']}",
    "state": "{'description': ['State of the affinity group.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

# Create a affinity group
- local_action:
    module: cs_affinitygroup
    name: haproxy
    affinity_type: host anti-affinity

# Remove a affinity group
- local_action:
    module: cs_affinitygroup
    name: haproxy
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
