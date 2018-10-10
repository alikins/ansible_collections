# Ansible module: ansible.module_bigip_monitor_dns


Manage DNS monitors on a BIG-IP

## Description

Manages DNS monitors on a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "accept_rcode": "{'description': ['Specifies the RCODE required in the response for an up status.', 'When creating a new monitor, if this parameter is not specified, the default value is C(no-error).', 'When C(no-error), specifies that the status of the node will be marked up if the received DNS message has no error.', 'When C(anything), specifies that the status of the node will be marked up irrespective of the RCODE in the DNS message received.', 'If this parameter is set to C(anything), it will disregard the C(receive) string, and nullify it if the monitor is being updated.'], 'choices': ['no-error', 'anything']}",
    "adaptive": "{'description': ['Specifies whether adaptive response time monitoring is enabled for this monitor.', 'When C(yes), the monitor determines the state of a service based on how divergent from the mean latency a monitor probe for that service is allowed to be. Also, values for the C(allowed_divergence), C(adaptive_limit), and and C(sampling_timespan) will be enforced.', 'When C(disabled), the monitor determines the state of a service based on the C(interval), C(up_interval), C(time_until_up), and C(timeout) monitor settings.'], 'type': 'bool'}",
    "adaptive_limit": "{'description': ['Specifies the absolute number of milliseconds that may not be exceeded by a monitor probe, regardless of C(allowed_divergence) setting, for a probe to be considered successful.', 'This value applies regardless of the value of the C(allowed_divergence) setting.', 'While this value can be configured when C(adaptive) is C(no), it will not take effect on the system until C(adaptive) is C(yes).']}",
    "allowed_divergence_type": "{'description': ['When specifying a new monitor, if C(adaptive) is C(yes), the default is C(relative)', 'When C(absolute), the number of milliseconds the latency of a monitor probe can exceed the mean latency of a monitor probe for the service being probed. In typical cases, if the monitor detects three probes in a row that miss the latency value you set, the pool member or node is marked down.', 'When C(relative), the percentage of deviation the latency of a monitor probe can exceed the mean latency of a monitor probe for the service being probed.'], 'choices': ['relative', 'absolute']}",
    "allowed_divergence_value": "{'description': ['When specifying a new monitor, if C(adaptive) is C(yes), and C(type) is C(relative), the default is C(25) percent.']}",
    "answer_section_contains": "{'description': ['Specifies the type of DNS query that the monitor sends.', 'When creating a new monitor, if this value is not specified, the default value is C(query-type).', 'When C(query-type), specifies that the response should contain at least one answer of which the resource record type matches the query type.', 'When C(any-type), specifies that the DNS message should contain at least one answer.', 'When C(anything), specifies that an empty answer is enough to mark the status of the node up.'], 'choices': ['any-type', 'anything', 'query-type']}",
    "description": "{'description': ['The description of the monitor.']}",
    "interval": "{'description': ['The interval specifying how frequently the monitor instance of this template will run.', 'This value B(must) be less than the C(timeout) value.', 'When creating a new monitor, if this parameter is not provided, the default C(5) will be used.']}",
    "ip": "{'description': ['IP address part of the IP/port definition.', 'If this parameter is not provided when creating a new monitor, then the default value will be C(*).']}",
    "manual_resume": "{'description': ['Specifies whether the system automatically changes the status of a resource to B(enabled) at the next successful monitor check.', 'If you set this option to C(yes), you must manually re-enable the resource before the system can use it for load balancing connections.', 'When creating a new monitor, if this parameter is not specified, the default value is C(no).', 'When C(yes), specifies that you must manually re-enable the resource after an unsuccessful monitor check.', 'When C(no), specifies that the system automatically changes the status of a resource to B(enabled) at the next successful monitor check.'], 'type': 'bool'}",
    "name": "{'description': ['Specifies the name of the monitor.'], 'required': True}",
    "parent": "{'description': ['The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the C(dns) parent on the C(Common) partition.'], 'default': '/Common/dns'}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['Port address part of the IP/port definition.', 'If this parameter is not provided when creating a new monitor, then the default value will be C(*).', 'Note that if specifying an IP address, a value between 1 and 65535 must be specified.']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "query_name": "{'description': ['Specifies a query name for the monitor to use in a DNS query.']}",
    "query_type": "{'description': ['Specifies the type of DNS query that the monitor sends.', 'When creating a new monitor, if this parameter is not specified, the default value is C(a).', 'When C(a), specifies that the monitor will send a DNS query of type A.', 'When C(aaaa), specifies that the monitor will send a DNS query of type AAAA.'], 'choices': ['a', 'aaaa']}",
    "receive": "{'description': ['Specifies the IP address that the monitor uses from the resource record sections of the DNS response.', 'The IP address should be specified in the dotted-decimal notation or IPv6 notation.']}",
    "reverse": "{'description': ['Specifies whether the monitor operates in reverse mode.', 'When the monitor is in reverse mode, a successful receive string match marks the monitored object down instead of up. You can use the this mode only if you configure the C(receive) option.', 'This parameter is not compatible with the C(time_until_up) parameter. If C(time_until_up) is specified, it must be C(0). Or, if it already exists, it must be C(0).'], 'type': 'bool'}",
    "sampling_timespan": "{'description': ['Specifies the length, in seconds, of the probe history window that the system uses to calculate the mean latency and standard deviation of a monitor probe.', 'While this value can be configured when C(adaptive) is C(no), it will not take effect on the system until C(adaptive) is C(yes).']}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the monitor exists.', 'When C(absent), ensures the monitor is removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "time_until_up": "{'description': ['Specifies the amount of time in seconds after the first successful response before a node will be marked up.', 'A value of 0 will cause a node to be marked up immediately after a valid response is received from the node.', 'If this parameter is not provided when creating a new monitor, then the default value will be C(0).']}",
    "timeout": "{'description': ['The number of seconds in which the node or service must respond to the monitor request.', 'If the target responds within the set time period, it is considered up.', 'If the target does not respond within the set time period, it is considered down.', 'You can change this number to any number you want, however, it should be 3 times the interval number of seconds plus 1 second.', 'If this parameter is not provided when creating a new monitor, then the default value will be C(16).']}",
    "transparent": "{'description': ['Specifies whether the monitor operates in transparent mode.', 'Monitors in transparent mode can monitor pool members through firewalls.', 'When creating a new monitor, if this parameter is not provided, then the default value will be C(no).'], 'type': 'bool'}",
    "up_interval": "{'description': ['Specifies the interval for the system to use to perform the health check when a resource is up.', 'When C(0), specifies that the system uses the interval specified in C(interval) to check the health of the resource.', 'When any other number, enables specification of a different interval to use when checking the health of a resource that is up.', 'When creating a new monitor, if this parameter is not provided, the default C(0) will be used.']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create a DNS monitor
  bigip_monitor_dns:
    name: DNS-UDP-V6
    interval: 2
    query_name: localhost
    query_type: aaaa
    up_interval: 5
    adaptive: no
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)', 'Wojciech Wypior (@wojtek0806)']
  - ['Tim Rupp (@caphrim007)', 'Wojciech Wypior (@wojtek0806)']
