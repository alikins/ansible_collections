# Ansible module: ansible.module_cv_server_provision


Provision server port by applying or removing template configuration to an Arista CloudVision Portal configlet that is applied to a switch

## Description

This module allows a server team to provision server network ports for new servers without having to access Arista CVP or asking the network team to do it for them. Provide the information for connecting to CVP, switch rack, port the new server is connected to, optional vlan, and an action and the module will apply the configuration to the switch port via CVP. Actions are add (applies template config to port), remove (defaults the interface config) and show (returns the current port config).

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['The action for the module to take. The actions are add, which applies the specified template config to port, remove, which defaults the specified interface configuration, and show, which will return the current port configuration with no changes.'], 'default': 'show', 'choices': ['show', 'add', 'remove']}",
    "auto_run": "{'description': ['Flag that determines whether or not the module will execute the CVP task spawned as a result of changes to a switch configlet. When an add or remove action is taken which results in a change to a switch configlet, CVP will spawn a task that needs to be executed for the configuration to be applied to the switch. If this option is True then the module will determined the task number created by the configuration change, execute it and wait for the task to complete. If the option is False then the task will remain in the Pending state in CVP for a network administrator to review and execute.'], 'type': 'bool', 'default': False}",
    "host": "{'description': ['The hostname or IP address of the CVP node being connected to.'], 'required': True}",
    "password": "{'description': ['The password of the user that will be used to connect to CVP for API calls.'], 'required': True}",
    "port": "{'description': ['The port number to use when making API calls to the CVP node. This will default to the default port for the specified protocol. Port 80 for http and port 443 for https.']}",
    "port_vlan": "{'description': ['The vlan that should be applied to the port for this server. This parameter is dependent on a proper template that supports single vlan provisioning with it. If a port vlan is specified by the template specified does not support this the module will exit out with no changes. If a template is specified that requires a port vlan but no port vlan is specified the module will exit out with no changes.']}",
    "protocol": "{'description': ['The protocol to use when making API calls to CVP. CVP defaults to https and newer versions of CVP no longer support http.'], 'default': 'https', 'choices': ['https', 'http']}",
    "server_name": "{'description': ["The hostname or identifier for the server that is having it's switch port provisioned."], 'required': True}",
    "switch_name": "{'description': ['The hostname of the switch is being configured for the server being provisioned.'], 'required': True}",
    "switch_port": "{'description': ['The physical port number on the switch that the new server is connected to.'], 'required': True}",
    "template": "{'description': ['A path to a Jinja formatted template file that contains the configuration block that will be applied to the specified switch port. This template will have variable fields replaced by the module before being applied to the switch configuration.'], 'required': True}",
    "username": "{'description': ['The user that will be used to connect to CVP for making API calls.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Get current configuration for interface Ethernet2
  cv_server_provision:
    host: cvp_node
    username: cvp_user
    password: cvp_pass
    protocol: https
    server_name: new_server
    switch_name: eos_switch_1
    switch_port: 2
    template: template_file.j2
    action: show

- name: Remove existing configuration from interface Ethernet2. Run task.
  cv_server_provision:
    host: cvp_node
    username: cvp_user
    password: cvp_pass
    protocol: https
    server_name: new_server
    switch_name: eos_switch_1
    switch_port: 2
    template: template_file.j2
    action: remove
    auto_run: True

- name: Add template configuration to interface Ethernet2. No VLAN. Run task.
  cv_server_provision:
    host: cvp_node
    username: cvp_user
    password: cvp_pass
    protocol: https
    server_name: new_server
    switch_name: eos_switch_1
    switch_port: 2
    template: single_attached_trunk.j2
    action: add
    auto_run: True

- name: Add template with VLAN configuration to interface Ethernet2. Run task.
  cv_server_provision:
    host: cvp_node
    username: cvp_user
    password: cvp_pass
    protocol: https
    server_name: new_server
    switch_name: eos_switch_1
    switch_port: 2
    port_vlan: 22
    template: single_attached_vlan.j2
    action: add
    auto_run: True

```

## License

TODO

## Author Information
  - ['EOS+ CS (ansible-dev@arista.com) (@mharista)']
