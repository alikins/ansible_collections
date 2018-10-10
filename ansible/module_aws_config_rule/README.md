# Ansible module: ansible.module_aws_config_rule


Manage AWS Config resources

## Description

Module manages AWS Config rules

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "description": "{'description': ['The description that you provide for the AWS Config rule.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "execution_frequency": "{'description': ['The maximum frequency with which AWS Config runs evaluations for a rule.'], 'choices': ['One_Hour', 'Three_Hours', 'Six_Hours', 'Twelve_Hours', 'TwentyFour_Hours']}",
    "input_parameters": "{'description': ['A string, in JSON format, that is passed to the AWS Config rule Lambda function.']}",
    "name": "{'description': ['The name of the AWS Config resource.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "scope": "{'description': ['Defines which resources can trigger an evaluation for the rule.'], 'suboptions': {'compliance_types': {'description': ['The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for `compliance_id`.']}, 'compliance_id': {'description': ['The ID of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for `compliance_types`.']}, 'tag_key': {'description': ['The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule.']}, 'tag_value': {'description': ['The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule. If you specify a value for `tag_value`, you must also specify a value for `tag_key`.']}}}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "source": "{'description': ['Provides the rule owner (AWS or customer), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.'], 'suboptions': {'owner': {'description': ['The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for `compliance_id`.']}, 'identifier': {'description': ['The ID of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for `compliance_types`.']}, 'details': {'description': ['Provides the source and type of the event that causes AWS Config to evaluate your AWS resources.', 'This parameter expects a list of dictionaries.  Each dictionary expects the following key/value pairs.', 'Key `EventSource` The source of the event, such as an AWS service, that triggers AWS Config to evaluate your AWS resources.', 'Key `MessageType` The type of notification that triggers AWS Config to run an evaluation for a rule.', 'Key `MaximumExecutionFrequency` The frequency at which you want AWS Config to run evaluations for a custom rule with a periodic trigger.']}}}",
    "state": "{'description': ['Whether the Config rule should be present or absent.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

- name: Create Config Rule for AWS Config
  aws_config_rule:
    name: test_config_rule
    state: present
    description: 'This AWS Config rule checks for public write access on S3 buckets'
    scope:
        compliance_types:
            - 'AWS::S3::Bucket'
    source:
        owner: AWS
        identifier: 'S3_BUCKET_PUBLIC_WRITE_PROHIBITED'


```

## License

TODO

## Author Information
  - ['Aaron Smith (@slapula)']
