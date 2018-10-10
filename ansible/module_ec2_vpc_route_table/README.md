# Ansible module: ansible.module_ec2_vpc_route_table


Manage route tables for AWS virtual private clouds

## Description

Manage route tables for AWS virtual private clouds

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "lookup": "{'description': ['Look up route table by either tags or by route table ID. Non-unique tag lookup will fail. If no tags are specified then no lookup for an existing route table is performed and a new route table will be created. To change tags of a route table you must look up by id.'], 'default': 'tag', 'choices': ['tag', 'id']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "propagating_vgw_ids": "{'description': ['Enable route propagation from virtual gateways specified by ID.']}",
    "purge_routes": "{'version_added': '2.3', 'description': ['Purge existing routes that are not found in routes.'], 'type': 'bool', 'default': True}",
    "purge_subnets": "{'version_added': '2.3', 'description': ['Purge existing subnets that are not found in subnets. Ignored unless the subnets option is supplied.'], 'default': 'true'}",
    "purge_tags": "{'version_added': '2.5', 'description': ['Purge existing tags that are not found in route table'], 'type': 'bool', 'default': False}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "route_table_id": "{'description': ['The ID of the route table to update or delete.']}",
    "routes": "{'description': ["List of routes in the route table. Routes are specified as dicts containing the keys 'dest' and one of 'gateway_id', 'instance_id', 'network_interface_id', or 'vpc_peering_connection_id'. If 'gateway_id' is specified, you can refer to the VPC's IGW by using the value 'igw'. Routes are required for present states."]}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Create or destroy the VPC route table'], 'default': 'present', 'choices': ['present', 'absent']}",
    "subnets": "{'description': ["An array of subnets to add to this route table. Subnets may be specified by either subnet ID, Name tag, or by a CIDR such as '10.0.0.0/24'."]}",
    "tags": "{'description': ['A dictionary of resource tags of the form: { tag1: value1, tag2: value2 }. Tags are used to uniquely identify route tables within a VPC when the route_table_id is not supplied.\n'], 'aliases': ['resource_tags']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "vpc_id": "{'description': ['VPC ID of the VPC in which to create the route table.'], 'required': True}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Basic creation example:
- name: Set up public subnet route table
  ec2_vpc_route_table:
    vpc_id: vpc-1245678
    region: us-west-1
    tags:
      Name: Public
    subnets:
      - "{{ jumpbox_subnet.subnet.id }}"
      - "{{ frontend_subnet.subnet.id }}"
      - "{{ vpn_subnet.subnet_id }}"
    routes:
      - dest: 0.0.0.0/0
        gateway_id: "{{ igw.gateway_id }}"
  register: public_route_table

- name: Set up NAT-protected route table
  ec2_vpc_route_table:
    vpc_id: vpc-1245678
    region: us-west-1
    tags:
      Name: Internal
    subnets:
      - "{{ application_subnet.subnet.id }}"
      - 'Database Subnet'
      - '10.0.0.0/8'
    routes:
      - dest: 0.0.0.0/0
        instance_id: "{{ nat.instance_id }}"
  register: nat_route_table

- name: delete route table
  ec2_vpc_route_table:
    vpc_id: vpc-1245678
    region: us-west-1
    route_table_id: "{{ route_table.id }}"
    lookup: id
    state: absent

```

## License

TODO

## Author Information
  - ['Robert Estelle (@erydo)', 'Rob White (@wimnat)', 'Will Thames (@willthames)']
  - ['Robert Estelle (@erydo)', 'Rob White (@wimnat)', 'Will Thames (@willthames)']
  - ['Robert Estelle (@erydo)', 'Rob White (@wimnat)', 'Will Thames (@willthames)']
