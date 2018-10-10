# Ansible module: ansible.module_aci_encap_pool


Manage encap pools (fvns:VlanInstP, fvns:VxlanInstP, fvns:VsanInstP)

## Description

Manage vlan, vxlan, and vsan pools on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "description": "{'description': ['Description for the C(pool).'], 'aliases': ['descr']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "pool": "{'description': ['The name of the pool.'], 'aliases': ['name', 'pool_name']}",
    "pool_allocation_mode": "{'description': ['The method used for allocating encaps to resources.', 'Only vlan and vsan support allocation modes.'], 'choices': ['dynamic', 'static'], 'aliases': ['allocation_mode', 'mode']}",
    "pool_type": "{'description': ['The encap type of C(pool).'], 'required': True, 'aliases': ['type'], 'choices': ['vlan', 'vxlan', 'vsan']}",
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

- name: Add a new vlan pool
  aci_encap_pool:
    host: apic
    username: admin
    password: SomeSecretPassword
    pool: production
    pool_type: vlan
    description: Production VLANs
    state: present
  delegate_to: localhost

- name: Remove a vlan pool
  aci_encap_pool:
    host: apic
    username: admin
    password: SomeSecretPassword
    pool: production
    pool_type: vlan
    state: absent
  delegate_to: localhost

- name: Query a vlan pool
  aci_encap_pool:
    host: apic
    username: admin
    password: SomeSecretPassword
    pool: production
    pool_type: vlan
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all vlan pools
  aci_encap_pool:
    host: apic
    username: admin
    password: SomeSecretPassword
    pool_type: vlan
    state: query
  delegate_to: localhost
  register: query_result

```

## License

TODO

## Author Information
  - ['Jacob McGill (@jmcgill298)']
