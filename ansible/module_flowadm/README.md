# Ansible module: ansible.module_flowadm


Manage bandwidth resource control and priority for protocols, services and zones on Solaris/illumos systems

## Description

Create/modify/remove networking bandwidth and associated resources for a type of traffic on a particular link.

## Requirements

TODO

## Arguments

``` json
{
    "dsfield": "{'description': ['- Identifies the 8-bit differentiated services field (as defined in RFC 2474). The optional dsfield_mask is used to state the bits of interest in the differentiated services field when comparing with the dsfield value. Both values must be in hexadecimal.\n'], 'required': False}",
    "link": "{'description': ['Specifiies a link to configure flow on.'], 'required': False}",
    "local_ip": "{'description': ['Identifies a network flow by the local IP address.'], 'required': False}",
    "local_port": "{'description': ['Identifies a service specified by the local port.'], 'required': False}",
    "maxbw": "{'description': ['- Sets the full duplex bandwidth for the flow. The bandwidth is specified as an integer with one of the scale suffixes(K, M, or G for Kbps, Mbps, and Gbps). If no units are specified, the input value will be read as Mbps.\n'], 'required': False}",
    "name": "{'description': ['- A flow is defined as a set of attributes based on Layer 3 and Layer 4 headers, which can be used to identify a protocol, service, or a zone.\n'], 'required': True, 'aliases': ['flow']}",
    "priority": "{'description': ['Sets the relative priority for the flow.'], 'required': False, 'default': 'medium', 'choices': ['low', 'medium', 'high']}",
    "remote_ip": "{'description': ['Identifies a network flow by the remote IP address.'], 'required': False}",
    "state": "{'description': ['Create/delete/enable/disable an IP address on the network interface.'], 'required': False, 'default': 'present', 'choices': ['absent', 'present', 'resetted']}",
    "temporary": "{'description': ['Specifies that the configured flow is temporary. Temporary flows do not persist across reboots.'], 'required': False, 'default': False, 'type': 'bool'}",
    "transport": "{'description': ['- Specifies a Layer 4 protocol to be used. It is typically used in combination with I(local_port) to identify the service that needs special attention.\n'], 'required': False}",
}
```

## Examples


``` yaml

# Limit SSH traffic to 100M via vnic0 interface
- flowadm:
    link: vnic0
    flow: ssh_out
    transport: tcp
    local_port: 22
    maxbw: 100M
    state: present

# Reset flow properties
- flowadm:
    name: dns
    state: resetted

# Configure policy for EF PHB (DSCP value of 101110 from RFC 2598) with a bandwidth of 500 Mbps and a high priority.
- flowadm:
    link: bge0
    dsfield: '0x2e:0xfc'
    maxbw: 500M
    priority: high
    flow: efphb-flow
    state: present

```

## License

TODO

## Author Information
  - ['Adam Števko (@xen0l)']
