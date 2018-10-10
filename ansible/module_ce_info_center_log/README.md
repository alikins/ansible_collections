# Ansible module: ansible.module_ce_info_center_log


Manages information center log configuration on HUAWEI CloudEngine switches

## Description

Setting the Timestamp Format of Logs. Configuring the Device to Output Logs to the Log Buffer.

## Requirements

TODO

## Arguments

``` json
{
    "channel_id": "{'description': ['Specifies a channel ID. The value is an integer ranging from 0 to 9.']}",
    "log_buff_enable": "{'description': ['Enables the Switch to send logs to the log buffer.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "log_buff_size": "{'description': ['Specifies the maximum number of logs in the log buffer. The value is an integer that ranges from 0 to 10240. If logbuffer-size is 0, logs are not displayed.']}",
    "log_enable": "{'description': ['Indicates whether log filtering is enabled.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "log_level": "{'description': ['Specifies a log severity.'], 'choices': ['emergencies', 'alert', 'critical', 'error', 'warning', 'notification', 'informational', 'debugging']}",
    "log_time_stamp": "{'description': ['Sets the timestamp format of logs.'], 'choices': ['date_boot', 'date_second', 'date_tenthsecond', 'date_millisecond', 'shortdate_second', 'shortdate_tenthsecond', 'shortdate_millisecond', 'formatdate_second', 'formatdate_tenthsecond', 'formatdate_millisecond']}",
    "module_name": "{'description': ['Specifies the name of a module. The value is a module name in registration logs.']}",
    "state": "{'description': ['Determines whether the config should be present or not on the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml


- name: CloudEngine info center log test
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

  - name: "Setting the timestamp format of logs"
    ce_info_center_log:
      log_time_stamp: date_tenthsecond
      provider: "{{ cli }}"

  - name: "Enabled to output information to the log buffer"
    ce_info_center_log:
      log_buff_enable: true
      provider: "{{ cli }}"

  - name: "Set the maximum number of logs in the log buffer"
    ce_info_center_log:
      log_buff_size: 100
      provider: "{{ cli }}"

  - name: "Set a rule for outputting logs to a channel"
    ce_info_center_log:
      module_name: aaa
      channel_id: 1
      log_enable: true
      log_level: critical
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['QijunPan (@CloudEngine-Ansible)']
