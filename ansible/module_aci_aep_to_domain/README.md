# Ansible module: ansible.module_aci_aep_to_domain


Bind AEPs to Physical or Virtual Domains (infra:RsDomP)

## Description

Bind AEPs to Physical or Virtual Domains on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "aep": "{'description': ['The name of the Attachable Access Entity Profile.'], 'aliases': ['aep_name']}",
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "domain": "{'description': ['Name of the physical or virtual domain being associated with the AEP.'], 'aliases': ['domain_name', 'domain_profile']}",
    "domain_type": "{'description': ['Determines if the Domain is physical (phys) or virtual (vmm).'], 'choices': ['fc', 'l2dom', 'l3dom', 'phys', 'vmm'], 'aliases': ['type']}",
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
    "vm_provider": "{'description': ['The VM platform for VMM Domains.', 'Support for Kubernetes was added in ACI v3.0.', 'Support for CloudFoundry, OpenShift and Red Hat was added in ACI v3.1.'], 'choices': ['cloudfoundry', 'kubernetes', 'microsoft', 'openshift', 'openstack', 'redhat', 'vmware']}",
}
```

## Examples


``` yaml

- name: Add AEP to domain binding
  aci_aep_to_domain: &binding_present
    host: apic
    username: admin
    password: SomeSecretPassword
    aep: test_aep
    domain: phys_dom
    domain_type: phys
    state: present
  delegate_to: localhost

- name: Remove AEP to domain binding
  aci_aep_to_domain: &binding_absent
    host: apic
    username: admin
    password: SomeSecretPassword
    aep: test_aep
    domain: phys_dom
    domain_type: phys
    state: absent
  delegate_to: localhost

- name: Query our AEP to domain binding
  aci_aep_to_domain:
    host: apic
    username: admin
    password: SomeSecretPassword
    aep: test_aep
    domain: phys_dom
    domain_type: phys
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all AEP to domain bindings
  aci_aep_to_domain: &binding_query
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
