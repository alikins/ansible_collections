# Ansible module: ansible.module_gcp_forwarding_rule


Create, Update or Destroy a Forwarding_Rule

## Description

Create, Update or Destroy a Forwarding_Rule. See U(https://cloud.google.com/compute/docs/load-balancing/http/target-proxies) for an overview. More details on the Global Forwarding_Rule API can be found at U(https://cloud.google.com/compute/docs/reference/latest/globalForwardingRules) More details on the Forwarding Rules API can be found at U(https://cloud.google.com/compute/docs/reference/latest/forwardingRules)

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['IPv4 or named IP address. Must be of the same scope (regional, global). Reserved addresses can (and probably should) be used for global forwarding rules. You may reserve IPs from the console or via the gce_eip module.'], 'required': False}",
    "forwarding_rule_name": "{'description': ['Name of the Forwarding_Rule.'], 'required': True}",
    "port_range": "{'description': ['For global forwarding rules, must be set to 80 or 8080 for TargetHttpProxy, and 443 for TargetHttpsProxy or TargetSslProxy.'], 'required': False}",
    "protocol": "{'description': ['For global forwarding rules, TCP, UDP, ESP, AH, SCTP or ICMP. Default is TCP.'], 'required': False}",
    "region": "{'description': ["The region for this forwarding rule. Currently, only 'global' is supported."], 'required': False}",
    "state": "{'description': ["The state of the Forwarding Rule. 'present' or 'absent'"], 'required': True, 'choices': ['present', 'absent']}",
    "target": "{'description': ['Target resource for forwarding rule. For global proxy, this is a Global TargetProxy resource. Required for external load balancing (including Global load balancing)'], 'required': False}",
}
```

## Examples


``` yaml

- name: Create Minimum GLOBAL Forwarding_Rule
  gcp_forwarding_rule:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    forwarding_rule_name: my-forwarding_rule
    protocol: TCP
    port_range: 80
    region: global
    target: my-target-proxy
    state: present

- name: Create Forwarding_Rule w/reserved static address
  gcp_forwarding_rule:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    forwarding_rule_name: my-forwarding_rule
    protocol: TCP
    port_range: 80
    address: my-reserved-static-address-name
    region: global
    target: my-target-proxy
    state: present

```

## License

TODO

## Author Information
  - ['Tom Melendez (@supertom) <tom@supertom.com>']
