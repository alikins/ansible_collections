# Ansible module: ansible.module_bigip_routedomain


Manage route domains on a BIG-IP

## Description

Manage route domains on a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "bwc_policy": "{'description': ['The bandwidth controller for the route domain.']}",
    "connection_limit": "{'description': ['The maximum number of concurrent connections allowed for the route domain. Setting this to C(0) turns off connection limits.']}",
    "description": "{'description': ['Specifies descriptive text that identifies the route domain.']}",
    "flow_eviction_policy": "{'description': ['The eviction policy to use with this route domain. Apply an eviction policy to provide customized responses to flow overflows and slow flows on the route domain.']}",
    "id": "{'description': ['The unique identifying integer representing the route domain.', 'This field is required when creating a new route domain.', 'In version 2.5, this value is no longer used to reference a route domain when making modifications to it (for instance during update and delete operations). Instead, the C(name) parameter is used. In version 2.6, the C(name) value will become a required parameter.']}",
    "name": "{'description': ['The name of the route domain.'], 'version_added': 2.5}",
    "parent": "{'description': ['Specifies the route domain the system searches when it cannot find a route in the configured domain.']}",
    "partition": "{'description': ['Partition to create the route domain on. Partitions cannot be updated once they are created.'], 'default': 'Common', 'version_added': 2.5}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "routing_protocol": "{'description': ['Dynamic routing protocols for the system to use in the route domain.'], 'choices': ['none', 'BFD', 'BGP', 'IS-IS', 'OSPFv2', 'OSPFv3', 'PIM', 'RIP', 'RIPng']}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "service_policy": "{'description': ['Service policy to associate with the route domain.']}",
    "state": "{'description': ['Whether the route domain should exist or not.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "strict": "{'description': ['Specifies whether the system enforces cross-routing restrictions or not.'], 'type': 'bool'}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
    "vlans": "{'description': ['VLANs for the system to use in the route domain.']}",
}
```

## Examples


``` yaml

- name: Create a route domain
  bigip_routedomain:
    name: foo
    id: 1234
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Set VLANs on the route domain
  bigip_routedomain:
    name: bar
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
    vlans:
      - net1
      - foo
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
