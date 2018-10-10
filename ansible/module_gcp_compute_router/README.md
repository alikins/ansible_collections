# Ansible module: ansible.module_gcp_compute_router


Creates a GCP Router

## Description

Represents a Router resource.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "bgp": "{'description': ['BGP information specific to this router.'], 'required': False, 'suboptions': {'asn': {'description': ['Local BGP Autonomous System Number (ASN). Must be an RFC6996 private ASN, either 16-bit or 32-bit. The value will be fixed for this router resource. All VPN tunnels that link to this router will have the same local ASN.'], 'required': True}, 'advertise_mode': {'description': ['User-specified flag to indicate which mode to use for advertisement.', 'Valid values of this enum field are: DEFAULT, CUSTOM .'], 'required': False, 'default': 'DEFAULT', 'choices': ['DEFAULT', 'CUSTOM']}, 'advertised_groups': {'description': ['User-specified list of prefix groups to advertise in custom mode.', 'This field can only be populated if advertiseMode is CUSTOM and is advertised to all peers of the router. These groups will be advertised in addition to any specified prefixes. Leave this field blank to advertise no custom groups.', 'This enum field has the one valid value: ALL_SUBNETS .'], 'required': False}, 'advertised_ip_ranges': {'description': ['User-specified list of individual IP ranges to advertise in custom mode. This field can only be populated if advertiseMode is CUSTOM and is advertised to all peers of the router. These IP ranges will be advertised in addition to any specified groups.', 'Leave this field blank to advertise no custom IP ranges.'], 'required': False, 'suboptions': {'range': {'description': ['The IP range to advertise. The value must be a CIDR-formatted string.'], 'required': False}, 'description': {'description': ['User-specified description for the IP range.'], 'required': False}}}}}",
    "description": "{'description': ['An optional description of this resource.'], 'required': False}",
    "name": "{'description': ['Name of the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': True}",
    "network": "{'description': ['A reference to the network to which this router belongs.'], 'required': True}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "region": "{'description': ['Region where the router resides.'], 'required': True}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: create a network
  gcp_compute_network:
      name: "network-router"
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: network

- name: create a router
  gcp_compute_router:
      name: "test_object"
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
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
