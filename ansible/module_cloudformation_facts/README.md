# Ansible module: ansible.module_cloudformation_facts


Obtain facts about an AWS CloudFormation stack

## Description

Gets information about an AWS CloudFormation stack

## Requirements

TODO

## Arguments

``` json
{
    "all_facts": "{'description': ['Get all stack information for the stack'], 'default': 'no'}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "stack_events": "{'description': ['Get stack events for the stack'], 'default': 'no'}",
    "stack_name": "{'description': ['The name or id of the CloudFormation stack. Gathers facts for all stacks by default.']}",
    "stack_policy": "{'description': ['Get stack policy for the stack'], 'default': 'no'}",
    "stack_resources": "{'description': ['Get stack resources for the stack'], 'default': 'no'}",
    "stack_template": "{'description': ['Get stack template body for the stack'], 'default': 'no'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Get summary information about a stack
- cloudformation_facts:
    stack_name: my-cloudformation-stack

# Facts are published in ansible_facts['cloudformation'][<stack_name>]
- debug:
    msg: "{{ ansible_facts['cloudformation']['my-cloudformation-stack'] }}"

# Get stack outputs, when you have the stack name available as a fact
- set_fact:
    stack_name: my-awesome-stack

- cloudformation_facts:
    stack_name: "{{ stack_name }}"
  register: my_stack

- debug:
    msg: "{{ my_stack.ansible_facts.cloudformation[stack_name].stack_outputs }}"

# Get all stack information about a stack
- cloudformation_facts:
    stack_name: my-cloudformation-stack
    all_facts: true

# Get stack resource and stack policy information about a stack
- cloudformation_facts:
    stack_name: my-cloudformation-stack
    stack_resources: true
    stack_policy: true

# Fail if the stack doesn't exist
- name: try to get facts about a stack but fail if it doesn't exist
  cloudformation_facts:
    stack_name: nonexistent-stack
    all_facts: yes
  failed_when: cloudformation['nonexistent-stack'] is undefined

# Example dictionary outputs for stack_outputs, stack_parameters and stack_resources:
# "stack_outputs": {
#     "ApplicationDatabaseName": "dazvlpr01xj55a.ap-southeast-2.rds.amazonaws.com",
#     ...
# },
# "stack_parameters": {
#     "DatabaseEngine": "mysql",
#     "DatabasePassword": "****",
#     ...
# },
# "stack_resources": {
#     "AutoscalingGroup": "dev-someapp-AutoscalingGroup-1SKEXXBCAN0S7",
#     "AutoscalingSecurityGroup": "sg-abcd1234",
#     "ApplicationDatabase": "dazvlpr01xj55a",
#     "EcsTaskDefinition": "arn:aws:ecs:ap-southeast-2:123456789:task-definition/dev-someapp-EcsTaskDefinition-1F2VM9QB0I7K9:1"
#     ...
# }

```

## License

TODO

## Author Information
  - ['Justin Menga (@jmenga)']
