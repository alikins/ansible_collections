# Ansible module: ansible.module_slxos_command


Run commands on remote devices running Extreme Networks SLX-OS

## Description

Sends arbitrary commands to an SLX node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.
This module does not support running commands in configuration mode. Please use M(slxos_config) to configure SLX-OS devices.

## Requirements

TODO

## Arguments

``` json
{
    "commands": "{'description': ['List of commands to send to the remote SLX-OS device over the configured provider. The resulting output from the command is returned. If the I(wait_for) argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired.'], 'required': True}",
    "interval": "{'description': ['Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.'], 'default': 1}",
    "match": "{'description': ['The I(match) argument is used in conjunction with the I(wait_for) argument to specify the match policy.  Valid values are C(all) or C(any).  If the value is set to C(all) then all conditionals in the wait_for must be satisfied.  If the value is set to C(any) then only one of the values must be satisfied.'], 'default': 'all', 'choices': ['any', 'all']}",
    "retries": "{'description': ['Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the I(wait_for) conditions.'], 'default': 10}",
    "wait_for": "{'description': ['List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples.']}",
}
```

## Examples


``` yaml

tasks:
  - name: run show version on remote devices
    slxos_command:
      commands: show version

  - name: run show version and check to see if output contains SLX
    slxos_command:
      commands: show version
      wait_for: result[0] contains SLX

  - name: run multiple commands on remote nodes
    slxos_command:
      commands:
        - show version
        - show interfaces

  - name: run multiple commands and evaluate the output
    slxos_command:
      commands:
        - show version
        - show interface status
      wait_for:
        - result[0] contains SLX
        - result[1] contains Eth
  - name: run command that requires answering a prompt
    slxos_command:
      commands:
        - command: 'clear sessions'
          prompt: 'This operation will logout all the user sessions. Do you want to continue (yes/no)?:'
          answer: y

```

## License

TODO

## Author Information
  - ['Lindsay Hill (@LindsayHill)']
