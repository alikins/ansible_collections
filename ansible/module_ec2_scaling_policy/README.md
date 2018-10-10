# Ansible module: ansible.module_ec2_scaling_policy


Create or delete AWS scaling policies for Autoscaling groups

## Description

Can create or delete scaling policies for autoscaling groups
Referenced autoscaling groups must already exist

## Requirements

TODO

## Arguments

``` json
{
    "adjustment_type": "{'description': ['The type of change in capacity of the autoscaling group'], 'required': False, 'choices': ['ChangeInCapacity', 'ExactCapacity', 'PercentChangeInCapacity']}",
    "asg_name": "{'description': ['Name of the associated autoscaling group'], 'required': True}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "cooldown": "{'description': ['The minimum period of time between which autoscaling actions can take place'], 'required': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "min_adjustment_step": "{'description': ['Minimum amount of adjustment when policy is triggered'], 'required': False}",
    "name": "{'description': ['Unique name for the scaling policy'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "scaling_adjustment": "{'description': ['The amount by which the autoscaling group is adjusted by the policy'], 'required': False}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['register or deregister the policy'], 'required': True, 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

- ec2_scaling_policy:
    state: present
    region: US-XXX
    name: "scaledown-policy"
    adjustment_type: "ChangeInCapacity"
    asg_name: "slave-pool"
    scaling_adjustment: -1
    min_adjustment_step: 1
    cooldown: 300

```

## License

TODO

## Author Information
  - ['Zacharie Eakin (@zeekin)']
