# Ansible module: ansible.module_aws_application_scaling_policy


Manage Application Auto Scaling Scaling Policies

## Description

Creates, updates or removes a Scaling Policy

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "maximum_tasks": "{'description': ['The maximum value to scale to in response to a scale out event. This parameter is required if you are creating a first new policy for the specified service.'], 'required': False, 'version_added': '2.6'}",
    "minimum_tasks": "{'description': ['The minimum value to scale to in response to a scale in event. This parameter is required if you are creating a first new policy for the specified service.'], 'required': False, 'version_added': '2.6'}",
    "override_task_capacity": "{'description': ["Whether or not to override values of minimum and/or maximum tasks if it's already set."], 'required': False, 'default': False, 'type': 'bool', 'version_added': '2.6'}",
    "policy_name": "{'description': ['The name of the scaling policy.'], 'required': True}",
    "policy_type": "{'description': ['The policy type.'], 'required': True, 'choices': ['StepScaling', 'TargetTrackingScaling']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "resource_id": "{'description': ['The identifier of the resource associated with the scalable target.'], 'required': True}",
    "scalable_dimension": "{'description': ['The scalable dimension associated with the scalable target.'], 'required': True, 'choices': ['ecs:service:DesiredCount', 'ec2:spot-fleet-request:TargetCapacity', 'elasticmapreduce:instancegroup:InstanceCount', 'appstream:fleet:DesiredCapacity', 'dynamodb:table:ReadCapacityUnits', 'dynamodb:table:WriteCapacityUnits', 'dynamodb:index:ReadCapacityUnits', 'dynamodb:index:WriteCapacityUnits']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "service_namespace": "{'description': ['The namespace of the AWS service.'], 'required': True, 'choices': ['ecs', 'elasticmapreduce', 'ec2', 'appstream', 'dynamodb']}",
    "step_scaling_policy_configuration": "{'description': ['A step scaling policy. This parameter is required if you are creating a policy and the policy type is StepScaling.'], 'required': False}",
    "target_tracking_scaling_policy_configuration": "{'description': ['A target tracking policy. This parameter is required if you are creating a new policy and the policy type is TargetTrackingScaling.'], 'required': False}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create step scaling policy for ECS Service
- name: scaling_policy
  aws_application_scaling_policy:
    state: present
    policy_name: test_policy
    service_namespace: ecs
    resource_id: service/poc-pricing/test-as
    scalable_dimension: ecs:service:DesiredCount
    policy_type: StepScaling
    minimum_tasks: 1
    maximum_tasks: 6
    step_scaling_policy_configuration:
      AdjustmentType: ChangeInCapacity
      StepAdjustments:
        - MetricIntervalUpperBound: 123
          ScalingAdjustment: 2
        - MetricIntervalLowerBound: 123
          ScalingAdjustment: -2
      Cooldown: 123
      MetricAggregationType: Average

# Create target tracking scaling policy for ECS Service
- name: scaling_policy
  aws_application_scaling_policy:
    state: present
    policy_name: test_policy
    service_namespace: ecs
    resource_id: service/poc-pricing/test-as
    scalable_dimension: ecs:service:DesiredCount
    policy_type: TargetTrackingScaling
    minimum_tasks: 1
    maximum_tasks: 6
    target_tracking_scaling_policy_configuration:
      TargetValue: 60
      PredefinedMetricSpecification:
        PredefinedMetricType: ECSServiceAverageCPUUtilization
      ScaleOutCooldown: 60
      ScaleInCooldown: 60

# Remove scalable target for ECS Service
- name: scaling_policy
  aws_application_scaling_policy:
    state: absent
    policy_name: test_policy
    policy_type: StepScaling
    service_namespace: ecs
    resource_id: service/cluster-name/service-name
    scalable_dimension: ecs:service:DesiredCount

```

## License

TODO

## Author Information
  - ['Gustavo Maia(@gurumaia)', 'Chen Leibovich(@chenl87)']
  - ['Gustavo Maia(@gurumaia)', 'Chen Leibovich(@chenl87)']
