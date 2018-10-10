# Ansible module: ansible.module_bigip_ssl_certificate


Import/Delete certificates from BIG-IP

## Description

This module will import/delete SSL certificates on BIG-IP LTM. Certificates can be imported from certificate and key files on the local disk, in PEM format.

## Requirements

TODO

## Arguments

``` json
{
    "content": "{'description': ['Sets the contents of a certificate directly to the specified value. This is used with lookup plugins or for anything with formatting or', 'C(content) must be provided when C(state) is C(present).'], 'aliases': ['cert_content']}",
    "issuer_cert": "{'description': ['Issuer certificate used for OCSP monitoring.', 'This parameter is only valid on versions of BIG-IP 13.0.0 or above.'], 'version_added': 2.5}",
    "name": "{'description': ['SSL Certificate Name. This is the cert name used when importing a certificate into the F5. It also determines the filenames of the objects on the LTM.'], 'required': True}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common', 'version_added': 2.5}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['Certificate state. This determines if the provided certificate and key is to be made C(present) on the device or C(absent).'], 'default': 'present', 'choices': ['present', 'absent']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Use a file lookup to import PEM Certificate
  bigip_ssl_certificate:
    name: certificate-name
    server: lb.mydomain.com
    user: admin
    password: secret
    state: present
    content: "{{ lookup('file', '/path/to/cert.crt') }}"
  delegate_to: localhost

- name: Use a file lookup to import CA certificate chain
  bigip_ssl_certificate:
    name: ca-chain-name
    server: lb.mydomain.com
    user: admin
    password: secret
    state: present
    content: "{{ lookup('file', '/path/to/ca-chain.crt') }}"
  delegate_to: localhost

- name: Delete Certificate
  bigip_ssl_certificate:
    name: certificate-name
    server: lb.mydomain.com
    user: admin
    password: secret
    state: absent
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
