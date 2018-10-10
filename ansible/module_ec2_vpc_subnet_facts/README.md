# Ansible module: ansible.module_ec2_vpc_subnet_facts


Gather facts about ec2 VPC subnets in AWS

## Description

Gather facts about ec2 VPC subnets in AWS

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "filters": "{'description': ['A dict of filters to apply. Each dict item consists of a filter key and a filter value. See U(http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html) for possible filters.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "subnet_ids": "{'description': ['A list of subnet IDs to gather facts for.'], 'version_added': '2.5', 'aliases': ['subnet_id']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Gather facts about all VPC subnets
- ec2_vpc_subnet_facts:

# Gather facts about a particular VPC subnet using ID
- ec2_vpc_subnet_facts:
    subnet_ids: subnet-00112233

# Gather facts about any VPC subnet with a tag key Name and value Example
- ec2_vpc_subnet_facts:
    filters:
      "tag:Name": Example

# Gather facts about any VPC subnet within VPC with ID vpc-abcdef00
- ec2_vpc_subnet_facts:
    filters:
      vpc-id: vpc-abcdef00

# Gather facts about a set of VPC subnets, publicA, publicB and publicC within a
# VPC with ID vpc-abcdef00 and then use the jinja map function to return the
# subnet_ids as a list.

- ec2_vpc_subnet_facts:
    filters:
      vpc-id: vpc-abcdef00
      "tag:Name": "{{ item }}"
  with_items:
    - publicA
    - publicB
    - publicC
  register: subnet_facts

- set_fact:
    subnet_ids: "{{ subnet_facts.subnets|map(attribute='id')|list }}"

```

## License

TODO

## Author Information
  - ['Rob White (@wimnat)']
