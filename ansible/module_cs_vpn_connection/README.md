# Ansible module: ansible.module_cs_vpn_connection


Manages site-to-site VPN connections on Apache CloudStack based clouds

## Description

Create and remove VPN connections.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the VPN connection is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "domain": "{'description': ['Domain the VPN connection is related to.']}",
    "force": "{'description': ['Activate the VPN gateway if not already activated on C(state=present).', 'Also see M(cs_vpn_gateway).'], 'default': False, 'type': 'bool'}",
    "passive": "{'description': ['State of the VPN connection.', 'Only considered when C(state=present).'], 'default': False, 'type': 'bool'}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'default': True, 'type': 'bool'}",
    "project": "{'description': ['Name of the project the VPN connection is related to.']}",
    "state": "{'description': ['State of the VPN connection.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vpc": "{'description': ['Name of the VPC the VPN connection is related to.'], 'required': True}",
    "vpn_customer_gateway": "{'description': ['Name of the VPN customer gateway.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create a VPN connection with activated VPN gateway
  local_action:
    module: cs_vpn_connection
    vpn_customer_gateway: my vpn connection
    vpc: my vpc

- name: Create a VPN connection and force VPN gateway activation
  local_action:
    module: cs_vpn_connection
    vpn_customer_gateway: my vpn connection
    vpc: my vpc
    force: yes

- name: Remove a vpn connection
  local_action:
    module: cs_vpn_connection
    vpn_customer_gateway: my vpn connection
    vpc: my vpc
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
