# Ansible module: ansible.module_bigiq_regkey_license_assignment


Manage regkey license assignment on BIG-IPs from a BIG-IQ

## Description

Manages the assignment of regkey licenses on a BIG-IQ. Assignment means that the license is assigned to a BIG-IP, or, it needs to be assigned to a BIG-IP. Additionally, this module supported revoking the assignments from BIG-IP devices.

## Requirements

TODO

## Arguments

``` json
{
    "device": "{'description': ['When C(managed) is C(no), specifies the address, or hostname, where the BIG-IQ can reach the remote device to register.', 'When C(managed) is C(yes), specifies the managed device, or device UUID, that you want to register.', "If C(managed) is C(yes), it is very important that you do not have more than one device with the same name. BIG-IQ internally recognizes devices by their ID, and therefore, this module's cannot guarantee that the correct device will be registered. The device returned is the device that will be used."]}",
    "device_password": "{'description': ['The password of the C(device_username).', 'When C(managed) is C(no), this parameter is required.']}",
    "device_port": "{'description': ['Specifies the port of the remote device to connect to.', 'If this parameter is not specified, the default of C(443) will be used.'], 'default': 443}",
    "device_username": "{'description': ['The username used to connect to the remote device.', 'This username should be one that has sufficient privileges on the remote device to do licensing. Usually this is the C(Administrator) role.', 'When C(managed) is C(no), this parameter is required.']}",
    "key": "{'description': ['The registration key that you want to assign from the pool.'], 'required': True}",
    "managed": "{'description': ['Whether the specified device is a managed or un-managed device.', 'When C(state) is C(present), this parameter is required.'], 'type': 'bool'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "pool": "{'description': ['The registration key pool to use.'], 'required': True}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the device is assigned the specified license.', 'When C(absent), ensures the license is revokes from the remote device and freed on the BIG-IQ.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Register an unmanaged device
  bigiq_regkey_license_assignment:
    pool: my-regkey-pool
    key: XXXX-XXXX-XXXX-XXXX-XXXX
    device: 1.1.1.1
    managed: no
    device_username: admin
    device_password: secret
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Register a managed device, by name
  bigiq_regkey_license_assignment:
    pool: my-regkey-pool
    key: XXXX-XXXX-XXXX-XXXX-XXXX
    device: bigi1.foo.com
    managed: yes
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Register a managed device, by UUID
  bigiq_regkey_license_assignment:
    pool: my-regkey-pool
    key: XXXX-XXXX-XXXX-XXXX-XXXX
    device: 7141a063-7cf8-423f-9829-9d40599fa3e0
    managed: yes
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
