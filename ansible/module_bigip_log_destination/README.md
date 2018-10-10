# Ansible module: ansible.module_bigip_log_destination


Manages log destinations on a BIG-IP

## Description

Manages log destinations on a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['The description of the log destination.']}",
    "name": "{'description': ['Specifies the name of the log destination.'], 'required': True}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "pool_settings": "{'description': ['This parameter is only available when C(type) is C(remote-high-speed-log).'], 'suboptions': {'pool': {'description': ['Specifies the existing pool of remote high-speed log servers where logs will be sent.', 'When creating a new destination (and C(type) is C(remote-high-speed-log)), this parameter is required.']}, 'protocol': {'description': ['Specifies the protocol for the system to use to send logs to the pool of remote high-speed log servers, where the logs are stored.', 'When creating a new log destination (and C(type) is C(remote-high-speed-log)), if this parameter is not specified, the default is C(tcp).'], 'choices': ['tcp', 'udp']}, 'distribution': {'description': ['Specifies the distribution method used by the Remote High Speed Log destination to send messages to pool members.', 'When C(adaptive), connections to pool members will be added as required to provide enough logging bandwidth. This can have the undesirable effect of logs accumulating on only one pool member when it provides sufficient logging bandwidth on its own.', "When C(balanced), sends each successive log to a new pool member, balancing the logs among them according to the pool's load balancing method.", 'When C(replicated), replicates each log to all pool members, for redundancy.', 'When creating a new log destination (and C(type) is C(remote-high-speed-log)), if this parameter is not specified, the default is C(adaptive).'], 'choices': ['adaptive', 'balanced', 'replicated']}}}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the resource exists.', 'When C(absent), ensures the resource is removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "syslog_settings": "{'description': ['This parameter is only available when C(type) is C(remote-syslog).'], 'suboptions': {'syslog_format': {'description': ['Specifies the method to use to format the logs associated with the remote Syslog log destination.', 'When creating a new log destination (and C(type) is C(remote-syslog)), if this parameter is not specified, the default is C(bsd-syslog).', 'The C(syslog) and C(rfc5424) choices are two ways of saying the same thing.', 'The C(bsd-syslog) and C(rfc3164) choices are two ways of saying the same thing.'], 'choices': ['bsd-syslog', 'syslog', 'legacy-bigip', 'rfc5424', 'rfc3164']}, 'forward_to': {'description': ['Specifies the management port log destination, which will be used to forward the logs to a single log server, or a remote high-speed log destination, which will be used to forward the logs to a pool of remote log servers.', 'When creating a new log destination (and C(type) is C(remote-syslog)), this parameter is required.']}}}",
    "type": "{'description': ['Specifies the type of log destination.', 'Once created, this parameter cannot be changed.'], 'choices': ['remote-high-speed-log', 'remote-syslog'], 'required': True}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create a high-speed logging destination
  bigip_log_destination:
    name: foo
    type: remote-high-speed-log
    pool_settings:
      pool: my-ltm-pool
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Create a remote-syslog logging destination
  bigip_log_destination:
    name: foo
    type: remote-syslog
    syslog_settings:
      syslog_format: rfc5424
      forward_to: my-destination
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
