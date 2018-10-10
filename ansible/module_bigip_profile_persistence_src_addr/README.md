# Ansible module: ansible.module_bigip_profile_persistence_src_addr


Manage source address persistence profiles

## Description

Manages source address persistence profiles.

## Requirements

TODO

## Arguments

``` json
{
    "entry_timeout": "{'description': ['Specifies the duration of the persistence entries.', 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.', 'To specify an indefinite timeout, use the value C(indefinite).', 'If specifying a numeric timeout, the value must be between C(1) and C(4294967295).']}",
    "hash_algorithm": "{'description': ['Specifies the algorithm the system uses for hash persistence load balancing. The hash result is the input for the algorithm.', 'When C(default), specifies that the system uses the index of pool members to obtain the hash result for the input to the algorithm.', 'When C(carp), specifies that the system uses the Cache Array Routing Protocol (CARP) to obtain the hash result for the input to the algorithm.', 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.'], 'choices': ['default', 'carp']}",
    "match_across_pools": "{'description': ['When C(yes), specifies that the system can use any pool that contains this persistence record.', 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.'], 'type': 'bool'}",
    "match_across_services": "{'description': ['When C(yes), specifies that all persistent connections from a client IP address that go to the same virtual IP address also go to the same node.', 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.'], 'type': 'bool'}",
    "match_across_virtuals": "{'description': ['When C(yes), specifies that all persistent connections from the same client IP address go to the same node.', 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.'], 'type': 'bool'}",
    "name": "{'description': ['Specifies the name of the profile.'], 'required': True}",
    "override_connection_limit": "{'description': ['When C(yes), specifies that the system allows you to specify that pool member connection limits will be overridden for persisted clients.', 'Per-virtual connection limits remain hard limits and are not overridden.'], 'type': 'bool'}",
    "parent": "{'description': ['Specifies the profile from which this profile inherits settings.', 'When creating a new profile, if this parameter is not specified, the default is the system-supplied C(source_addr) profile.']}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the profile exists.', 'When C(absent), ensures the profile is removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create a profile
  bigip_profile_persistence_src_addr:
    name: foo
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
    hash_algorithm: carp
    match_across_services: yes
    match_across_virtuals: yes
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
