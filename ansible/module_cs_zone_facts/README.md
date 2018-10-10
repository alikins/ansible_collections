# Ansible module: ansible.module_cs_zone_facts


Gathering facts of zones from Apache CloudStack based clouds

## Description

Gathering facts from the API of a zone.
Sets Ansible facts accessable by the key C(cloudstack_zone) and since version 2.6 also returns results.

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
    "name": "{'description': ['Name of the zone.'], 'required': True, 'aliases': ['zone']}",
}
```

## Examples


``` yaml

- name: Gather facts from a zone
  local_action:
    module: cs_zone_facts
    name: ch-gva-1
  register: zone

- name: Show the returned results of the registered variable
  debug:
    var: zone

- name: Show the facts by the ansible_facts key cloudstack_zone
  debug:
    var: cloudstack_zone

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
