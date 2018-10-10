# Ansible module: ansible.module_win_firewall_rule


Windows firewall automation

## Description

Allows you to create/remove/update firewall rules.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['What to do with the items this rule is for.'], 'required': True, 'choices': ['allow', 'block', 'bypass']}",
    "description": "{'description': ['Description for the firewall rule.']}",
    "direction": "{'description': ['Is this rule for inbound or outbound traffic.'], 'required': True, 'choices': ['in', 'out']}",
    "enabled": "{'description': ['Is this firewall rule enabled or disabled.'], 'type': 'bool', 'default': True, 'aliases': ['enable']}",
    "force": "{'description': ['Replace any existing rule by removing it first.', 'This is no longer required in 2.4 as rules no longer need replacing when being modified.', 'DEPRECATED in 2.4 and will be removed in 2.9.'], 'type': 'bool', 'default': False}",
    "localip": "{'description': ['The local ip address this rule applies to.'], 'default': 'any'}",
    "localport": "{'description': ['The local port this rule applies to.']}",
    "name": "{'description': ['The rules name'], 'required': True}",
    "profiles": "{'description': ['The profile this rule applies to.'], 'type': 'list', 'default': 'domain,private,public', 'aliases': ['profile']}",
    "program": "{'description': ['The program this rule applies to.']}",
    "protocol": "{'description': ['The protocol this rule applies to.'], 'default': 'any'}",
    "remoteip": "{'description': ['The remote ip address/range this rule applies to.'], 'default': 'any'}",
    "remoteport": "{'description': ['The remote port this rule applies to.']}",
    "service": "{'description': ['The service this rule applies to.']}",
    "state": "{'description': ['Should this rule be added or removed.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Firewall rule to allow SMTP on TCP port 25
  win_firewall_rule:
    name: SMTP
    localport: 25
    action: allow
    direction: in
    protocol: tcp
    state: present
    enabled: yes

- name: Firewall rule to allow RDP on TCP port 3389
  win_firewall_rule:
    name: Remote Desktop
    localport: 3389
    action: allow
    direction: in
    protocol: tcp
    profiles: private
    state: present
    enabled: yes

```

## License

TODO

## Author Information
  - ['Artem Zinenko (@ar7z1)', 'Timothy Vandenbrande (@TimothyVandenbrande)']
  - ['Artem Zinenko (@ar7z1)', 'Timothy Vandenbrande (@TimothyVandenbrande)']
