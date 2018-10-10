# Ansible module: ansible.module_bigip_gtm_monitor_https


Manages F5 BIG-IP GTM https monitors

## Description

Manages F5 BIG-IP GTM https monitors.

## Requirements

TODO

## Arguments

``` json
{
    "cipher_list": "{'description': ['Specifies the list of ciphers for this monitor.', 'The items in the cipher list are separated with the colon C(:) symbol.', 'When creating a new monitor, if this parameter is not specified, the default list is C(DEFAULT:+SHA:+3DES:+kEDH).']}",
    "client_cert": "{'description': ['Specifies a fully-qualified path for a client certificate that the monitor sends to the target SSL server.']}",
    "client_key": "{'description': ['Specifies a key for a client certificate that the monitor sends to the target SSL server.']}",
    "compatibility": "{'description': ['Specifies, when enabled, that the SSL options setting (in OpenSSL) is set to B(all).', 'When creating a new monitor, if this value is not specified, the default is C(yes)'], 'type': 'bool'}",
    "ignore_down_response": "{'description': ['Specifies that the monitor allows more than one probe attempt per interval.', 'When C(yes), specifies that the monitor ignores down responses for the duration of the monitor timeout. Once the monitor timeout is reached without the system receiving an up response, the system marks the object down.', 'When C(no), specifies that the monitor immediately marks an object down when it receives a down response.', 'When creating a new monitor, if this parameter is not provided, then the default value will be C(no).'], 'type': 'bool'}",
    "interval": "{'description': ['The interval specifying how frequently the monitor instance of this template will run.', 'If this parameter is not provided when creating a new monitor, then the default value will be 30.', 'This value B(must) be less than the C(timeout) value.']}",
    "ip": "{'description': ["IP address part of the IP/port definition. If this parameter is not provided when creating a new monitor, then the default value will be '*'.", 'If this value is an IP address, then a C(port) number must be specified.']}",
    "name": "{'description': ['Monitor name.'], 'required': True}",
    "parent": "{'description': ['The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the C(tcp) parent on the C(Common) partition.'], 'default': '/Common/https'}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ["Port address part of the IP/port definition. If this parameter is not provided when creating a new monitor, then the default value will be '*'. Note that if specifying an IP address, a value between 1 and 65535 must be specified."]}",
    "probe_timeout": "{'description': ['Specifies the number of seconds after which the system times out the probe request to the system.', 'When creating a new monitor, if this parameter is not provided, then the default value will be C(5).']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "receive": "{'description': ['The receive string for the monitor call.']}",
    "reverse": "{'description': ['Instructs the system to mark the target resource down when the test is successful. This setting is useful, for example, if the content on your web site home page is dynamic and changes frequently, you may want to set up a reverse ECV service check that looks for the string Error.', 'A match for this string means that the web server was down.', 'To use this option, you must specify values for C(send) and C(receive).'], 'type': 'bool'}",
    "send": "{'description': ['The send string for the monitor call.', 'When creating a new monitor, if this parameter is not provided, the default of C(GET /\\r\\n) will be used.']}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the monitor exists.', 'When C(absent), ensures the monitor is removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "target_password": "{'description': ['Specifies the password, if the monitored target requires authentication.']}",
    "target_username": "{'description': ['Specifies the user name, if the monitored target requires authentication.']}",
    "timeout": "{'description': ['The number of seconds in which the node or service must respond to the monitor request. If the target responds within the set time period, it is considered up. If the target does not respond within the set time period, it is considered down. You can change this number to any number you want, however, it should be 3 times the interval number of seconds plus 1 second.', 'If this parameter is not provided when creating a new monitor, then the default value will be 120.']}",
    "transparent": "{'description': ['Specifies whether the monitor operates in transparent mode.', 'A monitor in transparent mode directs traffic through the associated pool members or nodes (usually a router or firewall) to the aliased destination (that is, it probes the C(ip)-C(port) combination specified in the monitor).', 'If the monitor cannot successfully reach the aliased destination, the pool member or node through which the monitor traffic was sent is marked down.', 'When creating a new monitor, if this parameter is not provided, then the default value will be C(no).'], 'type': 'bool'}",
    "update_password": "{'description': ['C(always) will update passwords if the C(target_password) is specified.', 'C(on_create) will only set the password for newly created monitors.'], 'default': 'always', 'choices': ['always', 'on_create']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create a GTM HTTPS monitor
  bigip_gtm_monitor_https:
    name: my_monitor
    ip: 1.1.1.1
    port: 80
    send: my send string
    receive: my receive string
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Remove HTTPS Monitor
  bigip_gtm_monitor_https:
    name: my_monitor
    state: absent
    server: lb.mydomain.com
    user: admin
    password: secret
  delegate_to: localhost

- name: Add HTTPS monitor for all addresses, port 514
  bigip_gtm_monitor_https:
    name: my_monitor
    server: lb.mydomain.com
    user: admin
    port: 514
    password: secret
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
