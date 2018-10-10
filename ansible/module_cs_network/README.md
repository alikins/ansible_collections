# Ansible module: ansible.module_cs_network


Manages networks on Apache CloudStack based clouds

## Description

Create, update, restart and delete networks.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the network is related to.']}",
    "acl": "{'description': ['The name of the access control list for the VPC network tier.'], 'version_added': '2.5'}",
    "acl_type": "{'description': ['Access control type for the VPC network tier.', 'Only considered on create.'], 'default': 'account', 'choices': ['account', 'domain']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "cidr_ipv6": "{'description': ['CIDR of IPv6 network, must be at least /64.', 'Only considered on create.']}",
    "clean_up": "{'description': ['Cleanup old network elements.', 'Only considered on C(state=restarted).'], 'default': False, 'type': 'bool'}",
    "display_text": "{'description': ['Display text of the network.', 'If not specified, C(name) will be used as C(display_text).']}",
    "domain": "{'description': ['Domain the network is related to.']}",
    "end_ip": "{'description': ['The ending IPv4 address of the network belongs to.', 'If not specified, value of C(start_ip) is used.', 'Only considered on create.']}",
    "end_ipv6": "{'description': ['The ending IPv6 address of the network belongs to.', 'If not specified, value of C(start_ipv6) is used.', 'Only considered on create.']}",
    "gateway": "{'description': ['The gateway of the network.', 'Required for shared networks and isolated networks when it belongs to a VPC.', 'Only considered on create.']}",
    "gateway_ipv6": "{'description': ['The gateway of the IPv6 network.', 'Required for shared networks.', 'Only considered on create.']}",
    "isolated_pvlan": "{'description': ['The isolated private VLAN for this network.']}",
    "name": "{'description': ['Name (case sensitive) of the network.'], 'required': True}",
    "netmask": "{'description': ['The netmask of the network.', 'Required for shared networks and isolated networks when it belongs to a VPC.', 'Only considered on create.']}",
    "network_domain": "{'description': ['The network domain.']}",
    "network_offering": "{'description': ['Name of the offering for the network.', 'Required if C(state=present).']}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'default': True, 'type': 'bool'}",
    "project": "{'description': ['Name of the project the network to be deployed in.']}",
    "start_ip": "{'description': ['The beginning IPv4 address of the network belongs to.', 'Only considered on create.']}",
    "start_ipv6": "{'description': ['The beginning IPv6 address of the network belongs to.', 'Only considered on create.']}",
    "state": "{'description': ['State of the network.'], 'default': 'present', 'choices': ['present', 'absent', 'restarted']}",
    "subdomain_access": "{'description': ['Defines whether to allow subdomains to use networks dedicated to their parent domain(s).', 'Should be used with C(acl_type=domain).', 'Only considered on create.'], 'type': 'bool', 'version_added': '2.5'}",
    "vlan": "{'description': ['The ID or VID of the network.']}",
    "vpc": "{'description': ['Name of the VPC of the network.']}",
    "zone": "{'description': ['Name of the zone in which the network should be deployed.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

- name: Create a network
  local_action:
    module: cs_network
    name: my network
    zone: gva-01
    network_offering: DefaultIsolatedNetworkOfferingWithSourceNatService
    network_domain: example.com

- name: Create a VPC tier
  local_action:
    module: cs_network
    name: my VPC tier 1
    zone: gva-01
    vpc: my VPC
    network_offering: DefaultIsolatedNetworkOfferingForVpcNetworks
    gateway: 10.43.0.1
    netmask: 255.255.255.0
    acl: my web acl

- name: Update a network
  local_action:
    module: cs_network
    name: my network
    display_text: network of domain example.local
    network_domain: example.local

- name: Restart a network with clean up
  local_action:
    module: cs_network
    name: my network
    clean_up: yes
    state: restared

- name: Remove a network
  local_action:
    module: cs_network
    name: my network
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
