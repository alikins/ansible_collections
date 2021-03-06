# Ansible module: ansible.module_bigip_snmp


Manipulate general SNMP settings on a BIG-IP

## Description

Manipulate general SNMP settings on a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "agent_authentication_traps": "{'description': ['When C(enabled), ensures that the system sends authentication warning traps to the trap destinations. This is usually disabled by default on a BIG-IP.'], 'choices': ['enabled', 'disabled']}",
    "agent_status_traps": "{'description': ['When C(enabled), ensures that the system sends a trap whenever the SNMP agent starts running or stops running. This is usually enabled by default on a BIG-IP.'], 'choices': ['enabled', 'disabled']}",
    "allowed_addresses": "{'description': ['Configures the IP addresses of the SNMP clients from which the snmpd daemon accepts requests.', 'This value can be hostnames, IP addresses, or IP networks.', "You may specify a single list item of C(default) to set the value back to the system's default of C(127.0.0.0/8).", 'You can remove all allowed addresses by either providing the word C(none), or by providing the empty string C("").'], 'version_added': 2.6}",
    "contact": "{'description': ['Specifies the name of the person who administers the SNMP service for this system.']}",
    "device_warning_traps": "{'description': ['When C(enabled), ensures that the system sends device warning traps to the trap destinations. This is usually enabled by default on a BIG-IP.'], 'choices': ['enabled', 'disabled']}",
    "location": "{'description': ["Specifies the description of this system's physical location."]}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Set snmp contact
  bigip_snmp:
    contact: Joe User
    password: secret
    server: lb.mydomain.com
    user: admin
    validate_certs: false
  delegate_to: localhost

- name: Set snmp location
  bigip_snmp:
    location: US West 1
    password: secret
    server: lb.mydomain.com
    user: admin
    validate_certs: no
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
