# Ansible module: ansible.module_cs_loadbalancer_rule


Manages load balancer rules on Apache CloudStack based clouds

## Description

Add, update and remove load balancer rules.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the rule is related to.']}",
    "algorithm": "{'description': ['Load balancer algorithm', 'Required when using C(state=present).'], 'choices': ['source', 'roundrobin', 'leastconn'], 'default': 'source'}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "cidr": "{'description': ['CIDR (full notation) to be used for firewall rule if required.']}",
    "description": "{'description': ['The description of the load balancer rule.']}",
    "domain": "{'description': ['Domain the rule is related to.']}",
    "ip_address": "{'description': ['Public IP address from where the network traffic will be load balanced from.'], 'required': True, 'aliases': ['public_ip']}",
    "name": "{'description': ['The name of the load balancer rule.'], 'required': True}",
    "open_firewall": "{'description': ['Whether the firewall rule for public port should be created, while creating the new rule.', 'Use M(cs_firewall) for managing firewall rules.'], 'type': 'bool', 'default': False}",
    "private_port": "{'description': ['The private port of the private ip address/virtual machine where the network traffic will be load balanced to.', 'Required when using C(state=present).', 'Can not be changed once the rule exists due API limitation.']}",
    "project": "{'description': ['Name of the project the load balancer IP address is related to.']}",
    "protocol": "{'description': ['The protocol to be used on the load balancer']}",
    "public_port": "{'description': ['The public port from where the network traffic will be load balanced from.', 'Required when using C(state=present).', 'Can not be changed once the rule exists due API limitation.'], 'required': True}",
    "state": "{'description': ['State of the rule.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "zone": "{'description': ['Name of the zone in which the rule should be created.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

# Create a load balancer rule
- local_action:
    module: cs_loadbalancer_rule
    name: balance_http
    public_ip: 1.2.3.4
    algorithm: leastconn
    public_port: 80
    private_port: 8080

# update algorithm of an existing load balancer rule
- local_action:
    module: cs_loadbalancer_rule
    name: balance_http
    public_ip: 1.2.3.4
    algorithm: roundrobin
    public_port: 80
    private_port: 8080

# Delete a load balancer rule
- local_action:
    module: cs_loadbalancer_rule
    name: balance_http
    public_ip: 1.2.3.4
    state: absent

```

## License

TODO

## Author Information
  - ['Darren Worrall (@dazworrall)', 'René Moser (@resmo)']
  - ['Darren Worrall (@dazworrall)', 'René Moser (@resmo)']
