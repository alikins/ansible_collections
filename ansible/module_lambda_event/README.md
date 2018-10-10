# Ansible module: ansible.module_lambda_event


Creates, updates or deletes AWS Lambda function event mappings

## Description

This module allows the management of AWS Lambda function event source mappings such as DynamoDB and Kinesis stream events via the Ansible framework. These event source mappings are relevant only in the AWS Lambda pull model, where AWS Lambda invokes the function. It is idempotent and supports "Check" mode.  Use module M(lambda) to manage the lambda function itself and M(lambda_alias) to manage function aliases.

## Requirements

TODO

## Arguments

``` json
{
    "alias": "{'description': ['Name of the function alias. Mutually exclusive with C(version).'], 'required': True}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "event_source": "{'description': ['Source of the event that triggers the lambda function.', "For DynamoDB and Kinesis events, select 'stream'", "For SQS queues, select 'sqs'"], 'required': False, 'default': 'stream', 'choices': ['stream', 'sqs']}",
    "lambda_function_arn": "{'description': ['The name or ARN of the lambda function.'], 'required': True, 'aliases': ['function_name', 'function_arn']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "source_params": "{'description': ['Sub-parameters required for event source.', 'I(== stream event source ==)', 'C(source_arn) The Amazon Resource Name (ARN) of the Kinesis or DynamoDB stream that is the event source.', 'C(enabled) Indicates whether AWS Lambda should begin polling the event source. Default is True.', 'C(batch_size) The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Default is 100.', 'C(starting_position) The position in the stream where AWS Lambda should start reading. Choices are TRIM_HORIZON or LATEST.', 'I(== sqs event source ==)', 'C(source_arn) The Amazon Resource Name (ARN) of the SQS queue to read events from.', 'C(enabled) Indicates whether AWS Lambda should begin reading from the event source. Default is True.', 'C(batch_size) The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Default is 100.'], 'required': True}",
    "state": "{'description': ['Describes the desired state.'], 'required': True, 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "version": "{'description': ['Version of the Lambda function. Mutually exclusive with C(alias).'], 'required': False}",
}
```

## Examples


``` yaml

---
# Example that creates a lambda event notification for a DynamoDB stream
- hosts: localhost
  gather_facts: no
  vars:
    state: present
  tasks:
  - name: DynamoDB stream event mapping
    lambda_event:
      state: "{{ state | default('present') }}"
      event_source: stream
      function_name: "{{ function_name }}"
      alias: Dev
      source_params:
        source_arn: arn:aws:dynamodb:us-east-1:123456789012:table/tableName/stream/2016-03-19T19:51:37.457
        enabled: True
        batch_size: 100
        starting_position: TRIM_HORIZON

  - name: Show source event
    debug:
      var: lambda_stream_events

```

## License

TODO

## Author Information
  - ['Pierre Jodouin (@pjodouin), Ryan Brown (@ryansb)']
