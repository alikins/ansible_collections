# Ansible module: ansible.module_bigip_appsvcs_extension


Manage application service deployments

## Description

Manages application service deployments via the App Services Extension functionality in BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "content": "{'description': ['Declaration of tenants configured on the system.', 'This parameter is most often used along with the C(file) or C(template) lookup plugins. Refer to the examples section for correct usage.', 'For anything advanced or with formatting consider using the C(template) lookup.', 'This can additionally be used for specifying application service configurations directly in YAML, however that is not an encouraged practice and, if used at all, should only be used for the absolute smallest of configurations to prevent your Playbooks from becoming too large.', 'If you C(content) includes encrypted values (such as ciphertexts, passphrases, etc), the returned C(changed) value will always be true.'], 'required': True}",
    "force": "{'description': ['Force updates a declaration.', 'This parameter should be used in cases where your declaration includes items that are encrypted or in cases (such as WAF Policies) where you want a large reload to take place.'], 'type': 'bool', 'default': False}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(state) is C(present), ensures the configuration exists.', 'When C(state) is C(absent), ensures that the configuration is removed.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tenants": "{'description': ['A list of tenants that you want to remove.', 'This parameter is only relevant when C(state) is C(absent). It will be ignored when C(state) is C(present).', 'A value of C(all) will remove all tenants.', 'Tenants can be specified as a list as well to remove only specific tenants.']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Deploy an app service configuration
  bigip_appsvcs_extension:
    content: "{{ lookup('file', '/path/to/appsvcs.json') }}"
    state: present
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove all app service configurations
  bigip_appsvcs_extension:
    tenants: all
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove tenants T1 and T2 from app service configurations
  bigip_appsvcs_extension:
    tenants:
      - T1
      - T2
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
