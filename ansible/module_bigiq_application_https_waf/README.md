# Ansible module: ansible.module_bigiq_application_https_waf


Manages BIG-IQ HTTPS WAF applications

## Description

Manages BIG-IQ applications used for load balancing an HTTPS application on port 443 with a Web Application Firewall (WAF) using an ASM Rapid Deployment policy.

## Requirements

TODO

## Arguments

``` json
{
    "add_analytics": "{'description': ['Collects statistics of the BIG-IP that the application is deployed to.', 'This parameter is only relevant when specifying a C(service_environment) which is a BIG-IP; not an SSG.'], 'type': 'bool', 'default': False}",
    "client_ssl_profile": "{'description': ['Specifies the SSL profile for managing client-side SSL traffic.'], 'suboptions': {'name': {'description': ['The name of the client SSL profile to created and used.', 'When creating a new application, if this value is not specified, the default value of C(clientssl) will be used.']}, 'cert_key_chain': {'description': ['One or more certificates and keys to associate with the SSL profile.', 'This option is always a list. The keys in the list dictate the details of the client/key/chain/passphrase combination.', 'Note that BIG-IPs can only have one of each type of each certificate/key type. This means that you can only have one RSA, one DSA, and one ECDSA per profile.', 'If you attempt to assign two RSA, DSA, or ECDSA certificate/key combo, the device will reject this.', 'This list is a complex list that specifies a number of keys.', 'When creating a new profile, if this parameter is not specified, the default value of C(inherit) will be used.'], 'suboptions': {'cert': {'description': ['Specifies a cert name for use.'], 'required': True}, 'key': {'description': ['Specifies a key name.'], 'required': True}, 'chain': {'description': ['Specifies a certificate chain that is relevant to the certificate and key mentioned earlier.', 'This key is optional.']}, 'passphrase': {'description': ['Contains the passphrase of the key file, should it require one.', 'Passphrases are encrypted on the remote BIG-IP device.']}}}}}",
    "description": "{'description': ['Description of the application.']}",
    "domain_names": "{'description': ['Specifies host names that are used to access the web application that this security policy protects.', 'When creating a new application, this parameter is required.']}",
    "inbound_virtual": "{'description': ['Settings to configure the virtual which will receive the inbound connection.', 'This virtual will be used to host the HTTPS endpoint of the application.', 'Traffic destined to the C(redirect_virtual) will be offloaded to this parameter to ensure that proper redirection from insecure, to secure, occurs.'], 'suboptions': {'address': {'description': ['Specifies destination IP address information to which the virtual server sends traffic.', 'This parameter is required when creating a new application.']}, 'netmask': {'description': ['Specifies the netmask to associate with the given C(destination).', 'This parameter is required when creating a new application.']}, 'port': {'description': ['The port that the virtual listens for connections on.', 'When creating a new application, if this parameter is not specified, the default value of C(443) will be used.'], 'default': 443}}}",
    "name": "{'description': ['Name of the new application.'], 'required': True}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "redirect_virtual": "{'description': ['Settings to configure the virtual which will receive the connection to be redirected.', 'This virtual will be used to host the HTTP endpoint of the application.', 'Traffic destined to this parameter will be offloaded to the C(inbound_virtual) parameter to ensure that proper redirection from insecure, to secure, occurs.'], 'suboptions': {'address': {'description': ['Specifies destination IP address information to which the virtual server sends traffic.', 'This parameter is required when creating a new application.']}, 'netmask': {'description': ['Specifies the netmask to associate with the given C(destination).', 'This parameter is required when creating a new application.']}, 'port': {'description': ['The port that the virtual listens for connections on.', 'When creating a new application, if this parameter is not specified, the default value of C(80) will be used.'], 'default': 80}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "servers": "{'description': ['A list of servers that the application is hosted on.', 'If you are familiar with other BIG-IP setting, you might also refer to this list as the list of pool members.', 'When creating a new application, at least one server is required.'], 'suboptions': {'address': {'description': ['The IP address of the server.']}, 'port': {'description': ['The port of the server.'], 'default': 80}}}",
    "service_environment": "{'description': ['Specifies the name of service environment that the application will be deployed to.', 'When creating a new application, this parameter is required.']}",
    "state": "{'description': ['The state of the resource on the system.', 'When C(present), guarantees that the resource exists with the provided attributes.', 'When C(absent), removes the resource from the system.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
    "wait": "{'description': ['If the module should wait for the application to be created, deleted or updated.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Load balance an HTTPS application on port 443 with a WAF using ASM
  bigiq_application_https_waf:
    name: my-app
    description: Redirect HTTP to HTTPS via WAF
    service_environment: my-ssg
    servers:
      - address: 1.2.3.4
        port: 8080
      - address: 5.6.7.8
        port: 8080
    inbound_virtual:
      address: 2.2.2.2
      netmask: 255.255.255.255
      port: 443
    redirect_virtual:
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
