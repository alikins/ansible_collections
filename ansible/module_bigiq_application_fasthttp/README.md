# Ansible module: ansible.module_bigiq_application_fasthttp


Manages BIG-IQ FastHTTP applications

## Description

Manages BIG-IQ applications used for load balancing an HTTP-based application, speeding up connections and reducing the number of connections to the back-end server.

## Requirements

TODO

## Arguments

``` json
{
    "add_analytics": "{'description': ['Collects statistics of the BIG-IP that the application is deployed to.', 'This parameter is only relevant when specifying a C(service_environment) which is a BIG-IP; not an SSG.'], 'type': 'bool', 'default': False}",
    "description": "{'description': ['Description of the application.']}",
    "inbound_virtual": "{'description': ['Settings to configure the virtual which will receive the inbound connection.', 'This virtual will be used to host the HTTP endpoint of the application.'], 'suboptions': {'address': {'description': ['Specifies destination IP address information to which the virtual server sends traffic.', 'This parameter is required when creating a new application.'], 'required': True}, 'netmask': {'description': ['Specifies the netmask to associate with the given C(destination).', 'This parameter is required when creating a new application.'], 'required': True}, 'port': {'description': ['The port that the virtual listens for connections on.', 'When creating a new application, if this parameter is not specified, the default value of C(80) will be used.'], 'default': 80}}}",
    "name": "{'description': ['Name of the new application.'], 'required': True}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "servers": "{'description': ['A list of servers that the application is hosted on.', 'If you are familiar with other BIG-IP setting, you might also refer to this list as the list of pool members.', 'When creating a new application, at least one server is required.'], 'suboptions': {'address': {'description': ['The IP address of the server.'], 'required': True}, 'port': {'description': ['The port of the server.', 'When creating a new application and specifying a server, if this parameter is not provided, the default of C(80) will be used.'], 'default': 80}}}",
    "service_environment": "{'description': ['Specifies the name of service environment that the application will be deployed to.', 'When creating a new application, this parameter is required.', 'The service environment type will be discovered by this module automatically. Therefore, it is crucial that you maintain unique names for items in the different service environment types (at this time, SSGs and BIGIPs).']}",
    "state": "{'description': ['The state of the resource on the system.', 'When C(present), guarantees that the resource exists with the provided attributes.', 'When C(absent), removes the resource from the system.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
    "wait": "{'description': ['If the module should wait for the application to be created, deleted or updated.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Load balance an HTTP application on port 80 on BIG-IP
  bigiq_application_fasthttp:
    name: my-app
    description: Fast HTTP
    service_environment: my-ssg
    servers:
      - address: 1.2.3.4
        port: 8080
      - address: 5.6.7.8
        port: 8080
    inbound_virtual:
      name: foo
      address: 2.2.2.2
      netmask: 255.255.255.255
      port: 80
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
    state: present
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
