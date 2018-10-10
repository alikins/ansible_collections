# Ansible module: ansible.module_ec2_asg_lifecycle_hook


Create, delete or update AWS ASG Lifecycle Hooks

## Description

When no given Hook found, will create one.
In case Hook found, but provided parameters are differes, will update existing Hook.
In case state=absent and Hook exists, will delete it.

## Requirements

TODO

## Arguments

``` json
{
    "autoscaling_group_name": "{'description': ['The name of the Auto Scaling group to which you want to assign the lifecycle hook.'], 'required': True}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "default_result": "{'description': ['Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. This parameter can be either CONTINUE or ABANDON.'], 'required': False, 'choices': ['ABANDON', 'CONTINUE'], 'default': 'ABANDON'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "heartbeat_timeout": "{'description': ['The amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the default action. You can prevent the lifecycle hook from timing out by calling RecordLifecycleActionHeartbeat.'], 'required': False, 'default': '3600 (1 hour)'}",
    "lifecycle_hook_name": "{'description': ['The name of the lifecycle hook.'], 'required': True}",
    "notification_meta_data": "{'description': ['Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.'], 'required': False}",
    "notification_target_arn": "{'description': ['The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This target can be either an SQS queue or an SNS topic. If you specify an empty string, this overrides the current ARN.'], 'required': False}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "role_arn": "{'description': ['The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.'], 'required': False}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Create or delete Lifecycle Hook. Present updates existing one or creates if not found.'], 'required': False, 'choices': ['present', 'absent'], 'default': 'present'}",
    "transition": "{'description': ['The instance state to which you want to attach the lifecycle hook.'], 'required': True, 'choices': ['autoscaling:EC2_INSTANCE_TERMINATING', 'autoscaling:EC2_INSTANCE_LAUNCHING']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Create / Update lifecycle hook
- ec2_asg_lifecycle_hook:
    region: eu-central-1
    state: present
    autoscaling_group_name: example
    lifecycle_hook_name: example
    transition: autoscaling:EC2_INSTANCE_LAUNCHING
    heartbeat_timeout: 7000
    default_result: ABANDON

# Delete lifecycle hook
- ec2_asg_lifecycle_hook:
    region: eu-central-1
    state: absent
    autoscaling_group_name: example
    lifecycle_hook_name: example


```

## License

TODO

## Author Information
  - ["Igor 'Tsigankov' Eyrich (@tsiganenok) <tsiganenok@gmail.com>"]
