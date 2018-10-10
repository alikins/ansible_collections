# Ansible module: ansible.module_bigip_gtm_pool


Manages F5 BIG-IP GTM pools

## Description

Manages F5 BIG-IP GTM pools.

## Requirements

TODO

## Arguments

``` json
{
    "alternate_lb_method": "{'description': ['The load balancing mode that the system tries if the C(preferred_lb_method) is unsuccessful in picking a pool.'], 'choices': ['round-robin', 'return-to-dns', 'none', 'ratio', 'topology', 'static-persistence', 'global-availability', 'virtual-server-capacity', 'packet-rate', 'drop-packet', 'fallback-ip', 'virtual-server-score']}",
    "availability_requirements": "{'description': ['Specifies, if you activate more than one health monitor, the number of health monitors that must receive successful responses in order for the link to be considered available.'], 'suboptions': {'type': {'description': ['Monitor rule type when C(monitors) is specified.', "When creating a new pool, if this value is not specified, the default of 'all' will be used."], 'choices': ['all', 'at_least', 'require']}, 'at_least': {'description': ['Specifies the minimum number of active health monitors that must be successful before the link is considered up.', 'This parameter is only relevant when a C(type) of C(at_least) is used.', 'This parameter will be ignored if a type of either C(all) or C(require) is used.']}, 'number_of_probes': {'description': ['Specifies the minimum number of probes that must succeed for this server to be declared up.', 'When creating a new virtual server, if this parameter is specified, then the C(number_of_probers) parameter must also be specified.', 'The value of this parameter should always be B(lower) than, or B(equal to), the value of C(number_of_probers).', 'This parameter is only relevant when a C(type) of C(require) is used.', 'This parameter will be ignored if a type of either C(all) or C(at_least) is used.']}, 'number_of_probers': {'description': ['Specifies the number of probers that should be used when running probes.', 'When creating a new virtual server, if this parameter is specified, then the C(number_of_probes) parameter must also be specified.', 'The value of this parameter should always be B(higher) than, or B(equal to), the value of C(number_of_probers).', 'This parameter is only relevant when a C(type) of C(require) is used.', 'This parameter will be ignored if a type of either C(all) or C(at_least) is used.']}}, 'version_added': 2.6}",
    "fallback_ip": "{'description': ['Specifies the IPv4, or IPv6 address of the server to which the system directs requests when it cannot use one of its pools to do so. Note that the system uses the fallback IP only if you select the C(fallback_ip) load balancing method.']}",
    "fallback_lb_method": "{'description': ['The load balancing mode that the system tries if both the C(preferred_lb_method) and C(alternate_lb_method)s are unsuccessful in picking a pool.'], 'choices': ['round-robin', 'return-to-dns', 'ratio', 'topology', 'static-persistence', 'global-availability', 'virtual-server-capacity', 'least-connections', 'lowest-round-trip-time', 'fewest-hops', 'packet-rate', 'cpu', 'completion-rate', 'quality-of-service', 'kilobytes-per-second', 'drop-packet', 'fallback-ip', 'virtual-server-score', 'none']}",
    "members": "{'description': ['Members to assign to the pool.', 'The order of the members in this list is the order that they will be listed in the pool.'], 'suboptions': {'server': {'description': ['Name of the server which the pool member is a part of.'], 'required': True}, 'virtual_server': {'description': ['Name of the virtual server, associated with the server, that the pool member is a part of.'], 'required': True}}, 'version_added': 2.6}",
    "monitors": "{'description': ['Specifies the health monitors that the system currently uses to monitor this resource.', 'When C(availability_requirements.type) is C(require), you may only have a single monitor in the C(monitors) list.'], 'version_added': 2.6}",
    "name": "{'description': ['Name of the GTM pool.'], 'required': True}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common', 'version_added': 2.5}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "preferred_lb_method": "{'description': ['The load balancing mode that the system tries first.'], 'choices': ['round-robin', 'return-to-dns', 'ratio', 'topology', 'static-persistence', 'global-availability', 'virtual-server-capacity', 'least-connections', 'lowest-round-trip-time', 'fewest-hops', 'packet-rate', 'cpu', 'completion-rate', 'quality-of-service', 'kilobytes-per-second', 'drop-packet', 'fallback-ip', 'virtual-server-score']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['Pool state. When C(present), ensures that the pool is created and enabled. When C(absent), ensures that the pool is removed from the system. When C(enabled) or C(disabled), ensures that the pool is enabled or disabled (respectively) on the remote device.'], 'choices': ['present', 'absent', 'enabled', 'disabled'], 'default': 'present'}",
    "type": "{'description': ['The type of GTM pool that you want to create. On BIG-IP releases prior to version 12, this parameter is not required. On later versions of BIG-IP, this is a required parameter.'], 'choices': ['a', 'aaaa', 'cname', 'mx', 'naptr', 'srv']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create a GTM pool
  bigip_gtm_pool:
    server: lb.mydomain.com
    user: admin
    password: secret
    name: my_pool
  delegate_to: localhost

- name: Disable pool
  bigip_gtm_pool:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: disabled
    name: my_pool
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
