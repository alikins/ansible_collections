# Ansible module: ansible.module_gce_net


create/destroy GCE networks and firewall rules

## Description

This module can create and destroy Google Compute Engine networks and firewall rules U(https://cloud.google.com/compute/docs/networking). The I(name) parameter is reserved for referencing a network while the I(fwname) parameter is used to reference firewall rules. IPv4 Address ranges must be specified using the CIDR U(http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) format. Full install/configuration instructions for the gce* modules can be found in the comments of ansible/test/gce_tests.py.

## Requirements

TODO

## Arguments

``` json
{
    "allowed": "{'description': ['the protocol:ports to allow (I(tcp:80) or I(tcp:80,443) or I(tcp:80-800;udp:1-25)) this parameter is mandatory when creating or updating a firewall rule']}",
    "credentials_file": "{'version_added': '2.1.0', 'description': ['path to the JSON file associated with the service account email']}",
    "fwname": "{'description': ['name of the firewall rule'], 'aliases': ['fwrule']}",
    "ipv4_range": "{'description': ['the IPv4 address range in CIDR notation for the network this parameter is not mandatory when you specified existing network in name parameter, but when you create new network, this parameter is mandatory'], 'aliases': ['cidr']}",
    "mode": "{'version_added': '2.2', 'description': ['network mode for Google Cloud C(legacy) indicates a network with an IP address range; C(auto) automatically generates subnetworks in different regions; C(custom) uses networks to group subnets of user specified IP address ranges https://cloud.google.com/compute/docs/networking#network_types'], 'default': 'legacy', 'choices': ['legacy', 'auto', 'custom']}",
    "name": "{'description': ['name of the network']}",
    "pem_file": "{'version_added': '1.6', 'description': ['path to the pem file associated with the service account email This option is deprecated. Use C(credentials_file).']}",
    "project_id": "{'version_added': '1.6', 'description': ['your GCE project ID']}",
    "service_account_email": "{'version_added': '1.6', 'description': ['service account email']}",
    "src_range": "{'description': ['the source IPv4 address range in CIDR notation'], 'default': [], 'aliases': ['src_cidr']}",
    "src_tags": "{'description': ['the source instance tags for creating a firewall rule'], 'default': []}",
    "state": "{'description': ['desired state of the network or firewall'], 'default': 'present', 'choices': ['active', 'present', 'absent', 'deleted']}",
    "subnet_desc": "{'version_added': '2.2', 'description': ['description of subnet to create']}",
    "subnet_name": "{'version_added': '2.2', 'description': ['name of subnet to create']}",
    "subnet_region": "{'version_added': '2.2', 'description': ['region of subnet to create']}",
    "target_tags": "{'version_added': '1.9', 'description': ['the target instance tags for creating a firewall rule'], 'default': []}",
}
```

## Examples


``` yaml

# Create a 'legacy' Network
- name: Create Legacy Network
  gce_net:
    name: legacynet
    ipv4_range: '10.24.17.0/24'
    mode: legacy
    state: present

# Create an 'auto' Network
- name: Create Auto Network
  gce_net:
    name: autonet
    mode: auto
    state: present

# Create a 'custom' Network
- name: Create Custom Network
  gce_net:
    name: customnet
    mode: custom
    subnet_name: "customsubnet"
    subnet_region: us-east1
    ipv4_range: '10.240.16.0/24'
    state: "present"

# Create Firewall Rule with Source Tags
- name: Create Firewall Rule w/Source Tags
  gce_net:
    name: default
    fwname: "my-firewall-rule"
    allowed: tcp:80
    state: "present"
    src_tags: "foo,bar"

# Create Firewall Rule with Source Range
- name: Create Firewall Rule w/Source Range
  gce_net:
    name: default
    fwname: "my-firewall-rule"
    allowed: tcp:80
    state: "present"
    src_range: ['10.1.1.1/32']

# Create Custom Subnetwork
- name: Create Custom Subnetwork
  gce_net:
    name: privatenet
    mode: custom
    subnet_name: subnet_example
    subnet_region: us-central1
    ipv4_range: '10.0.0.0/16'

```

## License

TODO

## Author Information
  - ['Eric Johnson (@erjohnso) <erjohnso@google.com>, Tom Melendez (@supertom) <supertom@google.com>']
