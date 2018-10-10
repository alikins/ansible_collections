# Ansible module: ansible.module_eos_command


Run arbitrary commands on an Arista EOS device

## Description

Sends an arbitrary set of commands to an EOS node and returns the results read from the device.  This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.

## Requirements

TODO

## Arguments

``` json
{
    "auth_pass": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes) with C(become_pass).', 'This option is only required if you are using eAPI.', 'For more information please see the L(EOS Platform Options guide, ../network/user_guide/platform_eos.html).', 'HORIZONTALLINE', 'Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}",
    "authorize": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes).', 'This option is only required if you are using eAPI.', 'For more information please see the L(EOS Platform Options guide, ../network/user_guide/platform_eos.html).', 'HORIZONTALLINE', 'Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "commands": "{'description': ['The commands to send to the remote EOS device over the configured provider.  The resulting output from the command is returned.  If the I(wait_for) argument is provided, the module is not returned until the condition is satisfied or the number of I(retries) has been exceeded.'], 'required': True}",
    "interval": "{'description': ['Configures the interval in seconds to wait between retries of the command.  If the command does not pass the specified conditional, the interval indicates how to long to wait before trying the command again.'], 'default': 1}",
    "match": "{'description': ['The I(match) argument is used in conjunction with the I(wait_for) argument to specify the match policy.  Valid values are C(all) or C(any).  If the value is set to C(all) then all conditionals in the I(wait_for) must be satisfied.  If the value is set to C(any) then only one of the values must be satisfied.'], 'default': 'all', 'choices': ['any', 'all'], 'version_added': '2.2'}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using eAPI.', 'For more information please see the L(EOS Platform Options guide, ../network/user_guide/platform_eos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(eapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the eAPI authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(eapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['eapi', 'cli'], 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=eapi).  If the transport argument is not eapi, this value is ignored.'], 'type': 'bool', 'default': 'yes'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not eapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "retries": "{'description': ['Specifies the number of retries a command should be tried before it is considered failed.  The command is run on the target device every retry and evaluated against the I(wait_for) conditionals.'], 'default': 10}",
    "wait_for": "{'description': ["Specifies what to evaluate from the output of the command and what conditionals to apply.  This argument will cause the task to wait for a particular conditional to be true before moving forward.   If the conditional is not true by the configured retries, the task fails. Note - With I(wait_for) the value in C(result['stdout']) can be accessed using C(result), that is to access C(result['stdout'][0]) use C(result[0]) See examples."], 'aliases': ['waitfor'], 'version_added': '2.2'}",
}
```

## Examples


``` yaml

- name: run show version on remote devices
  eos_command:
    commands: show version

- name: run show version and check to see if output contains Arista
  eos_command:
    commands: show version
    wait_for: result[0] contains Arista

- name: run multiple commands on remote nodes
  eos_command:
    commands:
      - show version
      - show interfaces

- name: run multiple commands and evaluate the output
  eos_command:
    commands:
      - show version
      - show interfaces
    wait_for:
      - result[0] contains Arista
      - result[1] contains Loopback0

- name: run commands and specify the output format
  eos_command:
    commands:
      - command: show version
        output: json

- name: using cli transport, check whether the switch is in maintenance mode
  eos_command:
    commands: show maintenance
    wait_for: result[0] contains 'Under Maintenance'

- name: using cli transport, check whether the switch is in maintenance mode using json output
  eos_command:
    commands: show maintenance | json
    wait_for: result[0].units.System.state eq 'underMaintenance'

- name: "using eapi transport check whether the switch is in maintenance,
         with 8 retries and 2 second interval between retries"
  eos_command:
    commands: show maintenance
    wait_for: result[0]['units']['System']['state'] eq 'underMaintenance'
    interval: 2
    retries: 8
    provider:
      transport: eapi

```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip)']
