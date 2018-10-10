# Ansible module: ansible.module_junos_command


Run arbitrary commands on an Juniper JUNOS device

## Description

Sends an arbitrary set of commands to an JUNOS node and returns the results read from the device.  This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.

## Requirements

TODO

## Arguments

``` json
{
    "commands": "{'description': ['The commands to send to the remote junos device over the configured provider.  The resulting output from the command is returned.  If the I(wait_for) argument is provided, the module is not returned until the condition is satisfied or the number of I(retries) has been exceeded.']}",
    "display": "{'description': ['Encoding scheme to use when serializing output from the device. This handles how to properly understand the output and apply the conditionals path to the result set. For I(rpcs) argument default display is C(xml) and for I(commands) argument default display is C(text). Value C(set) is applicable only for fetching configuration from device.'], 'default': 'depends on input argument I(rpcs) or I(commands)', 'aliases': ['format', 'output'], 'choices': ['text', 'json', 'xml', 'set'], 'version_added': '2.3'}",
    "interval": "{'description': ['Configures the interval in seconds to wait between retries of the command.  If the command does not pass the specified conditional, the interval indicates how to long to wait before trying the command again.'], 'default': 1}",
    "match": "{'description': ['The I(match) argument is used in conjunction with the I(wait_for) argument to specify the match policy.  Valid values are C(all) or C(any).  If the value is set to C(all) then all conditionals in the I(wait_for) must be satisfied.  If the value is set to C(any) then only one of the values must be satisfied.'], 'default': 'all', 'choices': ['any', 'all'], 'version_added': '2.2'}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "retries": "{'description': ['Specifies the number of retries a command should be tried before it is considered failed.  The command is run on the target device every retry and evaluated against the I(wait_for) conditionals.'], 'default': 10}",
    "rpcs": "{'description': ['The C(rpcs) argument accepts a list of RPCs to be executed over a netconf session and the results from the RPC execution is return to the playbook via the modules results dictionary.'], 'version_added': '2.3'}",
    "wait_for": "{'description': ['Specifies what to evaluate from the output of the command and what conditionals to apply.  This argument will cause the task to wait for a particular conditional to be true before moving forward.   If the conditional is not true by the configured retries, the task fails.  See examples.'], 'aliases': ['waitfor'], 'version_added': '2.2'}",
}
```

## Examples


``` yaml

- name: run show version on remote devices
  junos_command:
    commands: show version

- name: run show version and check to see if output contains Juniper
  junos_command:
    commands: show version
    wait_for: result[0] contains Juniper

- name: run multiple commands on remote nodes
  junos_command:
    commands:
      - show version
      - show interfaces

- name: run multiple commands and evaluate the output
  junos_command:
    commands:
      - show version
      - show interfaces
    wait_for:
      - result[0] contains Juniper
      - result[1] contains Loopback0

- name: run commands and specify the output format
  junos_command:
    commands: show version
    display: json

- name: run rpc on the remote device
  junos_command:
    commands: show configuration
    display: set

- name: run rpc on the remote device
  junos_command:
    rpcs: get-software-information

```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip)']
