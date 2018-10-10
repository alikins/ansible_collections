# Ansible module: ansible.module_ec2_ami_facts


Gather facts about ec2 AMIs

## Description

G
a
t
h
e
r
 
f
a
c
t
s
 
a
b
o
u
t
 
e
c
2
 
A
M
I
s

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "describe_image_attributes": "{'description': ['Describe attributes (like launchPermission) of the images found.'], 'default': False, 'type': 'bool'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "executable_users": "{'description': ['Filter images by users with explicit launch permissions. Valid options are an AWS account ID, self, or all (public AMIs).'], 'aliases': ['executable_user']}",
    "filters": "{'description': ['A dict of filters to apply. Each dict item consists of a filter key and a filter value.', 'See U(https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html) for possible filters.', 'Filter names and values are case sensitive.']}",
    "image_ids": "{'description': ['One or more image IDs.'], 'aliases': ['image_id']}",
    "owners": "{'description': ['Filter the images by the owner. Valid options are an AWS account ID, self,', 'or an AWS owner alias ( amazon | aws-marketplace | microsoft ).'], 'aliases': ['owner']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: gather facts about an AMI using ami-id
  ec2_ami_facts:
    image_ids: ami-5b488823

- name: gather facts about all AMIs with tag key Name and value webapp
  ec2_ami_facts:
    filters:
      "tag:Name": webapp

- name: gather facts about an AMI with 'AMI Name' equal to foobar
  ec2_ami_facts:
    filters:
      name: foobar

- name: gather facts about Ubuntu 17.04 AMIs published by Canonical (099720109477)
  ec2_ami_facts:
    owners: 099720109477
    filters:
      name: "ubuntu/images/ubuntu-zesty-17.04-*"

```

## License

TODO

## Author Information
  - ['Prasad Katti, @prasadkatti']
