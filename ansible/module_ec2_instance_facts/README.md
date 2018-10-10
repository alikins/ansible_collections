# Ansible module: ansible.module_ec2_instance_facts


Gather facts about ec2 instances in AWS

## Description

Gather facts about ec2 instances in AWS

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "filters": "{'description': ['A dict of filters to apply. Each dict item consists of a filter key and a filter value. See U(http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html) for possible filters. Filter names and values are case sensitive.'], 'required': False, 'default': {}}",
    "instance_ids": "{'description': ['If you specify one or more instance IDs, only instances that have the specified IDs are returned.'], 'required': False, 'version_added': 2.4}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Gather facts about all instances
- ec2_instance_facts:

# Gather facts about all instances in AZ ap-southeast-2a
- ec2_instance_facts:
    filters:
      availability-zone: ap-southeast-2a

# Gather facts about a particular instance using ID
- ec2_instance_facts:
    instance_ids:
      - i-12345678

# Gather facts about any instance with a tag key Name and value Example
- ec2_instance_facts:
    filters:
      "tag:Name": Example

```

## License

TODO

## Author Information
  - ['Michael Schuett (@michaeljs1990)', 'Rob White (@wimnat)']
  - ['Michael Schuett (@michaeljs1990)', 'Rob White (@wimnat)']
