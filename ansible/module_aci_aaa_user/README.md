# Ansible module: ansible.module_aci_aaa_user


Manage AAA users (aaa:User)

## Description

Manage AAA users on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "aaa_password": "{'description': ['The password of the locally-authenticated user.']}",
    "aaa_password_lifetime": "{'description': ['The lifetime of the locally-authenticated user password.'], 'type': 'int'}",
    "aaa_password_update_required": "{'description': ['Whether this account needs password update.'], 'type': 'bool'}",
    "aaa_user": "{'description': ['The name of the locally-authenticated user user to add.'], 'aliases': ['name', 'user']}",
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "clear_password_history": "{'description': ['Whether to clear the password history of a locally-authenticated user.'], 'type': 'bool'}",
    "description": "{'description': ['Description for the AAA user.'], 'aliases': ['descr']}",
    "email": "{'description': ['The email address of the locally-authenticated user.']}",
    "enabled": "{'description': ['The status of the locally-authenticated user account.'], 'type': 'bool'}",
    "expiration": "{'description': ['The expiration date of the locally-authenticated user account.']}",
    "expires": "{'description': ['Whether to enable an expiration date for the locally-authenticated user account.'], 'type': 'bool'}",
    "first_name": "{'description': ['The first name of the locally-authenticated user.']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "last_name": "{'description': ['The last name of the locally-authenticated user.']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "phone": "{'description': ['The phone number of the locally-authenticated user.']}",
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

- name: Add a user
  aci_aaa_user:
    host: apic
    username: admin
    password: SomeSecretPassword
    aaa_user: dag
    aaa_password: AnotherSecretPassword
    expiration: never
    expires: no
    email: dag@wieers.com
    phone: 1-234-555-678
    first_name: Dag
    last_name: Wieers
    state: present
  delegate_to: localhost

- name: Remove a user
  aci_aaa_user:
    host: apic
    username: admin
    password: SomeSecretPassword
    aaa_user: dag
    state: absent
  delegate_to: localhost

- name: Query a user
  aci_aaa_user:
    host: apic
    username: admin
    password: SomeSecretPassword
    aaa_user: dag
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all users
  aci_aaa_user:
    host: apic
    username: admin
    password: SomeSecretPassword
    state: query
  delegate_to: localhost
  register: query_result

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
