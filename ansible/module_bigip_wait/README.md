# Ansible module: ansible.module_bigip_wait


Wait for a BIG-IP condition before continuing

## Description

You can wait for BIG-IP to be "ready". By "ready", we mean that BIG-IP is ready to accept configuration.
This module can take into account situations where the device is in the middle of rebooting due to a configuration change.

## Requirements

TODO

## Arguments

``` json
{
    "delay": "{'description': ['Number of seconds to wait before starting to poll.'], 'default': 0}",
    "msg": "{'description': ['This overrides the normal error message from a failure to meet the required conditions.']}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "sleep": "{'default': 1, 'description': ['Number of seconds to sleep between checks, before 2.3 this was hardcoded to 1 second.']}",
    "timeout": "{'description': ['Maximum number of seconds to wait for.', 'When used without other conditions it is equivalent of just sleeping.', 'The default timeout is deliberately set to 2 hours because no individual REST API.'], 'default': 7200}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Wait for BIG-IP to be ready to take configuration
  bigip_wait:
    password: secret
    server: lb.mydomain.com
    user: admin
  delegate_to: localhost

- name: Wait a maximum of 300 seconds for BIG-IP to be ready to take configuration
  bigip_wait:
    timeout: 300
    password: secret
    server: lb.mydomain.com
    user: admin
  delegate_to: localhost

- name: Wait for BIG-IP to be ready, don't start checking for 10 seconds
  bigip_wait:
    delay: 10
    password: secret
    server: lb.mydomain.com
    user: admin
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
