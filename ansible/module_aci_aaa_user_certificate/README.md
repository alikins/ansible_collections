# Ansible module: ansible.module_aci_aaa_user_certificate


Manage AAA user certificates (aaa:UserCert)

## Description

Manage AAA user certificates on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "aaa_user": "{'description': ['The name of the user to add a certificate to.'], 'required': True}",
    "aaa_user_type": "{'description': ['Whether this is a normal user or an appuser.'], 'choices': ['appuser', 'user'], 'default': 'user'}",
    "certificate": "{'description': ['The PEM format public key extracted from the X.509 certificate.'], 'aliases': ['cert_data', 'certificate_data']}",
    "certificate_name": "{'description': ['The name of the user certificate entry in ACI.'], 'aliases': ['cert_name']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Add a certificate to user
  aci_aaa_user_certificate:
    host: apic
    username: admin
    password: SomeSecretPassword
    aaa_user: admin
    certificate_name: admin
    certificate_data: '{{ lookup("file", "pki/admin.crt") }}'
    state: present
  delegate_to: localhost

- name: Remove a certificate of a user
  aci_aaa_user_certificate:
    host: apic
    username: admin
    password: SomeSecretPassword
    aaa_user: admin
    certificate_name: admin
    state: absent
  delegate_to: localhost

- name: Query a certificate of a user
  aci_aaa_user_certificate:
    host: apic
    username: admin
    password: SomeSecretPassword
    aaa_user: admin
    certificate_name: admin
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all certificates of a user
  aci_aaa_user_certificate:
    host: apic
    username: admin
    password: SomeSecretPassword
    aaa_user: admin
    state: query
  delegate_to: localhost
  register: query_result

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
