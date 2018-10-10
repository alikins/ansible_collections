# Ansible module: ansible.module_ce_ntp


Manages core NTP configuration on HUAWEI CloudEngine switches

## Description

Manages core NTP configuration on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "is_preferred": "{'description': ['Makes given NTP server or peer the preferred NTP server or peer for the device.'], 'choices': ['enable', 'disable']}",
    "key_id": "{'description': ['Authentication key identifier to use with given NTP server or peer.']}",
    "peer": "{'description': ['Network address of NTP peer.']}",
    "server": "{'description': ['Network address of NTP server.']}",
    "source_int": "{'description': ['Local source interface from which NTP messages are sent. Must be fully qualified interface name, i.e. C(40GE1/0/22), C(vlanif10). Interface types, such as C(10GE), C(40GE), C(100GE), C(Eth-Trunk), C(LoopBack), C(MEth), C(NULL), C(Tunnel), C(Vlanif).']}",
    "state": "{'description': ['Manage the state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "vpn_name": "{'description': ['Makes the device communicate with the given NTP server or peer over a specific vpn.'], 'default': '_public_'}",
}
```

## Examples


``` yaml

- name: NTP test
  hosts: cloudengine
  connection: local
  gather_facts: no
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

  - name: "Set NTP Server with parameters"
    ce_ntp:
      server: 192.8.2.6
      vpn_name: js
      source_int: vlanif4001
      is_preferred: enable
      key_id: 32
      provider: "{{ cli }}"

  - name: "Set NTP Peer with parameters"
    ce_ntp:
      peer: 192.8.2.6
      vpn_name: js
      source_int: vlanif4001
      is_preferred: enable
      key_id: 32
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Zhijin Zhou (@CloudEngine-Ansible)']
