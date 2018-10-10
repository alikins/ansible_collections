# Ansible module: ansible.module_elb_target


Manage a target in a target group

## Description

Used to register or deregister a target in a target group

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "deregister_unused": "{'description': ['The default behaviour for targets that are unused is to leave them registered. If instead you would like to remove them set I(deregister_unused) to yes.'], 'type': 'bool'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Register or deregister the target.'], 'required': True, 'choices': ['present', 'absent']}",
    "target_az": "{'description': ['An Availability Zone or all. This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer. This parameter is not supported if the target type of the target group is instance.']}",
    "target_group_arn": "{'description': ['The Amazon Resource Name (ARN) of the target group. Mutually exclusive of I(target_group_name).']}",
    "target_group_name": "{'description': ['The name of the target group. Mutually exclusive of I(target_group_arn).']}",
    "target_id": "{'description': ['The ID of the target.'], 'required': True}",
    "target_port": "{'description': ['The port on which the target is listening. You can specify a port override. If a target is already registered, you can register it again using a different port.'], 'required': False, 'default': 'The default port for a target is the port for the target group.'}",
    "target_status": "{'description': ['Blocks and waits for the target status to equal given value. For more detail on target status see U(http://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html#target-health-states)'], 'required': False, 'choices': ['initial', 'healthy', 'unhealthy', 'unused', 'draining', 'unavailable']}",
    "target_status_timeout": "{'description': ['Maximum time in seconds to wait for target_status change'], 'required': False, 'default': 60}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Register an IP address target to a target group
- elb_target:
    target_group_name: myiptargetgroup
    target_id: 10.0.0.10
    state: present

# Register an instance target to a target group
- elb_target:
    target_group_name: mytargetgroup
    target_id: i-1234567
    state: present

# Deregister a target from a target group
- elb_target:
    target_group_name: mytargetgroup
    target_id: i-1234567
    state: absent

# Modify a target to use a different port
# Register a target to a target group
- elb_target:
    target_group_name: mytargetgroup
    target_id: i-1234567
    target_port: 8080
    state: present


```

## License

TODO

## Author Information
  - ['Rob White (@wimnat)']
