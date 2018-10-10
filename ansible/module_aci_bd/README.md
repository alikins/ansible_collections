# Ansible module: ansible.module_aci_bd


Manage Bridge Domains (BD) objects (fv:BD)

## Description

Manages Bridge Domains (BD) on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "arp_flooding": "{'description': ['Determines if the Bridge Domain should flood ARP traffic.', 'The APIC defaults to C(no) when unset during creation.'], 'type': 'bool'}",
    "bd": "{'description': ['The name of the Bridge Domain.'], 'aliases': ['bd_name', 'name']}",
    "bd_type": "{'description': ['The type of traffic on the Bridge Domain.', 'The APIC defaults to C(ethernet) when unset during creation.'], 'choices': ['ethernet', 'fc']}",
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "description": "{'description': ['Description for the Bridge Domain.']}",
    "enable_multicast": "{'description': ['Determines if PIM is enabled.', 'The APIC defaults to C(no) when unset during creation.'], 'type': 'bool'}",
    "enable_routing": "{'description': ['Determines if IP forwarding should be allowed.', 'The APIC defaults to C(yes) when unset during creation.'], 'type': 'bool'}",
    "endpoint_clear": "{'description': ['Clears all End Points in all Leaves when C(yes).', 'The value is not reset to disabled once End Points have been cleared; that requires a second task.', 'The APIC defaults to C(no) when unset during creation.'], 'type': 'bool'}",
    "endpoint_move_detect": "{'description': ['Determines if GARP should be enabled to detect when End Points move.', 'The APIC defaults to C(garp) when unset during creation.'], 'choices': ['default', 'garp']}",
    "endpoint_retention_action": "{'description': ['Determines if the Bridge Domain should inherit or resolve the End Point Retention Policy.', 'The APIC defaults to C(resolve) when unset during creation.'], 'choices': ['inherit', 'resolve']}",
    "endpoint_retention_policy": "{'description': ['The name of the End Point Retention Policy the Bridge Domain should use when overriding the default End Point Retention Policy.']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "igmp_snoop_policy": "{'description': ['The name of the IGMP Snooping Policy the Bridge Domain should use when overriding the default IGMP Snooping Policy.']}",
    "ip_learning": "{'description': ['Determines if the Bridge Domain should learn End Point IPs.', 'The APIC defaults to C(yes) when unset during creation.'], 'type': 'bool'}",
    "ipv6_nd_policy": "{'description': ['The name of the IPv6 Neighbor Discovery Policy the Bridge Domain should use when overridding the default IPV6 ND Policy.']}",
    "l2_unknown_unicast": "{'description': ['Determines what forwarding method to use for unknown l2 destinations.', 'The APIC defaults to C(proxy) when unset during creation.'], 'choices': ['proxy', 'flood']}",
    "l3_unknown_multicast": "{'description': ['Determines the forwarding method to use for unknown multicast destinations.', 'The APIC defaults to C(flood) when unset during creation.'], 'choices': ['flood', 'opt-flood']}",
    "limit_ip_learn": "{'description': ['Determines if the BD should limit IP learning to only subnets owned by the Bridge Domain.', 'The APIC defaults to C(yes) when unset during creation.'], 'type': 'bool'}",
    "mac_address": "{'description': ['The MAC Address to assign to the C(bd) instead of using the default.', 'The APIC defaults to C(00:22:BD:F8:19:FF) when unset during creation.'], 'aliases': ['mac'], 'version_added': '2.5'}",
    "multi_dest": "{'description': ['Determines the forwarding method for L2 multicast, broadcast, and link layer traffic.', 'The APIC defaults to C(bd-flood) when unset during creation.'], 'choices': ['bd-flood', 'drop', 'encap-flood']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "tenant": "{'description': ['The name of the Tenant.'], 'aliases': ['tenant_name']}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
    "vrf": "{'description': ['The name of the VRF.'], 'aliases': ['vrf_name']}",
}
```

## Examples


``` yaml

- name: Add Bridge Domain
  aci_bd:
    host: "{{ inventory_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: no
    tenant: prod
    bd: web_servers
    mac_address: 00:22:BD:F8:19:FE
    vrf: prod_vrf
    state: present
  delegate_to: localhost

- name: Add an FC Bridge Domain
  aci_bd:
    host: "{{ inventory_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: no
    tenant: prod
    bd: storage
    bd_type: fc
    vrf: fc_vrf
    enable_routing: no
    state: present
  delegate_to: localhost

- name: Modify a Bridge Domain
  aci_bd:
    host: "{{ inventory_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: yes
    tenant: prod
    bd: web_servers
    arp_flooding: yes
    l2_unknown_unicast: flood
    state: present
  delegate_to: localhost

- name: Query All Bridge Domains
  aci_bd:
    host: "{{ inventory_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: yes
    state: query
  delegate_to: localhost
  register: query_result

- name: Query a Bridge Domain
  aci_bd:
    host: "{{ inventory_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: yes
    tenant: prod
    bd: web_servers
    state: query
  delegate_to: localhost
  register: query_result

- name: Delete a Bridge Domain
  aci_bd:
    host: "{{ inventory_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: yes
    tenant: prod
    bd: web_servers
    state: absent
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Jacob McGill (@jmcgill298)']
