# Ansible module: ansible.module_bigip_static_route


Manipulate static routes on a BIG-IP

## Description

Manipulate static routes on a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['Descriptive text that identifies the route.']}",
    "destination": "{'description': ['Specifies an IP address for the static entry in the routing table. When creating a new static route, this value is required.', 'This value cannot be changed once it is set.']}",
    "gateway_address": "{'description': ['Specifies the router for the system to use when forwarding packets to the destination host or network. Also known as the next-hop router address. This can be either an IPv4 or IPv6 address. When it is an IPv6 address that starts with C(FE80:), the address will be treated as a link-local address. This requires that the C(vlan) parameter also be supplied.']}",
    "mtu": "{'description': ['Specifies a specific maximum transmission unit (MTU).']}",
    "name": "{'description': ['Name of the static route.'], 'required': True}",
    "netmask": "{'description': ['The netmask for the static route. When creating a new static route, this value is required.', 'This value can be in either IP or CIDR format.', 'This value cannot be changed once it is set.']}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common', 'version_added': 2.6}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "pool": "{'description': ['Specifies the pool through which the system forwards packets to the destination.']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "reject": "{'description': ['Specifies that the system drops packets sent to the destination.'], 'type': 'bool'}",
    "route_domain": "{'description': ['The route domain id of the system. When creating a new static route, if this value is not specified, a default value of C(0) will be used.', 'This value cannot be changed once it is set.']}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the static route exists.', 'When C(absent), ensures that the static does not exist.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
    "vlan": "{'description': ['Specifies the VLAN or Tunnel through which the system forwards packets to the destination. When C(gateway_address) is a link-local IPv6 address, this value is required']}",
}
```

## Examples


``` yaml

- name: Create static route with gateway address
  bigip_static_route:
    destination: 10.10.10.10
    netmask: 255.255.255.255
    gateway_address: 10.2.2.3
    name: test-route
    password: secret
    server: lb.mydomain.come
    user: admin
    validate_certs: no
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
