# Ansible module: ansible.module_bigip_profile_client_ssl


Manages client SSL profiles on a BIG-IP

## Description

Manages client SSL profiles on a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "allow_non_ssl": "{'description': ['Enables or disables acceptance of non-SSL connections.', 'When creating a new profile, the setting is provided by the parent profile.'], 'type': 'bool', 'version_added': 2.7}",
    "cert_key_chain": "{'description': ['One or more certificates and keys to associate with the SSL profile. This option is always a list. The keys in the list dictate the details of the client/key/chain combination. Note that BIG-IPs can only have one of each type of each certificate/key type. This means that you can only have one RSA, one DSA, and one ECDSA per profile. If you attempt to assign two RSA, DSA, or ECDSA certificate/key combo, the device will reject this.', 'This list is a complex list that specifies a number of keys.'], 'suboptions': {'cert': {'description': ['Specifies a cert name for use.'], 'required': True}, 'key': {'description': ['Contains a key name.'], 'required': True}, 'chain': {'description': ['Contains a certificate chain that is relevant to the certificate and key mentioned earlier.', 'This key is optional.']}, 'passphrase': {'description': ['Contains the passphrase of the key file, should it require one.', 'Passphrases are encrypted on the remote BIG-IP device. Therefore, there is no way to compare them when updating a client SSL profile. Due to this, if you specify a passphrase, this module will always register a C(changed) event.']}}}",
    "ciphers": "{'description': ['Specifies the list of ciphers that the system supports. When creating a new profile, the default cipher list is provided by the parent profile.']}",
    "name": "{'description': ['Specifies the name of the profile.'], 'required': True}",
    "options": "{'description': ['Options that the system uses for SSL processing in the form of a list. When creating a new profile, the list is provided by the parent profile.', "When a C('') or C(none) value is provided all options for SSL processing are disabled."], 'choices': ['netscape-reuse-cipher-change-bug', 'microsoft-big-sslv3-buffer', 'msie-sslv2-rsa-padding', 'ssleay-080-client-dh-bug', 'tls-d5-bug', 'tls-block-padding-bug', 'dont-insert-empty-fragments', 'no-ssl', 'no-dtls', 'no-session-resumption-on-renegotiation', 'no-tlsv1.1', 'no-tlsv1.2', 'single-dh-use', 'ephemeral-rsa', 'cipher-server-preference', 'tls-rollback-bug', 'no-sslv2', 'no-sslv3', 'no-tls', 'no-tlsv1', 'pkcs1-check-1', 'pkcs1-check-2', 'netscape-ca-dn-bug', 'netscape-demo-cipher-change-bug'], 'version_added': 2.7}",
    "parent": "{'description': ['The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the C(clientssl) parent on the C(Common) partition.'], 'default': '/Common/clientssl'}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common', 'version_added': 2.5}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "secure_renegotiation": "{'description': ['Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.', 'When C(request) is set the ssystem request secure renegotation of SSL connections.', 'C(require) is a default setting and when set the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.', 'The C(require-strict) setting the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers.'], 'choices': ['require', 'require-strict', 'request'], 'version_added': 2.7}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the profile exists.', 'When C(absent), ensures the profile is removed.'], 'default': 'present', 'choices': ['present', 'absent'], 'version_added': 2.5}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create client SSL profile
  bigip_profile_client_ssl:
    state: present
    server: lb.mydomain.com
    user: admin
    password: secret
    name: my_profile
  delegate_to: localhost

- name: Create client SSL profile with specific ciphers
  bigip_profile_client_ssl:
    state: present
    server: lb.mydomain.com
    user: admin
    password: secret
    name: my_profile
    ciphers: "!SSLv3:!SSLv2:ECDHE+AES-GCM+SHA256:ECDHE-RSA-AES128-CBC-SHA"
  delegate_to: localhost

- name: Create client SSL profile with specific SSL options
  bigip_profile_client_ssl:
    state: present
    server: lb.mydomain.com
    user: admin
    password: secret
    name: my_profile
    options:
      - no-sslv2
      - no-sslv3
  delegate_to: localhost

- name: Create client SSL profile require secure renegotiation
  bigip_profile_client_ssl:
    state: present
    server: lb.mydomain.com
    user: admin
    password: secret
    name: my_profile
    secure_renegotation: request
  delegate_to: localhost

- name: Create a client SSL profile with a cert/key/chain setting
  bigip_profile_client_ssl:
    state: present
    server: lb.mydomain.com
    user: admin
    password: secret
    name: my_profile
    cert_key_chain:
      - cert: bigip_ssl_cert1
        key: bigip_ssl_key1
        chain: bigip_ssl_cert1
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)', 'Wojciech Wypior (@wojtek0806)']
  - ['Tim Rupp (@caphrim007)', 'Wojciech Wypior (@wojtek0806)']
