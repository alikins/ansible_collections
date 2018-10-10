# Ansible module: ansible.module_cs_loadbalancer_rule_member


Manages load balancer rule members on Apache CloudStack based clouds

## Description

Add and remove load balancer rule members.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the rule is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "domain": "{'description': ['Domain the rule is related to.']}",
    "ip_address": "{'description': ['Public IP address from where the network traffic will be load balanced from.', 'Only needed to find the rule if C(name) is not unique.'], 'aliases': ['public_ip']}",
    "name": "{'description': ['The name of the load balancer rule.'], 'required': True}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'type': 'bool', 'default': True}",
    "project": "{'description': ['Name of the project the firewall rule is related to.']}",
    "state": "{'description': ['Should the VMs be present or absent from the rule.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vms": "{'description': ['List of VMs to assign to or remove from the rule.'], 'required': True, 'aliases': ['vm']}",
    "zone": "{'description': ['Name of the zone in which the rule should be located.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

- name: Add VMs to an existing load balancer
  local_action:
    module: cs_loadbalancer_rule_member
    name: balance_http
    vms:
      - web01
      - web02

- name: Remove a VM from an existing load balancer
  local_action:
    module: cs_loadbalancer_rule_member
    name: balance_http
    vms:
      - web01
      - web02
    state: absent

# Rolling upgrade of hosts
- hosts: webservers
  serial: 1
  pre_tasks:
    - name: Remove from load balancer
      local_action:
        module: cs_loadbalancer_rule_member
        name: balance_http
        vm: "{{ ansible_hostname }}"
        state: absent
  tasks:
    # Perform update
  post_tasks:
    - name: Add to load balancer
      local_action:
        module: cs_loadbalancer_rule_member
        name: balance_http
        vm: "{{ ansible_hostname }}"
        state: present

```

## License

TODO

## Author Information
  - ['Darren Worrall (@dazworrall)', 'René Moser (@resmo)']
  - ['Darren Worrall (@dazworrall)', 'René Moser (@resmo)']
