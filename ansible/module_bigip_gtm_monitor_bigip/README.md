# Ansible module: ansible.module_bigip_gtm_monitor_bigip


Manages F5 BIG-IP GTM BIG-IP monitors

## Description

Manages F5 BIG-IP GTM BIG-IP monitors. This monitor is used by GTM to monitor BIG-IPs themselves.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate_dynamic_ratios": "{'description': ['Specifies how the system combines the module values to create the proportion (score) for the load balancing operation.', "The score represents the module's estimated capacity for handing traffic.", 'Averaged values are appropriate for downstream Web Accelerator or Application Security Manager virtual servers.', 'When creating a new monitor, if this parameter is not specified, the default of C(none) is used, meaning that the system does not use the scores in the load balancing operation.', 'When C(none), specifies that the monitor ignores the nodes and pool member scores.', "When C(average-nodes), specifies that the system averages the dynamic ratios on the nodes associated with the monitor's target virtual servers and returns that average as the virtual servers' score.", "When C(sum-nodes), specifies that the system adds together the scores of the nodes associated with the monitor's target virtual servers and uses that value in the load balancing operation.", "When C(average-members), specifies that the system averages the dynamic ratios on the pool members associated with the monitor's target virtual servers and returns that average as the virtual servers' score.", "When C(sum-members), specifies that the system adds together the scores of the pool members associated with the monitor's target virtual servers and uses that value in the load balancing operation."], 'choices': ['none', 'average-nodes', 'sum-nodes', 'average-members', 'sum-members']}",
    "ignore_down_response": "{'description': ['Specifies that the monitor allows more than one probe attempt per interval.', 'When C(yes), specifies that the monitor ignores down responses for the duration of the monitor timeout. Once the monitor timeout is reached without the system receiving an up response, the system marks the object down.', 'When C(no), specifies that the monitor immediately marks an object down when it receives a down response.', 'When creating a new monitor, if this parameter is not provided, then the default value will be C(no).'], 'type': 'bool'}",
    "interval": "{'description': ['Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown.', 'When creating a new monitor, if this parameter is not provided, then the default value will be C(30). This value B(must) be less than the C(timeout) value.']}",
    "ip": "{'description': ["IP address part of the IP/port definition. If this parameter is not provided when creating a new monitor, then the default value will be '*'."]}",
    "name": "{'description': ['Monitor name.'], 'required': True}",
    "parent": "{'description': ['The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the C(bigip) parent on the C(Common) partition.'], 'default': '/Common/bigip'}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ["Port address part of the IP/port definition. If this parameter is not provided when creating a new monitor, then the default value will be '*'. Note that if specifying an IP address, a value between 1 and 65535 must be specified"]}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the monitor exists.', 'When C(absent), ensures the monitor is removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "timeout": "{'description': ['Specifies the number of seconds the target has in which to respond to the monitor request.', 'If the target responds within the set time period, it is considered up.', 'If the target does not respond within the set time period, it is considered down.', 'When this value is set to 0 (zero), the system uses the interval from the parent monitor.', 'When creating a new monitor, if this parameter is not provided, then the default value will be C(90).']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create BIG-IP Monitor
  bigip_gtm_monitor_bigip:
    state: present
    ip: 10.10.10.10
    server: lb.mydomain.com
    user: admin
    password: secret
    name: my_monitor
  delegate_to: localhost

- name: Remove BIG-IP Monitor
  bigip_gtm_monitor_bigip:
    state: absent
    server: lb.mydomain.com
    user: admin
    password: secret
    name: my_monitor
  delegate_to: localhost

- name: Add BIG-IP monitor for all addresses, port 514
  bigip_gtm_monitor_bigip:
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
