# Ansible module: ansible.module_aci_access_port_to_interface_policy_leaf_profile


Manage Fabric interface policy leaf profile interface selectors (infra:HPortS, infra:RsAccBaseGrp, infra:PortBlk)

## Description

Manage Fabric interface policy leaf profile interface selectors on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "access_port_selector": "{'description': ['The name of the Fabric access policy leaf interface profile access port selector.'], 'required': True, 'aliases': ['name', 'access_port_selector_name']}",
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "description": "{'description': ['The description to assign to the C(access_port_selector)']}",
    "from_card": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.8 we recommend using the module L(aci_access_port_block_to_access_port, aci_access_port_block_to_access_port.html).', 'The parameter will be removed in Ansible 2.12.', 'HORIZONTALLINE', 'The beginning (from-range) of the card range block for the leaf access port block.'], 'aliases': ['from_card_range'], 'version_added': '2.6'}",
    "from_port": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.8 we recommend using the module L(aci_access_port_block_to_access_port, aci_access_port_block_to_access_port.html).', 'The parameter will be removed in Ansible 2.12.', 'HORIZONTALLINE', 'The beginning (from-range) of the port range block for the leaf access port block.'], 'aliases': ['from', 'fromPort', 'from_port_range'], 'required': True}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "interface_type": "{'description': ['The type of interface for the static EPG deployement.'], 'choices': ['fex', 'port_channel', 'switch_port', 'vpc'], 'default': 'switch_port', 'version_added': '2.6'}",
    "leaf_interface_profile": "{'description': ['The name of the Fabric access policy leaf interface profile.'], 'required': True, 'aliases': ['leaf_interface_profile_name']}",
    "leaf_port_blk": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.8 we recommend using the module L(aci_access_port_block_to_access_port, aci_access_port_block_to_access_port.html).', 'The parameter will be removed in Ansible 2.12.', 'HORIZONTALLINE', 'The name of the Fabric access policy leaf interface profile access port block.'], 'required': True, 'aliases': ['leaf_port_blk_name']}",
    "leaf_port_blk_description": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.8 we recommend using the module L(aci_access_port_block_to_access_port, aci_access_port_block_to_access_port.html).', 'The parameter will be removed in Ansible 2.12.', 'HORIZONTALLINE', 'The description to assign to the C(leaf_port_blk)']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "policy_group": "{'description': ['The name of the fabric access policy group to be associated with the leaf interface profile interface selector.'], 'aliases': ['policy_group_name']}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "to_card": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.8 we recommend using the module L(aci_access_port_block_to_access_port, aci_access_port_block_to_access_port.html).', 'The parameter will be removed in Ansible 2.12.', 'HORIZONTALLINE', 'The end (to-range) of the card range block for the leaf access port block.'], 'aliases': ['to_card_range'], 'version_added': '2.6'}",
    "to_port": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.8 we recommend using the module L(aci_access_port_block_to_access_port, aci_access_port_block_to_access_port.html).', 'The parameter will be removed in Ansible 2.12.', 'HORIZONTALLINE', 'The end (to-range) of the port range block for the leaf access port block.'], 'aliases': ['to', 'toPort', 'to_port_range'], 'required': True}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Associate an Interface Access Port Selector to an Interface Policy Leaf Profile with a Policy Group
  aci_access_port_to_interface_policy_leaf_profile:
    host: apic
    username: admin
    password: SomeSecretPassword
    leaf_interface_profile: leafintprfname
    access_port_selector: accessportselectorname
    leaf_port_blk: leafportblkname
    from_port: 13
    toi_port: 16
    policy_group: policygroupname
    state: present
  delegate_to: localhost

- name: Associate an interface access port selector to an Interface Policy Leaf Profile (w/o policy group) (check if this works)
  aci_access_port_to_interface_policy_leaf_profile:
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

- name: Remove an interface access port selector associated with an Interface Policy Leaf Profile
  aci_access_port_to_interface_policy_leaf_profile:
    host: apic
    username: admin
    password: SomeSecretPassword
    leaf_interface_profile: leafintprfname
    access_port_selector: accessportselectorname
    state: absent
  delegate_to: localhost

- name: Query Specific access_port_selector under given leaf_interface_profile
  aci_access_port_to_interface_policy_leaf_profile:
    host: apic
    username: admin
    password: SomeSecretPassword
    leaf_interface_profile: leafintprfname
    access_port_selector: accessportselectorname
    state: query
  delegate_to: localhost
  register: query_result

```

## License

TODO

## Author Information
  - ['Bruno Calogero (@brunocalogero)']
