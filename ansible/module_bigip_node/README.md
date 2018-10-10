# Ansible module: ansible.module_bigip_node


Manages F5 BIG-IP LTM nodes

## Description

Manages F5 BIG-IP LTM nodes.

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['IP address of the node. This can be either IPv4 or IPv6. When creating a new node, one of either C(address) or C(fqdn) must be provided. This parameter cannot be updated after it is set.'], 'aliases': ['ip', 'host'], 'version_added': 2.2}",
    "connection_limit": "{'description': ['Node connection limit. Setting this to 0 disables the limit.'], 'version_added': 2.7}",
    "description": "{'description': ['Specifies descriptive text that identifies the node.', 'You can remove a description by either specifying an empty string, or by specifying the special value C(none).']}",
    "dynamic_ratio": "{'description': ['The dynamic ratio number for the node. Used for dynamic ratio load balancing.', 'When creating a new node, if this parameter is not specified, the default of C(1) will be used.'], 'version_added': 2.7}",
    "fqdn": "{'description': ['FQDN name of the node. This can be any name that is a valid RFC 1123 DNS name. Therefore, the only characters that can be used are "A" to "Z", "a" to "z", "0" to "9", the hyphen ("-") and the period (".").', 'FQDN names must include at lease one period; delineating the host from the domain. ex. C(host.domain).', 'FQDN names must end with a letter or a number.', 'When creating a new node, one of either C(address) or C(fqdn) must be provided. This parameter cannot be updated after it is set.'], 'aliases': ['hostname'], 'version_added': 2.5}",
    "fqdn_address_type": "{'description': ['Specifies whether the FQDN of the node resolves to an IPv4 or IPv6 address.', 'When creating a new node, if this parameter is not specified and C(fqdn) is specified, this parameter will default to C(ipv4).', 'This parameter cannot be changed after it has been set.'], 'choices': ['ipv4', 'ipv6', 'all'], 'version_added': 2.6}",
    "fqdn_auto_populate": "{'description': ['Specifies whether the system automatically creates ephemeral nodes using the IP addresses returned by the resolution of a DNS query for a node defined by an FQDN.', 'When C(yes), the system generates an ephemeral node for each IP address returned in response to a DNS query for the FQDN of the node. Additionally, when a DNS response indicates the IP address of an ephemeral node no longer exists, the system deletes the ephemeral node.', 'When C(no), the system resolves a DNS query for the FQDN of the node with the single IP address associated with the FQDN.', 'When creating a new node, if this parameter is not specified and C(fqdn) is specified, this parameter will default to C(yes).', 'This parameter cannot be changed after it has been set.'], 'type': 'bool', 'version_added': 2.6}",
    "fqdn_down_interval": "{'description': ['Specifies the interval in which a query occurs, when the DNS server is down. The associated monitor continues polling as long as the DNS server is down.', 'When creating a new node, if this parameter is not specified and C(fqdn) is specified, this parameter will default to C(5).'], 'version_added': 2.6}",
    "fqdn_up_interval": "{'description': ['Specifies the interval in which a query occurs, when the DNS server is up. The associated monitor attempts to probe three times, and marks the server down if it there is no response within the span of three times the interval value, in seconds.', 'This parameter accepts a value of C(ttl) to query based off of the TTL of the FQDN. The default TTL interval is akin to specifying C(3600).', 'When creating a new node, if this parameter is not specified and C(fqdn) is specified, this parameter will default to C(3600).'], 'version_added': 2.6}",
    "monitor_type": "{'description': ["Monitor rule type when C(monitors) is specified. When creating a new pool, if this value is not specified, the default of 'and_list' will be used.", 'Both C(single) and C(and_list) are functionally identical since BIG-IP considers all monitors as "a list". BIG=IP either has a list of many, or it has a list of one. Where they differ is in the extra guards that C(single) provides; namely that it only allows a single monitor.'], 'version_added': '1.3', 'choices': ['and_list', 'm_of_n', 'single']}",
    "monitors": "{'description': ['Specifies the health monitors that the system currently uses to monitor this node.'], 'version_added': 2.2}",
    "name": "{'description': ['Specifies the name of the node.'], 'required': True}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common', 'version_added': 2.5}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "quorum": "{'description': ['Monitor quorum value when C(monitor_type) is C(m_of_n).'], 'version_added': 2.2}",
    "rate_limit": "{'description': ['Node rate limit (connections-per-second). Setting this to 0 disables the limit.'], 'version_added': 2.7}",
    "ratio": "{'description': ['Node ratio weight. Valid values range from 1 through 100.', 'When creating a new node, if this parameter is not specified, the default of C(1) will be used.'], 'version_added': 2.7}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ["Specifies the current state of the node. C(enabled) (All traffic allowed), specifies that system sends traffic to this node regardless of the node's state. C(disabled) (Only persistent or active connections allowed), Specifies that the node can handle only persistent or active connections. C(offline) (Only active connections allowed), Specifies that the node can handle only active connections. In all cases except C(absent), the node will be created if it does not yet exist.", 'Be particularly careful about changing the status of a node whose FQDN cannot be resolved. These situations disable your ability to change their C(state) to C(disabled) or C(offline). They will remain in an *Unavailable - Enabled* state.'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled', 'offline']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Add node
  bigip_node:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: present
    partition: Common
    host: 10.20.30.40
    name: 10.20.30.40
  delegate_to: localhost

- name: Add node with a single 'ping' monitor
  bigip_node:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: present
    partition: Common
    host: 10.20.30.40
    name: mytestserver
    monitors:
      - /Common/icmp
  delegate_to: localhost

- name: Modify node description
  bigip_node:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: present
    partition: Common
    name: 10.20.30.40
    description: Our best server yet
  delegate_to: localhost

- name: Delete node
  bigip_node:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: absent
    partition: Common
    name: 10.20.30.40
  delegate_to: localhost

- name: Force node offline
  bigip_node:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: disabled
    partition: Common
    name: 10.20.30.40
  delegate_to: localhost

- name: Add node by their FQDN
  bigip_node:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: present
    partition: Common
    fqdn: foo.bar.com
    name: 10.20.30.40
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
