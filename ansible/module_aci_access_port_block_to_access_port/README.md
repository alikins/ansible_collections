# Ansible module: ansible.module_aci_access_port_block_to_access_port


Manage port blocks of Fabric interface policy leaf profile interface selectors (infra:HPortS, infra:PortBlk)

## Description

Manage port blocks of Fabric interface policy leaf profile interface selectors on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "access_port_selector": "{'description': ['The name of the Fabric access policy leaf interface profile access port selector.'], 'required': True, 'aliases': ['name', 'access_port_selector_name']}",
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "from_card": "{'description': ['The beginning (from-range) of the card range block for the leaf access port block.'], 'aliases': ['from_card_range']}",
    "from_port": "{'description': ['The beginning (from-range) of the port range block for the leaf access port block.'], 'aliases': ['from', 'fromPort', 'from_port_range'], 'required': True}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "leaf_interface_profile": "{'description': ['The name of the Fabric access policy leaf interface profile.'], 'required': True, 'aliases': ['leaf_interface_profile_name']}",
    "leaf_port_blk": "{'description': ['The name of the Fabric access policy leaf interface profile access port block.'], 'required': True, 'aliases': ['leaf_port_blk_name']}",
    "leaf_port_blk_description": "{'description': ['The description to assign to the C(leaf_port_blk).']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "to_card": "{'description': ['The end (to-range) of the card range block for the leaf access port block.'], 'aliases': ['to_card_range']}",
    "to_port": "{'description': ['The end (to-range) of the port range block for the leaf access port block.'], 'aliases': ['to', 'toPort', 'to_port_range'], 'required': True}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Associate an access port block (single port) to an interface selector
  aci_access_port_block_to_access_port:
    host: apic
    username: admin
    password: SomeSecretPassword
    leaf_interface_profile: leafintprfname
    access_port_selector: accessportselectorname
    leaf_port_blk: leafportblkname
    from_port: 13
    to_port: 13
    state: present
  delegate_to: localhost

- name: Associate an access port block (port range) to an interface selector
  aci_access_port_block_to_access_port:
    host: apic
    username: admin
    password: SomeSecretPassword
    leaf_interface_profile: leafintprfname
    access_port_selector: accessportselectorname
    leaf_port_blk: leafportblkname
    from_port: 13
    to_port: 16
    state: present
  delegate_to: localhost

- name: Remove an access port block from an interface selector
  aci_access_port_block_to_access_port:
    host: apic
    username: admin
    password: SomeSecretPassword
    leaf_interface_profile: leafintprfname
    access_port_selector: accessportselectorname
    leaf_port_blk: leafportblkname
    from_port: 13
    to_port: 13
    state: absent
  delegate_to: localhost

- name: Query Specific access port block under given access port selector
  aci_access_port_block_to_access_port:
    host: apic
    username: admin
    password: SomeSecretPassword
    leaf_interface_profile: leafintprfname
    access_port_selector: accessportselectorname
    leaf_port_blk: leafportblkname
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all access port blocks under given leaf interface profile
  aci_access_port_block_to_access_port:
    host: apic
    username: admin
    password: SomeSecretPassword
    leaf_interface_profile: leafintprfname
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all access port blocks in the fabric
  aci_access_port_block_to_access_port:
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
  - ['Simon Metzger (@smnmtzgr)']
