# Ansible module: ansible.module_aci_bd_subnet


Manage Subnets (fv:Subnet)

## Description

Manage Subnets on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "bd": "{'description': ['The name of the Bridge Domain.'], 'aliases': ['bd_name']}",
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "description": "{'description': ['The description for the Subnet.'], 'aliases': ['descr']}",
    "enable_vip": "{'description': ['Determines if the Subnet should be treated as a VIP; used when the BD is extended to multiple sites.', 'The APIC defaults to C(no) when unset during creation.'], 'type': 'bool'}",
    "gateway": "{'description': ['The IPv4 or IPv6 gateway address for the Subnet.'], 'aliases': ['gateway_ip']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "mask": "{'description': ['The subnet mask for the Subnet.', 'This is the number assocated with CIDR notation.', 'For IPv4 addresses, accepted values range between C(0) and C(32).', 'For IPv6 addresses, accepted Values range between C(0) and C(128).'], 'type': 'int', 'aliases': ['subnet_mask']}",
    "nd_prefix_policy": "{'description': ['The IPv6 Neighbor Discovery Prefix Policy to associate with the Subnet.']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "preferred": "{'description': ['Determines if the Subnet is preferred over all available Subnets. Only one Subnet per Address Family (IPv4/IPv6). can be preferred in the Bridge Domain.', 'The APIC defaults to C(no) when unset during creation.'], 'type': 'bool'}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "route_profile": "{'description': ['The Route Profile to the associate with the Subnet.']}",
    "route_profile_l3_out": "{'description': ['The L3 Out that contains the assocated Route Profile.']}",
    "scope": "{'description': ['Determines the scope of the Subnet.', 'The C(private) option only allows communication with hosts in the same VRF.', 'The C(public) option allows the Subnet to be advertised outside of the ACI Fabric, and allows communication with hosts in other VRFs.', 'The shared option limits communication to hosts in either the same VRF or the shared VRF.', 'The value is a list of options, C(private) and C(public) are mutually exclusive, but both can be used with C(shared).', 'The APIC defaults to C(private) when unset during creation.'], 'type': 'list', 'choices': ['private', 'public', 'shared']}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "subnet_control": "{'description': ["Determines the Subnet's Control State.", 'The C(querier_ip) option is used to treat the gateway_ip as an IGMP querier source IP.', 'The C(nd_ra) option is used to treate the gateway_ip address as a Neighbor Discovery Router Advertisement Prefix.', 'The C(no_gw) option is used to remove default gateway functionality from the gateway address.', 'The APIC defaults to C(nd_ra) when unset during creation.'], 'choices': ['nd_ra', 'no_gw', 'querier_ip', 'unspecified']}",
    "subnet_name": "{'description': ['The name of the Subnet.'], 'aliases': ['name']}",
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

- name: Create a tenant
  aci_tenant:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    state: present
  delegate_to: localhost

- name: Create a bridge domain
  aci_bd:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    bd: database
    state: present
  delegate_to: localhost

- name: Create a subnet
  aci_bd_subnet:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    bd: database
    gateway: 10.1.1.1
    mask: 24
    state: present
  delegate_to: localhost

- name: Create a subnet with options
  aci_bd_subnet:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    bd: database
    subnet_name: sql
    gateway: 10.1.2.1
    mask: 23
    description: SQL Servers
    scope: public
    route_profile_l3_out: corp
    route_profile: corp_route_profile
    state: present
  delegate_to: localhost

- name: Update a subnets scope to private and shared
  aci_bd_subnet:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    bd: database
    gateway: 10.1.1.1
    mask: 24
    scope: [private, shared]
    state: present
  delegate_to: localhost

- name: Get all subnets
  aci_bd_subnet:
    host: apic
    username: admin
    password: SomeSecretPassword
    state: query
  delegate_to: localhost

- name: Get all subnets of specific gateway in specified tenant
  aci_bd_subnet:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    gateway: 10.1.1.1
    mask: 24
    state: query
  delegate_to: localhost
  register: query_result

- name: Get specific subnet
  aci_bd_subnet:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    bd: database
    gateway: 10.1.1.1
    mask: 24
    state: query
  delegate_to: localhost
  register: query_result

- name: Delete a subnet
  aci_bd_subnet:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    bd: database
    gateway: 10.1.1.1
    mask: 24
    state: absent
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Jacob McGill (@jmcgill298)']
