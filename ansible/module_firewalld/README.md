# Ansible module: ansible.module_firewalld


Manage arbitrary ports/services with firewalld

## Description

This module allows for addition or deletion of services and ports either tcp or udp in either running or permanent firewalld rules.

## Requirements

TODO

## Arguments

``` json
{
    "immediate": "{'description': ['Should this configuration be applied immediately, if set as permanent'], 'type': 'bool', 'default': False, 'version_added': '1.9'}",
    "interface": "{'description': ['The interface you would like to add/remove to/from a zone in firewalld'], 'version_added': '2.1'}",
    "masquerade": "{'description': ['The masquerade setting you would like to enable/disable to/from zones within firewalld'], 'version_added': '2.1'}",
    "permanent": "{'description': ["Should this configuration be in the running firewalld configuration or persist across reboots. As of Ansible version 2.3, permanent operations can operate on firewalld configs when it's not running (requires firewalld >= 3.0.9). (NOTE: If this is false, immediate is assumed true.)\n"], 'type': 'bool'}",
    "port": "{'description': ['Name of a port or port range to add/remove to/from firewalld. Must be in the form PORT/PROTOCOL or PORT-PORT/PROTOCOL for port ranges.']}",
    "rich_rule": "{'description': ['Rich rule to add/remove to/from firewalld.']}",
    "service": "{'description': ['Name of a service to add/remove to/from firewalld - service must be listed in output of firewall-cmd --get-services.']}",
    "source": "{'description': ['The source/network you would like to add/remove to/from firewalld'], 'version_added': '2.0'}",
    "state": "{'description': ['Enable or disable a setting. For ports: Should this port accept(enabled) or reject(disabled) connections. The states "present" and "absent" can only be used in zone level operations (i.e. when no other parameters but zone and state are set).\n'], 'required': True, 'choices': ['enabled', 'disabled', 'present', 'absent']}",
    "timeout": "{'description': ['The amount of time the rule should be in effect for when non-permanent.'], 'default': 0}",
    "zone": "{'description': ['The firewalld zone to add/remove to/from (NOTE: default zone can be configured per system but "public" is default from upstream. Available choices can be extended based on per-system configs, listed here are "out of the box" defaults).\n'], 'default': 'system-default(public)', 'choices': ['work', 'drop', 'internal', 'external', 'trusted', 'home', 'dmz', 'public', 'block']}",
}
```

## Examples


``` yaml

- firewalld:
    service: https
    permanent: yes
    state: enabled

- firewalld:
    port: 8081/tcp
    permanent: yes
    state: disabled

- firewalld:
    port: 161-162/udp
    permanent: yes
    state: enabled

- firewalld:
    zone: dmz
    service: http
    permanent: yes
    state: enabled

- firewalld:
    rich_rule: 'rule service name="ftp" audit limit value="1/m" accept'
    permanent: yes
    state: enabled

- firewalld:
    source: 192.0.2.0/24
    zone: internal
    state: enabled

- firewalld:
    zone: trusted
    interface: eth2
    permanent: yes
    state: enabled

- firewalld:
    masquerade: yes
    state: enabled
    permanent: yes
    zone: dmz

- firewalld:
    zone: custom
    state: present
    permanent: yes

- name: Redirect port 443 to 8443 with Rich Rule
  firewalld:
    rich_rule: rule family={{ item }} forward-port port=443 protocol=tcp to-port=8443
    zone:      public
    permanent: yes
    immediate: yes
    state:     enabled
  with_items:
    - ipv4
    - ipv6

```

## License

TODO

## Author Information
  - ['Adam Miller (@maxamillion)']
