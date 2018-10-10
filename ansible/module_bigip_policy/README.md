# Ansible module: ansible.module_bigip_policy


Manage general policy configuration on a BIG-IP

## Description

Manages general policy configuration on a BIG-IP. This module is best used in conjunction with the C(bigip_policy_rule) module. This module can handle general configuration like setting the draft state of the policy, the description, and things unrelated to the policy rules themselves. It is also the first module that should be used when creating rules as the C(bigip_policy_rule) module requires a policy parameter.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['The description to attach to the policy.', 'This parameter is only supported on versions of BIG-IP >= 12.1.0. On earlier versions it will simply be ignored.']}",
    "name": "{'description': ['The name of the policy to create.'], 'required': True}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "rules": "{'description': ['Specifies a list of rules that you want associated with this policy. The order of this list is the order they will be evaluated by BIG-IP. If the specified rules do not exist (for example when creating a new policy) then they will be created.', 'The C(conditions) for a default rule are C(all).', 'The C(actions) for a default rule are C(ignore).', 'The C(bigip_policy_rule) module can be used to create and edit existing and new rules.']}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(state) is C(present), ensures that the policy exists and is published. When C(state) is C(absent), ensures that the policy is removed, even if it is currently drafted.', 'When C(state) is C(draft), ensures that the policy exists and is drafted. When modifying rules, it is required that policies first be in a draft.', 'Drafting is only supported on versions of BIG-IP >= 12.1.0. On versions prior to that, specifying a C(state) of C(draft) will raise an error.'], 'choices': ['present', 'absent', 'draft'], 'default': 'present'}",
    "strategy": "{'description': ['Specifies the method to determine which actions get executed in the case where there are multiple rules that match. When creating new policies, the default is C(first).', 'This module does not allow you to specify the C(best) strategy to use. It will choose the system default (C(/Common/best-match)) for you instead.'], 'choices': ['first', 'all', 'best']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create policy which is immediately published
  bigip_policy:
    name: Policy-Foo
    state: present
  delegate_to: localhost

- name: Add a rule to the new policy - Immediately published
  bigip_policy_rule:
    policy: Policy-Foo
    name: ABC
    conditions:
      - type: http_uri
        path_starts_with:
          - /ABC
          - foo
          - bar
        path_ends_with:
          - baz
    actions:
      - forward: yes
        select: yes
        pool: pool-svrs

- name: Add multiple rules to the new policy - Added in the order they are specified
  bigip_policy_rule:
    policy: Policy-Foo
    name: "{{ item.name }}"
    conditions: "{{ item.conditions }}"
    actions: "{{ item.actions }}"
  with_items:
    - name: rule1
      actions:
        - type: forward
          pool: pool-svrs
      conditions:
        - type: http_uri
          path_starts_with: /euro
    - name: HomePage
      actions:
        - type: forward
          pool: pool-svrs
      conditions:
        - type: http_uri
          path_starts_with: /HomePage/

- name: Create policy specify default rules - Immediately published
  bigip_policy:
    name: Policy-Bar
    state: present
    rules:
      - rule1
      - rule2
      - rule3

- name: Create policy specify default rules - Left in a draft
  bigip_policy:
    name: Policy-Baz
    state: draft
    rules:
      - rule1
      - rule2
      - rule3

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
