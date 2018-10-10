# Ansible module: ansible.module_panos_security_policy


Create security rule policy on PanOS devices

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
    "commit": "{'description': ['Commit configuration if changed.'], 'default': True}",
    "data_filtering": "{'description': ['Name of the already defined data_filtering profile.']}",
    "description": "{'description': ['Description for the security rule.']}",
    "destination": "{'description': ['List of destination addresses.'], 'default': 'any'}",
    "devicegroup": "{'description': ['Device groups are used for the Panorama interaction with Firewall(s). The group must exists on Panorama. If device group is not define we assume that we are contacting Firewall.\n']}",
    "file_blocking": "{'description': ['Name of the already defined file_blocking profile.']}",
    "from_zone": "{'description': ['List of source zones.'], 'default': 'any'}",
    "group_profile": "{'description': ['Security profile group that is already defined in the system. This property supersedes antivirus, vulnerability, spyware, url_filtering, file_blocking, data_filtering, and wildfire_analysis properties.\n']}",
    "hip_profiles": "{'description': ["If you are using GlobalProtect with host information profile (HIP) enabled, you can also base the policy on information collected by GlobalProtect. For example, the user access level can be determined HIP that notifies the firewall about the user's local configuration.\n"], 'default': 'any'}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device being configured.'], 'required': True}",
    "log_end": "{'description': ['Whether to log at session end.'], 'default': True}",
    "log_start": "{'description': ['Whether to log at session start.']}",
    "password": "{'description': ['Password credentials to use for auth unless I(api_key) is set.'], 'required': True}",
    "rule_name": "{'description': ['Name of the security rule.'], 'required': True}",
    "rule_type": "{'description': ['Type of security rule (version 6.1 of PanOS and above).'], 'default': 'universal'}",
    "service": "{'description': ['List of services.'], 'default': 'application-default'}",
    "source": "{'description': ['List of source addresses.'], 'default': 'any'}",
    "source_user": "{'description': ['Use users to enforce policy for individual users or a group of users.'], 'default': 'any'}",
    "spyware": "{'description': ['Name of the already defined spyware profile.']}",
    "tag": "{'description': ['Administrative tags that can be added to the rule. Note, tags must be already defined.']}",
    "to_zone": "{'description': ['List of destination zones.'], 'default': 'any'}",
    "url_filtering": "{'description': ['Name of the already defined url_filtering profile.']}",
    "username": "{'description': ['Username credentials to use for auth unless I(api_key) is set.'], 'default': 'admin'}",
    "vulnerability": "{'description': ['Name of the already defined vulnerability profile.']}",
    "wildfire_analysis": "{'description': ['Name of the already defined wildfire_analysis profile.']}",
}
```

## Examples


``` yaml

- name: permit ssh to 1.1.1.1
  panos_security_policy:
    ip_address: '10.5.172.91'
    username: 'admin'
    password: 'paloalto'
    rule_name: 'SSH permit'
    description: 'SSH rule test'
    from_zone: ['public']
    to_zone: ['private']
    source: ['any']
    source_user: ['any']
    destination: ['1.1.1.1']
    category: ['any']
    application: ['ssh']
    service: ['application-default']
    hip_profiles: ['any']
    action: 'allow'
    commit: false

- name: Allow HTTP multimedia only from CDNs
  panos_security_policy:
    ip_address: '10.5.172.91'
    username: 'admin'
    password: 'paloalto'
    rule_name: 'HTTP Multimedia'
    description: 'Allow HTTP multimedia only to host at 1.1.1.1'
    from_zone: ['public']
    to_zone: ['private']
    source: ['any']
    source_user: ['any']
    destination: ['1.1.1.1']
    category: ['content-delivery-networks']
    application: ['http-video', 'http-audio']
    service: ['service-http', 'service-https']
    hip_profiles: ['any']
    action: 'allow'
    commit: false

- name: more complex fictitious rule that uses profiles
  panos_security_policy:
    ip_address: '10.5.172.91'
    username: 'admin'
    password: 'paloalto'
    rule_name: 'Allow HTTP w profile'
    log_start: false
    log_end: true
    action: 'allow'
    antivirus: 'default'
    vulnerability: 'default'
    spyware: 'default'
    url_filtering: 'default'
    wildfire_analysis: 'default'
    commit: false

- name: deny all
  panos_security_policy:
    ip_address: '10.5.172.91'
    username: 'admin'
    password: 'paloalto'
    rule_name: 'DenyAll'
    log_start: true
    log_end: true
    action: 'deny'
    rule_type: 'interzone'
    commit: false

# permit ssh to 1.1.1.1 using panorama and pushing the configuration to firewalls
# that are defined in 'DeviceGroupA' device group
- name: permit ssh to 1.1.1.1 through Panorama
  panos_security_policy:
    ip_address: '10.5.172.92'
    password: 'paloalto'
    rule_name: 'SSH permit'
    description: 'SSH rule test'
    from_zone: ['public']
    to_zone: ['private']
    source: ['any']
    source_user: ['any']
    destination: ['1.1.1.1']
    category: ['any']
    application: ['ssh']
    service: ['application-default']
    hip_profiles: ['any']
    action: 'allow'
    devicegroup: 'DeviceGroupA'

```

## License

TODO

## Author Information
  - ['Ivan Bojer (@ivanbojer)']
