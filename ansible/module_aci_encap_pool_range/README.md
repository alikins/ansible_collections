# Ansible module: ansible.module_aci_encap_pool_range


Manage encap ranges assigned to pools (fvns:EncapBlk, fvns:VsanEncapBlk)

## Description

Manage vlan, vxlan, and vsan ranges that are assigned to pools on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "allocation_mode": "{'description': ['The method used for allocating encaps to resources.', 'Only vlan and vsan support allocation modes.'], 'choices': ['dynamic', 'inherit', 'static'], 'aliases': ['mode']}",
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "description": "{'description': ['Description for the pool range.'], 'aliases': ['descr']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "pool": "{'description': ['The name of the pool that the range should be assigned to.'], 'aliases': ['pool_name']}",
    "pool_allocation_mode": "{'description': ['The method used for allocating encaps to resources.', 'Only vlan and vsan support allocation modes.'], 'choices': ['dynamic', 'static'], 'aliases': ['pool_mode']}",
    "pool_type": "{'description': ['The encap type of C(pool).'], 'required': True, 'aliases': ['type'], 'choices': ['vlan', 'vxlan', 'vsan']}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "range_end": "{'description': ['The end of encap range.'], 'type': 'int', 'aliases': ['end']}",
    "range_name": "{'description': ['The name to give to the encap range.'], 'aliases': ['name', 'range']}",
    "range_start": "{'description': ['The start of the encap range.'], 'type': 'int', 'aliases': ['start']}",
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

- name: Add a new VLAN range
  aci_vlan_pool_encap_block:
    host: apic
    username: admin
    password: SomeSecretPassword
    pool: production
    pool_type: vlan
    encap_start: 20
    encap_end: 50
    state: present
  delegate_to: localhost

- name: Remove a VLAN range
  aci_vlan_pool_encap_block:
    host: apic
    username: admin
    password: SomeSecretPassword
    pool: production
    pool_type: vlan
    encap_start: 20
    encap_end: 50
    state: absent
  delegate_to: localhost

- name: Query a VLAN range
  aci_vlan_pool_encap_block:
    host: apic
    username: admin
    password: SomeSecretPassword
    pool: production
    pool_type: vlan
    encap_start: 20
    encap_end: 50
    state: query
  delegate_to: localhost
  register: query_result

- name: Query a VLAN pool for ranges
  aci_vlan_pool_encap_block:
    host: apic
    username: admin
    password: SomeSecretPassword
    pool: production
    pool_type: vlan
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all VLAN ranges
  aci_vlan_pool_encap_block:
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
