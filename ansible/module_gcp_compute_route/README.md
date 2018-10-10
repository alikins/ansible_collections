# Ansible module: ansible.module_gcp_compute_route


Creates a GCP Route

## Description

Represents a Route resource.
A route is a rule that specifies how certain packets should be handled by the virtual network. Routes are associated with virtual machines by tag, and the set of routes for a particular virtual machine is called its routing table. For each packet leaving a virtual machine, the system searches that virtual machine's routing table for a single best matching route.
Routes match packets by destination IP address, preferring smaller or more specific ranges over larger ones. If there is a tie, the system selects the route with the smallest priority value. If there is still a tie, it uses the layer three and four packet headers to select just one of the remaining matching routes. The packet is then forwarded as specified by the next_hop field of the winning route -- either to another virtual machine destination, a virtual machine gateway or a Compute Engine-operated gateway. Packets that do not match any route in the sending virtual machine's routing table will be dropped.
A Route resource must have exactly one specification of either nextHopGateway, nextHopInstance, nextHopIp, or nextHopVpnTunnel.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "description": "{'description': ['An optional description of this resource. Provide this property when you create the resource.'], 'required': False, 'version_added': 2.7}",
    "dest_range": "{'description': ['The destination range of outgoing packets that this route applies to.', 'Only IPv4 is supported.'], 'required': True}",
    "name": "{'description': ['Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035.  Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': True}",
    "network": "{'description': ['The network that this route applies to.'], 'required': True}",
    "next_hop_gateway": "{'description': ['URL to a gateway that should handle matching packets.', 'Currently, you can only specify the internet gateway, using a full or partial valid URL:  * U(https://www.googleapis.com/compute/v1/projects/project/global/gateways/default-internet-gateway) * projects/project/global/gateways/default-internet-gateway * global/gateways/default-internet-gateway .'], 'required': False}",
    "next_hop_instance": "{'description': ['URL to an instance that should handle matching packets.', 'You can specify this as a full or partial URL. For example:  * U(https://www.googleapis.com/compute/v1/projects/project/zones/zone/) instances/instance * projects/project/zones/zone/instances/instance * zones/zone/instances/instance .'], 'required': False}",
    "next_hop_ip": "{'description': ['Network IP address of an instance that should handle matching packets.'], 'required': False}",
    "next_hop_vpn_tunnel": "{'description': ['URL to a VpnTunnel that should handle matching packets.'], 'required': False}",
    "priority": "{'description': ['The priority of this route. Priority is used to break ties in cases where there is more than one matching route of equal prefix length.', 'In the case of two routes with equal prefix length, the one with the lowest-numbered priority value wins.', 'Default value is 1000. Valid range is 0 through 65535.'], 'required': False}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tags": "{'description': ['A list of instance tags to which this route applies.'], 'required': False}",
}
```

## Examples


``` yaml

- name: create a network
  gcp_compute_network:
      name: "network-route"
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: network

- name: create a route
  gcp_compute_route:
      name: "test_object"
      dest_range: 192.168.6.0/24
      next_hop_gateway: global/gateways/default-internet-gateway
      network: "{{ network }}"
      tags:
      - backends
      - databases
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
