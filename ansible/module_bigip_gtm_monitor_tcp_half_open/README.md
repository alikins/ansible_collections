# Ansible module: ansible.module_bigip_gtm_monitor_tcp_half_open


Manages F5 BIG-IP GTM tcp half-open monitors

## Description

Manages F5 BIG-IP GTM tcp half-open monitors.

## Requirements

TODO

## Arguments

``` json
{
    "ignore_down_response": "{'description': ['Specifies that the monitor allows more than one probe attempt per interval.', 'When C(yes), specifies that the monitor ignores down responses for the duration of the monitor timeout. Once the monitor timeout is reached without the system receiving an up response, the system marks the object down.', 'When C(no), specifies that the monitor immediately marks an object down when it receives a down response.', 'When creating a new monitor, if this parameter is not provided, then the default value will be C(no).'], 'type': 'bool'}",
    "interval": "{'description': ['Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown.', 'When creating a new monitor, if this parameter is not provided, then the default value will be C(30). This value B(must) be less than the C(timeout) value.']}",
    "ip": "{'description': ["IP address part of the IP/port definition. If this parameter is not provided when creating a new monitor, then the default value will be '*'."]}",
    "name": "{'description': ['Monitor name.'], 'required': True}",
    "parent": "{'description': ['The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the C(tcp_half_open) parent on the C(Common) partition.'], 'default': '/Common/tcp_half_open'}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ["Port address part of the IP/port definition. If this parameter is not provided when creating a new monitor, then the default value will be '*'. Note that if specifying an IP address, a value between 1 and 65535 must be specified"]}",
    "probe_attempts": "{'description': ['Specifies the number of times the system attempts to probe the host server, after which the system considers the host server down or unavailable.', 'When creating a new monitor, if this parameter is not provided, then the default value will be C(3).']}",
    "probe_interval": "{'description': ['Specifies the number of seconds the big3d process waits before sending out a subsequent probe attempt when a probe fails and multiple probe attempts have been requested.', 'When creating a new monitor, if this parameter is not provided, then the default value will be C(1).']}",
    "probe_timeout": "{'description': ['Specifies the number of seconds after which the system times out the probe request to the system.', 'When creating a new monitor, if this parameter is not provided, then the default value will be C(5).']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the monitor exists.', 'When C(absent), ensures the monitor is removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "timeout": "{'description': ['Specifies the number of seconds the target has in which to respond to the monitor request.', 'If the target responds within the set time period, it is considered up.', 'If the target does not respond within the set time period, it is considered down.', 'When this value is set to 0 (zero), the system uses the interval from the parent monitor.', 'When creating a new monitor, if this parameter is not provided, then the default value will be C(120).']}",
    "transparent": "{'description': ['Specifies whether the monitor operates in transparent mode.', 'A monitor in transparent mode directs traffic through the associated pool members or nodes (usually a router or firewall) to the aliased destination (that is, it probes the C(ip)-C(port) combination specified in the monitor).', 'If the monitor cannot successfully reach the aliased destination, the pool member or node through which the monitor traffic was sent is marked down.', 'When creating a new monitor, if this parameter is not provided, then the default value will be C(no).'], 'type': 'bool'}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create TCP half-open Monitor
  bigip_gtm_monitor_tcp_half_open:
    state: present
    ip: 10.10.10.10
    server: lb.mydomain.com
    user: admin
    password: secret
    name: my_monitor
  delegate_to: localhost

- name: Remove TCP half-open Monitor
  bigip_gtm_monitor_tcp_half_open:
    state: absent
    server: lb.mydomain.com
    user: admin
    password: secret
    name: my_monitor
  delegate_to: localhost

- name: Add half-open monitor for all addresses, port 514
  bigip_gtm_monitor_tcp_half_open:
    server: lb.mydomain.com
    user: admin
    port: 514
    password: secret
    name: my_monitor
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
