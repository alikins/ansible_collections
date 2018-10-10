# Ansible module: ansible.module_bigip_device_sshd


Manage the SSHD settings of a BIG-IP

## Description

Manage the SSHD settings of a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "allow": "{'description': ['Specifies, if you have enabled SSH access, the IP address or address range for other systems that can use SSH to communicate with this system.', 'To specify all addresses, use the value C(all).', 'IP address can be specified, such as 172.27.1.10.', 'IP rangees can be specified, such as 172.27.*.* or 172.27.0.0/255.255.0.0.']}",
    "banner": "{'description': ['Whether to enable the banner or not.'], 'choices': ['enabled', 'disabled']}",
    "banner_text": "{'description': ['Specifies the text to include on the pre-login banner that displays when a user attempts to login to the system using SSH.']}",
    "inactivity_timeout": "{'description': ['Specifies the number of seconds before inactivity causes an SSH session to log out.']}",
    "log_level": "{'description': ['Specifies the minimum SSHD message level to include in the system log.'], 'choices': ['debug', 'debug1', 'debug2', 'debug3', 'error', 'fatal', 'info', 'quiet', 'verbose']}",
    "login": "{'description': ['Specifies, when checked C(enabled), that the system accepts SSH communications.'], 'choices': ['enabled', 'disabled']}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['Port that you want the SSH daemon to run on.']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Set the banner for the SSHD service from a string
  bigip_device_sshd:
    banner: enabled
    banner_text: banner text goes here
    password: secret
    server: lb.mydomain.com
    user: admin
  delegate_to: localhost

- name: Set the banner for the SSHD service from a file
  bigip_device_sshd:
    banner: enabled
    banner_text: "{{ lookup('file', '/path/to/file') }}"
    password: secret
    server: lb.mydomain.com
    user: admin
  delegate_to: localhost

- name: Set the SSHD service to run on port 2222
  bigip_device_sshd:
    password: secret
    port: 2222
    server: lb.mydomain.com
    user: admin
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
