# Ansible module: ansible.module_ce_ntp_auth


Manages NTP authentication configuration on HUAWEI CloudEngine switches

## Description

Manages NTP authentication configuration on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "auth_mode": "{'description': ['Specify authentication algorithm.'], 'choices': ['hmac-sha256', 'md5']}",
    "auth_pwd": "{'description': ['Plain text with length of 1 to 255, encrypted text with length of 20 to 392.']}",
    "auth_type": "{'description': ['Whether the given password is in cleartext or has been encrypted. If in cleartext, the device will encrypt it before storing it.'], 'default': 'encrypt', 'choices': ['text', 'encrypt']}",
    "authentication": "{'description': ['Configure ntp authentication enable or unconfigure ntp authentication enable.'], 'choices': ['enable', 'disable']}",
    "key_id": "{'description': ['Authentication key identifier (numeric).'], 'required': True}",
    "state": "{'description': ['Manage the state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "trusted_key": "{'description': ['Whether the given key is required to be supplied by a time source for the device to synchronize to the time source.'], 'default': 'disable', 'choices': ['enable', 'disable']}",
}
```

## Examples


``` yaml

- name: NTP AUTH test
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

  - name: "Configure ntp authentication key-id"
    ce_ntp_auth:
      key_id: 32
      auth_mode: md5
      auth_pwd: 11111111111111111111111
      provider: "{{ cli }}"

  - name: "Configure ntp authentication key-id and trusted authentication keyid"
    ce_ntp_auth:
      key_id: 32
      auth_mode: md5
      auth_pwd: 11111111111111111111111
      trusted_key: enable
      provider: "{{ cli }}"

  - name: "Configure ntp authentication key-id and authentication enable"
    ce_ntp_auth:
      key_id: 32
      auth_mode: md5
      auth_pwd: 11111111111111111111111
      authentication: enable
      provider: "{{ cli }}"

  - name: "Unconfigure ntp authentication key-id and trusted authentication keyid"
    ce_ntp_auth:
      key_id: 32
      state: absent
      provider: "{{ cli }}"

  - name: "Unconfigure ntp authentication key-id and authentication enable"
    ce_ntp_auth:
      key_id: 32
      authentication: enable
      state: absent
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Zhijin Zhou (@CloudEngine-Ansible)']
