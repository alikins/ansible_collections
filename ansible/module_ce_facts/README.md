# Ansible module: ansible.module_ce_facts


Gets facts about HUAWEI CloudEngine switches

## Description

Collects facts from CloudEngine devices running the CloudEngine operating system.  Fact collection is supported over Cli transport.  This module prepends all of the base network fact keys with C(ansible_net_<fact>).  The facts module will always collect a base set of facts from the device and can enable or disable collection of additional facts.

## Requirements

TODO

## Arguments

``` json
{
    "gather_subset": "{'description': ['When supplied, this argument will restrict the facts collected to a given subset.  Possible values for this argument include all, hardware, config, and interfaces.  Can specify a list of values to include a larger subset.  Values can also be used with an initial C(M(!)) to specify that a specific subset should not be collected.'], 'required': False, 'default': '!config'}",
}
```

## Examples


``` yaml

# Note: examples below use the following provider dict to handle
#       transport and authentication to the node.

- name: CloudEngine facts test
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

  - name: "Gather_subset is all"
    ce_facts:
      gather_subset: all
      provider: "{{ cli }}"

  - name: "Collect only the config facts"
    ce_facts:
      gather_subset: config
      provider: "{{ cli }}"

  - name: "Do not collect hardware facts"
    ce_facts:
      gather_subset: "!hardware"
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
