# Ansible module: ansible.module_edgeos_command


Run one or more commands on EdgeOS devices

## Description

This command module allows running one or more commands on a remote device running EdgeOS, such as the Ubiquiti EdgeRouter.
This module does not support running commands in configuration mode.
Certain C(show) commands in EdgeOS produce many lines of output and use a custom pager that can cause this module to hang.  If the value of the environment variable C(ANSIBLE_EDGEOS_TERMINAL_LENGTH) is not set, the default number of 10000 is used.
This is a network module and requires C(connection: network_cli) in order to work properly.
For more information please see the L(Network Guide,../network/getting_started/index.html).

## Requirements

TODO

## Arguments

``` json
{
    "commands": "{'description': ['The commands or ordered set of commands that should be run against the remote device. The output of the command is returned to the playbook. If the C(wait_for) argument is provided, the module is not returned until the condition is met or the number of retries is exceeded.'], 'required': True}",
    "interval": "{'description': ['The number of seconds to wait between C(retries) of the command.'], 'required': False, 'default': 1}",
    "match": "{'description': ['Used in conjunction with C(wait_for) to create match policy. If set to C(all), then all conditions in C(wait_for) must be met. If set to C(any), then only one condition must match.'], 'required': False, 'default': 'all', 'choices': ['any', 'all']}",
    "retries": "{'description': ['Number of times a command should be tried before it is considered failed. The command is run on the target device and evaluated against the C(wait_for) conditionals.'], 'required': False, 'default': 10}",
    "wait_for": "{'description': ['Causes the task to wait for a specific condition to be met before moving forward. If the condition is not met before the specified number of retries is exceeded, the task will fail.'], 'required': False}",
}
```

## Examples


``` yaml

tasks:
  - name: Reboot the device
    edgeos_command:
      commands: reboot now

  - name: Show the configuration for eth0 and eth1
    edgeos_command:
      commands: show interfaces ethernet {{ item }}
    loop:
      - eth0
      - eth1

```

## License

TODO

## Author Information
  - ['Chad Norgan (@BeardyMcBeards)', 'Sam Doran (@samdoran)']
  - ['Chad Norgan (@BeardyMcBeards)', 'Sam Doran (@samdoran)']
