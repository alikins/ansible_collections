# Ansible module: ansible.module_bigip_pool_member


Manages F5 BIG-IP LTM pool members

## Description

Manages F5 BIG-IP LTM pool members via iControl SOAP API.

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['IP address of the pool member. This can be either IPv4 or IPv6. When creating a new pool member, one of either C(address) or C(fqdn) must be provided. This parameter cannot be updated after it is set.'], 'aliases': ['ip', 'host'], 'version_added': 2.2}",
    "connection_limit": "{'description': ['Pool member connection limit. Setting this to 0 disables the limit.']}",
    "description": "{'description': ['Pool member description.']}",
    "fqdn": "{'description': ['FQDN name of the pool member. This can be any name that is a valid RFC 1123 DNS name. Therefore, the only characters that can be used are "A" to "Z", "a" to "z", "0" to "9", the hyphen ("-") and the period (".").', 'FQDN names must include at lease one period; delineating the host from the domain. ex. C(host.domain).', 'FQDN names must end with a letter or a number.', 'When creating a new pool member, one of either C(address) or C(fqdn) must be provided. This parameter cannot be updated after it is set.'], 'aliases': ['hostname'], 'version_added': 2.6}",
    "fqdn_auto_populate": "{'description': ['Specifies whether the system automatically creates ephemeral nodes using the IP addresses returned by the resolution of a DNS query for a node defined by an FQDN.', 'When C(yes), the system generates an ephemeral node for each IP address returned in response to a DNS query for the FQDN of the node. Additionally, when a DNS response indicates the IP address of an ephemeral node no longer exists, the system deletes the ephemeral node.', 'When C(no), the system resolves a DNS query for the FQDN of the node with the single IP address associated with the FQDN.', 'When creating a new pool member, the default for this parameter is C(yes).', 'This parameter is ignored when C(reuse_nodes) is C(yes).'], 'type': 'bool', 'version_added': 2.6}",
    "name": "{'description': ['Name of the node to create, or re-use, when creating a new pool member.', 'This parameter is optional and, if not specified, a node name will be created automatically from either the specified C(address) or C(fqdn).', 'The C(enabled) state is an alias of C(present).'], 'version_added': 2.6}",
    "partition": "{'description': ['Partition'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "pool": "{'description': ['Pool name. This pool must exist.'], 'required': True}",
    "port": "{'description': ['Pool member port.', 'This value cannot be changed after it has been set.'], 'required': True}",
    "preserve_node": "{'description': ['When state is C(absent) attempts to remove the node that the pool member references.', 'The node will not be removed if it is still referenced by other pool members. If this happens, the module will not raise an error.', 'Setting this to C(yes) disables this behavior.'], 'type': 'bool', 'version_added': 2.1}",
    "priority_group": "{'description': ['Specifies a number representing the priority group for the pool member.', 'When adding a new member, the default is 0, meaning that the member has no priority.', 'To specify a priority, you must activate priority group usage when you create a new pool or when adding or removing pool members. When activated, the system load balances traffic according to the priority group number assigned to the pool member.', 'The higher the number, the higher the priority, so a member with a priority of 3 has higher priority than a member with a priority of 1.'], 'version_added': 2.5}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "rate_limit": "{'description': ['Pool member rate limit (connections-per-second). Setting this to 0 disables the limit.']}",
    "ratio": "{'description': ['Pool member ratio weight. Valid values range from 1 through 100. New pool members -- unless overridden with this value -- default to 1.']}",
    "reuse_nodes": "{'description': ['Reuses node definitions if requested.'], 'default': True, 'type': 'bool', 'version_added': 2.6}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['Pool member state.'], 'required': True, 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled', 'forced_offline']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Add pool member
  bigip_pool_member:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: present
    pool: my-pool
    partition: Common
    host: "{{ ansible_default_ipv4['address'] }}"
    port: 80
    description: web server
    connection_limit: 100
    rate_limit: 50
    ratio: 2
  delegate_to: localhost

- name: Modify pool member ratio and description
  bigip_pool_member:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: present
    pool: my-pool
    partition: Common
    host: "{{ ansible_default_ipv4['address'] }}"
    port: 80
    ratio: 1
    description: nginx server
  delegate_to: localhost

- name: Remove pool member from pool
  bigip_pool_member:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: absent
    pool: my-pool
    partition: Common
    host: "{{ ansible_default_ipv4['address'] }}"
    port: 80
  delegate_to: localhost

- name: Force pool member offline
  bigip_pool_member:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: forced_offline
    pool: my-pool
    partition: Common
    host: "{{ ansible_default_ipv4['address'] }}"
    port: 80
  delegate_to: localhost

- name: Create members with priority groups
  bigip_pool_member:
    server: lb.mydomain.com
    user: admin
    password: secret
    pool: my-pool
    partition: Common
    host: "{{ item.address }}"
    name: "{{ item.name }}"
    priority_group: "{{ item.priority_group }}"
    port: 80
  delegate_to: localhost
  loop:
    - host: 1.1.1.1
      name: web1
      priority_group: 4
    - host: 2.2.2.2
      name: web2
      priority_group: 3
    - host: 3.3.3.3
      name: web3
      priority_group: 2
    - host: 4.4.4.4
      name: web4
      priority_group: 1

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
