# Ansible module: ansible.module_ce_stp


Manages STP configuration on HUAWEI CloudEngine switches

## Description

Manages STP configurations on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "bpdu_filter": "{'description': ['Specify a port as a BPDU filter port.'], 'choices': ['enable', 'disable']}",
    "bpdu_protection": "{'description': ['Configure BPDU protection on an edge port. This function prevents network flapping caused by attack packets.'], 'choices': ['enable', 'disable']}",
    "cost": "{'description': ['Set the path cost of the current port. The default instance is 0.']}",
    "edged_port": "{'description': ['Set the current port as an edge port.'], 'choices': ['enable', 'disable']}",
    "interface": "{'description': ['Interface name. If the value is C(all), will apply configuration to all interfaces. if the value is a special name, only support input the full name.']}",
    "loop_protection": "{'description': ['Enable loop protection on the current port.'], 'choices': ['enable', 'disable']}",
    "root_protection": "{'description': ['Enable root protection on the current port.'], 'choices': ['enable', 'disable']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "stp_converge": "{'description': ['STP convergence mode. Fast means set STP aging mode to Fast. Normal means set STP aging mode to Normal.'], 'choices': ['fast', 'normal']}",
    "stp_enable": "{'description': ['Enable or disable STP on a switch.'], 'choices': ['enable', 'disable']}",
    "stp_mode": "{'description': ['Set an operation mode for the current MSTP process. The mode can be STP, RSTP, or MSTP.'], 'choices': ['stp', 'rstp', 'mstp']}",
    "tc_protection": "{'description': ['Configure the TC BPDU protection function for an MSTP process.'], 'choices': ['enable', 'disable']}",
    "tc_protection_interval": "{'description': ['Set the time the MSTP device takes to handle the maximum number of TC BPDUs and immediately refresh forwarding entries. The value is an integer ranging from 1 to 600, in seconds.']}",
    "tc_protection_threshold": "{'description': ['Set the maximum number of TC BPDUs that the MSTP can handle. The value is an integer ranging from 1 to 255. The default value is 1 on the switch.']}",
}
```

## Examples


``` yaml


- name: CloudEngine stp test
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

  - name: "Config stp mode"
    ce_stp:
      state: present
      stp_mode: stp
      provider: "{{ cli }}"

  - name: "Undo stp mode"
    ce_stp:
      state: absent
      stp_mode: stp
      provider: "{{ cli }}"

  - name: "Enable bpdu protection"
    ce_stp:
      state: present
      bpdu_protection: enable
      provider: "{{ cli }}"

  - name: "Disable bpdu protection"
    ce_stp:
      state: present
      bpdu_protection: disable
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
