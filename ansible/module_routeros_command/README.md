# Ansible module: ansible.module_routeros_command


Run commands on remote devices running MikroTik RouterOS

## Description

Sends arbitrary commands to an RouterOS node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.

## Requirements

TODO

## Arguments

``` json
{
    "commands": "{'description': ['List of commands to send to the remote RouterOS device over the configured provider. The resulting output from the command is returned. If the I(wait_for) argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired.'], 'required': True}",
    "interval": "{'description': ['Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.'], 'default': 1}",
    "match": "{'description': ['The I(match) argument is used in conjunction with the I(wait_for) argument to specify the match policy.  Valid values are C(all) or C(any).  If the value is set to C(all) then all conditionals in the wait_for must be satisfied.  If the value is set to C(any) then only one of the values must be satisfied.'], 'default': 'all', 'choices': ['any', 'all']}",
    "retries": "{'description': ['Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the I(wait_for) conditions.'], 'default': 10}",
    "wait_for": "{'description': ['List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples.']}",
}
```

## Examples


``` yaml

tasks:
  - name: run command on remote devices
    routeros_command:
      commands: /system routerboard print

  - name: run command and check to see if output contains routeros
    routeros_command:
      commands: /system resource print
      wait_for: result[0] contains MikroTik

  - name: run multiple commands on remote nodes
    routeros_command:
      commands:
        - /system routerboard print
        - /system identity print

  - name: run multiple commands and evaluate the output
    routeros_command:
      commands:
        - /system routerboard print
        - /interface ethernet print
      wait_for:
        - result[0] contains x86
        - result[1] contains ether1

```

## License

TODO

## Author Information
  - ['Egor Zaitsev (@heuels)']
