# Ansible module: ansible.module_panos_match_rule


Test for match against a security rule on PAN-OS devices or Panorama management console

## Description

Security policies allow you to enforce rules and take action, and can be as general or specific as needed.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['API key that can be used instead of I(username)/I(password) credentials.']}",
    "application": "{'description': ['The application.']}",
    "category": "{'description': ['URL category']}",
    "destination_ip": "{'description': ['The destination IP address.']}",
    "destination_port": "{'description': ['The destination port.']}",
    "destination_zone": "{'description': ['The destination zone.']}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device being configured.'], 'required': True}",
    "password": "{'description': ['Password credentials to use for auth unless I(api_key) is set.'], 'required': True}",
    "protocol": "{'description': ['The IP protocol number from 1 to 255.']}",
    "rule_type": "{'description': ['Type of rule. Valid types are I(security) or I(nat).'], 'default': 'security'}",
    "source_ip": "{'description': ['The source IP address.'], 'required': True}",
    "source_port": "{'description': ['The source port.']}",
    "source_user": "{'description': ['The source user or group.']}",
    "source_zone": "{'description': ['The source zone.']}",
    "to_interface": "{'description': ['The inbound interface in a NAT rule.']}",
    "username": "{'description': ['Username credentials to use for auth unless I(api_key) is set.'], 'default': 'admin'}",
    "vsys_id": "{'description': ['ID of the VSYS object.'], 'default': 'vsys1', 'required': True}",
}
```

## Examples


``` yaml

- name: check security rules for Google DNS
  panos_match_rule:
    ip_address: '{{ ip_address }}'
    username: '{{ username }}'
    password: '{{ password }}'
    rule_type: 'security'
    source_ip: '10.0.0.0'
    destination_ip: '8.8.8.8'
    application: 'dns'
    destination_port: '53'
    protocol: '17'
  register: result
- debug: msg='{{result.stdout_lines}}'

- name: check security rules inbound SSH with user match
  panos_match_rule:
    ip_address: '{{ ip_address }}'
    username: '{{ username }}'
    password: '{{ password }}'
    rule_type: 'security'
    source_ip: '0.0.0.0'
    source_user: 'mydomain\jsmith'
    destination_ip: '192.168.100.115'
    destination_port: '22'
    protocol: '6'
  register: result
- debug: msg='{{result.stdout_lines}}'

- name: check NAT rules for source NAT
  panos_match_rule:
    ip_address: '{{ ip_address }}'
    username: '{{ username }}'
    password: '{{ password }}'
    rule_type: 'nat'
    source_zone: 'Prod-DMZ'
    source_ip: '10.10.118.50'
    to_interface: 'ethernet1/2'
    destination_zone: 'Internet'
    destination_ip: '0.0.0.0'
    protocol: '6'
  register: result
- debug: msg='{{result.stdout_lines}}'

- name: check NAT rules for inbound web
  panos_match_rule:
    ip_address: '{{ ip_address }}'
    username: '{{ username }}'
    password: '{{ password }}'
    rule_type: 'nat'
    source_zone: 'Internet'
    source_ip: '0.0.0.0'
    to_interface: 'ethernet1/1'
    destination_zone: 'Prod DMZ'
    destination_ip: '192.168.118.50'
    destination_port: '80'
    protocol: '6'
  register: result
- debug: msg='{{result.stdout_lines}}'

- name: check security rules for outbound POP3 in vsys4
  panos_match_rule:
    ip_address: '{{ ip_address }}'
    username: '{{ username }}'
    password: '{{ password }}'
    vsys_id: 'vsys4'
    rule_type: 'security'
    source_ip: '10.0.0.0'
    destination_ip: '4.3.2.1'
    application: 'pop3'
    destination_port: '110'
    protocol: '6'
  register: result
- debug: msg='{{result.stdout_lines}}'


```

## License

TODO

## Author Information
  - ['Robert Hagen (@rnh556)']
