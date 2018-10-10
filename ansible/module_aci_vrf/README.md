# Ansible module: ansible.module_aci_vrf


Manage contexts or VRFs (fv:Ctx)

## Description

Manage contexts or VRFs on Cisco ACI fabrics.
Each context is a private network associated to a tenant, i.e. VRF.

## Requirements

TODO

## Arguments

``` json
{
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "description": "{'description': ['The description for the VRF.'], 'aliases': ['descr']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "policy_control_direction": "{'description': ['Determines if the policy should be enforced by the fabric on ingress or egress.'], 'choices': ['egress', 'ingress']}",
    "policy_control_preference": "{'description': ['Determines if the fabric should enforce contract policies to allow routing and packet forwarding.'], 'choices': ['enforced', 'unenforced']}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "tenant": "{'description': ['The name of the Tenant the VRF should belong to.'], 'aliases': ['tenant_name']}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
    "vrf": "{'description': ['The name of the VRF.'], 'aliases': ['context', 'name', 'vrf_name']}",
}
```

## Examples


``` yaml

- name: Add a new VRF to a tenant
  aci_vrf:
    host: apic
    username: admin
    password: SomeSecretPassword
    vrf: vrf_lab
    tenant: lab_tenant
    descr: Lab VRF
    policy_control_preference: enforced
    policy_control_direction: ingress
    state: present
  delegate_to: localhost

- name: Remove a VRF for a tenant
  aci_vrf:
    host: apic
    username: admin
    password: SomeSecretPassword
    vrf: vrf_lab
    tenant: lab_tenant
    state: absent
  delegate_to: localhost

- name: Query a VRF of a tenant
  aci_vrf:
    host: apic
    username: admin
    password: SomeSecretPassword
    vrf: vrf_lab
    tenant: lab_tenant
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all VRFs
  aci_vrf:
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
  - ['Jacob McGill (@jmcgill298)']
