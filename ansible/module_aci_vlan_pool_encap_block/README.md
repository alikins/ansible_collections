# Ansible module: ansible.module_aci_vlan_pool_encap_block


Manage encap blocks assigned to VLAN pools (fvns:EncapBlk)

## Description

Manage VLAN encap blocks that are assigned to VLAN pools on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "allocation_mode": "{'description': ['The method used for allocating encaps to resources.'], 'aliases': ['mode'], 'choices': ['dynamic', 'inherit', 'static']}",
    "block_end": "{'description': ['The end of encap block.'], 'type': 'int', 'aliases': ['end']}",
    "block_name": "{'description': ['The name to give to the encap block.'], 'aliases': ['name']}",
    "block_start": "{'description': ['The start of the encap block.'], 'type': 'int', 'aliases': ['start']}",
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "description": "{'description': ['Description for the pool encap block.'], 'aliases': ['descr']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "pool": "{'description': ['The name of the pool that the encap block should be assigned to.'], 'aliases': ['pool_name']}",
    "pool_allocation_mode": "{'description': ['The method used for allocating encaps to resources.'], 'choices': ['dynamic', 'static'], 'aliases': ['pool_mode']}",
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

- name: Add a new VLAN encap block
  aci_vlan_pool_encap_block:
    host: apic
    username: admin
    password: SomeSecretPassword
    pool: production
    block_start: 20
    block_end: 50
    state: present
  delegate_to: localhost

- name: Remove a VLAN encap block
  aci_vlan_pool_encap_block:
    host: apic
    username: admin
    password: SomeSecretPassword
    pool: production
    block_start: 20
    block_end: 50
    state: absent
  delegate_to: localhost

- name: Query a VLAN encap block
  aci_vlan_pool_encap_block:
    host: apic
    username: admin
    password: SomeSecretPassword
    pool: production
    block_start: 20
    block_end: 50
    state: query
  delegate_to: localhost
  register: query_result

- name: Query a VLAN pool for encap blocks
  aci_vlan_pool_encap_block:
    host: apic
    username: admin
    password: SomeSecretPassword
    pool: production
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all VLAN encap blocks
  aci_vlan_pool_encap_block:
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
  - ['Jacob McGill (@jmcgill298)', 'Dag Wieers (@dagwieers)']
  - ['Jacob McGill (@jmcgill298)', 'Dag Wieers (@dagwieers)']
