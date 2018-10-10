# Ansible module: ansible.module_bigip_irule


Manage iRules across different modules on a BIG-IP

## Description

Manage iRules across different modules on a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "content": "{'description': ["When used instead of 'src', sets the contents of an iRule directly to the specified value. This is for simple values, but can be used with lookup plugins for anything complex or with formatting. Either one of C(src) or C(content) must be provided."]}",
    "module": "{'description': ['The BIG-IP module to add the iRule to.'], 'required': True, 'choices': ['ltm', 'gtm']}",
    "name": "{'description': ['The name of the iRule.'], 'required': True}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common', 'version_added': 2.5}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "src": "{'description': ['The iRule file to interpret and upload to the BIG-IP. Either one of C(src) or C(content) must be provided.'], 'required': True}",
    "state": "{'description': ['Whether the iRule should exist or not.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Add the iRule contained in template irule.tcl to the LTM module
  bigip_irule:
    content: "{{ lookup('template', 'irule.tcl') }}"
    module: ltm
    name: MyiRule
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Add the iRule contained in static file irule.tcl to the LTM module
  bigip_irule:
    module: ltm
    name: MyiRule
    password: secret
    server: lb.mydomain.com
    src: irule.tcl
    state: present
    user: admin
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
