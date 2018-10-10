# Ansible module: ansible.module_iosxr_command


Run commands on remote devices running Cisco IOS XR

## Description

Sends arbitrary commands to an IOS XR node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.
This module does not support running commands in configuration mode. Please use M(iosxr_config) to configure iosxr devices.

## Requirements

TODO

## Arguments

``` json
{
    "commands": "{'description': ['List of commands to send to the remote iosxr device over the configured provider. The resulting output from the command is returned. If the I(wait_for) argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired.'], 'required': True}",
    "interval": "{'description': ['Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.'], 'default': 1}",
    "match": "{'description': ['The I(match) argument is used in conjunction with the I(wait_for) argument to specify the match policy.  Valid values are C(all) or C(any).  If the value is set to C(all) then all conditionals in the wait_for must be satisfied.  If the value is set to C(any) then only one of the values must be satisfied.'], 'default': 'all', 'choices': ['any', 'all'], 'version_added': '2.2'}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "retries": "{'description': ['Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the I(wait_for) conditions.'], 'default': 10}",
    "wait_for": "{'description': ['List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples.'], 'aliases': ['waitfor'], 'version_added': '2.2'}",
}
```

## Examples


``` yaml

tasks:
  - name: run show version on remote devices
    iosxr_command:
      commands: show version

  - name: run show version and check to see if output contains iosxr
    iosxr_command:
      commands: show version
      wait_for: result[0] contains IOS-XR

  - name: run multiple commands on remote nodes
    iosxr_command:
      commands:
        - show version
        - show interfaces
        - { command: example command that prompts, prompt: expected prompt, answer: yes}

  - name: run multiple commands and evaluate the output
    iosxr_command:
      commands:
        - show version
        - show interfaces
      wait_for:
        - result[0] contains IOS-XR
        - result[1] contains Loopback0

```

## License

TODO

## Author Information
  - ['Ricardo Carrillo Cruz (@rcarrillocruz)']
