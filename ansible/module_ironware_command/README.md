# Ansible module: ansible.module_ironware_command


Run arbitrary commands on Extreme IronWare devices

## Description

Sends arbitrary commands to a Extreme Ironware node and returns the results read from the device. This module includes a I(wait_for) argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.

## Requirements

TODO

## Arguments

``` json
{
    "authorize": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.7 we recommend using C(connection: network_cli) and C(become: yes).', 'For more information please see the L(IronWare Platform Options guide, ../network/user_guide/platform_ironware.html).', 'HORIZONTALLINE', 'Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "commands": "{'description': ['List of commands to send to the remote device over the configured provider. The resulting output from the command is returned. If the I(wait_for) argument is provided, the module is not returned until the condition is satisfied or the number of retires as expired.'], 'required': True}",
    "interval": "{'description': ['Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.'], 'default': 1}",
    "match": "{'description': ['The I(match) argument is used in conjunction with the I(wait_for) argument to specify the match policy. If the value is set to C(all) then all conditionals in the I(wait_for) must be satisfied.  If the value is set to C(any) then only one of the values must be satisfied.'], 'default': 'all', 'choices': ['any', 'all']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.7 we recommend using C(connection: network_cli) and C(become: yes).', 'For more information please see the L(IronWare Platform Options guide, ../network/user_guide/platform_ironware.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.']}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}, 'timeout': {'description': ['Specifies idle timeout in seconds for the connection, in seconds. Useful if the console freezes before continuing. For example when saving configurations.'], 'default': 10}}}",
    "retries": "{'description': ['Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the I(wait_for) conditions.'], 'default': 10}",
    "wait_for": "{'description': ['List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples.']}",
}
```

## Examples


``` yaml

- ironware_command:
    commands:
      - show version

- ironware_command:
    commands:
      - show interfaces brief wide
      - show mpls vll

```

## License

TODO

## Author Information
  - ['Paul Baker (@paulquack)']
