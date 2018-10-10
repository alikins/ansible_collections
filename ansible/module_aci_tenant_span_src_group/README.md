# Ansible module: ansible.module_aci_tenant_span_src_group


Manage SPAN source groups (span:SrcGrp)

## Description

Manage SPAN source groups on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "admin_state": "{'description': ['Enable or disable the span sources.', 'The APIC defaults to C(yes) when unset during creation.'], 'type': 'bool'}",
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "description": "{'description': ['The description for Span source group.'], 'aliases': ['descr']}",
    "dst_group": "{'description': ['The Span destination group to associate with the source group.']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "src_group": "{'description': ['The name of the Span source group.'], 'aliases': ['name']}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "tenant": "{'description': ['The name of the Tenant.'], 'aliases': ['tenant_name']}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- aci_tenant_span_src_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    src_group: "{{ src_group }}"
    dst_group: "{{ dst_group }}"
    admin_state: "{{ admin_state }}"
    description: "{{ description }}"
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Jacob McGill (@jmcgill298)']
