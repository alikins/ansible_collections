# Ansible module: ansible.module_cs_region


Manages regions on Apache CloudStack based clouds

## Description

Add, update and remove regions.

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
    "endpoint": "{'description': ['Endpoint URL of the region.', 'Required if C(state=present)']}",
    "id": "{'description': ['ID of the region.', 'Must be an number (int).'], 'required': True}",
    "name": "{'description': ['Name of the region.', 'Required if C(state=present)']}",
    "state": "{'description': ['State of the region.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

# create a region
- local_action:
    module: cs_region
    id: 2
    name: geneva
    endpoint: https://cloud.gva.example.com

# remove a region with ID 2
- local_action:
    module: cs_region
    id: 2
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
