# Ansible module: ansible.module_cs_vpc


Manages VPCs on Apache CloudStack based clouds

## Description

Create, update and delete VPCs.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the VPC is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "cidr": "{'description': ['CIDR of the VPC, e.g. 10.1.0.0/16', "All VPC guest networks' CIDRs must be within this CIDR.", 'Required on I(state=present).']}",
    "clean_up": "{'description': ['Whether to redeploy a VPC router or not when I(state=restarted)'], 'version_added': '2.5', 'type': 'bool'}",
    "display_text": "{'description': ['Display text of the VPC.', 'If not set, C(name) will be used for creating.']}",
    "domain": "{'description': ['Domain the VPC is related to.']}",
    "name": "{'description': ['Name of the VPC.'], 'required': True}",
    "network_domain": "{'description': ['Network domain for the VPC.', 'All networks inside the VPC will belong to this domain.', 'Only considered while creating the VPC, can not be changed.']}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'default': True, 'type': 'bool'}",
    "project": "{'description': ['Name of the project the VPC is related to.']}",
    "state": "{'description': ['State of the VPC.', 'The state C(present) creates a started VPC.', 'The state C(stopped) is only considered while creating the VPC, added in version 2.6.'], 'default': 'present', 'choices': ['present', 'absent', 'stopped', 'restarted']}",
    "tags": "{'description': ['List of tags. Tags are a list of dictionaries having keys C(key) and C(value).', 'For deleting all tags, set an empty list e.g. I(tags: []).'], 'aliases': ['tag']}",
    "vpc_offering": "{'description': ['Name of the VPC offering.', 'If not set, default VPC offering is used.']}",
    "zone": "{'description': ['Name of the zone.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

- name: Ensure a VPC is present but not started after creating
  local_action:
    module: cs_vpc
    name: my_vpc
    display_text: My example VPC
    cidr: 10.10.0.0/16
    state: stopped

- name: Ensure a VPC is present and started after creating
  local_action:
    module: cs_vpc
    name: my_vpc
    display_text: My example VPC
    cidr: 10.10.0.0/16

- name: Ensure a VPC is absent
  local_action:
    module: cs_vpc
    name: my_vpc
    state: absent

- name: Ensure a VPC is restarted with clean up
  local_action:
    module: cs_vpc
    name: my_vpc
    clean_up: yes
    state: restarted

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
