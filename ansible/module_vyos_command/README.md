# Ansible module: ansible.module_vyos_command


Run one or more commands on VyOS devices

## Description

The command module allows running one or more commands on remote devices running VyOS.  This module can also be introspected to validate key parameters before returning successfully.  If the conditional statements are not met in the wait period, the task fails.
Certain C(show) commands in VyOS produce many lines of output and use a custom pager that can cause this module to hang.  If the value of the environment variable C(ANSIBLE_VYOS_TERMINAL_LENGTH) is not set, the default number of 10000 is used.

## Requirements

TODO

## Arguments

``` json
{
    "commands": "{'description': ['The ordered set of commands to execute on the remote device running VyOS.  The output from the command execution is returned to the playbook.  If the I(wait_for) argument is provided, the module is not returned until the condition is satisfied or the number of retries has been exceeded.'], 'required': True}",
    "interval": "{'description': ['Configures the interval in seconds to wait between I(retries) of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.'], 'default': 1}",
    "match": "{'description': ['The I(match) argument is used in conjunction with the I(wait_for) argument to specify the match policy. Valid values are C(all) or C(any).  If the value is set to C(all) then all conditionals in the wait_for must be satisfied.  If the value is set to C(any) then only one of the values must be satisfied.'], 'default': 'all', 'choices': ['any', 'all']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "retries": "{'description': ['Specifies the number of retries a command should be tried before it is considered failed. The command is run on the target device every retry and evaluated against the I(wait_for) conditionals.'], 'default': 10}",
    "wait_for": "{'description': ['Specifies what to evaluate from the output of the command and what conditionals to apply.  This argument will cause the task to wait for a particular conditional to be true before moving forward.  If the conditional is not true by the configured I(retries), the task fails. See examples.'], 'aliases': ['waitfor']}",
}
```

## Examples


``` yaml

tasks:
  - name: show configuration on ethernet devices eth0 and eth1
    vyos_command:
      commands:
        - show interfaces ethernet {{ item }}
    with_items:
      - eth0
      - eth1

  - name: run multiple commands and check if version output contains specific version string
    vyos_command:
      commands:
        - show version
        - show hardware cpu
      wait_for:
        - "result[0] contains 'VyOS 1.1.7'"

  - name: run command that requires answering a prompt
    vyos_command:
      commands:
        - command: 'rollback 1'
          prompt: 'Proceed with reboot? [confirm][y]'
          answer: y

```

## License

TODO

## Author Information
  - ['Nathaniel Case (@qalthos)']
