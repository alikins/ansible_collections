# Ansible module: ansible.module_bigip_device_auth


Manage system authentication on a BIG-IP

## Description

Manage the system authentication configuration. This module can assist in configuring a number of different system authentication types. Note that this module can not be used to configure APM authentication types.

## Requirements

TODO

## Arguments

``` json
{
    "authentication": "{'description': ['Specifies the process the system employs when sending authentication requests.', 'When C(use-first-server), specifies that the system sends authentication attempts to only the first server in the list.', 'When C(use-all-servers), specifies that the system sends an authentication request to each server until authentication succeeds, or until the system has sent a request to all servers in the list.', 'This parameter is supported by the C(tacacs) type.'], 'choices': ['use-first-server', 'use-all-servers']}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "protocol_name": "{'description': ['Specifies the protocol associated with the value specified in C(service_name), which is a subset of the associated service being used for client authorization or system accounting.', 'Note that the majority of TACACS+ implementations are of protocol type C(ip), so try that first.'], 'choices': ['lcp', 'ip', 'ipx', 'atalk', 'vines', 'lat', 'xremote', 'tn3270', 'telnet', 'rlogin', 'pad', 'vpdn', 'ftp', 'http', 'deccp', 'osicp', 'unknown']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "secret": "{'description': ['Secret key used to encrypt and decrypt packets sent or received from the server.', 'B(Do not) use the pound/hash sign in the secret for TACACS+ servers.', 'When configuring TACACS+ auth for the first time, this value is required.']}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "servers": "{'description': ['Specifies a list of the IPv4 addresses for servers using the Terminal Access Controller Access System (TACACS)+ protocol with which the system communicates to obtain authorization data.', 'For each address, an alternate TCP port number may be optionally specified by specifying the C(port) key.', 'If no port number is specified, the default port C(49163) is used.', 'This parameter is supported by the C(tacacs) type.'], 'suboptions': {'address': {'description': ['The IP address of the server.', 'This field is required, unless you are specifying a simple list of servers. In that case, the simple list can specify server IPs. See examples for more clarification.']}, 'port': {'description': ['The port of the server.'], 'default': 49163}}}",
    "service_name": "{'description': ['Specifies the name of the service that the user is requesting to be authorized to use.', 'Identifying what the user is asking to be authorized for, enables the TACACS+ server to behave differently for different types of authorization requests.', 'When configuring this form of system authentication, this setting is required.', 'Note that the majority of TACACS+ implementations are of service type C(ppp), so try that first.'], 'choices': ['slip', 'ppp', 'arap', 'shell', 'tty-daemon', 'connection', 'system', 'firewall']}",
    "state": "{'description': ['The state of the authentication configuration on the system.', 'When C(present), guarantees that the system is configured for the specified C(type).', 'When C(absent), sets the system auth source back to C(local).'], 'default': 'present', 'choices': ['absent', 'present']}",
    "type": "{'description': ['The authentication type to manage with this module.', 'Take special note that the parameters supported by this module will vary depending on the C(type) that you are configuring.', 'This module only supports a subset, at this time, of the total available auth types.'], 'choices': ['tacacs', 'local']}",
    "update_secret": "{'description': ['C(always) will allow to update secrets if the user chooses to do so.', 'C(on_create) will only set the secret when a C(use_auth_source) is C(yes) and TACACS+ is not currently the auth source.'], 'default': 'always', 'choices': ['always', 'on_create']}",
    "use_for_auth": "{'description': ['Specifies whether or not this auth source is put in use on the system.'], 'type': 'bool'}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Set the system auth to TACACS+, default server port
  bigip_device_auth:
    type: tacacs
    authentication: use-all-servers
    protocol_name: ip
    secret: secret
    servers:
      - 10.10.10.10
      - 10.10.10.11
    service_name: ppp
    state: present
    use_for_auth: yes
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Set the system auth to TACACS+, override server port
  bigip_device_auth:
    type: tacacs
    authentication: use-all-servers
    protocol_name: ip
    secret: secret
    servers:
      - address: 10.10.10.10
        port: 1234
      - 10.10.10.11
    service_name: ppp
    use_for_auth: yes
    state: present
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
