# Ansible module: ansible.module_cloudtrail


manage CloudTrail create, delete, update

## Description

Creates, deletes, or updates CloudTrail configuration. Ensures logging is also enabled.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "cloudwatch_logs_log_group_arn": "{'description': ['A full ARN specifying a valid CloudWatch log group to which CloudTrail logs will be delivered. The log group should already exist.', 'See U(https://docs.aws.amazon.com/awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.html)', 'Required when C(cloudwatch_logs_role_arn)'], 'version_added': '2.4'}",
    "cloudwatch_logs_role_arn": "{'description': ['Specifies a full ARN for an IAM role that assigns the proper permissions for CloudTrail to create and write to the log group.', 'See U(https://docs.aws.amazon.com/awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.html)', 'Required when C(cloudwatch_logs_log_group_arn)'], 'version_added': '2.4'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "enable_log_file_validation": "{'description': ['Specifies whether log file integrity validation is enabled.', 'CloudTrail will create a hash for every log file delivered and produce a signed digest file that can be used to ensure log files have not been tampered.'], 'version_added': '2.4', 'aliases': ['log_file_validation_enabled']}",
    "enable_logging": "{'description': ['Start or stop the CloudTrail logging. If stopped the trail will be paused and will not record events or deliver log files.'], 'default': True, 'version_added': '2.4'}",
    "include_global_events": "{'description': ['Record API calls from global services such as IAM and STS.'], 'default': True, 'aliases': ['include_global_service_events']}",
    "is_multi_region_trail": "{'description': ['Specify whether the trail belongs only to one region or exists in all regions.'], 'default': False, 'version_added': '2.4'}",
    "kms_key_id": "{'description': ['Specifies the KMS key ID to use to encrypt the logs delivered by CloudTrail. This also has the effect of enabling log file encryption.', 'The value can be an alias name prefixed by "alias/", a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.', 'See U(https://docs.aws.amazon.com/awscloudtrail/latest/userguide/encrypting-cloudtrail-log-files-with-aws-kms.html)'], 'version_added': '2.4'}",
    "name": "{'description': ['Name for the CloudTrail.', 'Names are unique per-region unless the CloudTrail is a multi-region trail, in which case it is unique per-account.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "s3_bucket_name": "{'description': ['An existing S3 bucket where CloudTrail will deliver log files.', 'This bucket should exist and have the proper policy.', 'See U(http://docs.aws.amazon.com/awscloudtrail/latest/userguide/aggregating_logs_regions_bucket_policy.html)', 'Required when C(state=present)'], 'version_added': '2.4'}",
    "s3_key_prefix": "{'description': ['S3 Key prefix for delivered log files. A trailing slash is not necessary and will be removed.']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "sns_topic_name": "{'description': ['SNS Topic name to send notifications to when a log file is delivered'], 'version_added': '2.4'}",
    "state": "{'description': ['Add or remove CloudTrail configuration.', 'The following states have been preserved for backwards compatibility. C(state=enabled) and C(state=disabled).', 'enabled=present and disabled=absent.'], 'required': True, 'choices': ['present', 'absent', 'enabled', 'disabled']}",
    "tags": "{'description': ['A hash/dictionary of tags to be applied to the CloudTrail resource.', 'Remove completely or specify an empty dictionary to remove all tags.'], 'default': {}, 'version_added': '2.4'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

- name: create single region cloudtrail
  cloudtrail:
    state: present
    name: default
    s3_bucket_name: mylogbucket
    s3_key_prefix: cloudtrail
    region: us-east-1

- name: create multi-region trail with validation and tags
  cloudtrail:
    state: present
    name: default
    s3_bucket_name: mylogbucket
    region: us-east-1
    is_multi_region_trail: true
    enable_log_file_validation: true
    cloudwatch_logs_role_arn: "arn:aws:iam::123456789012:role/CloudTrail_CloudWatchLogs_Role"
    cloudwatch_logs_log_group_arn: "arn:aws:logs:us-east-1:123456789012:log-group:CloudTrail/DefaultLogGroup:*"
    kms_key_id: "alias/MyAliasName"
    tags:
      environment: dev
      Name: default

- name: show another valid kms_key_id
  cloudtrail:
    state: present
    name: default
    s3_bucket_name: mylogbucket
    kms_key_id: "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
    # simply "12345678-1234-1234-1234-123456789012" would be valid too.

- name: pause logging the trail we just created
  cloudtrail:
    state: present
    name: default
    enable_logging: false
    s3_bucket_name: mylogbucket
    region: us-east-1
    is_multi_region_trail: true
    enable_log_file_validation: true
    tags:
      environment: dev
      Name: default

- name: delete a trail
  cloudtrail:
    state: absent
    name: default

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Ted Timmons (@tedder)', 'Daniel Shepherd (@shepdelacreme)']
  - ['Ansible Core Team', 'Ted Timmons (@tedder)', 'Daniel Shepherd (@shepdelacreme)']
  - ['Ansible Core Team', 'Ted Timmons (@tedder)', 'Daniel Shepherd (@shepdelacreme)']
