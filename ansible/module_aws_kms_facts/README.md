# Ansible module: ansible.module_aws_kms_facts


Gather facts about AWS KMS keys

## Description

Gather facts about AWS KMS keys including tags and grants

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "filters": "{'description': ["A dict of filters to apply. Each dict item consists of a filter key and a filter value. The filters aren't natively supported by boto3, but are supported to provide similar functionality to other modules. Standard tag filters (C(tag-key), C(tag-value) and C(tag:tagName)) are available, as are C(key-id) and C(alias)"]}",
    "pending_deletion": "{'description': ['Whether to get full details (tags, grants etc.) of keys pending deletion'], 'default': False}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Gather facts about all KMS keys
- aws_kms_facts

# Gather facts about all keys with a Name tag
- aws_kms_facts:
    filters:
      tag-key: Name

# Gather facts about all keys with a specific name
- aws_kms_facts:
    filters:
      "tag:Name": Example

```

## License

TODO

## Author Information
  - ['Will Thames (@willthames)']
