# Ansible module: ansible.module_gcp_compute_subnetwork


Creates a GCP Subnetwork

## Description

A VPC network is a virtual version of the traditional physical networks that exist within and between physical data centers. A VPC network provides connectivity for your Compute Engine virtual machine (VM) instances, Container Engine containers, App Engine Flex services, and other network-related resources.
Each GCP project contains one or more VPC networks. Each VPC network is a global entity spanning all GCP regions. This global VPC network allows VM instances and other resources to communicate with each other via internal, private IP addresses.
Each VPC network is subdivided into subnets, and each subnet is contained within a single region. You can have more than one subnet in a region for a given VPC network. Each subnet has a contiguous private RFC1918 IP space. You create instances, containers, and the like in these subnets.
When you create an instance, you must create it in a subnet, and the instance draws its internal IP address from that subnet.
Virtual machine (VM) instances in a VPC network can communicate with instances in all other subnets of the same VPC network, regardless of region, using their RFC1918 private IP addresses. You can isolate portions of the network, even entire subnets, using firewall rules.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "description": "{'description': ['An optional description of this resource. Provide this property when you create the resource. This field can be set only at resource creation time.'], 'required': False}",
    "ip_cidr_range": "{'description': ['The range of internal addresses that are owned by this subnetwork.', 'Provide this property when you create the subnetwork. For example, 10.0.0.0/8 or 192.168.0.0/16. Ranges must be unique and non-overlapping within a network. Only IPv4 is supported.'], 'required': True}",
    "name": "{'description': ['The name of the resource, provided by the client when initially creating the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': True}",
    "network": "{'description': ['The network this subnet belongs to.', 'Only networks that are in the distributed mode can have subnetworks.'], 'required': True}",
    "private_ip_google_access": "{'description': ['Whether the VMs in this subnet can access Google services without assigned external IP addresses.'], 'required': False, 'type': 'bool'}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "region": "{'description': ['URL of the GCP region for this subnetwork.'], 'required': True}",
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
      name: "network-subnetwork"
      auto_create_subnetworks: true
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: network

- name: create a subnetwork
  gcp_compute_subnetwork:
      name: ansiblenet
      region: us-west1
      network: "{{ network }}"
      ip_cidr_range: 172.16.0.0/16
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
