# Ansible module: ansible.module_aws_config_recorder


Manage AWS Config Recorders

## Description

Module manages AWS Config configuration recorder settings

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "name": "{'description': ['The name of the AWS Config resource.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "recording_group": "{'description': ['Specifies the types of AWS resources for which AWS Config records configuration changes.', 'Required when state=present'], 'suboptions': {'all_supported': {'description': ['Specifies whether AWS Config records configuration changes for every supported type of regional resource.', 'If you set this option to `true`, when AWS Config adds support for a new type of regional resource, it starts recording resources of that type automatically.', 'If you set this option to `true`, you cannot enumerate a list of `resource_types`.']}, 'include_global_types': {'description': ['Specifies whether AWS Config includes all supported types of global resources (for example, IAM resources) with the resources that it records.', 'Before you can set this option to `true`, you must set the allSupported option to `true`.', 'If you set this option to `true`, when AWS Config adds support for a new type of global resource, it starts recording resources of that type automatically.', 'The configuration details for any global resource are the same in all regions. To prevent duplicate configuration items, you should consider customizing AWS Config in only one region to record global resources.']}, 'resource_types': {'description': ['A list that specifies the types of AWS resources for which AWS Config records configuration changes (for example, `AWS::EC2::Instance` or `AWS::CloudTrail::Trail`).', 'Before you can set this option to `true`, you must set the `all_supported` option to `false`.']}}}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "role_arn": "{'description': ['Amazon Resource Name (ARN) of the IAM role used to describe the AWS resources associated with the account.', 'Required when state=present']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Whether the Config rule should be present or absent.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

- name: Create Configuration Recorder for AWS Config
  aws_config_recorder:
    name: test_configuration_recorder
    state: present
    role_arn: 'arn:aws:iam::123456789012:role/AwsConfigRecorder'
    recording_group:
        all_supported: true
        include_global_types: true

```

## License

TODO

## Author Information
  - ['Aaron Smith (@slapula)']
