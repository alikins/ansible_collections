# Ansible module: ansible.module_bigip_command


Run arbitrary command on F5 devices

## Description

Sends an arbitrary command to an BIG-IP node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.
This module is B(not) idempotent, nor will it ever be. It is intended as a stop-gap measure to satisfy automation requirements until such a time as a real module has been developed to configure in the way you need.
If you are using this module, you should probably also be filing an issue to have a B(real) module created for your needs.

## Requirements

TODO

## Arguments

``` json
{
    "chdir": "{'description': ['Change into this directory before running the command.'], 'version_added': 2.6}",
    "commands": "{'description': ['The commands to send to the remote BIG-IP device over the configured provider. The resulting output from the command is returned. If the I(wait_for) argument is provided, the module is not returned until the condition is satisfied or the number of retries as expired.', "Only C(tmsh) commands are supported. If you are piping or adding additional logic that is outside of C(tmsh) (such as grep'ing, awk'ing or other shell related things that are not C(tmsh), this behavior is not supported."], 'required': True}",
    "interval": "{'description': ['Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditional, the interval indicates how to long to wait before trying the command again.'], 'default': 1}",
    "match": "{'description': ['The I(match) argument is used in conjunction with the I(wait_for) argument to specify the match policy. Valid values are C(all) or C(any). If the value is set to C(all) then all conditionals in the I(wait_for) must be satisfied. If the value is set to C(any) then only one of the values must be satisfied.'], 'choices': ['any', 'all'], 'default': 'all'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "retries": "{'description': ['Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the I(wait_for) conditionals.'], 'default': 10}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "transport": "{'description': ['Configures the transport connection to use when connecting to the remote device. The transport argument supports connectivity to the device over cli (ssh) or rest.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'rest', 'version_added': 2.5}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
    "wait_for": "{'description': ['Specifies what to evaluate from the output of the command and what conditionals to apply.  This argument will cause the task to wait for a particular conditional to be true before moving forward. If the conditional is not true by the configured retries, the task fails. See examples.'], 'aliases': ['waitfor']}",
    "warn": "{'description': ['Whether the module should raise warnings related to command idempotency or not.', 'Note that the F5 Ansible developers specifically leave this on to make you aware that your usage of this module may be better served by official F5 Ansible modules. This module should always be used as a last resort.'], 'default': True, 'type': 'bool', 'version_added': 2.6}",
}
```

## Examples


``` yaml

- name: run show version on remote devices
  bigip_command:
    commands: show sys version
    server: lb.mydomain.com
    password: secret
    user: admin
    validate_certs: no
  delegate_to: localhost

- name: run show version and check to see if output contains BIG-IP
  bigip_command:
    commands: show sys version
    wait_for: result[0] contains BIG-IP
    server: lb.mydomain.com
    password: secret
    user: admin
    validate_certs: no
  register: result
  delegate_to: localhost

- name: run multiple commands on remote nodes
  bigip_command:
    commands:
      - show sys version
      - list ltm virtual
    server: lb.mydomain.com
    password: secret
    user: admin
    validate_certs: no
  delegate_to: localhost

- name: run multiple commands and evaluate the output
  bigip_command:
    commands:
      - show sys version
      - list ltm virtual
    wait_for:
      - result[0] contains BIG-IP
      - result[1] contains my-vs
    server: lb.mydomain.com
    password: secret
    user: admin
    validate_certs: no
  register: result
  delegate_to: localhost

- name: tmsh prefixes will automatically be handled
  bigip_command:
    commands:
      - show sys version
      - tmsh list ltm virtual
    server: lb.mydomain.com
    password: secret
    user: admin
    validate_certs: no
  delegate_to: localhost

- name: Delete all LTM nodes in Partition1, assuming no dependencies exist
  bigip_command:
    commands:
      - delete ltm node all
    chdir: Partition1
    server: lb.mydomain.com
    password: secret
    user: admin
    validate_certs: no
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
