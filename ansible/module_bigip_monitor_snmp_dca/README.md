# Ansible module: ansible.module_bigip_monitor_snmp_dca


Manages BIG-IP SNMP data collecting agent (DCA) monitors

## Description

The BIG-IP has an SNMP data collecting agent (DCA) that can query remote SNMP agents of various types, including the UC Davis agent (UCD) and the Windows 2000 Server agent (WIN2000).

## Requirements

TODO

## Arguments

``` json
{
    "agent_type": "{'description': ['Specifies the SNMP agent running on the monitored server. When creating a new monitor, the default is C(UCD) (UC-Davis).'], 'choices': ['UCD', 'WIN2000', 'GENERIC']}",
    "community": "{'description': ['Specifies the community name that the system must use to authenticate with the host server through SNMP. When creating a new monitor, the default value is C(public). Note that this value is case sensitive.']}",
    "cpu_coefficient": "{'description': ['Specifies the coefficient that the system uses to calculate the weight of the CPU threshold in the dynamic ratio load balancing algorithm. When creating a new monitor, the default is C(1.5).']}",
    "cpu_threshold": "{'description': ['Specifies the maximum acceptable CPU usage on the target server. When creating a new monitor, the default is C(80) percent.']}",
    "description": "{'description': ['Specifies descriptive text that identifies the monitor.']}",
    "disk_coefficient": "{'description': ['Specifies the coefficient that the system uses to calculate the weight of the disk threshold in the dynamic ratio load balancing algorithm. When creating a new monitor, the default is C(2.0).']}",
    "disk_threshold": "{'description': ['Specifies the maximum acceptable disk usage on the target server. When creating a new monitor, the default is C(90) percent.']}",
    "interval": "{'description': ['Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown. When creating a new monitor, the default is C(10).']}",
    "memory_coefficient": "{'description': ['Specifies the coefficient that the system uses to calculate the weight of the memory threshold in the dynamic ratio load balancing algorithm. When creating a new monitor, the default is C(1.0).']}",
    "memory_threshold": "{'description': ['Specifies the maximum acceptable memory usage on the target server. When creating a new monitor, the default is C(70) percent.']}",
    "name": "{'description': ['Monitor name.'], 'required': True}",
    "parent": "{'description': ['The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the C(snmp_dca) parent on the C(Common) partition.'], 'default': '/Common/snmp_dca'}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the monitor exists.', 'When C(absent), ensures the monitor is removed.'], 'default': 'present', 'choices': ['present', 'absent'], 'version_added': 2.5}",
    "time_until_up": "{'description': ["Specifies the number of seconds to wait after a resource first responds correctly to the monitor before setting the resource to 'up'. During the interval, all responses from the resource must be correct. When the interval expires, the resource is marked 'up'. A value of 0, means that the resource is marked up immediately upon receipt of the first correct response. When creating a new monitor, the default is C(0)."]}",
    "timeout": "{'description': ["Specifies the number of seconds the target has in which to respond to the monitor request. When creating a new monitor, the default is C(30) seconds. If the target responds within the set time period, it is considered 'up'. If the target does not respond within the set time period, it is considered 'down'. When this value is set to 0 (zero), the system uses the interval from the parent monitor. Note that C(timeout) and C(time_until_up) combine to control when a resource is set to up."]}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
    "version": "{'description': ['Specifies the version of SNMP that the host server uses. When creating a new monitor, the default is C(v1). When C(v1), specifies that the host server uses SNMP version 1. When C(v2c), specifies that the host server uses SNMP version 2c.'], 'choices': ['v1', 'v2c']}",
}
```

## Examples


``` yaml

- name: Create SNMP DCS monitor
  bigip_monitor_snmp_dca:
    state: present
    server: lb.mydomain.com
    user: admin
    password: secret
    name: my_monitor
  delegate_to: localhost

- name: Remove TCP Echo Monitor
  bigip_monitor_snmp_dca:
    state: absent
    server: lb.mydomain.com
    user: admin
    password: secret
    name: my_monitor
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)', 'Wojciech Wypior (@wojtek0806)']
  - ['Tim Rupp (@caphrim007)', 'Wojciech Wypior (@wojtek0806)']
