# Ansible module: ansible.module_bigip_device_license


Manage license installation and activation on BIG-IP devices

## Description

Manage license installation and activation on a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "accept_eula": "{'description': ['Declares whether you accept the BIG-IP EULA or not. By default, this value is C(no). You must specifically declare that you have viewed and accepted the license. This module will not present you with that EULA though, so it is incumbent on you to read it.', 'The EULA can be found here; https://support.f5.com/csp/article/K12902.', 'This parameter is not required when C(state) is C(absent) and will be ignored if it is provided.'], 'type': 'bool'}",
    "license_key": "{'description': ['The registration key to use to license the BIG-IP.', 'This parameter is required if the C(state) is equal to C(present).', 'This parameter is not required when C(state) is C(absent) and will be ignored if it is provided.']}",
    "license_server": "{'description': ['The F5 license server to use when getting a license and validating a dossier.', 'This parameter is required if the C(state) is equal to C(present).', 'This parameter is not required when C(state) is C(absent) and will be ignored if it is provided.'], 'default': 'activate.f5.com'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['The state of the license on the system.', 'When C(present), only guarantees that a license is there.', 'When C(latest), ensures that the license is always valid.', 'When C(absent), removes the license on the system.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: License BIG-IP using a key
  bigip_device_license:
    license_key: "XXXXX-XXXXX-XXXXX-XXXXX-XXXXXXX"
    provider:
      server: "lb.mydomain.com"
      user: "admin"
      password: "secret"
  delegate_to: localhost

- name: Remove the license from the system
  bigip_device_license:
    state: "absent"
    provider:
      server: "lb.mydomain.com"
      user: "admin"
      password: "secret"
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
