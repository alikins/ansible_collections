# Ansible module: ansible.module_cs_securitygroup_rule


Manages security group rules on Apache CloudStack based clouds

## Description

Add and remove security group rules.

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
    "cidr": "{'description': ['CIDR (full notation) to be used for security group rule.'], 'default': '0.0.0.0/0'}",
    "end_port": "{'description': ['End port for this rule. Required if C(protocol=tcp) or C(protocol=udp), but C(start_port) will be used if not set.']}",
    "icmp_code": "{'description': ['Error code for this icmp message. Required if C(protocol=icmp).']}",
    "icmp_type": "{'description': ['Type of the icmp message being sent. Required if C(protocol=icmp).']}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'default': True}",
    "project": "{'description': ['Name of the project the security group to be created in.']}",
    "protocol": "{'description': ['Protocol of the security group rule.'], 'default': 'tcp', 'choices': ['tcp', 'udp', 'icmp', 'ah', 'esp', 'gre']}",
    "security_group": "{'description': ['Name of the security group the rule is related to. The security group must be existing.'], 'required': True}",
    "start_port": "{'description': ['Start port for this rule. Required if C(protocol=tcp) or C(protocol=udp).'], 'aliases': ['port']}",
    "state": "{'description': ['State of the security group rule.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "type": "{'description': ['Ingress or egress security group rule.'], 'default': 'ingress', 'choices': ['ingress', 'egress']}",
    "user_security_group": "{'description': ['Security group this rule is based of.']}",
}
```

## Examples


``` yaml

---
- name: allow inbound port 80/tcp from 1.2.3.4 added to security group 'default'
  local_action:
    module: cs_securitygroup_rule
    security_group: default
    port: 80
    cidr: 1.2.3.4/32

- name: allow tcp/udp outbound added to security group 'default'
  local_action:
    module: cs_securitygroup_rule
    security_group: default
    type: egress
    start_port: 1
    end_port: 65535
    protocol: '{{ item }}'
  with_items:
  - tcp
  - udp

- name: allow inbound icmp from 0.0.0.0/0 added to security group 'default'
  local_action:
    module: cs_securitygroup_rule
    security_group: default
    protocol: icmp
    icmp_code: -1
    icmp_type: -1

- name: remove rule inbound port 80/tcp from 0.0.0.0/0 from security group 'default'
  local_action:
    module: cs_securitygroup_rule
    security_group: default
    port: 80
    state: absent

- name: allow inbound port 80/tcp from security group web added to security group 'default'
  local_action:
    module: cs_securitygroup_rule
    security_group: default
    port: 80
    user_security_group: web

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
