# Ansible module: ansible.module_aci_domain


Manage physical, virtual, bridged, routed or FC domain profiles (phys:DomP, vmm:DomP, l2ext:DomP, l3ext:DomP, fc:DomP)

## Description

Manage physical, virtual, bridged, routed or FC domain profiles on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "domain": "{'description': ['Name of the physical, virtual, bridged routed or FC domain profile.'], 'aliases': ['domain_name', 'domain_profile', 'name']}",
    "domain_type": "{'description': ['The type of domain profile.', 'C(fc): The FC domain profile is a policy pertaining to single FC Management domain', 'C(l2dom): The external bridged domain profile is a policy for managing L2 bridged infrastructure bridged outside the fabric.', 'C(l3dom): The external routed domain profile is a policy for managing L3 routed infrastructure outside the fabric.', 'C(phys): The physical domain profile stores the physical resources and encap resources that should be used for EPGs associated with this domain.', 'C(vmm): The VMM domain profile is a policy for grouping VM controllers with similar networking policy requirements.'], 'choices': ['fc', 'l2dom', 'l3dom', 'phys', 'vmm'], 'aliases': ['type']}",
    "dscp": "{'description': ['The target Differentiated Service (DSCP) value.', 'The APIC defaults to C(unspecified) when unset during creation.'], 'choices': ['AF11', 'AF12', 'AF13', 'AF21', 'AF22', 'AF23', 'AF31', 'AF32', 'AF33', 'AF41', 'AF42', 'AF43', 'CS0', 'CS1', 'CS2', 'CS3', 'CS4', 'CS5', 'CS6', 'CS7', 'EF', 'VA', 'unspecified'], 'aliases': ['target']}",
    "encap_mode": "{'description': ['The layer 2 encapsulation protocol to use with the virtual switch.'], 'choices': ['unknown', 'vlan', 'vxlan']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "multicast_address": "{'description': ['The muticast IP address to use for the virtual switch.']}",
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
    "vswitch": "{'description': ['The virtual switch to use for vmm domains.', 'The APIC defaults to C(default) when unset during creation.'], 'choices': ['avs', 'default', 'dvs', 'unknown']}",
}
```

## Examples


``` yaml

- name: Add a new physical domain
  aci_domain:
    host: apic
    username: admin
    password: SomeSecretPassword
    domain: phys_dom
    domain_type: phys
    state: present

- name: Remove a physical domain
  aci_domain:
    host: apic
    username: admin
    password: SomeSecretPassword
    domain: phys_dom
    domain_type: phys
    state: absent

- name: Add a new VMM domain
  aci_domain:
    host: apic
    username: admin
    password: SomeSecretPassword
    domain: hyperv_dom
    domain_type: vmm
    vm_provider: microsoft
    state: present
  delegate_to: localhost

- name: Remove a VMM domain
  aci_domain:
    host: apic
    username: admin
    password: SomeSecretPassword
    domain: hyperv_dom
    domain_type: vmm
    vm_provider: microsoft
    state: absent
  delegate_to: localhost

- name: Query a specific physical domain
  aci_domain:
    host: apic
    username: admin
    password: SomeSecretPassword
    domain: phys_dom
    domain_type: phys
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all domains
  aci_domain:
    host: apic
    username: admin
    password: SomeSecretPassword
    domain_type: phys
    state: query
  delegate_to: localhost
  register: query_result

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
