# Ansible module: ansible.module_bigip_profile_udp


Manage UDP profiles on a BIG-IP

## Description

Manage UDP profiles on a BIG-IP. Many of UDP profiles exist; each with their own adjustments to the standard C(udp) profile. Users of this module should be aware that many of the adjustable knobs have no module default. Instead, the default is assigned by the BIG-IP system itself which, in most cases, is acceptable.

## Requirements

TODO

## Arguments

``` json
{
    "datagram_load_balancing": "{'description': ['Specifies, when C(yes), that the system load balances UDP traffic packet-by-packet.'], 'type': 'bool'}",
    "idle_timeout": "{'description': ['Specifies the length of time that a connection is idle (has no traffic) before the connection is eligible for deletion.', 'When creating a new profile, if this parameter is not specified, the remote device will choose a default value appropriate for the profile, based on its C(parent) profile.', 'When a number is specified, indicates the number of seconds that the UDP connection can remain idle before the system deletes it.', 'When C(0), or C(indefinite), specifies that UDP connections can remain idle indefinitely.', 'When C(immediate), specifies that you do not want the UDP connection to remain idle, and that it is therefore immediately eligible for deletion.']}",
    "name": "{'description': ['Specifies the name of the profile.'], 'required': True}",
    "parent": "{'description': ['Specifies the profile from which this profile inherits settings.', 'When creating a new profile, if this parameter is not specified, the default is the system-supplied C(udp) profile.']}",
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

- name: Create a TCP profile
  bigip_profile_tcp:
    name: foo
    parent: udp
    idle_timeout: 300
    datagram_load_balancing: no
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
