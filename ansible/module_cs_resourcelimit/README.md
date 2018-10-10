# Ansible module: ansible.module_cs_resourcelimit


Manages resource limits on Apache CloudStack based clouds

## Description

Manage limits of resources for domains, accounts and projects.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the resource is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "domain": "{'description': ['Domain the resource is related to.']}",
    "limit": "{'description': ['Maximum number of the resource.', 'Default is unlimited C(-1).'], 'default': -1, 'aliases': ['max']}",
    "project": "{'description': ['Name of the project the resource is related to.']}",
    "resource_type": "{'description': ['Type of the resource.'], 'required': True, 'choices': ['instance', 'ip_address', 'volume', 'snapshot', 'template', 'network', 'vpc', 'cpu', 'memory', 'primary_storage', 'secondary_storage'], 'aliases': ['type']}",
}
```

## Examples


``` yaml

- name: Update a resource limit for instances of a domain
  local_action:
    module: cs_resourcelimit
    type: instance
    limit: 10
    domain: customers

- name: Update a resource limit for instances of an account
  local_action:
    module: cs_resourcelimit
    type: instance
    limit: 12
    account: moserre
    domain: customers

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
