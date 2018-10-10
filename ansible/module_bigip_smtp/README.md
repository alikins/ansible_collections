# Ansible module: ansible.module_bigip_smtp


Manages SMTP settings on the BIG-IP

## Description

Allows configuring of the BIG-IP to send mail via an SMTP server by configuring the parameters of an SMTP server.

## Requirements

TODO

## Arguments

``` json
{
    "authentication": "{'description': ["Credentials can be set on an SMTP server's configuration even if that authentication is not used (think staging configs or emergency changes). This parameter acts as a switch to make the specified C(smtp_server_username) and C(smtp_server_password) parameters active or not.", 'When C(yes), the authentication parameters will be active.', 'When C(no), the authentication parameters will be inactive.'], 'type': 'bool'}",
    "encryption": "{'description': ['Specifies whether the SMTP server requires an encrypted connection in order to send mail.'], 'choices': ['none', 'ssl', 'tls']}",
    "from_address": "{'description': ['Email address that the email is being sent from. This is the "Reply-to" address that the recipient sees.']}",
    "local_host_name": "{'description': ["Host name used in SMTP headers in the format of a fully qualified domain name. This setting does not refer to the BIG-IP system's hostname."]}",
    "name": "{'description': ['Specifies the name of the SMTP server configuration.'], 'required': True}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "smtp_server": "{'description': ['SMTP server host name in the format of a fully qualified domain name.', 'This value is required when create a new SMTP configuration.']}",
    "smtp_server_password": "{'description': ['Password that the SMTP server requires when validating a user.']}",
    "smtp_server_port": "{'description': ['Specifies the SMTP port number.', 'When creating a new SMTP configuration, the default is C(25) when C(encryption) is C(none) or C(tls). The default is C(465) when C(ssl) is selected.']}",
    "smtp_server_username": "{'description': ['User name that the SMTP server requires when validating a user.']}",
    "state": "{'description': ['When C(present), ensures that the SMTP configuration exists.', 'When C(absent), ensures that the SMTP configuration does not exist.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "update_password": "{'description': ['Passwords are stored encrypted, so the module cannot know if the supplied C(smtp_server_password) is the same or different than the existing password. This parameter controls the updating of the C(smtp_server_password) credential.', 'When C(always), will always update the password.', 'When C(on_create), will only set the password for newly created SMTP server configurations.'], 'default': 'always', 'choices': ['always', 'on_create']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create a base SMTP server configuration
  bigip_smtp:
    name: my-smtp
    smtp_server: 1.1.1.1
    smtp_server_username: mail-admin
    smtp_server_password: mail-secret
    local_host_name: smtp.mydomain.com
    from_address: no-reply@mydomain.com
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
