# Ansible module: ansible.module_aci_l3out


Manage Layer 3 Outside (L3Out) objects (l3ext:Out)

## Description

Manage Layer 3 Outside (L3Out) on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "asn": "{'description': ["The AS number for the L3Out. Only applicable when using 'eigrp' as the l3protocol"], 'aliases': ['as_number'], 'version_added': '2.8'}",
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "description": "{'description': ['Description for the L3Out.'], 'aliases': ['descr']}",
    "domain": "{'description': ['Name of the external L3 domain being associated with the L3Out.'], 'required': True, 'aliases': ['ext_routed_domain_name', 'routed_domain']}",
    "dscp": "{'description': ['The target Differentiated Service (DSCP) value.', 'The APIC defaults to C(unspecified) when unset during creation.'], 'choices': ['AF11', 'AF12', 'AF13', 'AF21', 'AF22', 'AF23', 'AF31', 'AF32', 'AF33', 'AF41', 'AF42', 'AF43', 'CS0', 'CS1', 'CS2', 'CS3', 'CS4', 'CS5', 'CS6', 'CS7', 'EF', 'VA', 'unspecified'], 'aliases': ['target']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "l3out": "{'description': ['Name of L3Out being created.'], 'required': True, 'aliases': ['l3out_name', 'name']}",
    "l3protocol": "{'description': ['Routing protocol for the L3Out'], 'type': 'list', 'choices': ['bgp', 'eigrp', 'ospf', 'pim', 'static']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "route_control": "{'description': ['Route Control enforcement direction. The only allowed values are export or import,export.'], 'type': 'list', 'choices': ['export', 'import'], 'aliases': ['route_control_enforcement']}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "tenant": "{'description': ['Name of an existing tenant.'], 'required': True, 'aliases': ['tenant_name']}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
    "vrf": "{'description': ['Name of the VRF being associated with the L3Out.'], 'required': True, 'aliases': ['vrf_name']}",
}
```

## Examples


``` yaml

- name: Add a new L3Out
  aci_l3out:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    name: prod_l3out
    description: L3Out for Production tenant
    domain: l3dom_prod
    vrf: prod
    l3protocol: ospf
    state: present
  delegate_to: localhost

- name: Delete L3Out
  aci_l3out:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    name: prod_l3out
    state: absent
  delegate_to: localhost

- name: Query L3Out information
  aci_l3out:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    name: prod_l3out
    state: query
  delegate_to: localhost
  register: query_result

```

## License

TODO

## Author Information
  - ['Rostyslav Davydenko (@rost-d)']
