# Ansible module: ansible.module_dellos10_command


Run commands on remote devices running Dell OS10

## Description

Sends arbitrary commands to a Dell OS10 node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.
This module does not support running commands in configuration mode. Please use M(dellos10_config) to configure Dell OS10 devices.

## Requirements

TODO

## Arguments

``` json
{
    "commands": "{'description': ['List of commands to send to the remote dellos10 device over the configured provider. The resulting output from the command is returned. If the I(wait_for) argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired.'], 'required': True}",
    "interval": "{'description': ['Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.'], 'default': 1}",
    "match": "{'description': ['The I(match) argument is used in conjunction with the I(wait_for) argument to specify the match policy.  Valid values are C(all) or C(any).  If the value is set to C(all) then all conditionals in the wait_for must be satisfied.  If the value is set to C(any) then only one of the values must be satisfied.'], 'default': 'all', 'choices': ['any', 'all'], 'version_added': '2.5'}",
    "provider": "{'description': ['A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['User to authenticate the SSH session to the remote device. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Password to authenticate the SSH session to the remote device. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'ssh_keyfile': {'description': ['Path to an ssh key used to authenticate the SSH session to the remote device.  If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'timeout': {'description': ['Specifies idle timeout (in seconds) for the connection. Useful if the console freezes before continuing. For example when saving configurations.'], 'default': 10}}}",
    "retries": "{'description': ['Specifies the number of retries a command should be tried before it is considered failed. The command is run on the target device every retry and evaluated against the I(wait_for) conditions.'], 'default': 10}",
    "wait_for": "{'description': ['List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of I(retries), the task fails. See examples.'], 'version_added': '2.2'}",
}
```

## Examples


``` yaml

tasks:
  - name: run show version on remote devices
    dellos10_command:
      commands: show version

  - name: run show version and check to see if output contains OS10
    dellos10_command:
      commands: show version
      wait_for: result[0] contains OS10

  - name: run multiple commands on remote nodes
    dellos10_command:
      commands:
        - show version
        - show interface

  - name: run multiple commands and evaluate the output
    dellos10_command:
      commands:
        - show version
        - show interface
      wait_for:
        - result[0] contains OS10
        - result[1] contains Ethernet

```

## License

TODO

## Author Information
  - ['Senthil Kumar Ganesan (@skg-net)']
