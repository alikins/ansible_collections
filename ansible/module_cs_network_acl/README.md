# Ansible module: ansible.module_cs_network_acl


Manages network access control lists (ACL) on Apache CloudStack based clouds

## Description

Create and remove network ACLs.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the network ACL rule is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "description": "{'description': ['Description of the network ACL.', 'If not set, identical to C(name).']}",
    "domain": "{'description': ['Domain the network ACL rule is related to.']}",
    "name": "{'description': ['Name of the network ACL.'], 'required': True}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'type': 'bool', 'default': True}",
    "project": "{'description': ['Name of the project the network ACL is related to.']}",
    "state": "{'description': ['State of the network ACL.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vpc": "{'description': ['VPC the network ACL is related to.'], 'required': True}",
    "zone": "{'description': ['Name of the zone the VPC is related to.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

# create a network ACL
- local_action:
    module: cs_network_acl
    name: Webserver ACL
    description: a more detailed description of the ACL
    vpc: customers

# remove a network ACL
- local_action:
    module: cs_network_acl
    name: Webserver ACL
    vpc: customers
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
