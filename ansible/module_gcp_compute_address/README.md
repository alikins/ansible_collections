# Ansible module: ansible.module_gcp_compute_address


Creates a GCP Address

## Description

Represents an Address resource.
Each virtual machine instance has an ephemeral internal IP address and, optionally, an external IP address. To communicate between instances on the same network, you can use an instance's internal IP address. To communicate with the Internet and instances outside of the same network, you must specify the instance's external IP address.
Internal IP addresses are ephemeral and only belong to an instance for the lifetime of the instance; if the instance is deleted and recreated, the instance is assigned a new internal IP address, either by Compute Engine or by you. External IP addresses can be either ephemeral or static.

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['The static external IP address represented by this resource. Only IPv4 is supported. An address may only be specified for INTERNAL address types. The IP address must be inside the specified subnetwork, if any.'], 'required': False}",
    "address_type": "{'description': ['The type of address to reserve, either INTERNAL or EXTERNAL.', 'If unspecified, defaults to EXTERNAL.'], 'required': False, 'default': 'EXTERNAL', 'version_added': 2.7, 'choices': ['INTERNAL', 'EXTERNAL']}",
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "description": "{'description': ['An optional description of this resource.'], 'required': False}",
    "name": "{'description': ['Name of the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': True}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "region": "{'description': ['URL of the region where the regional address resides.', 'This field is not applicable to global addresses.'], 'required': True}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "subnetwork": "{'description': ["The URL of the subnetwork in which to reserve the address. If an IP address is specified, it must be within the subnetwork's IP range.", 'This field can only be used with INTERNAL type with GCE_ENDPOINT/DNS_RESOLVER purposes.'], 'required': False, 'version_added': 2.7}",
}
```

## Examples


``` yaml

- name: create a address
  gcp_compute_address:
      name: test-address1
      region: us-west1
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
