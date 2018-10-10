# Ansible module: ansible.module_exo_dns_domain


Manages domain records on Exoscale DNS API

## Description

Create and remove domain records.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['API key of the Exoscale DNS API.', 'Since 2.4, the ENV variable C(CLOUDSTACK_KEY) is used as default, when defined.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'Since 2.4, the ENV variable C(CLOUDSTACK_REGION) is used as default, when defined.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the Exoscale DNS API.', 'Since 2.4, the ENV variable C(CLOUDSTACK_SECRET) is used as default, when defined.']}",
    "api_timeout": "{'description': ['HTTP timeout to Exoscale DNS API.', 'Since 2.4, the ENV variable C(CLOUDSTACK_TIMEOUT) is used as default, when defined.'], 'default': 10}",
    "name": "{'description': ['Name of the record.'], 'required': True}",
    "state": "{'description': ['State of the resource.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['Validate SSL certs of the Exoscale DNS API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Create a domain
  local_action:
    module: exo_dns_domain
    name: example.com

- name: Remove a domain
  local_action:
    module: exo_dns_domain
    name: example.com
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
