# Ansible module: ansible.module_vultr_firewall_rule


Manages firewall rules on Vultr

## Description

Create and remove firewall rules.

## Requirements

TODO

## Arguments

``` json
{
    "api_account": "{'description': ['Name of the ini section in the C(vultr.ini) file.', 'The ENV variable C(VULTR_API_ACCOUNT) is used as default, when defined.'], 'default': 'default'}",
    "api_endpoint": "{'description': ['URL to API endpint (without trailing slash).', 'The ENV variable C(VULTR_API_ENDPOINT) is used as default, when defined.', 'Fallback value is U(https://api.vultr.com) if not specified.']}",
    "api_key": "{'description': ['API key of the Vultr API.', 'The ENV variable C(VULTR_API_KEY) is used as default, when defined.']}",
    "api_retries": "{'description': ['Amount of retries in case of the Vultr API retuns an HTTP 503 code.', 'The ENV variable C(VULTR_API_RETRIES) is used as default, when defined.', 'Fallback value is 5 retries if not specified.']}",
    "api_timeout": "{'description': ['HTTP timeout to Vultr API.', 'The ENV variable C(VULTR_API_TIMEOUT) is used as default, when defined.', 'Fallback value is 60 seconds if not specified.']}",
    "cidr": "{'description': ['Network in CIDR format', 'The CIDR format must match with the C(ip_version) value.', 'Required if C(state=present).', 'Defaulted to 0.0.0.0/0 or ::/0 depending on C(ip_version).']}",
    "end_port": "{'description': ['End port for the firewall rule.', 'Only considered if C(protocol) is tcp or udp and I(state=present).']}",
    "group": "{'description': ['Name of the firewall group.'], 'required': True}",
    "ip_version": "{'description': ['IP address version'], 'choices': ['v4', 'v6'], 'default': 'v4', 'aliases': ['ip_type']}",
    "protocol": "{'description': ['Protocol of the firewall rule.'], 'choices': ['icmp', 'tcp', 'udp', 'gre'], 'default': 'tcp'}",
    "start_port": "{'description': ['Start port for the firewall rule.', 'Required if C(protocol) is tcp or udp and I(state=present).'], 'aliases': ['port']}",
    "state": "{'description': ['State of the firewall rule.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['Validate SSL certs of the Vultr API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: ensure a firewall rule is present
  local_action:
    module: vultr_firewall_rule
    group: application
    protocol: tcp
    start_port: 8000
    end_port: 9000
    cidr: 17.17.17.0/24

- name: open DNS port for all ipv4 and ipv6
  local_action:
    module: vultr_firewall_rule
    group: dns
    protocol: udp
    port: 53
    ip_version: "{{ item }}"
  with_items: [ v4, v6 ]

- name: allow ping
  local_action:
    module: vultr_firewall_rule
    group: web
    protocol: icmp

- name: ensure a firewall rule is absent
  local_action:
    module: vultr_firewall_rule
    group: application
    protocol: tcp
    start_port: 8000
    end_port: 9000
    cidr: 17.17.17.0/24
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
