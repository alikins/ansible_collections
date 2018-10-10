# Ansible module: ansible.module_cs_vpn_gateway


Manages site-to-site VPN gateways on Apache CloudStack based clouds

## Description

Creates and removes VPN site-to-site gateways.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the VPN gateway is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "domain": "{'description': ['Domain the VPN gateway is related to.']}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'type': 'bool', 'default': True}",
    "project": "{'description': ['Name of the project the VPN gateway is related to.']}",
    "state": "{'description': ['State of the VPN gateway.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vpc": "{'description': ['Name of the VPC.'], 'required': True}",
    "zone": "{'description': ['Name of the zone the VPC is related to.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

# Ensure a vpn gateway is present
- local_action:
    module: cs_vpn_gateway
    vpc: my VPC

# Ensure a vpn gateway is absent
- local_action:
    module: cs_vpn_gateway
    vpc: my VPC
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
