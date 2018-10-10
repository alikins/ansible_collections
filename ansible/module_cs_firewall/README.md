# Ansible module: ansible.module_cs_firewall


Manages firewall rules on Apache CloudStack based clouds

## Description

Creates and removes firewall rules.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the firewall rule is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "cidrs": "{'description': ['List of CIDRs (full notation) to be used for firewall rule.', 'Since version 2.5, it is a list of CIDR.'], 'default': '0.0.0.0/0', 'aliases': ['cidr']}",
    "domain": "{'description': ['Domain the firewall rule is related to.']}",
    "end_port": "{'description': ['End port for this rule. Considered if C(protocol=tcp) or C(protocol=udp).', 'If not specified, equal C(start_port).']}",
    "icmp_code": "{'description': ['Error code for this icmp message.', 'Considered if C(protocol=icmp).']}",
    "icmp_type": "{'description': ['Type of the icmp message being sent.', 'Considered if C(protocol=icmp).']}",
    "ip_address": "{'description': ['Public IP address the ingress rule is assigned to.', 'Required if C(type=ingress).']}",
    "network": "{'description': ['Network the egress rule is related to.', 'Required if C(type=egress).']}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'default': True, 'type': 'bool'}",
    "project": "{'description': ['Name of the project the firewall rule is related to.']}",
    "protocol": "{'description': ['Protocol of the firewall rule.', 'C(all) is only available if C(type=egress).'], 'default': 'tcp', 'choices': ['tcp', 'udp', 'icmp', 'all']}",
    "start_port": "{'description': ['Start port for this rule.', 'Considered if C(protocol=tcp) or C(protocol=udp).'], 'aliases': ['port']}",
    "state": "{'description': ['State of the firewall rule.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tags": "{'description': ['List of tags. Tags are a list of dictionaries having keys C(key) and C(value).', 'To delete all tags, set a empty list e.g. C(tags: []).'], 'aliases': ['tag'], 'version_added': '2.4'}",
    "type": "{'description': ['Type of the firewall rule.'], 'default': 'ingress', 'choices': ['ingress', 'egress']}",
    "zone": "{'description': ['Name of the zone in which the virtual machine is in.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

- name: Allow inbound port 80/tcp from 1.2.3.4 to 4.3.2.1
  local_action:
    module: cs_firewall
    ip_address: 4.3.2.1
    port: 80
    cidr: 1.2.3.4/32

- name: Allow inbound tcp/udp port 53 to 4.3.2.1
  local_action:
    module: cs_firewall
    ip_address: 4.3.2.1
    port: 53
    protocol: '{{ item }}'
  with_items:
  - tcp
  - udp

- name: Ensure firewall rule is removed
  local_action:
    module: cs_firewall
    ip_address: 4.3.2.1
    start_port: 8000
    end_port: 8888
    cidr: 17.0.0.0/8
    state: absent

- name: Allow all outbound traffic
  local_action:
    module: cs_firewall
    network: my_network
    type: egress
    protocol: all

- name: Allow only HTTP outbound traffic for an IP
  local_action:
    module: cs_firewall
    network: my_network
    type: egress
    port: 80
    cidr: 10.101.1.20

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
