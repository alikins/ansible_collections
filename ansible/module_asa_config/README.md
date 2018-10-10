# Ansible module: ansible.module_asa_config


Manage configuration sections on Cisco ASA devices

## Description

Cisco ASA configurations use a simple block indent file syntax for segmenting configuration into sections.  This module provides an implementation for working with ASA configuration sections in a deterministic way.

## Requirements

TODO

## Arguments

``` json
{
    "after": "{'description': ['The ordered set of commands to append to the end of the command stack if a change needs to be made.  Just like with I(before) this allows the playbook designer to append a set of commands to be executed after the command set.']}",
    "authorize": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "backup": "{'description': ['This argument will cause the module to create a full backup of the current C(running-config) from the remote device before any changes are made.  The backup file is written to the C(backup) folder in the playbook root directory.  If the directory does not exist, it is created.'], 'type': 'bool', 'default': False}",
    "before": "{'description': ['The ordered set of commands to push on to the command stack if a change needs to be made.  This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system.']}",
    "config": "{'description': ['The C(config) argument allows the playbook designer to supply the base configuration to be used to validate configuration changes necessary.  If this argument is provided, the module will not download the running-config from the remote node.']}",
    "context": "{'description': ['Specifies which context to target if you are running in the ASA in multiple context mode. Defaults to the current context you login to.']}",
    "defaults": "{'description': ['This argument specifies whether or not to collect all defaults when getting the remote device running config.  When enabled, the module will get the current config by issuing the command C(show running-config all).'], 'type': 'bool', 'default': False}",
    "lines": "{'description': ['The ordered set of commands that should be configured in the section.  The commands must be the exact same commands as found in the device running-config.  Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser.'], 'aliases': ['commands']}",
    "match": "{'description': ['Instructs the module on the way to perform the matching of the set of commands against the current device config.  If match is set to I(line), commands are matched line by line.  If match is set to I(strict), command lines are matched with respect to position.  If match is set to I(exact), command lines must be an equal match.  Finally, if match is set to I(none), the module will not attempt to compare the source configuration with the running configuration on the remote device.'], 'default': 'line', 'choices': ['line', 'strict', 'exact', 'none']}",
    "parents": "{'description': ['The ordered set of parents that uniquely identify the section or hierarchy the commands should be checked against.  If the parents argument is omitted, the commands are checked against the set of top level or global commands.']}",
    "passwords": "{'description': ['This argument specifies to include passwords in the config when retrieving the running-config from the remote device.  This includes passwords related to VPN endpoints.  This argument is mutually exclusive with I(defaults).'], 'type': 'bool', 'default': False}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.']}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}, 'timeout': {'description': ['Specifies idle timeout in seconds for the connection, in seconds. Useful if the console freezes before continuing. For example when saving configurations.'], 'default': 10}}}",
    "replace": "{'description': ['Instructs the module on the way to perform the configuration on the device.  If the replace argument is set to I(line) then the modified lines are pushed to the device in configuration mode.  If the replace argument is set to I(block) then the entire command block is pushed to the device in configuration mode if any line is not correct'], 'default': 'line', 'choices': ['line', 'block']}",
    "save": "{'description': ['The C(save) argument instructs the module to save the running- config to the startup-config at the conclusion of the module running.  If check mode is specified, this argument is ignored.'], 'type': 'bool', 'default': False}",
    "src": "{'description': ['Specifies the source path to the file that contains the configuration or configuration template to load.  The path to the source file can either be the full path on the Ansible control host or a relative path from the playbook or role root directory.  This argument is mutually exclusive with I(lines), I(parents).']}",
}
```

## Examples


``` yaml

# Note: examples below use the following provider dict to handle
#       transport and authentication to the node.
---
vars:
  cli:
    host: "{{ inventory_hostname }}"
    username: cisco
    password: cisco
    authorize: yes
    auth_pass: cisco

---
- asa_config:
    lines:
      - network-object host 10.80.30.18
      - network-object host 10.80.30.19
      - network-object host 10.80.30.20
    parents: ['object-group network OG-MONITORED-SERVERS']
    provider: "{{ cli }}"

- asa_config:
    host: "{{ inventory_hostname }}"
    lines:
      - message-length maximum client auto
      - message-length maximum 512
    match: line
    parents: ['policy-map type inspect dns PM-DNS', 'parameters']
    authorize: yes
    auth_pass: cisco
    username: admin
    password: cisco
    context: ansible

- asa_config:
    lines:
      - ikev1 pre-shared-key MyS3cretVPNK3y
    parents: tunnel-group 1.1.1.1 ipsec-attributes
    passwords: yes
    provider: "{{ cli }}"

- name: attach ASA acl on interface vlan13/nameif cloud13
  asa_config:
    lines:
      - access-group cloud-acl_access_in in interface cloud13
    provider: "{{ cli }}"

- name: configure ASA (>=9.2) default BGP
  asa_config:
    lines:
      - bgp log-neighbor-changes
      - bgp bestpath compare-routerid
    provider: "{{ cli }}"
    parents:
      - router bgp 65002
  register: bgp
  when: bgp_default_config is defined

- name: configure ASA (>=9.2) BGP neighbor in default/single context mode
  asa_config:
    lines:
      - "bgp router-id {{ bgp_router_id }}"
      - "neighbor {{ bgp_neighbor_ip }} remote-as {{ bgp_neighbor_as }}"
      - "neighbor {{ bgp_neighbor_ip }} description {{ bgp_neighbor_name }}"
    provider: "{{ cli }}"
    parents:
      - router bgp 65002
      - address-family ipv4 unicast
  register: bgp
  when: bgp_neighbor_as is defined

- name: configure ASA interface with standby
  asa_config:
    lines:
      - description my cloud interface
      - nameif cloud13
      - security-level 50
      - ip address 192.168.13.1 255.255.255.0 standby 192.168.13.2
    provider: "{{ cli }}"
    parents: ["interface Vlan13"]
  register: interface

- name: Show changes to interface from task above
  debug:
    var: interface


```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip), Patrick Ogenstad (@ogenstad)']
