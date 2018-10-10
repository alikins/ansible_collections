# Ansible module: ansible.module_aci_epg_to_domain


Bind EPGs to Domains (fv:RsDomAtt)

## Description

Bind EPGs to Physical and Virtual Domains on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "allow_useg": "{'description': ['Allows micro-segmentation.', 'The APIC defaults to C(encap) when unset during creation.'], 'choices': ['encap', 'useg']}",
    "ap": "{'description': ['Name of an existing application network profile, that will contain the EPGs.'], 'aliases': ['app_profile', 'app_profile_name']}",
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "deploy_immediacy": "{'description': ['Determines when the policy is pushed to hardware Policy CAM.', 'The APIC defaults to C(lazy) when unset during creation.'], 'choices': ['immediate', 'lazy']}",
    "domain": "{'description': ['Name of the physical or virtual domain being associated with the EPG.'], 'aliases': ['domain_name', 'domain_profile']}",
    "domain_type": "{'description': ['Determines if the Domain is physical (phys) or virtual (vmm).'], 'choices': ['phys', 'vmm'], 'aliases': ['type']}",
    "encap": "{'description': ['The VLAN encapsulation for the EPG when binding a VMM Domain with static encap_mode.', 'This acts as the secondary encap when using useg.', 'Accepted values range between C(1) and C(4096).'], 'type': 'int'}",
    "encap_mode": "{'description': ['The ecapsulataion method to be used.', 'The APIC defaults to C(auto) when unset during creation.'], 'choices': ['auto', 'vlan', 'vxlan']}",
    "epg": "{'description': ['Name of the end point group.'], 'aliases': ['epg_name', 'name']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "netflow": "{'description': ['Determines if netflow should be enabled.', 'The APIC defaults to C(no) when unset during creation.'], 'type': 'bool'}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "primary_encap": "{'description': ['Determines the primary VLAN ID when using useg.', 'Accepted values range between C(1) and C(4096).'], 'type': 'int'}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "resolution_immediacy": "{'description': ['Determines when the policies should be resolved and available.', 'The APIC defaults to C(lazy) when unset during creation.'], 'choices': ['immediate', 'lazy', 'pre-provision']}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "tenant": "{'description': ['Name of an existing tenant.'], 'aliases': ['tenant_name']}",
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

- name: Add a new physical domain to EPG binding
  aci_epg_to_domain:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: anstest
    ap: anstest
    epg: anstest
    domain: anstest
    domain_type: phys
    state: present
  delegate_to: localhost

- name: Remove an existing physical domain to EPG binding
  aci_epg_to_domain:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: anstest
    ap: anstest
    epg: anstest
    domain: anstest
    domain_type: phys
    state: absent
  delegate_to: localhost

- name: Query a specific physical domain to EPG binding
  aci_epg_to_domain:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: anstest
    ap: anstest
    epg: anstest
    domain: anstest
    domain_type: phys
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all domain to EPG bindings
  aci_epg_to_domain:
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
