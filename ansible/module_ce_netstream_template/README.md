# Ansible module: ansible.module_ce_netstream_template


Manages NetStream template configuration on HUAWEI CloudEngine switches

## Description

Manages NetStream template configuration on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "collect_counter": "{'description': ['Configure the number of packets and bytes that are included in the flexible flow statistics sent to NSC.'], 'choices': ['bytes', 'packets']}",
    "collect_interface": "{'description': ['Configure the input or output interface that are included in the flexible flow statistics sent to NSC.'], 'choices': ['input', 'output']}",
    "description": "{'description': ['Configure the description of netstream record. The value is a string of 1 to 80 case-insensitive characters.']}",
    "match": "{'description': ['Configure flexible flow statistics template keywords.'], 'choices': ['destination-address', 'destination-port', 'tos', 'protocol', 'source-address', 'source-port']}",
    "record_name": "{'description': ['Configure the name of netstream record. The value is a string of 1 to 32 case-insensitive characters.']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "type": "{'description': ['Configure the type of netstream record.'], 'required': True, 'choices': ['ip', 'vxlan']}",
}
```

## Examples


``` yaml

- name: netstream template module test
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

  - name: Config ipv4 netstream record
    ce_netstream_template:
      state: present
      type: ip
      record_name: test
      provider: "{{ cli }}"
  - name: Undo ipv4 netstream record
    ce_netstream_template:
      state: absent
      type: ip
      record_name: test
      provider: "{{ cli }}"
  - name: Config ipv4 netstream record collect_counter
    ce_netstream_template:
      state: present
      type: ip
      record_name: test
      collect_counter: bytes
      provider: "{{ cli }}"
  - name: Undo ipv4 netstream record collect_counter
    ce_netstream_template:
      state: absent
      type: ip
      record_name: test
      collect_counter: bytes
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
