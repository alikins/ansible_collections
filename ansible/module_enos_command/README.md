# Ansible module: ansible.module_enos_command


Run arbitrary commands on Lenovo ENOS devices

## Description

Sends arbitrary commands to an ENOS node and returns the results read from the device. The C(enos_command) module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.

## Requirements

TODO

## Arguments

``` json
{
    "auth_pass": "{'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}",
    "authorize": "{'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "commands": "{'description': ['List of commands to send to the remote device over the configured provider. The resulting output from the command is returned. If the I(wait_for) argument is provided, the module is not returned until the condition is satisfied or the number of retires as expired.'], 'required': True}",
    "interval": "{'description': ['Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.'], 'default': 1}",
    "match": "{'description': ['The I(match) argument is used in conjunction with the I(wait_for) argument to specify the match policy.  Valid values are C(all) or C(any).  If the value is set to C(all) then all conditionals in the wait_for must be satisfied.  If the value is set to C(any) then only one of the values must be satisfied.'], 'default': 'all', 'choices': ['any', 'all']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}}}",
    "retries": "{'description': ['Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the I(wait_for) conditions.'], 'default': 10}",
    "wait_for": "{'description': ['List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples.']}",
}
```

## Examples


``` yaml

# Note: examples below use the following provider dict to handle
#       transport and authentication to the node.
---
vars:
  cli:
    host: "{{ inventory_hostname }}"
    port: 22
    username: admin
    password: admin
    timeout: 30

---
- name: test contains operator
  enos_command:
    commands:
      - show version
      - show system memory
    wait_for:
      - "result[0] contains 'Lenovo'"
      - "result[1] contains 'MemFree'"
    provider: "{{ cli }}"
  register: result

- assert:
    that:
      - "result.changed == false"
      - "result.stdout is defined"

- name: get output for single command
  enos_command:
    commands: ['show version']
    provider: "{{ cli }}"
  register: result

- assert:
    that:
      - "result.changed == false"
      - "result.stdout is defined"

- name: get output for multiple commands
  enos_command:
    commands:
      - show version
      - show interface information
    provider: "{{ cli }}"
  register: result

- assert:
    that:
      - "result.changed == false"
      - "result.stdout is defined"
      - "result.stdout | length == 2"

```

## License

TODO

## Author Information
  - ['Anil Kumar Muraleedharan (@amuraleedhar)']
