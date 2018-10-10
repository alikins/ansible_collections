# Ansible module: ansible.module_bigip_snmp_trap


Manipulate SNMP trap information on a BIG-IP

## Description

Manipulate SNMP trap information on a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "community": "{'description': ['Specifies the community name for the trap destination.']}",
    "destination": "{'description': ['Specifies the address for the trap destination. This can be either an IP address or a hostname.']}",
    "name": "{'description': ['Name of the SNMP configuration endpoint.'], 'required': True}",
    "network": "{'description': ['Specifies the name of the trap network. This option is not supported in versions of BIG-IP < 12.1.0. If used on versions < 12.1.0, it will simply be ignored.', 'The value C(default) was removed in BIG-IP version 13.1.0. Specifying this value when configuring a BIG-IP will cause the module to stop and report an error. The usual remedy is to choose one of the other options, such as C(management).'], 'choices': ['other', 'management', 'default']}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common', 'version_added': 2.5}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['Specifies the port for the trap destination.']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "snmp_version": "{'description': ['Specifies to which Simple Network Management Protocol (SNMP) version the trap destination applies.'], 'choices': ['1', '2c']}",
    "state": "{'description': ['When C(present), ensures that the resource exists.', 'When C(absent), ensures that the resource does not exist.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create snmp v1 trap
  bigip_snmp_trap:
    community: general
    destination: 1.2.3.4
    name: my-trap1
    network: management
    port: 9000
    snmp_version: 1
    server: lb.mydomain.com
    user: admin
    password: secret
  delegate_to: localhost

- name: Create snmp v2 trap
  bigip_snmp_trap:
    community: general
    destination: 5.6.7.8
    name: my-trap2
    network: default
    port: 7000
    snmp_version: 2c
    server: lb.mydomain.com
    user: admin
    password: secret
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
