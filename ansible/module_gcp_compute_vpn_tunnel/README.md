# Ansible module: ansible.module_gcp_compute_vpn_tunnel


Creates a GCP VpnTunnel

## Description

VPN tunnel resource.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "description": "{'description': ['An optional description of this resource.'], 'required': False}",
    "ike_version": "{'description': ['IKE protocol version to use when establishing the VPN tunnel with peer VPN gateway.', 'Acceptable IKE versions are 1 or 2. Default version is 2.'], 'required': False, 'default': 2}",
    "labels": "{'description': ['Labels to apply to this VpnTunnel.'], 'required': False}",
    "local_traffic_selector": "{'description': ['Local traffic selector to use when establishing the VPN tunnel with peer VPN gateway. The value should be a CIDR formatted string, for example `192.168.0.0/16`. The ranges should be disjoint.', 'Only IPv4 is supported.'], 'required': False}",
    "name": "{'description': ['Name of the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': True}",
    "peer_ip": "{'description': ['IP address of the peer VPN gateway. Only IPv4 is supported.'], 'required': True}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "region": "{'description': ['The region where the tunnel is located.'], 'required': True}",
    "remote_traffic_selector": "{'description': ['Remote traffic selector to use when establishing the VPN tunnel with peer VPN gateway. The value should be a CIDR formatted string, for example `192.168.0.0/16`. The ranges should be disjoint.', 'Only IPv4 is supported.'], 'required': False}",
    "router": "{'description': ['URL of router resource to be used for dynamic routing.'], 'required': False}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "shared_secret": "{'description': ['Shared secret used to set the secure session between the Cloud VPN gateway and the peer VPN gateway.'], 'required': True}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "target_vpn_gateway": "{'description': ['URL of the Target VPN gateway with which this VPN tunnel is associated.'], 'required': True}",
}
```

## Examples


``` yaml

- name: create a network
  gcp_compute_network:
      name: "network-vpn_tunnel"
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: network

- name: create a router
  gcp_compute_router:
      name: "router-vpn_tunnel"
      network: "{{ network }}"
      bgp:
        asn: 64514
        advertise_mode: CUSTOM
        advertised_groups:
        - ALL_SUBNETS
        advertised_ip_ranges:
        - range: 1.2.3.4
        - range: 6.7.0.0/16
      region: us-central1
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: router

- name: create a target vpn gateway
  gcp_compute_target_vpn_gateway:
      name: "gateway-vpn_tunnel"
      region: us-west1
      network: "{{ network }}"
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: gateway

- name: create a vpn tunnel
  gcp_compute_vpn_tunnel:
      name: "test_object"
      region: us-west1
      target_vpn_gateway: "{{ gateway }}"
      router: "{{ router }}"
      shared_secret: super secret
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
