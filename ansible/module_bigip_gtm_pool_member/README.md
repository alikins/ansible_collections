# Ansible module: ansible.module_bigip_gtm_pool_member


Manage GTM pool member settings

## Description

Manages a variety of settings on GTM pool members. The settings that can be adjusted with this module are much more broad that what can be done in the C(bigip_gtm_pool) module. The pool module is intended to allow you to adjust the member order in the pool, not the various settings of the members. The C(bigip_gtm_pool_member) module should be used to adjust all of the other settings.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['The description of the pool member.']}",
    "limits": "{'description': ['Specifies resource thresholds or limit requirements at the pool member level.', 'When you enable one or more limit settings, the system then uses that data to take members in and out of service.', 'You can define limits for any or all of the limit settings. However, when a member does not meet the resource threshold limit requirement, the system marks the member as unavailable and directs load-balancing traffic to another resource.'], 'suboptions': {'bits_enabled': {'description': ['Whether the bits limit it enabled or not.', 'This parameter allows you to switch on or off the effect of the limit.'], 'type': 'bool'}, 'packets_enabled': {'description': ['Whether the packets limit it enabled or not.', 'This parameter allows you to switch on or off the effect of the limit.'], 'type': 'bool'}, 'connections_enabled': {'description': ['Whether the current connections limit it enabled or not.', 'This parameter allows you to switch on or off the effect of the limit.'], 'type': 'bool'}, 'bits_limit': {'description': ['Specifies the maximum allowable data throughput rate, in bits per second, for the member.', 'If the network traffic volume exceeds this limit, the system marks the member as unavailable.']}, 'packets_limit': {'description': ['Specifies the maximum allowable data transfer rate, in packets per second, for the member.', 'If the network traffic volume exceeds this limit, the system marks the member as unavailable.']}, 'connections_limit': {'description': ['Specifies the maximum number of concurrent connections, combined, for all of the member.', 'If the connections exceed this limit, the system marks the server as unavailable.']}}}",
    "member_order": "{'description': ['Specifies the order in which the member will appear in the pool.', 'The system uses this number with load balancing methods that involve prioritizing pool members, such as the Ratio load balancing method.', 'When creating a new member using this module, if the C(member_order) parameter is not specified, it will default to C(0) (first member in the pool).']}",
    "monitor": "{'description': ['Specifies the monitor assigned to this pool member.', 'Pool members only support a single monitor.', 'If the C(port) of the C(gtm_virtual_server) is C(*), the accepted values of this parameter will be affected.', 'When creating a new pool member, if this parameter is not specified, the default of C(default) will be used.', 'To remove the monitor from the pool member, use the value C(none).', 'For pool members created on different partitions, you can also specify the full path to the Common monitor. For example, C(/Common/tcp).']}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "pool": "{'description': ['Name of the GTM pool.'], 'required': True}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "ratio": "{'description': ['Specifies the weight of the pool member for load balancing purposes.']}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_name": "{'description': ['Specifies the GTM server which contains the C(virtual_server).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['Pool member state. When C(present), ensures that the pool member is created and enabled. When C(absent), ensures that the pool member is removed from the system. When C(enabled) or C(disabled), ensures that the pool member is enabled or disabled (respectively) on the remote device.', 'It is recommended that you use the C(members) parameter of the C(bigip_gtm_pool) module when adding and removing members and it provides an easier way of specifying order. If this is not possible, then the C(state) parameter here should be used.', 'Remember that the order of the members will be affected if you add or remove them using this method. To some extent, this can be controlled using the C(member_order) parameter.'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled']}",
    "type": "{'description': ['The type of GTM pool that the member is in.'], 'choices': ['a', 'aaaa', 'cname', 'mx', 'naptr', 'srv'], 'required': True}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
    "virtual_server": "{'description': ['Specifies the name of the GTM virtual server which is assigned to the specified C(server).'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create a ...
  bigip_gtm_pool_member:
    name: foo
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
