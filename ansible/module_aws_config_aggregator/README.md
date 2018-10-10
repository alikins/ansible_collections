# Ansible module: ansible.module_aws_config_aggregator


Manage AWS Config aggregations across multiple accounts

## Description

Module manages AWS Config resources

## Requirements

TODO

## Arguments

``` json
{
    "account_sources": "{'description': ['Provides a list of source accounts and regions to be aggregated.'], 'suboptions': {'account_ids': {'description': ['A list of 12-digit account IDs of accounts being aggregated.']}, 'aws_regions': {'description': ['A list of source regions being aggregated.']}, 'all_aws_regions': {'description': ['If true, aggreagate existing AWS Config regions and future regions.']}}}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "name": "{'description': ['The name of the AWS Config resource.'], 'required': True}",
    "organization_source": "{'description': ['The region authorized to collect aggregated data.'], 'suboptions': {'role_arn': {'description': ['ARN of the IAM role used to retreive AWS Organization details associated with the aggregator account.']}, 'aws_regions': {'description': ['The source regions being aggregated.']}, 'all_aws_regions': {'description': ['If true, aggreagate existing AWS Config regions and future regions.']}}}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Whether the Config rule should be present or absent.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

- name: Create cross-account aggregator
  aws_config_aggregator:
    name: test_config_rule
    state: present
    account_sources:
      account_ids:
      - 1234567890
      - 0123456789
      - 9012345678
      all_aws_regions: yes

```

## License

TODO

## Author Information
  - ['Aaron Smith (@slapula)']
