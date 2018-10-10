# Ansible module: ansible.module_cloudwatchevent_rule


Manage CloudWatch Event rules and targets

## Description

This module creates and manages CloudWatch event rules and targets.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "description": "{'description': ['A description of the rule'], 'required': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "event_pattern": "{'description': ['A string pattern (in valid JSON format) that is used to match against incoming events to determine if the rule should be triggered'], 'required': False}",
    "name": "{'description': ['The name of the rule you are creating, updating or deleting. No spaces or special characters allowed (i.e. must match C([\\.\\-_A-Za-z0-9]+))'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "role_arn": "{'description': ['The Amazon Resource Name (ARN) of the IAM role associated with the rule'], 'required': False}",
    "schedule_expression": "{'description': ['A cron or rate expression that defines the schedule the rule will trigger on. For example, C(cron(0 20 * * ? *)), C(rate(5 minutes))'], 'required': False}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Whether the rule is present (and enabled), disabled, or absent'], 'choices': ['present', 'disabled', 'absent'], 'default': 'present', 'required': False}",
    "targets": "{'description': ['A dictionary array of targets to add to or update for the rule, in the form C({ id: [string], arn: [string], role_arn: [string], input: [valid JSON string], input_path: [valid JSONPath string], ecs_parameters: {task_definition_arn: [string], task_count: [int]}}). I(id) [required] is the unique target assignment ID. I(arn) (required) is the Amazon Resource Name associated with the target. I(role_arn) (optional) is The Amazon Resource Name of the IAM role to be used for this target when the rule is triggered. I(input) (optional) is a JSON object that will override the event data when passed to the target.  I(input_path) (optional) is a JSONPath string (e.g. C($.detail)) that specifies the part of the event data to be passed to the target. If neither I(input) nor I(input_path) is specified, then the entire event is passed to the target in JSON form. I(task_definition_arn) [optional] is ecs task definition arn. I(task_count) [optional] is ecs task count.'], 'required': False}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

- cloudwatchevent_rule:
    name: MyCronTask
    schedule_expression: "cron(0 20 * * ? *)"
    description: Run my scheduled task
    targets:
      - id: MyTargetId
        arn: arn:aws:lambda:us-east-1:123456789012:function:MyFunction

- cloudwatchevent_rule:
    name: MyDisabledCronTask
    schedule_expression: "rate(5 minutes)"
    description: Run my disabled scheduled task
    state: disabled
    targets:
      - id: MyOtherTargetId
        arn: arn:aws:lambda:us-east-1:123456789012:function:MyFunction
        input: '{"foo": "bar"}'

- cloudwatchevent_rule:
    name: MyCronTask
    state: absent

```

## License

TODO

## Author Information
  - ['Jim Dalton (@jsdalton) <jim.dalton@gmail.com>']
