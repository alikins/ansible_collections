# Ansible module: ansible.module_ce_aaa_server_host


Manages AAA server host configuration on HUAWEI CloudEngine switches

## Description

Manages AAA server host configuration on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "hwtacacs_is_public_net": "{'description': ['Set the public-net.'], 'type': 'bool', 'default': False}",
    "hwtacacs_is_secondary_server": "{'description': ['Whether the server is secondary.'], 'type': 'bool', 'default': False}",
    "hwtacacs_server_host_name": "{'description': ['Hwtacacs server host name.']}",
    "hwtacacs_server_ip": "{'description': ['Server IPv4 address. Must be a valid unicast IP address. The value is a string of 0 to 255 characters, in dotted decimal notation.']}",
    "hwtacacs_server_ipv6": "{'description': ['Server IPv6 address. Must be a valid unicast IP address. The total length is 128 bits.']}",
    "hwtacacs_server_type": "{'description': ['Hwtacacs server type.'], 'choices': ['Authentication', 'Authorization', 'Accounting', 'Common']}",
    "hwtacacs_template": "{'description': ['Name of a HWTACACS template. The value is a string of 1 to 32 case-insensitive characters.']}",
    "hwtacacs_vpn_name": "{'description': ['VPN instance name.']}",
    "local_ftp_dir": "{'description': ['FTP user directory. The value is a string of 1 to 255 characters.']}",
    "local_password": "{'description': ['Login password of a user. The password can contain letters, numbers, and special characters. The value is a string of 1 to 255 characters.']}",
    "local_service_type": "{'description': ['The type of local user login through, such as ftp ssh snmp telnet.']}",
    "local_user_group": "{'description': ['Name of the user group where the user belongs. The user inherits all the rights of the user group. The value is a string of 1 to 32 characters.']}",
    "local_user_level": "{'description': ['Login level of a local user. The value is an integer ranging from 0 to 15.']}",
    "local_user_name": "{'description': ['Name of a local user. The value is a string of 1 to 253 characters.']}",
    "radius_group_name": "{'description': ["RADIUS server group's name. The value is a string of 1 to 32 case-insensitive characters."]}",
    "radius_server_ip": "{'description': ['IPv4 address of configured server. The value is a string of 0 to 255 characters, in dotted decimal notation.']}",
    "radius_server_ipv6": "{'description': ['IPv6 address of configured server. The total length is 128 bits.']}",
    "radius_server_mode": "{'description': ['Configured primary or secondary server for a particular server.'], 'choices': ['Secondary-server', 'Primary-server']}",
    "radius_server_name": "{'description': ['Hostname of configured server. The value is a string of 0 to 255 case-sensitive characters.']}",
    "radius_server_port": "{'description': ['Configured server port for a particular server. The value is an integer ranging from 1 to 65535.']}",
    "radius_server_type": "{'description': ['Type of Radius Server.'], 'choices': ['Authentication', 'Accounting']}",
    "radius_vpn_name": "{'description': ['Set VPN instance. The value is a string of 1 to 31 case-sensitive characters.']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml


- name: AAA server host test
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

  - name: "Config local user when use local scheme"
    ce_aaa_server_host:
      state: present
      local_user_name: user1
      local_password: 123456
      provider: "{{ cli }}"

  - name: "Undo local user when use local scheme"
    ce_aaa_server_host:
      state: absent
      local_user_name: user1
      local_password: 123456
      provider: "{{ cli }}"

  - name: "Config radius server ip"
    ce_aaa_server_host:
      state: present
      radius_group_name: group1
      radius_server_type: Authentication
      radius_server_ip: 10.1.10.1
      radius_server_port: 2000
      radius_server_mode: Primary-server
      radius_vpn_name: _public_
      provider: "{{ cli }}"

  - name: "Undo radius server ip"
    ce_aaa_server_host:
      state: absent
      radius_group_name: group1
      radius_server_type: Authentication
      radius_server_ip: 10.1.10.1
      radius_server_port: 2000
      radius_server_mode: Primary-server
      radius_vpn_name: _public_
      provider: "{{ cli }}"

  - name: "Config hwtacacs server ip"
    ce_aaa_server_host:
      state: present
      hwtacacs_template: template
      hwtacacs_server_ip: 10.10.10.10
      hwtacacs_server_type: Authorization
      hwtacacs_vpn_name: _public_
      provider: "{{ cli }}"

  - name: "Undo hwtacacs server ip"
    ce_aaa_server_host:
      state: absent
      hwtacacs_template: template
      hwtacacs_server_ip: 10.10.10.10
      hwtacacs_server_type: Authorization
      hwtacacs_vpn_name: _public_
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
