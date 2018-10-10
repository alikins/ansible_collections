# Ansible module: ansible.module_ovirt_auth


Module to manage authentication to oVirt/RHV

## Description

This module authenticates to oVirt/RHV engine and creates SSO token, which should be later used in all other oVirt/RHV modules, so all modules don't need to perform login and logout. This module returns an Ansible fact called I(ovirt_auth). Every module can use this fact as C(auth) parameter, to perform authentication.

## Requirements

TODO

## Arguments

``` json
{
    "ca_file": "{'required': False, 'description': ['A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If C(ca_file) parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.']}",
    "compress": "{'required': False, 'description': ['A boolean flag indicating if the SDK should ask the server to send compressed responses. The default is I(True). Note that this is a hint for the server, and that it may return uncompressed data even when this parameter is set to I(True).']}",
    "headers": "{'required': False, 'description': ['A dictionary of HTTP headers to be added to each API call.'], 'version_added': '2.4'}",
    "hostname": "{'required': False, 'description': ['A string containing the hostname of the server. For example: I(server.example.com). Default value is set by I(OVIRT_HOSTNAME) environment variable.', 'Either C(url) or C(hostname) is required.'], 'version_added': '2.6'}",
    "insecure": "{'required': False, 'description': ['A boolean flag that indicates if the server TLS certificate and host name should be checked.']}",
    "kerberos": "{'required': False, 'description': ['A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.']}",
    "password": "{'required': False, 'description': ['The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.']}",
    "state": "{'default': 'present', 'choices': ['present', 'absent'], 'description': ['Specifies if a token should be created or revoked.']}",
    "timeout": "{'required': False, 'description': ['The maximum total time to wait for the response, in seconds. A value of zero (the default) means wait forever. If the timeout expires before the response is received an exception will be raised.']}",
    "token": "{'required': False, 'description': ['SSO token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.'], 'version_added': 2.5}",
    "url": "{'required': False, 'description': ['A string containing the API URL of the server. For example: I(https://server.example.com/ovirt-engine/api). Default value is set by I(OVIRT_URL) environment variable.', 'Either C(url) or C(hostname) is required.']}",
    "username": "{'required': False, 'description': ['The name of the user. For example: I(admin@internal) Default value is set by I(OVIRT_USERNAME) environment variable.']}",
}
```

## Examples


``` yaml

  - block:
       # Create a vault with `ovirt_password` variable which store your
       # oVirt/RHV user's password, and include that yaml file with variable:
       - include_vars: ovirt_password.yml

       - name: Obtain SSO token with using username/password credentials
         ovirt_auth:
           url: https://ovirt.example.com/ovirt-engine/api
           username: admin@internal
           ca_file: ca.pem
           password: "{{ ovirt_password }}"

       # Previous task generated I(ovirt_auth) fact, which you can later use
       # in different modules as follows:
       - ovirt_vms:
           auth: "{{ ovirt_auth }}"
           state: absent
           name: myvm

    always:
      - name: Always revoke the SSO token
        ovirt_auth:
          state: absent
          ovirt_auth: "{{ ovirt_auth }}"

# When user will set following environment variables:
#   OVIRT_URL = https://fqdn/ovirt-engine/api
#   OVIRT_USERNAME = admin@internal
#   OVIRT_PASSWORD = the_password
# User can login the oVirt using environment variable instead of variables
# in yaml file.
# This is mainly useful when using Ansible Tower or AWX, as it will work
# for Red Hat Virtualization creadentials type.
  - name: Obtain SSO token
    ovirt_auth:
      state: present

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
