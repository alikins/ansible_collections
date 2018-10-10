# Ansible module: ansible.module_gcp_dns_managed_zone


Creates a GCP ManagedZone

## Description

A zone is a subtree of the DNS namespace under one administrative responsibility. A ManagedZone is a resource that represents a DNS zone hosted by the Cloud DNS service.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "description": "{'description': ["A mutable string of at most 1024 characters associated with this resource for the user's convenience. Has no effect on the managed zone's function."], 'required': False}",
    "dns_name": "{'description': ['The DNS name of this managed zone, for instance "example.com.".'], 'required': False}",
    "name": "{'description': ['User assigned name for this resource.', 'Must be unique within the project.'], 'required': True}",
    "name_server_set": "{'description': ['Optionally specifies the NameServerSet for this ManagedZone. A NameServerSet is a set of DNS name servers that all host the same ManagedZones. Most users will leave this field unset.'], 'required': False}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: create a managed zone
  gcp_dns_managed_zone:
      name: "test_object"
      dns_name: test.somewild2.example.com.
      description: test zone
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
