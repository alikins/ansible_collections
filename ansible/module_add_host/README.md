# Ansible module: ansible.module_add_host


add a host (and alternatively a group) to the ansible-playbook in-memory inventory

## Description

Use variables to create new hosts and groups in inventory for use in later plays of the same playbook. Takes variables so you can define the new hosts more fully.
This module is also supported for Windows targets.

## Requirements

TODO

## Arguments

``` json
{
    "groups": "{'aliases': ['groupname', 'group'], 'description': ['The groups to add the hostname to, comma separated.'], 'required': False}",
    "name": "{'aliases': ['hostname', 'host'], 'description': ['The hostname/ip of the host to add to the inventory, can include a colon and a port number.'], 'required': True}",
}
```

## Examples


``` yaml

- name: add host to group 'just_created' with variable foo=42
  add_host:
    name: "{{ ip_from_ec2 }}"
    groups: just_created
    foo: 42

- name: add host to multiple groups
  add_host:
    hostname: "{{ new_ip }}"
    groups:
      - group1
      - group2

- name: add a host with a non-standard port local to your machines
  add_host:
    name: "{{ new_ip }}:{{ new_port }}"

- name: add a host alias that we reach through a tunnel (Ansible <= 1.9)
  add_host:
    hostname: "{{ new_ip }}"
    ansible_ssh_host: "{{ inventory_hostname }}"
    ansible_ssh_port: "{{ new_port }}"

- name: add a host alias that we reach through a tunnel (Ansible >= 2.0)
  add_host:
    hostname: "{{ new_ip }}"
    ansible_host: "{{ inventory_hostname }}"
    ansible_port: "{{ new_port }}"

- name: Ensure inventory vars are set to the same value as the inventory_hostname has (close to pre 2.4 behaviour)
  add_host:
    hostname: charlie
    inventory_dir: "{{inventory_dir}}"

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Seth Vidal']
  - ['Ansible Core Team', 'Seth Vidal']
