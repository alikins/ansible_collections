# Ansible module: ansible.module_eos_config


Manage Arista EOS configuration sections

## Description

Arista EOS configurations use a simple block indent file syntax for segmenting configuration into sections.  This module provides an implementation for working with EOS configuration sections in a deterministic way.  This module works with either CLI or eAPI transports.

## Requirements

TODO

## Arguments

``` json
{
    "after": "{'description': ['The ordered set of commands to append to the end of the command stack if a change needs to be made.  Just like with I(before) this allows the playbook designer to append a set of commands to be executed after the command set.']}",
    "auth_pass": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes) with C(become_pass).', 'This option is only required if you are using eAPI.', 'For more information please see the L(EOS Platform Options guide, ../network/user_guide/platform_eos.html).', 'HORIZONTALLINE', 'Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}",
    "authorize": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) and C(become: yes).', 'This option is only required if you are using eAPI.', 'For more information please see the L(EOS Platform Options guide, ../network/user_guide/platform_eos.html).', 'HORIZONTALLINE', 'Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False}",
    "backup": "{'description': ['This argument will cause the module to create a full backup of the current C(running-config) from the remote device before any changes are made.  The backup file is written to the C(backup) folder in the playbook root directory or role root directory, if playbook is part of an ansible role. If the directory does not exist, it is created.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "before": "{'description': ['The ordered set of commands to push on to the command stack if a change needs to be made.  This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system.']}",
    "defaults": "{'description': ['The I(defaults) argument will influence how the running-config is collected from the device.  When the value is set to true, the command used to collect the running-config is append with the all keyword.  When the value is set to false, the command is issued without the all keyword'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "diff_against": "{'description': ['When using the C(ansible-playbook --diff) command line argument the module can generate diffs against different sources.', 'When this option is configure as I(startup), the module will return the diff of the running-config against the startup-config.', 'When this option is configured as I(intended), the module will return the diff of the running-config against the configuration provided in the C(intended_config) argument.', 'When this option is configured as I(running), the module will return the before and after diff of the running-config with respect to any changes made to the device configuration.', 'When this option is configured as C(session), the diff returned will be based on the configuration session.'], 'default': 'session', 'choices': ['startup', 'running', 'intended', 'session'], 'version_added': '2.4'}",
    "diff_ignore_lines": "{'description': ['Use this argument to specify one or more lines that should be ignored during the diff.  This is used for lines in the configuration that are automatically updated by the system.  This argument takes a list of regular expressions or exact line matches.'], 'version_added': '2.4'}",
    "force": "{'description': ['The force argument instructs the module to not consider the current devices running-config.  When set to true, this will cause the module to push the contents of I(src) into the device without first checking if already configured.', 'Note this argument should be considered deprecated.  To achieve the equivalent, set the C(match=none) which is idempotent.  This argument will be removed in Ansible 2.6.'], 'type': 'bool', 'default': False}",
    "intended_config": "{'description': ["The C(intended_config) provides the master configuration that the node should conform to and is used to check the final running-config against.   This argument will not modify any settings on the remote device and is strictly used to check the compliance of the current device's configuration against.  When specifying this argument, the task should also modify the C(diff_against) value and set it to I(intended)."], 'version_added': '2.4'}",
    "lines": "{'description': ['The ordered set of commands that should be configured in the section.  The commands must be the exact same commands as found in the device running-config.  Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser.'], 'aliases': ['commands']}",
    "match": "{'description': ['Instructs the module on the way to perform the matching of the set of commands against the current device config.  If match is set to I(line), commands are matched line by line.  If match is set to I(strict), command lines are matched with respect to position.  If match is set to I(exact), command lines must be an equal match.  Finally, if match is set to I(none), the module will not attempt to compare the source configuration with the running configuration on the remote device.'], 'default': 'line', 'choices': ['line', 'strict', 'exact', 'none']}",
    "parents": "{'description': ['The ordered set of parents that uniquely identify the section or hierarchy the commands should be checked against.  If the parents argument is omitted, the commands are checked against the set of top level or global commands.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using eAPI.', 'For more information please see the L(EOS Platform Options guide, ../network/user_guide/platform_eos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(eapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the eAPI authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(eapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': 'no'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['eapi', 'cli'], 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=eapi).  If the transport argument is not eapi, this value is ignored.'], 'type': 'bool', 'default': 'yes'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not eapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "replace": "{'description': ['Instructs the module on the way to perform the configuration on the device.  If the replace argument is set to I(line) then the modified lines are pushed to the device in configuration mode.  If the replace argument is set to I(block) then the entire command block is pushed to the device in configuration mode if any line is not correct.'], 'default': 'line', 'choices': ['line', 'block', 'config']}",
    "running_config": "{'description': ['The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source.  There are times when it is not desirable to have the task get the current running-config for every task in a playbook.  The I(running_config) argument allows the implementer to pass in the configuration to use as the base config for this module.'], 'aliases': ['config'], 'version_added': '2.4'}",
    "save": "{'description': ['The C(save) argument instructs the module to save the running-config to startup-config.  This operation is performed after any changes are made to the current running config.  If no changes are made, the configuration is still saved to the startup config.  This option will always cause the module to return changed.', 'This option is deprecated as of Ansible 2.4 and will be removed in Ansible 2.8, use C(save_when) instead.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "save_when": "{'description': ['When changes are made to the device running-configuration, the changes are not copied to non-volatile storage by default.  Using this argument will change that before.  If the argument is set to I(always), then the running-config will always be copied to the startup-config and the I(modified) flag will always be set to True.  If the argument is set to I(modified), then the running-config will only be copied to the startup-config if it has changed since the last save to startup-config.  If the argument is set to I(never), the running-config will never be copied to the startup-config. If the argument is set to I(changed), then the running-config will only be copied to the startup-config if the task has made a change. I(changed) was added in Ansible 2.5.'], 'default': 'never', 'choices': ['always', 'never', 'modified', 'changed'], 'version_added': '2.4'}",
    "src": "{'description': ['The I(src) argument provides a path to the configuration file to load into the remote system.  The path can either be a full system path to the configuration file if the value starts with / or relative to the root of the implemented role or playbook. This argument is mutually exclusive with the I(lines) and I(parents) arguments. It can be a Jinja2 template as well. src file must have same indentation as a live switch config. Arista EOS device config has 3 spaces indentation.'], 'version_added': '2.2'}",
}
```

## Examples


``` yaml

- name: configure top level settings
  eos_config:
    lines: hostname {{ inventory_hostname }}

- name: load an acl into the device
  eos_config:
    lines:
      - 10 permit ip 192.0.2.1/32 any log
      - 20 permit ip 192.0.2.2/32 any log
      - 30 permit ip 192.0.2.3/32 any log
      - 40 permit ip 192.0.2.4/32 any log
    parents: ip access-list test
    before: no ip access-list test
    replace: block

- name: load configuration from file
  eos_config:
    src: eos.cfg

- name: render a Jinja2 template onto an Arista switch
  eos_config:
    backup: yes
    src: eos_template.j2

- name: diff the running config against a master config
  eos_config:
    diff_against: intended
    intended_config: "{{ lookup('file', 'master.cfg') }}"

- name: for idempotency, use full-form commands
  eos_config:
    lines:
      # - shut
      - shutdown
    # parents: int eth1
    parents: interface Ethernet1

```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip)']
