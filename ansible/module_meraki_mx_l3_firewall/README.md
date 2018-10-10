# Ansible module: ansible.module_meraki_mx_l3_firewall


Manage MX appliance layer 3 firewalls in the Meraki cloud

## Description

Allows for creation, management, and visibility into layer 3 firewalls implemented on Meraki MX firewalls.

## Requirements

TODO

## Arguments

``` json
{
    "auth_key": "{'description': ['Authentication key provided by the dashboard. Required if environmental variable MERAKI_KEY is not set.']}",
    "host": "{'description': ['Hostname for Meraki dashboard', 'Only useful for internal Meraki developers'], 'type': 'string', 'default': 'api.meraki.com'}",
    "net_id": "{'description': ['ID of network which MX firewall is in.']}",
    "net_name": "{'description': ['Name of network which MX firewall is in.']}",
    "org_id": "{'description': ['ID of organization.']}",
    "org_name": "{'description': ['Name of organization.', 'If C(clone) is specified, C(org_name) is the name of the new organization.'], 'aliases': ['organization']}",
    "output_level": "{'description': ['Set amount of debug output during module execution'], 'choices': ['normal', 'debug'], 'default': 'normal'}",
    "rules": "{'description': ['List of firewall rules.'], 'suboptions': {'policy': {'description': ['Policy to apply if rule is hit.'], 'choices': ['allow', 'deny']}, 'protocol': {'description': ['Protocol to match against.'], 'choices': ['any', 'icmp', 'tcp', 'udp']}, 'dest_port': {'description': ['Comma separated list of destination port numbers to match against.']}, 'dest_cidr': {'description': ['Comma separated list of CIDR notation destination networks.']}, 'src_port': {'description': ['Comma separated list of source port numbers to match against.']}, 'src_cidr': {'description': ['Comma separated list of CIDR notation source networks.']}, 'comment': {'description': ['Optional comment to describe the firewall rule.']}, 'syslog_enabled': {'description': ['Whether to log hints against the firewall rule.', 'Only applicable if a syslog server is specified against the network.']}}}",
    "state": "{'description': ['Create or modify an organization.'], 'choices': ['present', 'query'], 'default': 'present'}",
    "syslog_default_rule": "{'description': ['Whether to log hits against the default firewall rule.', 'Only applicable if a syslog server is specified against the network.', 'This is not shown in response from Meraki. Instead, refer to the C(syslog_enabled) value in the default rule.'], 'type': 'bool', 'default': False}",
    "timeout": "{'description': ['Time to timeout for HTTP requests.'], 'type': 'int', 'default': 30}",
    "use_https": "{'description': ['If C(no), it will use HTTP. Otherwise it will use HTTPS.', 'Only useful for internal Meraki developers'], 'type': 'bool', 'default': True}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool'}",
    "validate_certs": "{'description': ['Whether to validate HTTP certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Query firewall rules
  meraki_mx_l3_firewall:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: query
  delegate_to: localhost

- name: Set two firewall rules
  meraki_mx_l3_firewall:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: present
    rules:
      - comment: Block traffic to server
        src_cidr: 192.0.1.0/24
        src_port: any
        dest_cidr: 192.0.2.2/32
        dest_port: any
        protocol: any
        policy: deny
      - comment: Allow traffic to group of servers
        src_cidr: 192.0.1.0/24
        src_port: any
        dest_cidr: 192.0.2.0/24
        dest_port: any
        protocol: any
        policy: permit
  delegate_to: localhost

- name: Set one firewall rule and enable logging of the default rule
  meraki_mx_l3_firewall:
    auth_key: abc123
    org_name: YourOrg
    net_name: YourNet
    state: present
    rules:
      - comment: Block traffic to server
        src_cidr: 192.0.1.0/24
        src_port: any
        dest_cidr: 192.0.2.2/32
        dest_port: any
        protocol: any
        policy: deny
    syslog_default_rule: yes
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Kevin Breit (@kbreit)']
