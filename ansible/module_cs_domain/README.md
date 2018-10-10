# Ansible module: ansible.module_cs_domain


Manages domains on Apache CloudStack based clouds

## Description

Create, update and remove domains.

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
    "clean_up": "{'description': ['Clean up all domain resources like child domains and accounts.', 'Considered on C(state=absent).'], 'default': False}",
    "network_domain": "{'description': ['Network domain for networks in the domain.']}",
    "path": "{'description': ['Path of the domain.', 'Prefix C(ROOT/) or C(/ROOT/) in path is optional.'], 'required': True}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'default': True}",
    "state": "{'description': ['State of the domain.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: Create a domain
  local_action:
    module: cs_domain
    path: ROOT/customers
    network_domain: customers.example.com

- name: Create another subdomain
  local_action:
    module: cs_domain
    path: ROOT/customers/xy
    network_domain: xy.customers.example.com

- name: Remove a domain
  local_action:
    module: cs_domain
    path: ROOT/customers/xy
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
