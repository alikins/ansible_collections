# Ansible module: ansible.module_ce_info_center_global


Manages outputting logs on HUAWEI CloudEngine switches

## Description

This module offers the ability to be output to the log buffer, log file, console, terminal, or log host on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "channel_cfg_name": "{'description': ['Channel name.The value is a string of 1 to 30 case-sensitive characters. The default value is console.'], 'default': 'console'}",
    "channel_id": "{'description': ['Number for channel. The value is an integer ranging from 0 to 9. The default value is 0.']}",
    "channel_name": "{'description': ['Channel name. The value is a string of 1 to 30 case-sensitive characters.']}",
    "channel_out_direct": "{'description': ['Direction of information output.'], 'choices': ['console', 'monitor', 'trapbuffer', 'logbuffer', 'snmp', 'logfile']}",
    "facility": "{'description': ['Log record tool.'], 'choices': ['local0', 'local1', 'local2', 'local3', 'local4', 'local5', 'local6', 'local7']}",
    "filter_feature_name": "{'description': ['Feature name of the filtered log. The value is a string of 1 to 31 case-insensitive characters.']}",
    "filter_log_name": "{'description': ['Name of the filtered log. The value is a string of 1 to 63 case-sensitive characters.']}",
    "info_center_enable": "{'description': ['Whether the info-center function is enabled. The value is of the Boolean type.'], 'choices': ['true', 'false']}",
    "ip_type": "{'description': ['Log server address type, IPv4 or IPv6.'], 'choices': ['ipv4', 'ipv6']}",
    "is_default_vpn": "{'description': ['Use the default VPN or not.'], 'type': 'bool', 'default': False}",
    "level": "{'description': ['Level of logs saved on a log server.'], 'choices': ['emergencies', 'alert', 'critical', 'error', 'warning', 'notification', 'informational', 'debugging']}",
    "logfile_max_num": "{'description': ['Maximum number of log files of the same type. The default value is 200.', 'The value range for log files is[3, 500], for security files is [1, 3],and for operation files is [1, 7].']}",
    "logfile_max_size": "{'description': ['Maximum size (in MB) of a log file. The default value is 32.', 'The value range for log files is [4, 8, 16, 32], for security files is [1, 4],', 'and for operation files is [1, 4].'], 'default': 32, 'choices': ['4', '8', '16', '32']}",
    "packet_priority": "{'description': ['Set the priority of the syslog packet.The value is an integer ranging from 0 to 7. The default value is 0.']}",
    "server_domain": "{'description': ['Server name. The value is a string of 1 to 255 case-sensitive characters.']}",
    "server_ip": "{'description': ['Log server address, IPv4 or IPv6 type. The value is a string of 0 to 255 characters. The value can be an valid IPv4 or IPv6 address.']}",
    "server_port": "{'description': ['Number of a port sending logs.The value is an integer ranging from 1 to 65535. For UDP, the default value is 514. For TCP, the default value is 601. For TSL, the default value is 6514.']}",
    "source_ip": "{'description': ['Log source ip address, IPv4 or IPv6 type. The value is a string of 0 to 255. The value can be an valid IPv4 or IPv6 address.']}",
    "ssl_policy_name": "{'description': ['SSL policy name. The value is a string of 1 to 23 case-sensitive characters.']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "suppress_enable": "{'description': ['Whether a device is enabled to suppress duplicate statistics. The value is of the Boolean type.'], 'choices': ['false', 'true']}",
    "timestamp": "{'description': ['Log server timestamp. The value is of the enumerated type and case-sensitive.'], 'choices': ['UTC', 'localtime']}",
    "transport_mode": "{'description': ['Transport mode. The value is of the enumerated type and case-sensitive.'], 'choices': ['tcp', 'udp']}",
    "vrf_name": "{'description': ['VPN name on a log server. The value is a string of 1 to 31 case-sensitive characters. The default value is _public_.']}",
}
```

## Examples


``` yaml

- name: info center global module test
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

  - name: Config info-center enable
    ce_info_center_global:
      info_center_enable: true
      state: present
      provider: "{{ cli }}"

  - name: Config statistic-suppress enable
    ce_info_center_global:
      suppress_enable: true
      state: present
      provider: "{{ cli }}"

  - name: Config info-center syslog packet-priority 1
    ce_info_center_global:
      packet_priority: 2
      state: present
      provider: "{{ cli }}"

  - name: Config info-center channel 1 name aaa
    ce_info_center_global:
      channel_id: 1
      channel_cfg_name: aaa
      state: present
      provider: "{{ cli }}"

  - name: Config info-center logfile size 10
    ce_info_center_global:
      logfile_max_num: 10
      state: present
      provider: "{{ cli }}"

  - name: Config info-center console channel 1
    ce_info_center_global:
      channel_out_direct: console
      channel_id: 1
      state: present
      provider: "{{ cli }}"

  - name: Config info-center filter-id bymodule-alias snmp snmp_ipunlock
    ce_info_center_global:
      filter_feature_name: SNMP
      filter_log_name: SNMP_IPLOCK
      state: present
      provider: "{{ cli }}"


  - name: Config info-center max-logfile-number 16
    ce_info_center_global:
      logfile_max_size: 16
      state: present
      provider: "{{ cli }}"

  - name: Config syslog loghost domain.
    ce_info_center_global:
      server_domain: aaa
      vrf_name: aaa
      channel_id: 1
      transport_mode: tcp
      facility: local4
      server_port: 100
      level: alert
      timestamp: UTC
      state: present
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Li Yanfeng (@CloudEngine-Ansible)']
