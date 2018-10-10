# Ansible module: ansible.module_ce_vrrp


Manages VRRP interfaces on HUAWEI CloudEngine devices

## Description

Manages VRRP interface attributes on HUAWEI CloudEngine devices.

## Requirements

TODO

## Arguments

``` json
{
    "admin_flowdown": "{'description': ['Disable the flowdown function for service VRRP.'], 'type': 'bool', 'default': False}",
    "admin_ignore_if_down": "{'description': ['mVRRP ignores an interface Down event.'], 'type': 'bool', 'default': False}",
    "admin_interface": "{'description': ['Tracked mVRRP interface name. The value is a string of 1 to 63 characters.']}",
    "admin_vrid": "{'description': ['Tracked mVRRP ID. The value is an integer ranging from 1 to 255.']}",
    "advertise_interval": "{'description': ['Configured interval between sending advertisements, in milliseconds. Only the master router sends VRRP advertisements. The default value is 1000 milliseconds.']}",
    "auth_key": "{'description': ['This object is set based on the authentication type. When noAuthentication is specified, the value is empty. When simpleTextPassword or md5Authentication is specified, the value is a string of 1 to 8 characters in plaintext and displayed as a blank text for security.']}",
    "auth_mode": "{'description': ['Authentication type used for VRRP packet exchanges between virtual routers. The values are noAuthentication, simpleTextPassword, md5Authentication. The default value is noAuthentication.'], 'choices': ['simple', 'md5', 'none']}",
    "fast_resume": "{'description': ["mVRRP's fast resume mode."], 'choices': ['enable', 'disable']}",
    "gratuitous_arp_interval": "{'description': ['Interval at which gratuitous ARP packets are sent, in seconds. The value ranges from 30 to 1200.The default value is 300.']}",
    "holding_multiplier": "{'description': ['The configured holdMultiplier.The value is an integer ranging from 3 to 10. The default value is 3.']}",
    "interface": "{'description': ['Name of an interface. The value is a string of 1 to 63 characters.']}",
    "is_plain": "{'description': ['Select the display mode of an authentication key. By default, an authentication key is displayed in ciphertext.'], 'type': 'bool', 'default': False}",
    "preempt_timer_delay": "{'description': ['Preemption delay. The value is an integer ranging from 0 to 3600. The default value is 0.']}",
    "priority": "{'description': ['Configured VRRP priority. The value ranges from 1 to 254. The default value is 100. A larger value indicates a higher priority.']}",
    "recover_delay": "{'description': ['Delay in recovering after an interface goes Up. The delay is used for interface flapping suppression. The value is an integer ranging from 0 to 3600. The default value is 0 seconds.']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "version": "{'description': ['VRRP version. The default version is v2.'], 'choices': ['v2', 'v3']}",
    "virtual_ip": "{'description': ['Virtual IP address. The value is a string of 0 to 255 characters.']}",
    "vrid": "{'description': ['VRRP backup group ID. The value is an integer ranging from 1 to 255.'], 'default': 'present'}",
    "vrrp_type": "{'description': ['Type of a VRRP backup group.'], 'choices': ['normal', 'member', 'admin']}",
}
```

## Examples


``` yaml

- name: vrrp module test
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

  - name: Set vrrp version
    ce_vrrp:
      version: v3
      provider: "{{ cli }}"

  - name: Set vrrp gratuitous-arp interval
    ce_vrrp:
      gratuitous_arp_interval: 40
      mlag_id: 4
      provider: "{{ cli }}"

  - name: Set vrrp recover-delay
    ce_vrrp:
      recover_delay: 10
      provider: "{{ cli }}"

  - name: Set vrrp vrid virtual-ip
    ce_vrrp:
      interface: 40GE2/0/8
      vrid: 1
      virtual_ip: 10.14.2.7
      provider: "{{ cli }}"

  - name: Set vrrp vrid admin
    ce_vrrp:
      interface: 40GE2/0/8
      vrid: 1
      vrrp_type: admin
      provider: "{{ cli }}"

  - name: Set vrrp vrid fast_resume
    ce_vrrp:
      interface: 40GE2/0/8
      vrid: 1
      fast_resume: enable
      provider: "{{ cli }}"

  - name: Set vrrp vrid holding-multiplier
    ce_vrrp:
      interface: 40GE2/0/8
      vrid: 1
      holding_multiplier: 4
      provider: "{{ cli }}"

  - name: Set vrrp vrid preempt timer delay
    ce_vrrp:
      interface: 40GE2/0/8
      vrid: 1
      preempt_timer_delay: 10
      provider: "{{ cli }}"

  - name: Set vrrp vrid admin-vrrp
    ce_vrrp:
      interface: 40GE2/0/8
      vrid: 1
      admin_interface: 40GE2/0/9
      admin_vrid: 2
      vrrp_type: member
      provider: "{{ cli }}"

  - name: Set vrrp vrid authentication-mode
    ce_vrrp:
      interface: 40GE2/0/8
      vrid: 1
      is_plain: true
      auth_mode: simple
      auth_key: aaa
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Li Yanfeng (@CloudEngine-Ansible)']
