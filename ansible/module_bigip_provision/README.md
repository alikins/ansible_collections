# Ansible module: ansible.module_bigip_provision


Manage BIG-IP module provisioning

## Description

Manage BIG-IP module provisioning. This module will only provision at the standard levels of Dedicated, Nominal, and Minimum.

## Requirements

TODO

## Arguments

``` json
{
    "level": "{'description': ['Sets the provisioning level for the requested modules. Changing the level for one module may require modifying the level of another module. For example, changing one module to C(dedicated) requires setting all others to C(none). Setting the level of a module to C(none) means that the module is not activated.', 'This parameter is not relevant to C(cgnat) and will not be applied to the C(cgnat) module.'], 'default': 'nominal', 'choices': ['dedicated', 'nominal', 'minimum']}",
    "module": "{'description': ['The module to provision in BIG-IP.'], 'required': True, 'choices': ['am', 'afm', 'apm', 'asm', 'avr', 'cgnat', 'fps', 'gtm', 'ilx', 'lc', 'ltm', 'pem', 'sam', 'swg', 'vcmp'], 'aliases': ['name']}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['The state of the provisioned module on the system. When C(present), guarantees that the specified module is provisioned at the requested level provided that there are sufficient resources on the device (such as physical RAM) to support the provisioned module. When C(absent), de-provision the module.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Provision PEM at "nominal" level
  bigip_provision:
    server: lb.mydomain.com
    module: pem
    level: nominal
    password: secret
    user: admin
    validate_certs: no
  delegate_to: localhost

- name: Provision a dedicated SWG. This will unprovision every other module
  bigip_provision:
    server: lb.mydomain.com
    module: swg
    password: secret
    level: dedicated
    user: admin
    validate_certs: no
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
