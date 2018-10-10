# Ansible module: ansible.module_ec2_asg


Create or delete AWS Autoscaling Groups

## Description

Can create or delete AWS Autoscaling Groups
Can be used with the ec2_lc module to manage Launch Configurations

## Requirements

TODO

## Arguments

``` json
{
    "availability_zones": "{'description': ['List of availability zone names in which to create the group.  Defaults to all the availability zones in the region if vpc_zone_identifier is not set.']}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "default_cooldown": "{'description': ['The number of seconds after a scaling activity completes before another can begin.'], 'default': '300 seconds', 'version_added': '2.0'}",
    "desired_capacity": "{'description': ['Desired number of instances in group, if unspecified then the current group value will be used.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "health_check_period": "{'description': ['Length of time in seconds after a new EC2 instance comes into service that Auto Scaling starts checking its health.'], 'required': False, 'default': '500 seconds', 'version_added': '1.7'}",
    "health_check_type": "{'description': ['The service you want the health status from, Amazon EC2 or Elastic Load Balancer.'], 'required': False, 'default': 'EC2', 'version_added': '1.7', 'choices': ['EC2', 'ELB']}",
    "launch_config_name": "{'description': ['Name of the Launch configuration to use for the group. See the ec2_lc module for managing these. If unspecified then the current group value will be used.  One of launch_config_name or launch_template must be provided.']}",
    "launch_template": "{'description': ['Dictionary describing the Launch Template to use'], 'suboptions': {'version': {'description': ['The version number of the launch template to use.  Defaults to latest version if not provided.'], 'default': 'latest'}, 'launch_template_name': {'description': ['The name of the launch template. Only one of launch_template_name or launch_template_id is required.']}, 'launch_template_id': {'description': ['The id of the launch template. Only one of launch_template_name or launch_template_id is required.']}}, 'version_added': '2.8'}",
    "lc_check": "{'description': ['Check to make sure instances that are being replaced with replace_instances do not already have the current launch_config.'], 'version_added': '1.8', 'default': 'yes'}",
    "load_balancers": "{'description': ['List of ELB names to use for the group. Use for classic load balancers.']}",
    "lt_check": "{'description': ['Check to make sure instances that are being replaced with replace_instances do not already have the current launch_template or launch_template version.'], 'version_added': '2.8', 'default': 'yes'}",
    "max_size": "{'description': ['Maximum number of instances in group, if unspecified then the current group value will be used.']}",
    "metrics_collection": "{'description': ['Enable ASG metrics collection'], 'type': 'bool', 'default': False, 'version_added': '2.6'}",
    "metrics_granularity": "{'description': ['When metrics_collection is enabled this will determine granularity of metrics collected by CloudWatch'], 'default': '1minute', 'version_added': '2.6'}",
    "metrics_list": "{'description': ['List of autoscaling metrics to collect when enabling metrics_collection'], 'default': ['GroupMinSize', 'GroupMaxSize', 'GroupDesiredCapacity', 'GroupInServiceInstances', 'GroupPendingInstances', 'GroupStandbyInstances', 'GroupTerminatingInstances', 'GroupTotalInstances'], 'version_added': '2.6'}",
    "min_size": "{'description': ['Minimum number of instances in group, if unspecified then the current group value will be used.']}",
    "name": "{'description': ['Unique name for group to be created or deleted'], 'required': True}",
    "notification_topic": "{'description': ['A SNS topic ARN to send auto scaling notifications to.'], 'version_added': '2.2'}",
    "notification_types": "{'description': ['A list of auto scaling events to trigger notifications on.'], 'default': ['autoscaling:EC2_INSTANCE_LAUNCH', 'autoscaling:EC2_INSTANCE_LAUNCH_ERROR', 'autoscaling:EC2_INSTANCE_TERMINATE', 'autoscaling:EC2_INSTANCE_TERMINATE_ERROR'], 'required': False, 'version_added': '2.2'}",
    "placement_group": "{'description': ['Physical location of your cluster placement group created in Amazon EC2.'], 'version_added': '2.3'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "replace_all_instances": "{'description': ['In a rolling fashion, replace all instances with an old launch configuration with one from the current launch configuration.'], 'version_added': '1.8', 'default': 'no'}",
    "replace_batch_size": "{'description': ["Number of instances you'd like to replace at a time.  Used with replace_all_instances."], 'required': False, 'version_added': '1.8', 'default': 1}",
    "replace_instances": "{'description': ['List of instance_ids belonging to the named ASG that you would like to terminate and be replaced with instances matching the current launch configuration.'], 'version_added': '1.8'}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['register or deregister the instance'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "suspend_processes": "{'description': ['A list of scaling processes to suspend.'], 'default': [], 'choices': ['Launch', 'Terminate', 'HealthCheck', 'ReplaceUnhealthy', 'AZRebalance', 'AlarmNotification', 'ScheduledActions', 'AddToLoadBalancer'], 'version_added': '2.3'}",
    "tags": "{'description': ["A list of tags to add to the Auto Scale Group. Optional key is 'propagate_at_launch', which defaults to true."], 'version_added': '1.7'}",
    "target_group_arns": "{'description': ['List of target group ARNs to use for the group. Use for application load balancers.'], 'version_added': '2.4'}",
    "termination_policies": "{'description': ['An ordered list of criteria used for selecting instances to be removed from the Auto Scaling group when reducing capacity.', 'For \'Default\', when used to create a new autoscaling group, the "Default"i value is used. When used to change an existent autoscaling group, the current termination policies are maintained.'], 'default': 'Default', 'choices': ['OldestInstance', 'NewestInstance', 'OldestLaunchConfiguration', 'ClosestToNextInstanceHour', 'Default'], 'version_added': '2.0'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "vpc_zone_identifier": "{'description': ['List of VPC subnets to use']}",
    "wait_for_instances": "{'description': ['Wait for the ASG instances to be in a ready state before exiting.  If instances are behind an ELB, it will wait until the ELB determines all instances have a lifecycle_state of  "InService" and  a health_status of "Healthy".'], 'version_added': '1.9', 'default': 'yes'}",
    "wait_timeout": "{'description': ['How long to wait for instances to become viable when replaced.  If you experience the error "Waited too long for ELB instances to be healthy", try increasing this value.'], 'default': 300, 'version_added': '1.8'}",
}
```

