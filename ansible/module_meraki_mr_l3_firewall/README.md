# Ansible module: ansible.module_meraki_mr_l3_firewall


Manage MR access point layer 3 firewalls in the Meraki cloud

## Description

Allows for creation, management, and visibility into layer 3 firewalls implemented on Meraki MR access points.

## Requirements

TODO

## Arguments

``` json
{
    "allow_lan_access": "{'description': ['Sets whether devices can talk to other devices on the same LAN.'], 'type': 'bool', 'default': True}",
    "auth_key": "{'description': ['Authentication key provided by the dashboard. Required if environmental variable MERAKI_KEY is not set.']}",
    "host": "{'description': ['Hostname for Meraki dashboard', 'Only useful for internal Meraki developers'], 'type': 'string', 'default': 'api.meraki.com'}",
    "net_id": "{'description': ['ID of network containing access points.']}",
    "net_name": "{'description': ['Name of network containing access points.']}",
    "number": "{'description': ['Number of SSID to apply firewall rule to.'], 'aliases': ['ssid_number']}",
    "org_id": "{'description': ['ID of organization.']}",
    "org_name": "{'description': ['Name of organization.'], 'aliases': ['organization']}",
    "output_level": "{'description': ['Set amount of debug output during module execution'], 'choices': ['normal', 'debug'], 'default': 'normal'}",
    "rules": "{'description': ['List of firewall rules.'], 'suboptions': {'policy': {'description': ['Specifies the action that should be taken when rule is hit.'], 'choices': ['allow', 'deny']}, 'protocol': {'description': ['Specifies protocol to match against.'], 'choices': ['any', 'icmp', 'tcp', 'udp']}, 'dest_port': {'description': ['Comma separated list of destination ports to match.']}, 'dest_cidr': {'description': ['Comma separated list of CIDR notation networks to match.']}, 'comment': {'description': ['Optional comment describing the firewall rule.']}}}",
    "ssid_name": "{'description': ['Name of SSID to apply firewall rule to.'], 'aliases': ['ssid']}",
    "state": "{'description': ['Create or modify an organization.'], 'default': 'present', 'choices': ['present', 'query']}",
    "timeout": "{'description': ['Time to timeout for HTTP requests.'], 'type': 'int', 'default': 30}",
    "use_https": "{'description': ['If C(no), it will use HTTP. Otherwise it will use HTTPS.', 'Only useful for internal Meraki developers'], 'type': 'bool', 'default': True}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool'}",
    "validate_certs": "{'description': ['Whether to validate HTTP certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Create single firewall rule
  meraki_mr_l3_firewall:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_id: 12345
    number: 1
    rules:
      - comment: Integration test rule
        policy: allow
        protocol: tcp
        dest_port: 80
        dest_cidr: 192.0.2.0/24
    allow_lan_access: no
  delegate_to: localhost

- name: Enable local LAN access
  meraki_mr_l3_firewall:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_id: 123
    number: 1
    rules:
    allow_lan_access: yes
  delegate_to: localhost

- name: Query firewall rules
  meraki_mr_l3_firewall:
    auth_key: abc123
    state: query
    org_name: YourOrg
    net_name: YourNet
    number: 1
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Kevin Breit (@kbreit)']
