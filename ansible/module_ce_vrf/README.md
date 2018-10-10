# Ansible module: ansible.module_ce_vrf


Manages VPN instance on HUAWEI CloudEngine switches

## Description

Manages VPN instance of HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['Description of the vrf, the string length is 1 - 242 .']}",
    "state": "{'description': ['Manage the state of the resource.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "vrf": "{'description': ['VPN instance, the length of vrf name is 1 - 31, i.e. "test", but can not be C(_public_).'], 'required': True}",
}
```

## Examples


``` yaml

- name: vrf module test
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

  - name: Config a vpn install named vpna, description is test
    ce_vrf:
      vrf: vpna
      description: test
      state: present
      provider: "{{ cli }}"
  - name: Delete a vpn install named vpna
    ce_vrf:
      vrf: vpna
      state: absent
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Yang yang (@CloudEngine-Ansible)']