## Examples


``` yaml

# Basic configuration with Launch Configuration

- ec2_asg:
    name: special
    load_balancers: [ 'lb1', 'lb2' ]
    availability_zones: [ 'eu-west-1a', 'eu-west-1b' ]
    launch_config_name: 'lc-1'
    min_size: 1
    max_size: 10
    desired_capacity: 5
    vpc_zone_identifier: [ 'subnet-abcd1234', 'subnet-1a2b3c4d' ]
    tags:
      - environment: production
        propagate_at_launch: no

# Rolling ASG Updates

# Below is an example of how to assign a new launch config to an ASG and terminate old instances.
#
# All instances in "myasg" that do not have the launch configuration named "my_new_lc" will be terminated in
# a rolling fashion with instances using the current launch configuration, "my_new_lc".
#
# This could also be considered a rolling deploy of a pre-baked AMI.
#
# If this is a newly created group, the instances will not be replaced since all instances
# will have the current launch configuration.

- name: create launch config
  ec2_lc:
    name: my_new_lc
    image_id: ami-lkajsf
    key_name: mykey
    region: us-east-1
    security_groups: sg-23423
    instance_type: m1.small
    assign_public_ip: yes

- ec2_asg:
    name: myasg
    launch_config_name: my_new_lc
    health_check_period: 60
    health_check_type: ELB
    replace_all_instances: yes
    min_size: 5
    max_size: 5
    desired_capacity: 5
    region: us-east-1

# To only replace a couple of instances instead of all of them, supply a list
# to "replace_instances":

- ec2_asg:
    name: myasg
    launch_config_name: my_new_lc
    health_check_period: 60
    health_check_type: ELB
    replace_instances:
    - i-b345231
    - i-24c2931
    min_size: 5
    max_size: 5
    desired_capacity: 5
    region: us-east-1

# Basic Configuration with Launch Template

- ec2_asg:
    name: special
    load_balancers: [ 'lb1', 'lb2' ]
    availability_zones: [ 'eu-west-1a', 'eu-west-1b' ]
    launch_template:
        version: '1'
        launch_template_name: 'lt-example'
        launch_template_id: 'lt-123456'
    min_size: 1
    max_size: 10
    desired_capacity: 5
    vpc_zone_identifier: [ 'subnet-abcd1234', 'subnet-1a2b3c4d' ]
    tags:
      - environment: production
        propagate_at_launch: no



```

## License

TODO

## Author Information
  - ['Gareth Rushgrove (@garethr)']
