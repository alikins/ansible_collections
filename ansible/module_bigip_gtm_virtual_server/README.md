# Ansible module: ansible.module_bigip_gtm_virtual_server


Manages F5 BIG-IP GTM virtual servers

## Description

Manages F5 BIG-IP GTM virtual servers. A GTM server can have many virtual servers associated with it. They are arranged in much the same way that pool members are to pools.

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['Specifies the IP Address of the virtual server.', 'When creating a new GTM virtual server, this parameter is required.'], 'version_added': 2.6}",
    "availability_requirements": "{'description': ['Specifies, if you activate more than one health monitor, the number of health monitors that must receive successful responses in order for the link to be considered available.'], 'suboptions': {'type': {'description': ['Monitor rule type when C(monitors) is specified.', "When creating a new virtual, if this value is not specified, the default of 'all' will be used."], 'choices': ['all', 'at_least', 'require']}, 'at_least': {'description': ['Specifies the minimum number of active health monitors that must be successful before the link is considered up.', 'This parameter is only relevant when a C(type) of C(at_least) is used.', 'This parameter will be ignored if a type of either C(all) or C(require) is used.']}, 'number_of_probes': {'description': ['Specifies the minimum number of probes that must succeed for this server to be declared up.', 'When creating a new virtual server, if this parameter is specified, then the C(number_of_probers) parameter must also be specified.', 'The value of this parameter should always be B(lower) than, or B(equal to), the value of C(number_of_probers).', 'This parameter is only relevant when a C(type) of C(require) is used.', 'This parameter will be ignored if a type of either C(all) or C(at_least) is used.']}, 'number_of_probers': {'description': ['Specifies the number of probers that should be used when running probes.', 'When creating a new virtual server, if this parameter is specified, then the C(number_of_probes) parameter must also be specified.', 'The value of this parameter should always be B(higher) than, or B(equal to), the value of C(number_of_probers).', 'This parameter is only relevant when a C(type) of C(require) is used.', 'This parameter will be ignored if a type of either C(all) or C(at_least) is used.']}}, 'version_added': 2.6}",
    "limits": "{'description': ['Specifies resource thresholds or limit requirements at the server level.', 'When you enable one or more limit settings, the system then uses that data to take servers in and out of service.', 'You can define limits for any or all of the limit settings. However, when a server does not meet the resource threshold limit requirement, the system marks the entire server as unavailable and directs load-balancing traffic to another resource.', 'The limit settings available depend on the type of server.'], 'suboptions': {'bits_enabled': {'description': ['Whether the bits limit is enabled or not.', 'This parameter allows you to switch on or off the effect of the limit.'], 'type': 'bool'}, 'packets_enabled': {'description': ['Whether the packets limit is enabled or not.', 'This parameter allows you to switch on or off the effect of the limit.'], 'type': 'bool'}, 'connections_enabled': {'description': ['Whether the current connections limit is enabled or not.', 'This parameter allows you to switch on or off the effect of the limit.'], 'type': 'bool'}, 'bits_limit': {'description': ['Specifies the maximum allowable data throughput rate, in bits per second, for the virtual servers on the server.', 'If the network traffic volume exceeds this limit, the system marks the server as unavailable.']}, 'packets_limit': {'description': ['Specifies the maximum allowable data transfer rate, in packets per second, for the virtual servers on the server.', 'If the network traffic volume exceeds this limit, the system marks the server as unavailable.']}, 'connections_limit': {'description': ['Specifies the maximum number of concurrent connections, combined, for all of the virtual servers on the server.', 'If the connections exceed this limit, the system marks the server as unavailable.']}}, 'version_added': 2.6}",
    "link": "{'description': ['Specifies a link to assign to the server or virtual server.'], 'version_added': 2.6}",
    "monitors": "{'description': ['Specifies the health monitors that the system currently uses to monitor this resource.', 'When C(availability_requirements.type) is C(require), you may only have a single monitor in the C(monitors) list.'], 'version_added': 2.6}",
    "name": "{'description': ['Specifies the name of the virtual server.'], 'version_added': 2.6}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common', 'version_added': 2.6}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['Specifies the service port number for the virtual server or pool member. For example, the HTTP service is typically port 80.', 'To specify all ports, use an C(*).', 'When creating a new GTM virtual server, if this parameter is not specified, a default of C(*) will be used.']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_name": "{'description': ['Specifies the name of the server that the virtual server is associated with.'], 'version_added': 2.6}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the resource exists.', 'When C(absent), ensures the resource is removed.'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled']}",
    "translation_address": "{'description': ['Specifies the translation IP address for the virtual server.', 'To unset this parameter, provide an empty string (C("")) as a value.', 'When creating a new GTM virtual server, if this parameter is not specified, a default of C(::) will be used.'], 'version_added': 2.6}",
    "translation_port": "{'description': ['Specifies the translation port number or service name for the virtual server.', 'To specify all ports, use an C(*).', 'When creating a new GTM virtual server, if this parameter is not specified, a default of C(*) will be used.'], 'version_added': 2.6}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
    "virtual_server_dependencies": "{'description': ['Specifies the virtual servers on which the current virtual server depends.', 'If any of the specified servers are unavailable, the current virtual server is also listed as unavailable.'], 'suboptions': {'server': {'description': ['Server which the dependant virtual server is part of.'], 'required': True}, 'virtual_server': {'description': ['Virtual server to depend on.'], 'required': True}}, 'version_added': 2.6}",
}
```

## Examples


``` yaml

- name: Enable virtual server
  bigip_gtm_virtual_server:
    server: lb.mydomain.com
    user: admin
    password: secret
    server_name: server1
    name: my-virtual-server
    state: enabled
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
