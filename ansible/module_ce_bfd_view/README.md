# Ansible module: ansible.module_ce_bfd_view


Manages BFD session view configuration on HUAWEI CloudEngine devices

## Description

Manages BFD session view configuration on HUAWEI CloudEngine devices.

## Requirements

TODO

## Arguments

``` json
{
    "admin_down": "{'description': ['Enables the BFD session to enter the AdminDown state. By default, a BFD session is enabled. The default value is bool type.'], 'type': 'bool', 'default': False}",
    "description": "{'description': ['Specifies the description of a BFD session. The value is a string of 1 to 51 case-sensitive characters with spaces.']}",
    "detect_multi": "{'description': ['Specifies the local detection multiplier of a BFD session. The value is an integer that ranges from 3 to 50.']}",
    "local_discr": "{'description': ['Specifies the local discriminator of a BFD session. The value is an integer that ranges from 1 to 16384.']}",
    "min_rx_interval": "{'description': ['Specifies the minimum interval for sending BFD packets. The value is an integer that ranges from 50 to 1000, in milliseconds.']}",
    "min_tx_interval": "{'description': ['Specifies the minimum interval for receiving BFD packets. The value is an integer that ranges from 50 to 1000, in milliseconds.']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(netconf).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, netconf=22).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the CLI login. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for cli transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh).'], 'required': True, 'default': 'cli'}}}",
    "remote_discr": "{'description': ['Specifies the remote discriminator of a BFD session. The value is an integer that ranges from 1 to 4294967295.']}",
    "session_name": "{'description': ['Specifies the name of a BFD session. The value is a string of 1 to 15 case-sensitive characters without spaces.'], 'required': True}",
    "state": "{'description': ['Determines whether the config should be present or not on the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tos_exp": "{'description': ['Specifies a priority for BFD control packets. The value is an integer ranging from 0 to 7. The default value is 7, which is the highest priority.']}",
    "wtr_interval": "{'description': ['Specifies the WTR time of a BFD session. The value is an integer that ranges from 1 to 60, in minutes. The default value is 0.']}",
}
```

## Examples


``` yaml

- name: bfd view module test
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
  - name: Set the local discriminator of a BFD session to 80 and the remote discriminator to 800
    ce_bfd_view:
      session_name: atob
      local_discr: 80
      remote_discr: 800
      state: present
      provider: '{{ cli }}'

  - name: Set the minimum interval for receiving BFD packets to 500 ms
    ce_bfd_view:
      session_name: atob
      min_rx_interval: 500
      state: present
      provider: '{{ cli }}'

```

## License

TODO

## Author Information
  - ['QijunPan (@CloudEngine-Ansible)']
