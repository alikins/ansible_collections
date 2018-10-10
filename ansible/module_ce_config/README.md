# Ansible module: ansible.module_ce_config


Manage Huawei CloudEngine configuration sections

## Description

Huawei CloudEngine configurations use a simple block indent file syntax for segmenting configuration into sections.  This module provides an implementation for working with CloudEngine configuration sections in a deterministic way.  This module works with CLI transports.

## Requirements

TODO

## Arguments

``` json
{
    "after": "{'description': ['The ordered set of commands to append to the end of the command stack if a change needs to be made.  Just like with I(before) this allows the playbook designer to append a set of commands to be executed after the command set.']}",
    "backup": "{'description': ['This argument will cause the module to create a full backup of the current C(current-configuration) from the remote device before any changes are made.  The backup file is written to the C(backup) folder in the playbook root directory.  If the directory does not exist, it is created.'], 'type': 'bool', 'default': False}",
    "before": "{'description': ['The ordered set of commands to push on to the command stack if a change needs to be made.  This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system.']}",
    "config": "{'description': ['The module, by default, will connect to the remote device and retrieve the current current-configuration to use as a base for comparing against the contents of source.  There are times when it is not desirable to have the task get the current-configuration for every task in a playbook.  The I(config) argument allows the implementer to pass in the configuration to use as the base config for comparison.']}",
    "defaults": "{'description': ['The I(defaults) argument will influence how the current-configuration is collected from the device.  When the value is set to true, the command used to collect the current-configuration is append with the all keyword.  When the value is set to false, the command is issued without the all keyword.'], 'type': 'bool', 'default': False}",
    "lines": "{'description': ['The ordered set of commands that should be configured in the section.  The commands must be the exact same commands as found in the device current-configuration.  Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser.']}",
    "match": "{'description': ['Instructs the module on the way to perform the matching of the set of commands against the current device config.  If match is set to I(line), commands are matched line by line.  If match is set to I(strict), command lines are matched with respect to position.  If match is set to I(exact), command lines must be an equal match.  Finally, if match is set to I(none), the module will not attempt to compare the source configuration with the current-configuration on the remote device.'], 'default': 'line', 'choices': ['line', 'strict', 'exact', 'none']}",
    "parents": "{'description': ['The ordered set of parents that uniquely identify the section or hierarchy the commands should be checked against.  If the parents argument is omitted, the commands are checked against the set of top level or global commands.']}",
    "replace": "{'description': ['Instructs the module on the way to perform the configuration on the device.  If the replace argument is set to I(line) then the modified lines are pushed to the device in configuration mode.  If the replace argument is set to I(block) then the entire command block is pushed to the device in configuration mode if any line is not correct.'], 'default': 'line', 'choices': ['line', 'block']}",
    "save": "{'description': ['The C(save) argument instructs the module to save the current-configuration to saved-configuration.  This operation is performed after any changes are made to the current running config.  If no changes are made, the configuration is still saved to the startup config.  This option will always cause the module to return changed.'], 'type': 'bool', 'default': False}",
    "src": "{'description': ['The I(src) argument provides a path to the configuration file to load into the remote system.  The path can either be a full system path to the configuration file if the value starts with / or relative to the root of the implemented role or playbook. This argument is mutually exclusive with the I(lines) and I(parents) arguments.']}",
}
```

## Examples


``` yaml

# Note: examples below use the following provider dict to handle
#       transport and authentication to the node.

- name: CloudEngine config test
  hosts: cloudengine
  connection: local
  gather_facts: no
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:
  - name: "Configure top level configuration and save it"
    ce_config:
      lines: sysname {{ inventory_hostname }}
      save: yes
      provider: "{{ cli }}"

  - name: "Configure acl configuration and save it"
    ce_config:
      lines:
        - rule 10 permit source 1.1.1.1 32
        - rule 20 permit source 2.2.2.2 32
        - rule 30 permit source 3.3.3.3 32
        - rule 40 permit source 4.4.4.4 32
        - rule 50 permit source 5.5.5.5 32
      parents: acl 2000
      before: undo acl 2000
      match: exact
      provider: "{{ cli }}"

  - name: "Configure acl configuration and save it"
    ce_config:
      lines:
        - rule 10 permit source 1.1.1.1 32
        - rule 20 permit source 2.2.2.2 32
        - rule 30 permit source 3.3.3.3 32
        - rule 40 permit source 4.4.4.4 32
      parents: acl 2000
      before: undo acl 2000
      replace: block
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['QijunPan (@CloudEngine-Ansible)']
