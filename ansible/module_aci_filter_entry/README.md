# Ansible module: ansible.module_aci_filter_entry


Manage filter entries (vz:Entry)

## Description

Manage filter entries for a filter on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "arp_flag": "{'description': ['The arp flag to use when the ether_type is arp.', 'The APIC defaults to C(unspecified) when unset during creation.'], 'choices': ['arp_reply', 'arp_request', 'unspecified']}",
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "description": "{'description': ['Description for the Filter Entry.'], 'aliases': ['descr']}",
    "dst_port": "{'description': ['Used to set both destination start and end ports to the same value when ip_protocol is tcp or udp.', 'Accepted values are any valid TCP/UDP port range.', 'The APIC defaults to C(unspecified) when unset during creation.']}",
    "dst_port_end": "{'description': ['Used to set the destination end port when ip_protocol is tcp or udp.', 'Accepted values are any valid TCP/UDP port range.', 'The APIC defaults to C(unspecified) when unset during creation.']}",
    "dst_port_start": "{'description': ['Used to set the destination start port when ip_protocol is tcp or udp.', 'Accepted values are any valid TCP/UDP port range.', 'The APIC defaults to C(unspecified) when unset during creation.']}",
    "entry": "{'description': ['Then name of the Filter Entry.'], 'aliases': ['entry_name', 'filter_entry', 'name']}",
    "ether_type": "{'description': ['The Ethernet type.', 'The APIC defaults to C(unspecified) when unset during creation.'], 'choices': ['arp', 'fcoe', 'ip', 'mac_security', 'mpls_ucast', 'trill', 'unspecified']}",
    "filter": "{'description': ['The name of Filter that the entry should belong to.'], 'aliases': ['filter_name']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "icmp6_msg_type": "{'description': ['ICMPv6 message type; used when ip_protocol is icmpv6.', 'The APIC defaults to C(unspecified) when unset during creation.'], 'choices': ['dst_unreachable', 'echo_request', 'echo_reply', 'neighbor_advertisement', 'neighbor_solicitation', 'redirect', 'time_exceeded', 'unspecified']}",
    "icmp_msg_type": "{'description': ['ICMPv4 message type; used when ip_protocol is icmp.', 'The APIC defaults to C(unspecified) when unset during creation.'], 'choices': ['dst_unreachable', 'echo', 'echo_reply', 'src_quench', 'time_exceeded', 'unspecified']}",
    "ip_protocol": "{'description': ['The IP Protocol type when ether_type is ip.', 'The APIC defaults to C(unspecified) when unset during creation.'], 'choices': ['eigrp', 'egp', 'icmp', 'icmpv6', 'igmp', 'igp', 'l2tp', 'ospfigp', 'pim', 'tcp', 'udp', 'unspecified']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "state": "{'description': ['present, absent, query'], 'default': 'present', 'choices': ['absent', 'present', 'query']}",
    "stateful": "{'description': ['Determines the statefulness of the filter entry.'], 'type': 'bool'}",
    "tenant": "{'description': ['The name of the tenant.'], 'aliases': ['tenant_name']}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- aci_filter_entry:
    host: "{{ inventory_hostname }}"
    username: "{{ user }}"
    password: "{{ pass }}"
    state: "{{ state }}"
    entry: "{{ entry }}"
    tenant: "{{ tenant }}"
    ether_name: "{{  ether_name }}"
    icmp_msg_type: "{{ icmp_msg_type }}"
    filter: "{{ filter }}"
    descr: "{{ descr }}"
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Jacob McGill (@jmcgill298)']
