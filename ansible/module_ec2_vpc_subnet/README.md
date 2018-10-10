# Ansible module: ansible.module_ec2_vpc_subnet


Manage subnets in AWS virtual private clouds

## Description

Manage subnets in AWS virtual private clouds

## Requirements

TODO

## Arguments

``` json
{
    "assign_instances_ipv6": "{'description': ['Specify C(yes) to indicate that instances launched into the subnet should be automatically assigned an IPv6 address.'], 'type': 'bool', 'default': False, 'version_added': '2.5'}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "az": "{'description': ['The availability zone for the subnet.']}",
    "cidr": "{'description': ['The CIDR block for the subnet. E.g. 192.0.2.0/24.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "ipv6_cidr": "{'description': ['The IPv6 CIDR block for the subnet. The VPC must have a /56 block assigned and this value must be a valid IPv6 /64 that falls in the VPC range.', 'Required if I(assign_instances_ipv6=true)'], 'version_added': '2.5'}",
    "map_public": "{'description': ['Specify C(yes) to indicate that instances launched into the subnet should be assigned public IP address by default.'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_tags": "{'description': ['Whether or not to remove tags that do not appear in the I(tags) list.'], 'type': 'bool', 'default': True, 'version_added': '2.5'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Create or remove the subnet'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tags": "{'description': ['A dict of tags to apply to the subnet. Any tags currently applied to the subnet and not present here will be removed.'], 'aliases': ['resource_tags']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "vpc_id": "{'description': ['VPC ID of the VPC in which to create or delete the subnet.'], 'required': True}",
    "wait": "{'description': ['When specified,I(state=present) module will wait for subnet to be in available state before continuing.'], 'type': 'bool', 'default': True, 'version_added': '2.5'}",
    "wait_timeout": "{'description': ['Number of seconds to wait for subnet to become available I(wait=True).'], 'default': 300, 'version_added': '2.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Create subnet for database servers
  ec2_vpc_subnet:
    state: present
    vpc_id: vpc-123456
    cidr: 10.0.1.16/28
    resource_tags:
      Name: Database Subnet
  register: database_subnet

- name: Remove subnet for database servers
  ec2_vpc_subnet:
    state: absent
    vpc_id: vpc-123456
    cidr: 10.0.1.16/28

- name: Create subnet with IPv6 block assigned
  ec2_vpc_subnet:
    state: present
    vpc_id: vpc-123456
    cidr: 10.1.100.0/24
    ipv6_cidr: 2001:db8:0:102::/64

- name: Remove IPv6 block assigned to subnet
  ec2_vpc_subnet:
    state: present
    vpc_id: vpc-123456
    cidr: 10.1.100.0/24
    ipv6_cidr: ''

```

## License

TODO

## Author Information
  - ['Robert Estelle (@erydo)', 'Brad Davidson (@brandond)']
  - ['Robert Estelle (@erydo)', 'Brad Davidson (@brandond)']
