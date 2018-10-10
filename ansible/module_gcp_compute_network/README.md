# Ansible module: ansible.module_gcp_compute_network


Creates a GCP Network

## Description

Represents a Network resource.
Your Cloud Platform Console project can contain multiple networks, and each network can have multiple instances attached to it. A network allows you to define a gateway IP and the network range for the instances attached to that network. Every project is provided with a default network with preset configurations and firewall rules. You can choose to customize the default network by adding or removing rules, or you can create new networks in that project. Generally, most users only need one network, although you can have up to five networks per project by default.
A network belongs to only one project, and each instance can only belong to one network. All Compute Engine networks use the IPv4 protocol. Compute Engine currently does not support IPv6. However, Google is a major advocate of IPv6 and it is an important future direction.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "auto_create_subnetworks": "{'description': ['When set to true, the network is created in "auto subnet mode". When set to false, the network is in "custom subnet mode".', 'In "auto subnet mode", a newly created network is assigned the default CIDR of 10.128.0.0/9 and it automatically creates one subnetwork per region.'], 'required': False, 'type': 'bool'}",
    "description": "{'description': ['An optional description of this resource. Provide this property when you create the resource.'], 'required': False}",
    "gateway_ipv4": "{'description': ['A gateway address for default routing to other networks. This value is read only and is selected by the Google Compute Engine, typically as the first usable address in the IPv4Range.'], 'required': False}",
    "ipv4_range": "{'description': ['The range of internal addresses that are legal on this network. This range is a CIDR specification, for example: 192.168.0.0/16. Provided by the client when the network is created.'], 'required': False}",
    "name": "{'description': ['Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': False}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
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
      name: "test_object"
      auto_create_subnetworks: true
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
