# Ansible module: ansible.module_bigip_partition


Manage BIG-IP partitions

## Description

Manage BIG-IP partitions.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['The description to attach to the Partition.']}",
    "name": "{'description': ['Name of the partition'], 'required': True}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "route_domain": "{'description': ['The default Route Domain to assign to the Partition. If no route domain is specified, then the default route domain for the system (typically zero) will be used only when creating a new partition.']}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['Whether the partition should exist or not.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create partition "foo" using the default route domain
  bigip_partition:
    name: foo
    password: secret
    server: lb.mydomain.com
    user: admin
  delegate_to: localhost

- name: Create partition "bar" using a custom route domain
  bigip_partition:
    name: bar
    route_domain: 3
    password: secret
    server: lb.mydomain.com
    user: admin
  delegate_to: localhost

- name: Change route domain of partition "foo"
  bigip_partition:
    name: foo
    route_domain: 8
    password: secret
    server: lb.mydomain.com
    user: admin
  delegate_to: localhost

- name: Set a description for partition "foo"
  bigip_partition:
    name: foo
    description: Tenant CompanyA
    password: secret
    server: lb.mydomain.com
    user: admin
  delegate_to: localhost

- name: Delete the "foo" partition
  bigip_partition:
    name: foo
    password: secret
    server: lb.mydomain.com
    user: admin
    state: absent
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
