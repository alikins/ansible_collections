# Ansible module: ansible.module_aci_switch_leaf_selector


Bind leaf selectors to switch policy leaf profiles (infra:LeafS, infra:NodeBlk, infra:RsAccNodePGrep)

## Description

Bind leaf selectors (with node block range and policy group) to switch policy leaf profiles on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "description": "{'description': ['The description to assign to the C(leaf).']}",
    "from": "{'description': ['Start of Node Block range.'], 'type': 'int', 'aliases': ['node_blk_range_from', 'from_range', 'range_from']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "leaf": "{'description': ['Name of Leaf Selector.'], 'aliases': ['name', 'leaf_name', 'leaf_profile_leaf_name', 'leaf_selector_name']}",
    "leaf_node_blk": "{'description': ['Name of Node Block range to be added to Leaf Selector of given Leaf Profile.'], 'aliases': ['leaf_node_blk_name', 'node_blk_name']}",
    "leaf_node_blk_description": "{'description': ['The description to assign to the C(leaf_node_blk)']}",
    "leaf_profile": "{'description': ['Name of the Leaf Profile to which we add a Selector.'], 'aliases': ['leaf_profile_name']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "policy_group": "{'description': ['Name of the Policy Group to be added to Leaf Selector of given Leaf Profile.'], 'aliases': ['name', 'policy_group_name']}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "to": "{'description': ['Start of Node Block range.'], 'type': 'int', 'aliases': ['node_blk_range_to', 'to_range', 'range_to']}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: adding a switch policy leaf profile selector associated Node Block range (w/ policy group)
  aci_switch_leaf_selector:
    host: apic
    username: admin
    password: SomeSecretPassword
    leaf_profile: sw_name
    leaf: leaf_selector_name
    leaf_node_blk: node_blk_name
    from: 1011
    to: 1011
    policy_group: somepolicygroupname
    state: present
  delegate_to: localhost

- name: adding a switch policy leaf profile selector associated Node Block range (w/o policy group)
  aci_switch_leaf_selector:
    host: apic
    username: admin
    password: SomeSecretPassword
    leaf_profile: sw_name
    leaf: leaf_selector_name
    leaf_node_blk: node_blk_name
    from: 1011
    to: 1011
    state: present
  delegate_to: localhost

- name: Removing a switch policy leaf profile selector
  aci_switch_leaf_selector:
    host: apic
    username: admin
    password: SomeSecretPassword
    leaf_profile: sw_name
    leaf: leaf_selector_name
    state: absent
  delegate_to: localhost

- name: Querying a switch policy leaf profile selector
  aci_switch_leaf_selector:
    host: apic
    username: admin
    password: SomeSecretPassword
    leaf_profile: sw_name
    leaf: leaf_selector_name
    state: query
  delegate_to: localhost
  register: query_result

```

## License

TODO

## Author Information
  - ['Bruno Calogero (@brunocalogero)']
