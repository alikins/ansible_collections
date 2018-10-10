# Ansible module: ansible.module_bigip_facts


Collect facts from F5 BIG-IP devices

## Description

Collect facts from F5 BIG-IP devices via iControl SOAP API

## Requirements

TODO

## Arguments

``` json
{
    "filter": "{'description': ['Shell-style glob matching string used to filter fact keys. Not applicable for software, provision, and system_info fact categories.']}",
    "include": "{'description': ['Fact category or list of categories to collect'], 'required': True, 'choices': ['address_class', 'certificate', 'client_ssl_profile', 'device', 'device_group', 'interface', 'key', 'node', 'pool', 'provision', 'rule', 'self_ip', 'software', 'system_info', 'traffic_group', 'trunk', 'virtual_address', 'virtual_server', 'vlan']}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "session": "{'description': ['BIG-IP session support; may be useful to avoid concurrency issues in certain circumstances.'], 'default': False, 'type': 'bool'}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Collect BIG-IP facts
  bigip_facts:
    server: lb.mydomain.com
    user: admin
    password: secret
    include:
      - interface
      - vlan
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Matt Hite (@mhite)', 'Tim Rupp (@caphrim007)']
  - ['Matt Hite (@mhite)', 'Tim Rupp (@caphrim007)']
