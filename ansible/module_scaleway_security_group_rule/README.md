# Ansible module: ansible.module_scaleway_security_group_rule


Scaleway Security Group Rule management module

## Description

This module manages Security Group Rule on Scaleway account U(https://developer.scaleway.com)

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['Rule action'], 'choices': ['accept', 'drop'], 'required': True}",
    "api_timeout": "{'description': ['HTTP timeout to Scaleway API in seconds.'], 'default': 30, 'aliases': ['timeout']}",
    "api_token": "{'description': ['Scaleway OAuth token.'], 'aliases': ['oauth_token']}",
    "api_url": "{'description': ['Scaleway API URL'], 'default': 'https://api.scaleway.com', 'aliases': ['base_url']}",
    "direction": "{'description': ['Rule direction'], 'choices': ['inbound', 'outbound'], 'required': True}",
    "ip_range": "{'description': ['IPV4 CIDR notation to apply to the rule'], 'default': '0.0.0.0/0'}",
    "port": "{'description': ['Port related to the rule, null value for all the ports'], 'required': True, 'type': 'int'}",
    "protocol": "{'description': ['Network protocol to use'], 'choices': ['TCP', 'UDP', 'ICMP'], 'required': True}",
    "region": "{'description': ['Scaleway region to use (for example C(par1)).'], 'required': True, 'choices': ['ams1', 'EMEA-NL-EVS', 'par1', 'EMEA-FR-PAR1']}",
    "security_group": "{'description': ['Security Group unique identifier'], 'required': True}",
    "state": "{'description': ['Indicate desired state of the Security Group Rule.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['Validate SSL certs of the Scaleway API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

  - name: Create a Security Group Rule
    scaleway_security_group_rule:
      state: present
      region: par1
      protocol: TCP
      port: 80
      ip_range: 0.0.0.0/0
      direction: inbound
      action: accept
      security_group: b57210ee-1281-4820-a6db-329f78596ecb
    register: security_group_rule_creation_task

```

## License

TODO

## Author Information
  - ['Antoine Barbare (@abarbare)']
