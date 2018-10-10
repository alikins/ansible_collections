# Ansible module: ansible.module_bigip_policy_rule


Manage LTM policy rules on a BIG-IP

## Description

This module will manage LTM policy rules on a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "actions": "{'description': ['The actions that you want the policy rule to perform.', 'The available attributes vary by the action, however, each action requires that a C(type) be specified.', 'These conditions can be specified in any order. Despite them being a list, the BIG-IP does not treat their order as anything special.'], 'suboptions': {'type': {'description': ['The action type. This value controls what below options are required.', 'When C(type) is C(forward), will associate a given C(pool), or C(virtual) with this rule.', 'When C(type) is C(enable), will associate a given C(asm_policy) with this rule.', 'When C(type) is C(ignore), will remove all existing actions from this rule.'], 'required': True, 'choices': ['forward', 'enable', 'ignore']}, 'pool': {'description': ['Pool that you want to forward traffic to.', 'This parameter is only valid with the C(forward) type.']}, 'virtual': {'description': ['Virtual Server that you want to forward traffic to.', 'This parameter is only valid with the C(forward) type.']}, 'asm_policy': {'description': ['ASM policy to enable.', 'This parameter is only valid with the C(enable) type.']}}}",
    "conditions": "{'description': ['A list of attributes that describe the condition.', 'See suboptions for details on how to construct each list entry.', 'The ordering of this list is important, the module will ensure the order is kept when modifying the task.', 'The suboption options listed below are not required for all condition types, read the description for more details.', 'These conditions can be specified in any order. Despite them being a list, the BIG-IP does not treat their order as anything special.'], 'suboptions': {'type': {'description': ['The condition type. This value controls what below options are required.', 'When C(type) is C(http_uri), will associate a given C(path_begins_with_any) list of strings with which the HTTP URI should begin with. Any item in the list will provide a match.', 'When C(type) is C(all_traffic), will remove all existing conditions from this rule.'], 'required': True, 'choices': ['http_uri', 'all_traffic']}, 'path_begins_with_any': {'description': ['A list of strings of characters that the HTTP URI should start with.', 'This parameter is only valid with the C(http_uri) type.']}}}",
    "description": "{'description': ['Description of the policy rule.']}",
    "name": "{'description': ['The name of the rule.'], 'required': True}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "policy": "{'description': ['The name of the policy that you want to associate this rule with.'], 'required': True}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the key is uploaded to the device. When C(absent), ensures that the key is removed from the device. If the key is currently in use, the module will not be able to remove the key.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create policies
  bigip_policy:
    name: Policy-Foo
    state: present
  delegate_to: localhost

- name: Add a rule to the new policy
  bigip_policy_rule:
    policy: Policy-Foo
    name: rule3
    conditions:
      - type: http_uri
        path_begins_with_any: /ABC
    actions:
      - type: forward
        pool: pool-svrs
  delegate_to: localhost

- name: Add multiple rules to the new policy
  bigip_policy_rule:
    policy: Policy-Foo
    name: "{{ item.name }}"
    conditions: "{{ item.conditions }}"
    actions: "{{ item.actions }}"
  delegate_to: localhost
  loop:
    - name: rule1
      actions:
        - type: forward
          pool: pool-svrs
      conditions:
        - type: http_uri
          path_starts_with: /euro
    - name: rule2
      actions:
        - type: forward
          pool: pool-svrs
      conditions:
        - type: http_uri
          path_starts_with: /HomePage/

- name: Remove all rules and confitions from the rule
  bigip_policy_rule:
    policy: Policy-Foo
    name: rule1
    conditions:
      - type: all_traffic
    actions:
      - type: ignore
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
