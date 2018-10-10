# Ansible module: ansible.module_aireos_config


Manage Cisco WLC configurations

## Description

AireOS does not use a block indent file syntax, so there are no sections or parents. This module provides an implementation for working with AireOS configurations in a deterministic way.

## Requirements

TODO

## Arguments

``` json
{
    "after": "{'description': ['The ordered set of commands to append to the end of the command stack if a change needs to be made.  Just like with I(before) this allows the playbook designer to append a set of commands to be executed after the command set.']}",
    "backup": "{'description': ['This argument will cause the module to create a full backup of the current C(running-config) from the remote device before any changes are made.  The backup file is written to the C(backup) folder in the playbook root directory.  If the directory does not exist, it is created.'], 'type': 'bool', 'default': False}",
    "before": "{'description': ['The ordered set of commands to push on to the command stack if a change needs to be made.  This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system.']}",
    "diff_against": "{'description': ['When using the C(ansible-playbook --diff) command line argument the module can generate diffs against different sources.', 'When this option is configured as I(intended), the module will return the diff of the running-config against the configuration provided in the C(intended_config) argument.', 'When this option is configured as I(running), the module will return the before and after diff of the running-config with respect to any changes made to the device configuration.'], 'choices': ['intended', 'running']}",
    "diff_ignore_lines": "{'description': ['Use this argument to specify one or more lines that should be ignored during the diff.  This is used for lines in the configuration that are automatically updated by the system.  This argument takes a list of regular expressions or exact line matches.']}",
    "intended_config": "{'description': ["The C(intended_config) provides the master configuration that the node should conform to and is used to check the final running-config against.   This argument will not modify any settings on the remote device and is strictly used to check the compliance of the current device's configuration against.  When specifying this argument, the task should also modify the C(diff_against) value and set it to I(intended)."]}",
    "lines": "{'description': ['The ordered set of commands that should be configured. The commands must be the exact same commands as found in the device run-config.  Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser.'], 'aliases': ['commands']}",
    "match": "{'description': ['Instructs the module on the way to perform the matching of the set of commands against the current device config.  If match is set to I(line), commands are matched line by line. If match is set to I(none), the module will not attempt to compare the source configuration with the running configuration on the remote device.'], 'default': 'line', 'choices': ['line', 'none']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote. device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "running_config": "{'description': ['The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source.  There are times when it is not desirable to have the task get the current running-config for every task in a playbook.  The I(running_config) argument allows the implementer to pass in the configuration to use as the base config for comparison.'], 'aliases': ['config']}",
    "save": "{'description': ['The C(save) argument instructs the module to save the running-config to startup-config.  This operation is performed after any changes are made to the current running config.  If no changes are made, the configuration is still saved to the startup config.  This option will always cause the module to return changed. This argument is mutually exclusive with I(save_when).', 'This option is deprecated as of Ansible 2.7, use C(save_when)'], 'type': 'bool', 'default': False}",
    "save_when": "{'description': ['When changes are made to the device running-configuration, the changes are not copied to non-volatile storage by default.  Using this argument will change that.  If the argument is set to I(always), then the running-config will always be copied to the startup-config and the module will always return as changed. If the argument is set to I(never), the running-config will never be copied to the startup-config.  If the argument is set to I(changed), then the running-config will only be copied to the startup-config if the task has made a change.'], 'default': 'never', 'choices': ['always', 'never', 'changed'], 'version_added': '2.7'}",
    "src": "{'description': ['Specifies the source path to the file that contains the configuration or configuration template to load.  The path to the source file can either be the full path on the Ansible control host or a relative path from the playbook or role root directory.  This argument is mutually exclusive with I(lines).']}",
}
```

## Examples


``` yaml

- name: configure configuration
  aireos_config:
    lines: sysname testDevice

- name: diff the running-config against a provided config
  aireos_config:
    diff_against: intended
    intended: "{{ lookup('file', 'master.cfg') }}"

- name: load new acl into device
  aireos_config:
    lines:
      - acl create testACL
      - acl rule protocol testACL 1 any
      - acl rule direction testACL 3 in
    before: acl delete testACL

```

## License

TODO

## Author Information
  - ['James Mighion (@jmighion)']
