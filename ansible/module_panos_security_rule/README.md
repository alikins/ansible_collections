# Ansible module: ansible.module_panos_security_rule


Create security rule policy on PAN-OS devices or Panorama management console

## Description

Security policies allow you to enforce rules and take action, and can be as general or specific as needed. The policy rules are compared against the incoming traffic in sequence, and because the first rule that matches the traffic is applied, the more specific rules must precede the more general ones.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['Action to apply once rules maches.'], 'default': 'allow'}",
    "antivirus": "{'description': ['Name of the already defined antivirus profile.']}",
    "api_key": "{'description': ['API key that can be used instead of I(username)/I(password) credentials.']}",
    "application": "{'description': ['List of applications.'], 'default': 'any'}",
    "commit": "{'description': ['Commit configuration if changed.'], 'type': 'bool', 'default': True}",
    "data_filtering": "{'description': ['Name of the already defined data_filtering profile.']}",
    "description": "{'description': ['Description for the security rule.']}",
    "destination_ip": "{'description': ['List of destination addresses.'], 'default': 'any'}",
    "destination_zone": "{'description': ['List of destination zones.'], 'default': 'any'}",
    "devicegroup": "{'description': ['- Device groups are used for the Panorama interaction with Firewall(s). The group must exists on Panorama. If device group is not define we assume that we are contacting Firewall.\n']}",
    "file_blocking": "{'description': ['Name of the already defined file_blocking profile.']}",
    "group_profile": "{'description': ['- Security profile group that is already defined in the system. This property supersedes antivirus, vulnerability, spyware, url_filtering, file_blocking, data_filtering, and wildfire_analysis properties.\n']}",
    "hip_profiles": "{'description': ["- If you are using GlobalProtect with host information profile (HIP) enabled, you can also base the policy on information collected by GlobalProtect. For example, the user access level can be determined HIP that notifies the firewall about the user's local configuration.\n"], 'default': 'any'}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device being configured.'], 'required': True}",
    "log_end": "{'description': ['Whether to log at session end.'], 'default': True}",
    "log_start": "{'description': ['Whether to log at session start.']}",
    "operation": "{'description': ['The action to be taken.  Supported values are I(add)/I(update)/I(find)/I(delete).'], 'default': 'add'}",
    "password": "{'description': ['Password credentials to use for auth unless I(api_key) is set.'], 'required': True}",
    "rule_name": "{'description': ['Name of the security rule.'], 'required': True}",
    "rule_type": "{'description': ['Type of security rule (version 6.1 of PanOS and above).'], 'default': 'universal'}",
    "service": "{'description': ['List of services.'], 'default': 'application-default'}",
    "source_ip": "{'description': ['List of source addresses.'], 'default': 'any'}",
    "source_user": "{'description': ['Use users to enforce policy for individual users or a group of users.'], 'default': 'any'}",
    "source_zone": "{'description': ['List of source zones.'], 'default': 'any'}",
    "spyware": "{'description': ['Name of the already defined spyware profile.']}",
    "tag_name": "{'description': ['Administrative tags that can be added to the rule. Note, tags must be already defined.']}",
    "url_filtering": "{'description': ['Name of the already defined url_filtering profile.']}",
    "username": "{'description': ['Username credentials to use for auth unless I(api_key) is set.'], 'default': 'admin'}",
    "vulnerability": "{'description': ['Name of the already defined vulnerability profile.']}",
    "wildfire_analysis": "{'description': ['Name of the already defined wildfire_analysis profile.']}",
}
```

## Examples


``` yaml

- name: add an SSH inbound rule to devicegroup
  panos_security_rule:
    ip_address: '{{ ip_address }}'
    username: '{{ username }}'
    password: '{{ password }}'
    operation: 'add'
    rule_name: 'SSH permit'
    description: 'SSH rule test'
    tag_name: ['ProjectX']
    source_zone: ['public']
    destination_zone: ['private']
    source_ip: ['any']
    source_user: ['any']
    destination_ip: ['1.1.1.1']
    category: ['any']
    application: ['ssh']
    service: ['application-default']
    hip_profiles: ['any']
    action: 'allow'
    devicegroup: 'Cloud Edge'

- name: add a rule to allow HTTP multimedia only from CDNs
  panos_security_rule:
    ip_address: '10.5.172.91'
    username: 'admin'
    password: 'paloalto'
    operation: 'add'
    rule_name: 'HTTP Multimedia'
    description: 'Allow HTTP multimedia only to host at 1.1.1.1'
    source_zone: ['public']
    destination_zone: ['private']
    source_ip: ['any']
    source_user: ['any']
    destination_ip: ['1.1.1.1']
    category: ['content-delivery-networks']
    application: ['http-video', 'http-audio']
    service: ['service-http', 'service-https']
    hip_profiles: ['any']
    action: 'allow'

- name: add a more complex rule that uses security profiles
  panos_security_rule:
    ip_address: '{{ ip_address }}'
    username: '{{ username }}'
    password: '{{ password }}'
    operation: 'add'
    rule_name: 'Allow HTTP w profile'
    log_start: false
    log_end: true
    action: 'allow'
    antivirus: 'default'
    vulnerability: 'default'
    spyware: 'default'
    url_filtering: 'default'
    wildfire_analysis: 'default'

- name: delete a devicegroup security rule
  panos_security_rule:
    ip_address: '{{ ip_address }}'
    api_key: '{{ api_key }}'
    operation: 'delete'
    rule_name: 'Allow telnet'
    devicegroup: 'DC Firewalls'

- name: find a specific security rule
  panos_security_rule:
    ip_address: '{{ ip_address }}'
    password: '{{ password }}'
    operation: 'find'
    rule_name: 'Allow RDP to DCs'
  register: result
- debug: msg='{{result.stdout_lines}}'


```

## License

TODO

## Author Information
  - ['Ivan Bojer (@ivanbojer), Robert Hagen (@rnh556)']
