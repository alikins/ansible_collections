# Ansible module: ansible.module_aci_interface_policy_leaf_policy_group


Manage fabric interface policy leaf policy groups (infra:AccBndlGrp, infra:AccPortGrp)

## Description

Manage fabric interface policy leaf policy groups on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "aep": "{'description': ['Choice of attached_entity_profile (AEP) to be used as part of the leaf policy group to be created.'], 'aliases': ['aep_name']}",
    "cdp_policy": "{'description': ['Choice of cdp_policy to be used as part of the leaf policy group to be created.'], 'aliases': ['cdp_policy_name']}",
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "description": "{'description': ['Description for the leaf policy group to be created.'], 'aliases': ['descr']}",
    "egress_data_plane_policing_policy": "{'description': ['Choice of egress_data_plane_policing_policy to be used as part of the leaf policy group to be created.'], 'aliases': ['egress_data_plane_policing_policy_name']}",
    "fibre_channel_interface_policy": "{'description': ['Choice of fibre_channel_interface_policy to be used as part of the leaf policy group to be created.'], 'aliases': ['fibre_channel_interface_policy_name']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "ingress_data_plane_policing_policy": "{'description': ['Choice of ingress_data_plane_policing_policy to be used as part of the leaf policy group to be created.'], 'aliases': ['ingress_data_plane_policing_policy_name']}",
    "l2_interface_policy": "{'description': ['Choice of l2_interface_policy to be used as part of the leaf policy group to be created.'], 'aliases': ['l2_interface_policy_name']}",
    "lag_type": "{'description': ['Selector for the type of leaf policy group we want to create.', 'C(leaf) for Leaf Access Port Policy Group', 'C(link) for Port Channel (PC)', 'C(node) for Virtual Port Channel (VPC)'], 'aliases': ['lag_type_name'], 'choices': ['leaf', 'link', 'node'], 'required': True}",
    "link_level_policy": "{'description': ['Choice of link_level_policy to be used as part of the leaf policy group to be created.'], 'aliases': ['link_level_policy_name']}",
    "lldp_policy": "{'description': ['Choice of lldp_policy to be used as part of the leaf policy group to be created.'], 'aliases': ['lldp_policy_name']}",
    "mcp_policy": "{'description': ['Choice of mcp_policy to be used as part of the leaf policy group to be created.'], 'aliases': ['mcp_policy_name']}",
    "monitoring_policy": "{'description': ['Choice of monitoring_policy to be used as part of the leaf policy group to be created.'], 'aliases': ['monitoring_policy_name']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "policy_group": "{'description': ['Name of the leaf policy group to be added/deleted.'], 'aliases': ['name', 'policy_group_name']}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "port_channel_policy": "{'description': ['Choice of port_channel_policy to be used as part of the leaf policy group to be created.'], 'aliases': ['port_channel_policy_name']}",
    "port_security_policy": "{'description': ['Choice of port_security_policy to be used as part of the leaf policy group to be created.'], 'aliases': ['port_security_policy_name']}",
    "priority_flow_control_policy": "{'description': ['Choice of priority_flow_control_policy to be used as part of the leaf policy group to be created.'], 'aliases': ['priority_flow_control_policy_name']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "slow_drain_policy": "{'description': ['Choice of slow_drain_policy to be used as part of the leaf policy group to be created.'], 'aliases': ['slow_drain_policy_name']}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "storm_control_interface_policy": "{'description': ['Choice of storm_control_interface_policy to be used as part of the leaf policy group to be created.'], 'aliases': ['storm_control_interface_policy_name']}",
    "stp_interface_policy": "{'description': ['Choice of stp_interface_policy to be used as part of the leaf policy group to be created.'], 'aliases': ['stp_interface_policy_name']}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Create a Port Channel (PC) Interface Policy Group
  aci_interface_policy_leaf_policy_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    lag_type: link
    policy_group: policygroupname
    description: policygroupname description
    link_level_policy: whateverlinklevelpolicy
    fibre_channel_interface_policy: whateverfcpolicy
    state: present
  delegate_to: localhost

- name: Create a Virtual Port Channel (VPC) Interface Policy Group (no description)
  aci_interface_policy_leaf_policy_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    lag_type: node
    policy_group: policygroupname
    link_level_policy: whateverlinklevelpolicy
    fibre_channel_interface_policy: whateverfcpolicy
    state: present
  delegate_to: localhost

- name: Create a Leaf Access Port Policy Group (no description)
  aci_interface_policy_leaf_policy_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    lag_type: leaf
    policy_group: policygroupname
    link_level_policy: whateverlinklevelpolicy
    fibre_channel_interface_policy: whateverfcpolicy
    state: present
  delegate_to: localhost

- name: Query all Leaf Access Port Policy Groups of type link
  aci_interface_policy_leaf_policy_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    lag_type: link
    state: query
  delegate_to: localhost
  register: query_result

- name: Query a specific Lead Access Port Policy Group
  aci_interface_policy_leaf_policy_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    lag_type: leaf
    policy_group: policygroupname
    state: query
  delegate_to: localhost
  register: query_result

- name: Delete an Interface policy Leaf Policy Group
  aci_interface_policy_leaf_policy_group:
    host: apic
    username: admin
    password: SomeSecretPassword
    lag_type: type_name
    policy_group: policygroupname
    state: absent
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Bruno Calogero (@brunocalogero)']
