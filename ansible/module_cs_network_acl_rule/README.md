# Ansible module: ansible.module_cs_network_acl_rule


Manages network access control list (ACL) rules on Apache CloudStack based clouds

## Description

Add, update and remove network ACL rules.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the VPC is related to.']}",
    "action_policy": "{'description': ['Action policy of the rule.'], 'choices': ['allow', 'deny'], 'default': 'ingress', 'aliases': ['action']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "cidr": "{'description': ['CIDR of the rule.'], 'default': '0.0.0.0/0'}",
    "domain": "{'description': ['Domain the VPC is related to.']}",
    "end_port": "{'description': ['End port for this rule.', 'Considered if C(protocol=tcp) or C(protocol=udp).', 'If not specified, equal C(start_port).']}",
    "icmp_code": "{'description': ['Error code for this icmp message.', 'Considered if C(protocol=icmp).']}",
    "icmp_type": "{'description': ['Type of the icmp message being sent.', 'Considered if C(protocol=icmp).']}",
    "network_acl": "{'description': ['Name of the network ACL.'], 'required': True, 'aliases': ['acl']}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'type': 'bool', 'default': True}",
    "project": "{'description': ['Name of the project the VPC is related to.']}",
    "protocol": "{'description': ['Protocol of the rule'], 'choices': ['tcp', 'udp', 'icmp', 'all', 'by_number'], 'default': 'tcp'}",
    "protocol_number": "{'description': ['Protocol number from 1 to 256 required if C(protocol=by_number).']}",
    "rule_position": "{'description': ['CIDR of the rule.'], 'required': True, 'aliases': ['number']}",
    "start_port": "{'description': ['Start port for this rule.', 'Considered if C(protocol=tcp) or C(protocol=udp).'], 'aliases': ['port']}",
    "state": "{'description': ['State of the network ACL rule.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tags": "{'description': ['List of tags. Tags are a list of dictionaries having keys C(key) and C(value).', 'If you want to delete all tags, set a empty list e.g. C(tags: []).'], 'aliases': ['tag']}",
    "traffic_type": "{'description': ['Traffic type of the rule.'], 'choices': ['ingress', 'egress'], 'default': 'ingress', 'aliases': ['type']}",
    "vpc": "{'description': ['VPC the network ACL is related to.'], 'required': True}",
    "zone": "{'description': ['Name of the zone the VPC related to.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

# create a network ACL rule, allow port 80 ingress
- local_action:
    module: cs_network_acl_rule
    network_acl: web
    rule_position: 1
    vpc: my vpc
    traffic_type: ingress
    action_policy: allow
    port: 80
    cidr: 0.0.0.0/0

# create a network ACL rule, deny port range 8000-9000 ingress for 10.20.0.0/16
- local_action:
    module: cs_network_acl_rule
    network_acl: web
    rule_position: 1
    vpc: my vpc
    traffic_type: ingress
    action_policy: deny
    start_port: 8000
    end_port: 8000
    cidr: 10.20.0.0/16

# create a network ACL rule
- local_action:
    module: cs_network_acl_rule
    network_acl: web
    rule_position: 1
    vpc: my vpc
    traffic_type: ingress
    action_policy: deny
    start_port: 8000
    end_port: 8000
    cidr: 10.20.0.0/16

# remove a network ACL rule
- local_action:
    module: cs_network_acl_rule
    network_acl: web
    rule_position: 1
    vpc: my vpc
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
