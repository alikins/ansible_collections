# Ansible module: ansible.module_cs_instance_nic


Manages NICs of an instance on Apache CloudStack based clouds

## Description

Add and remove nic to and from network

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
    "ip_address": "{'description': ['IP address to be used for the nic.']}",
    "network": "{'description': ['Name of the network.'], 'required': True}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'type': 'bool', 'default': True}",
    "project": "{'description': ['Name of the project the instance is deployed in.']}",
    "state": "{'description': ['State of the nic.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vm": "{'description': ['Name of instance.'], 'required': True, 'aliases': ['name']}",
    "vpc": "{'description': ['Name of the VPC the C(vm) is related to.']}",
    "zone": "{'description': ['Name of the zone in which the instance is deployed in.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

# Add a nic on another network
- local_action:
    module: cs_instance_nic
    vm: privnet
    network: privNetForBasicZone

# Ensure IP address on a nic
- local_action:
    module: cs_instance_nic
    vm: privnet
    ip_address: 10.10.11.32
    network: privNetForBasicZone

# Remove a secondary nic
- local_action:
    module: cs_instance_nic
    vm: privnet
    state: absent
    network: privNetForBasicZone

```

## License

TODO

## Author Information
  - ['Marc-Aurèle Brothier (@marcaurele)', 'René Moser (@resmo)']
  - ['Marc-Aurèle Brothier (@marcaurele)', 'René Moser (@resmo)']
