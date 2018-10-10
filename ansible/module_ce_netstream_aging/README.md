# Ansible module: ansible.module_ce_netstream_aging


Manages timeout mode of NetStream on HUAWEI CloudEngine switches

## Description

Manages timeout mode of NetStream on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "manual_slot": "{'description': ['Specifies the slot number of netstream manual timeout.']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout_interval": "{'description': ['Netstream timeout interval. If is active type the interval is 1-60. If is inactive ,the interval is 5-600.'], 'default': 30}",
    "timeout_type": "{'description': ['Netstream timeout type.'], 'choices': ['active', 'inactive', 'tcp-session', 'manual']}",
    "type": "{'description': ['Specifies the packet type of netstream timeout active interval.'], 'choices': ['ip', 'vxlan']}",
}
```

## Examples


``` yaml

- name: netstream aging module test
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

  - name: Configure netstream ip timeout active interval , the interval is 40 minutes.
    ce_netstream_aging:
      timeout_interval: 40
      type: ip
      timeout_type: active
      state: present
      provider: "{{ cli }}"

  - name: Configure netstream vxlan timeout active interval , the interval is 40 minutes.
    ce_netstream_aging:
      timeout_interval: 40
      type: vxlan
      timeout_type: active
      active_state: present
      provider: "{{ cli }}"

  - name: Delete netstream ip timeout active interval , set the ip timeout interval to 30 minutes.
    ce_netstream_aging:
      type: ip
      timeout_type: active
      state: absent
      provider: "{{ cli }}"

  - name: Delete netstream vxlan timeout active interval , set the vxlan timeout interval to 30 minutes.
    ce_netstream_aging:
      type: vxlan
      timeout_type: active
      state: absent
      provider: "{{ cli }}"

  - name: Enable netstream ip tcp session timeout.
    ce_netstream_aging:
      type: ip
      timeout_type: tcp-session
      state: present
      provider: "{{ cli }}"

  - name: Enable netstream vxlan tcp session timeout.
    ce_netstream_aging:
      type: vxlan
      timeout_type: tcp-session
      state: present
      provider: "{{ cli }}"

  - name: Disable netstream ip tcp session timeout.
    ce_netstream_aging:
      type: ip
      timeout_type: tcp-session
      state: absent
      provider: "{{ cli }}"

  - name: Disable netstream vxlan tcp session timeout.
    ce_netstream_aging:
      type: vxlan
      timeout_type: tcp-session
      state: absent
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['YangYang (@CloudEngine-Ansible)']
