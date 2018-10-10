# Ansible module: ansible.module_cs_instance_facts


Gathering facts from the API of instances from Apache CloudStack based clouds

## Description

Gathering facts from the API of an instance.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the instance is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "domain": "{'description': ['Domain the instance is related to.']}",
    "name": "{'description': ['Name or display name of the instance.'], 'required': True}",
    "project": "{'description': ['Project the instance is related to.']}",
}
```

## Examples


``` yaml

- name: gather instance facts
  cs_instance_facts:
    name: web-vm-1
  delegate_to: localhost
  register: vm

- debug:
    var: cloudstack_instance

- debug:
    var: vm

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
