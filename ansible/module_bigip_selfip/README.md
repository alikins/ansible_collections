# Ansible module: ansible.module_bigip_selfip


Manage Self-IPs on a BIG-IP system

## Description

Manage Self-IPs on a BIG-IP system.

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['The IP addresses for the new self IP. This value is ignored upon update as addresses themselves cannot be changed after they are created.', 'This value is required when creating new self IPs.']}",
    "allow_service": "{'description': ['Configure port lockdown for the Self IP. By default, the Self IP has a "default deny" policy. This can be changed to allow TCP and UDP ports as well as specific protocols. This list should contain C(protocol):C(port) values.']}",
    "name": "{'description': ['The self IP to create.', 'If this parameter is not specified, then it will default to the value supplied in the C(address) parameter.'], 'required': True}",
    "netmask": "{'description': ['The netmask for the self IP. When creating a new Self IP, this value is required.']}",
    "partition": "{'description': ['Device partition to manage resources on. You can set different partitions for Self IPs, but the address used may not match any other address used by a Self IP. In that sense, Self IPs are not isolated by partitions as other resources on a BIG-IP are.'], 'default': 'Common', 'version_added': 2.5}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "route_domain": "{'description': ['The route domain id of the system. When creating a new Self IP, if this value is not specified, a default value of C(0) will be used.', 'This value cannot be changed after it is set.'], 'version_added': 2.3}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), guarantees that the Self-IP exists with the provided attributes.', 'When C(absent), removes the Self-IP from the system.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "traffic_group": "{'description': ['The traffic group for the Self IP addresses in an active-active, redundant load balancer configuration. When creating a new Self IP, if this value is not specified, the default of C(/Common/traffic-group-local-only) will be used.']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
    "vlan": "{'description': ['The VLAN that the new self IPs will be on. When creating a new Self IP, this value is required.']}",
}
```

## Examples


``` yaml

- name: Create Self IP
  bigip_selfip:
    address: 10.10.10.10
    name: self1
    netmask: 255.255.255.0
    password: secret
    server: lb.mydomain.com
    user: admin
    validate_certs: no
    vlan: vlan1
  delegate_to: localhost

- name: Create Self IP with a Route Domain
  bigip_selfip:
    server: lb.mydomain.com
    user: admin
    password: secret
    validate_certs: no
    name: self1
    address: 10.10.10.10
    netmask: 255.255.255.0
    vlan: vlan1
    route_domain: 10
    allow_service: default
  delegate_to: localhost

- name: Delete Self IP
  bigip_selfip:
    name: self1
    password: secret
    server: lb.mydomain.com
    state: absent
    user: admin
    validate_certs: no
  delegate_to: localhost

- name: Allow management web UI to be accessed on this Self IP
  bigip_selfip:
    name: self1
    password: secret
    server: lb.mydomain.com
    state: absent
    user: admin
    validate_certs: no
    allow_service:
      - tcp:443
  delegate_to: localhost

- name: Allow HTTPS and SSH access to this Self IP
  bigip_selfip:
    name: self1
    password: secret
    server: lb.mydomain.com
    state: absent
    user: admin
    validate_certs: no
    allow_service:
      - tcp:443
      - tcp:22
  delegate_to: localhost

- name: Allow all services access to this Self IP
  bigip_selfip:
    name: self1
    password: secret
    server: lb.mydomain.com
    state: absent
    user: admin
    validate_certs: no
    allow_service:
      - all
  delegate_to: localhost

- name: Allow only GRE and IGMP protocols access to this Self IP
  bigip_selfip:
    name: self1
    password: secret
    server: lb.mydomain.com
    state: absent
    user: admin
    validate_certs: no
    allow_service:
      - gre:0
      - igmp:0
  delegate_to: localhost

- name: Allow all TCP, but no other protocols access to this Self IP
  bigip_selfip:
    name: self1
    password: secret
    server: lb.mydomain.com
    state: absent
    user: admin
    validate_certs: no
    allow_service:
      - tcp:0
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
