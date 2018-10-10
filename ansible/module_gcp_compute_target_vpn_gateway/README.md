# Ansible module: ansible.module_gcp_compute_target_vpn_gateway


Creates a GCP TargetVpnGateway

## Description

Represents a VPN gateway running in GCP. This virtual device is managed by Google, but used only by you.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "description": "{'description': ['An optional description of this resource.'], 'required': False}",
    "name": "{'description': ['Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035.  Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': True}",
    "network": "{'description': ['The network this VPN gateway is accepting traffic for.'], 'required': True}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "region": "{'description': ['The region this gateway should sit in.'], 'required': True}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: create a address
  gcp_compute_address:
      name: "address-vpngateway"
      region: us-west1
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: address

- name: create a network
  gcp_compute_network:
      name: "network-vpngateway"
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: network

- name: create a target vpn gateway
  gcp_compute_target_vpn_gateway:
      name: "test_object"
      region: us-west1
      network: "{{ network }}"
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
