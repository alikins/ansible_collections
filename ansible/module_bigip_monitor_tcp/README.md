# Ansible module: ansible.module_bigip_monitor_tcp


Manages F5 BIG-IP LTM tcp monitors

## Description

M
a
n
a
g
e
s
 
F
5
 
B
I
G
-
I
P
 
L
T
M
 
t
c
p
 
m
o
n
i
t
o
r
s
 
v
i
a
 
i
C
o
n
t
r
o
l
 
S
O
A
P
 
A
P
I
.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['The description of the monitor.'], 'version_added': 2.7}",
    "interval": "{'description': ['The interval specifying how frequently the monitor instance of this template will run. If this parameter is not provided when creating a new monitor, then the default value will be 5. This value B(must) be less than the C(timeout) value.']}",
    "ip": "{'description': ["IP address part of the IP/port definition. If this parameter is not provided when creating a new monitor, then the default value will be '*'.", 'If this value is an IP address, and the C(type) is C(tcp) (the default), then a C(port) number must be specified.']}",
    "name": "{'description': ['Monitor name.'], 'required': True}",
    "parent": "{'description': ['The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the C(tcp) parent on the C(Common) partition.'], 'default': '/Common/tcp'}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common', 'version_added': 2.5}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ["Port address part of the IP/port definition. If this parameter is not provided when creating a new monitor, then the default value will be '*'. Note that if specifying an IP address, a value between 1 and 65535 must be specified", 'This argument is not supported for TCP Echo types.']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "receive": "{'description': ['The receive string for the monitor call.']}",
    "send": "{'description': ['The send string for the monitor call.']}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the monitor exists.', 'When C(absent), ensures the monitor is removed.'], 'default': 'present', 'choices': ['present', 'absent'], 'version_added': 2.5}",
    "time_until_up": "{'description': ['Specifies the amount of time in seconds after the first successful response before a node will be marked up. A value of 0 will cause a node to be marked up immediately after a valid response is received from the node. If this parameter is not provided when creating a new monitor, then the default value will be 0.']}",
    "timeout": "{'description': ['The number of seconds in which the node or service must respond to the monitor request. If the target responds within the set time period, it is considered up. If the target does not respond within the set time period, it is considered down. You can change this number to any number you want, however, it should be 3 times the interval number of seconds plus 1 second. If this parameter is not provided when creating a new monitor, then the default value will be 16.']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create TCP Monitor
  bigip_monitor_tcp:
    state: present
    server: lb.mydomain.com
    user: admin
    password: secret
    name: my_tcp_monitor
    type: tcp
    send: tcp string to send
    receive: tcp string to receive
  delegate_to: localhost

- name: Remove TCP Monitor
  bigip_monitor_tcp:
    state: absent
    server: lb.mydomain.com
    user: admin
    password: secret
    name: my_tcp_monitor
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)', 'Wojciech Wypior (@wojtek0806)']
  - ['Tim Rupp (@caphrim007)', 'Wojciech Wypior (@wojtek0806)']
