# Ansible module: ansible.module_bigip_profile_http


Manage HTTP profiles on a BIG-IP

## Description

Manage HTTP profiles on a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['Description of the profile.']}",
    "dns_resolver": "{'description': ['Specifies the name of a configured DNS resolver, this option is mandatory when C(proxy_type) is set to C(explicit).', 'Format of the name can be either be prepended by partition (C(/Common/foo)), or specified just as an object name (C(foo)).', "To remove the entry a value of C(none) or C('') can be set, however the profile C(proxy_type) must not be set as C(explicit)."]}",
    "encrypt_cookie_secret": "{'description': ['Passphrase for cookie encryption.', 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.']}",
    "encrypt_cookies": "{'description': ['Cookie names for the system to encrypt.', "To remove the entry completely a value of C(none) or C('') should be set.", 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.'], 'type': 'list'}",
    "insert_xforwarded_for": "{'description': ['When specified system inserts an X-Forwarded-For header in an HTTP request with the client IP address, to use with connection pooling.', 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.'], 'type': 'bool'}",
    "name": "{'description': ['Specifies the name of the profile.'], 'required': True}",
    "parent": "{'description': ['Specifies the profile from which this profile inherits settings.', 'When creating a new profile, if this parameter is not specified, the default is the system-supplied C(http) profile.'], 'default': '/Common/http'}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "proxy_type": "{'description': ['Specifies the proxy mode for the profile.', 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.'], 'choices': ['reverse', 'transparent', 'explicit']}",
    "redirect_rewrite": "{'description': ['Specifies whether the system rewrites the URIs that are part of HTTP redirect (3XX) responses.', 'When set to C(none) the system will not rewrite the URI in any HTTP redirect responses.', 'When set to C(all) the system rewrites the URI in all HTTP redirect responses.', 'When set to C(matching) the system rewrites the URI in any HTTP redirect responses that match the request URI.', 'When set to C(nodes) if the URI contains a node IP address instead of a host name, the system changes it to the virtual server address.', 'When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.'], 'choices': ['none', 'all', 'matching', 'nodes']}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the profile exists.', 'When C(absent), ensures the profile is removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "update_password": "{'description': ['C(always) will update passwords if the C(encrypt_cookie_secret) is specified.', 'C(on_create) will only set the password for newly created profiles.'], 'default': 'always', 'choices': ['always', 'on_create']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create HTTP profile
  bigip_profile_http:
    name: my_profile
    password: secret
    server: lb.mydomain.com
    insert_xforwarded_for: yes
    redirect_rewrite: all
    state: present
    user: admin
  delegate_to: localhost

- name: Remove HTTP profile
  bigip_profile_http:
    name: my_profile
    state: absent
    server: lb.mydomain.com
    user: admin
    password: secret
  delegate_to: localhost

- name: Add HTTP profile for transparent proxy
  bigip_profile_http:
    name: my_profile
    server: lb.mydomain.com
    user: admin
    proxy_type: transparent
    password: secret
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Wojciech Wypior (@wojtek0806)']
