# Ansible module: ansible.module_bigip_profile_oneconnect


Manage OneConnect profiles on a BIG-IP

## Description

Manage OneConnect profiles on a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['Description of the profile.']}",
    "idle_timeout_override": "{'description': ['Specifies the number of seconds that a connection is idle before the connection flow is eligible for deletion.', 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.', 'You may specify a number of seconds for the timeout override.', 'When C(disabled), specifies that there is no timeout override for the connection.', 'When C(indefinite), Specifies that a connection may be idle with no timeout override.']}",
    "limit_type": "{'description': ['When C(none), simultaneous in-flight requests and responses over TCP connections to a pool member are counted toward the limit. This is the historical behavior.', 'When C(idle), idle connections will be dropped as the TCP connection limit is reached. For short intervals, during the overlap of the idle connection being dropped and the new connection being established, the TCP connection limit may be exceeded.', 'When C(strict), the TCP connection limit is honored with no exceptions. This means that idle connections will prevent new TCP connections from being made until they expire, even if they could otherwise be reused.', 'C(strict) is not a recommended configuration except in very special cases with short expiration timeouts.', 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.'], 'choices': ['none', 'idle', 'strict']}",
    "maximum_age": "{'description': ['Specifies the maximum number of seconds allowed for a connection in the connection reuse pool.', 'For any connection with an age higher than this value, the system removes that connection from the re-use pool.', 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.']}",
    "maximum_reuse": "{'description': ['Specifies the maximum number of times that a server-side connection can be reused.', 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.']}",
    "maximum_size": "{'description': ['Specifies the maximum number of connections that the system holds in the connection reuse pool.', 'If the pool is already full, then a server-side connection closes after the response is completed.', 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.']}",
    "name": "{'description': ['Specifies the name of the OneConnect profile.'], 'required': True}",
    "parent": "{'description': ['Specifies the profile from which this profile inherits settings.', 'When creating a new profile, if this parameter is not specified, the default is the system-supplied C(oneconnect) profile.']}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "share_pools": "{'description': ['Indicates that connections may be shared not only within a virtual server, but also among similar virtual servers', 'When C(yes), all virtual servers that use the same OneConnect and other internal network profiles can share connections.', 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.'], 'type': 'bool'}",
    "source_mask": "{'description': ['Specifies a value that the system applies to the source address to determine its eligibility for reuse.', 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.', 'The system applies the value of this setting to the server-side source address to determine its eligibility for reuse.', 'A mask of C(0) causes the system to share reused connections across all source addresses. A host mask of C(32) causes the system to share only those reused connections originating from the same source address.', 'When you are using a SNAT or SNAT pool, the server-side source address is translated first and then the OneConnect mask is applied to the translated address.']}",
    "state": "{'description': ['When C(present), ensures that the profile exists.', 'When C(absent), ensures the profile is removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create a OneConnect profile
  bigip_profile_oneconnect:
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
