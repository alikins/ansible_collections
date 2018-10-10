# Ansible module: ansible.module_cs_portforward


Manages port forwarding rules on Apache CloudStack based clouds

## Description

Create, update and remove port forwarding rules.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the C(vm) is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "domain": "{'description': ['Domain the C(vm) is related to.']}",
    "ip_address": "{'description': ['Public IP address the rule is assigned to.'], 'required': True}",
    "network": "{'description': ['Name of the network.'], 'version_added': '2.3'}",
    "open_firewall": "{'description': ['Whether the firewall rule for public port should be created, while creating the new rule.', 'Use M(cs_firewall) for managing firewall rules.'], 'default': False}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'default': True}",
    "private_end_port": "{'description': ['End private port for this rule.', 'If not specified equal C(private_port).']}",
    "private_port": "{'description': ['Start private port for this rule.'], 'required': True}",
    "project": "{'description': ['Name of the project the C(vm) is located in.']}",
    "protocol": "{'description': ['Protocol of the port forwarding rule.'], 'default': 'tcp', 'choices': ['tcp', 'udp']}",
    "public_end_port": "{'description': ['End public port for this rule.', 'If not specified equal C(public_port).']}",
    "public_port": "{'description': ['Start public port for this rule.'], 'required': True}",
    "state": "{'description': ['State of the port forwarding rule.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tags": "{'description': ['List of tags. Tags are a list of dictionaries having keys C(key) and C(value).', 'To delete all tags, set a empty list e.g. C(tags: []).'], 'aliases': ['tag'], 'version_added': '2.4'}",
    "vm": "{'description': ['Name of virtual machine which we make the port forwarding rule for.', 'Required if C(state=present).']}",
    "vm_guest_ip": "{'description': ['VM guest NIC secondary IP address for the port forwarding rule.'], 'default': False}",
    "vpc": "{'description': ['Name of the VPC.'], 'version_added': '2.3'}",
    "zone": "{'description': ['Name of the zone in which the virtual machine is in.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

- name: 1.2.3.4:80 -> web01:8080
  local_action:
    module: cs_portforward
    ip_address: 1.2.3.4
    vm: web01
    public_port: 80
    private_port: 8080

- name: forward SSH and open firewall
  local_action:
    module: cs_portforward
    ip_address: '{{ public_ip }}'
    vm: '{{ inventory_hostname }}'
    public_port: '{{ ansible_ssh_port }}'
    private_port: 22
    open_firewall: true

- name: forward DNS traffic, but do not open firewall
  local_action:
    module: cs_portforward
    ip_address: 1.2.3.4
    vm: '{{ inventory_hostname }}'
    public_port: 53
    private_port: 53
    protocol: udp

- name: remove ssh port forwarding
  local_action:
    module: cs_portforward
    ip_address: 1.2.3.4
    public_port: 22
    private_port: 22
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
