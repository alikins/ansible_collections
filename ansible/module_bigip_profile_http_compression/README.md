# Ansible module: ansible.module_bigip_profile_http_compression


Manage HTTP compression profiles on a BIG-IP

## Description

Manage HTTP compression profiles on a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "buffer_size": "{'description': ['Maximum number of compressed bytes that the system buffers before inserting a Content-Length header (which specifies the compressed size) into the response.', 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.']}",
    "description": "{'description': ['Description of the HTTP compression profile.']}",
    "gzip_level": "{'description': ['Specifies the degree to which the system compresses the content.', 'Higher compression levels cause the compression process to be slower.', 'Valid values are between 1 (least compression and fastest) to 9 (most compression and slowest).'], 'choices': [1, 2, 3, 4, 5, 6, 7, 8, 9]}",
    "gzip_memory_level": "{'description': ['Number of kilobytes of memory that the system uses for internal compression buffers when compressing a server response.'], 'choices': [1, 2, 4, 8, 16, 32, 64, 128, 256]}",
    "gzip_window_size": "{'description': ['Number of kilobytes in the window size that the system uses when compressing a server response.'], 'choices': [1, 2, 4, 8, 16, 32, 64, 128]}",
    "name": "{'description': ['Specifies the name of the compression profile.'], 'required': True}",
    "parent": "{'description': ['Specifies the profile from which this profile inherits settings.', 'When creating a new profile, if this parameter is not specified, the default is the system-supplied C(httpcompression) profile.']}",
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

- name: Create an HTTP compression profile
  bigip_profile_http_compression:
    name: profile1
    description: Custom HTTP Compression Profile
    buffer_size: 131072
    gzip_level: 6
    gzip_memory_level: 16k
    gzip_window_size: 64k
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
