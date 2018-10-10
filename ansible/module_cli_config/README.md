# Ansible module: ansible.module_cli_config


Push text based configuration to network devices over network_cli

## Description

This module provides platform agnostic way of pushing text based configuration to network devices over network_cli connection plugin.

## Requirements

TODO

## Arguments

``` json
{
    "commit": "{'description': ['The C(commit) argument instructs the module to push the configuration to the device. This is mapped to module check mode.'], 'type': 'bool'}",
    "commit_comment": "{'description': ['The C(commit_comment) argument specifies a text string to be used when committing the configuration. If the C(commit) argument is set to False, this argument is silently ignored. This argument is only valid for the platforms that support commit operation with comment.'], 'type': 'str'}",
    "config": "{'description': ['The config to be pushed to the network device. This argument is mutually exclusive with C(rollback) and either one of the option should be given as input. The config should have indentation that the device uses.'], 'type': 'str'}",
    "defaults": "{'description': ['The I(defaults) argument will influence how the running-config is collected from the device.  When the value is set to true, the command used to collect the running-config is append with the all keyword.  When the value is set to false, the command is issued without the all keyword.'], 'default': False, 'type': 'bool'}",
    "diff_ignore_lines": "{'description': ['Use this argument to specify one or more lines that should be ignored during the diff. This is used for lines in the configuration that are automatically updated by the system. This argument takes a list of regular expressions or exact line matches. Note that this parameter will be ignored if the platform has onbox diff support.']}",
    "diff_match": "{'description': ['Instructs the module on the way to perform the matching of the set of commands against the current device config. If C(diff_match) is set to I(line), commands are matched line by line. If C(diff_match) is set to I(strict), command lines are matched with respect to position. If C(diff_match) is set to I(exact), command lines must be an equal match. Finally, if C(diff_match) is set to I(none), the module will not attempt to compare the source configuration with the running configuration on the remote device. Note that this parameter will be ignored if the platform has onbox diff support.'], 'choices': ['line', 'strict', 'exact', 'none']}",
    "diff_replace": "{'description': ['Instructs the module on the way to perform the configuration on the device. If the C(diff_replace) argument is set to I(line) then the modified lines are pushed to the device in configuration mode. If the argument is set to I(block) then the entire command block is pushed to the device in configuration mode if any line is not correct. Note that this parameter will be ignored if the platform has onbox diff support.'], 'choices': ['line', 'block', 'config']}",
    "multiline_delimiter": "{'description': ['This argument is used when pushing a multiline configuration element to the device. It specifies the character to use as the delimiting character. This only applies to the configuration action.'], 'type': 'str'}",
    "replace": "{'description': ['If the C(replace) argument is set to C(yes), it will replace the entire running-config of the device with the C(config) argument value. For NXOS devices, C(replace) argument takes path to the file on the device that will be used for replacing the entire running-config. Nexus 9K devices only support replace. Use I(net_put) or I(nxos_file_copy) module to copy the flat file to remote device and then use set the fullpath to this argument.'], 'type': 'str'}",
    "rollback": "{'description': ['The C(rollback) argument instructs the module to rollback the current configuration to the identifier specified in the argument.  If the specified rollback identifier does not exist on the remote device, the module will fail. To rollback to the most recent commit, set the C(rollback) argument to 0. This option is mutually exclusive with C(config).']}",
}
```

## Examples


``` yaml

- name: configure device with config
  cli_config:
    config: "{{ lookup('template', 'basic/config.j2') }}"

- name: configure device with config with defaults enabled
  cli_config:
    config: "{{ lookup('template', 'basic/config.j2') }}"
    defaults: yes

- name: Use diff_match
  cli_config:
    config: "{{ lookup('file', 'interface_config') }}"
    diff_match: none

- name: nxos replace config
  cli_config:
    replace: 'bootflash:nxoscfg'

- name: commit with comment
  cli_config:
    config: set system host-name foo
    commit_comment: this is a test

```

## License

TODO

## Author Information
  - ['Trishna Guha (@trishnaguha)']
