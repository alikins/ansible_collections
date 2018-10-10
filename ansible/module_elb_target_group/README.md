# Ansible module: ansible.module_elb_target_group


Manage a target group for an Application or Network load balancer

## Description

Manage an AWS Elastic Load Balancer target group. See U(http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html) or U(http://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html) for details.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "deregistration_delay_timeout": "{'description': ['The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "health_check_interval": "{'description': ['The approximate amount of time, in seconds, between health checks of an individual target.'], 'required': False}",
    "health_check_path": "{'description': ['The ping path that is the destination on the targets for health checks. The path must be defined in order to set a health check.'], 'required': False}",
    "health_check_port": "{'description': ["The port the load balancer uses when performing health checks on targets. Can be set to 'traffic-port' to match target port."], 'required': False, 'default': 'The port on which each target receives traffic from the load balancer.'}",
    "health_check_protocol": "{'description': ['The protocol the load balancer uses when performing health checks on targets.'], 'required': False, 'choices': ['http', 'https', 'tcp']}",
    "health_check_timeout": "{'description': ['The amount of time, in seconds, during which no response from a target means a failed health check.'], 'required': False}",
    "healthy_threshold_count": "{'description': ['The number of consecutive health checks successes required before considering an unhealthy target healthy.'], 'required': False}",
    "modify_targets": "{'description': ['Whether or not to alter existing targets in the group to match what is passed with the module'], 'required': False, 'default': True}",
    "name": "{'description': ['The name of the target group.'], 'required': True}",
    "port": "{'description': ['The port on which the targets receive traffic. This port is used unless you specify a port override when registering the target. Required if I(state) is C(present).'], 'required': False}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "protocol": "{'description': ['The protocol to use for routing traffic to the targets. Required when I(state) is C(present).'], 'required': False, 'choices': ['http', 'https', 'tcp']}",
    "purge_tags": "{'description': ['If yes, existing tags will be purged from the resource to match exactly what is defined by I(tags) parameter. If the tag parameter is not set then tags will not be modified.'], 'required': False, 'default': True, 'type': 'bool'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Create or destroy the target group.'], 'required': True, 'choices': ['present', 'absent']}",
    "stickiness_enabled": "{'description': ['Indicates whether sticky sessions are enabled.'], 'type': 'bool'}",
    "stickiness_lb_cookie_duration": "{'description': ['The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds).']}",
    "stickiness_type": "{'description': ['The type of sticky sessions. The possible value is lb_cookie.'], 'default': 'lb_cookie'}",
    "successful_response_codes": "{'description': ['The HTTP codes to use when checking for a successful response from a target. You can specify multiple values (for example, "200,202") or a range of values (for example, "200-299").'], 'required': False}",
    "tags": "{'description': ['A dictionary of one or more tags to assign to the target group.'], 'required': False}",
    "target_type": "{'description': ["The type of target that you must specify when registering targets with this target group. The possible values are C(instance) (targets are specified by instance ID) or C(ip) (targets are specified by IP address). Note that you can't specify targets for a target group using both instance IDs and IP addresses. If the target type is ip, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group, the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10). You can't specify publicly routable IP addresses."], 'required': False, 'default': 'instance', 'choices': ['instance', 'ip'], 'version_added': 2.5}",
    "targets": "{'description': ["A list of targets to assign to the target group. This parameter defaults to an empty list. Unless you set the 'modify_targets' parameter then all existing targets will be removed from the group. The list should be an Id and a Port parameter. See the Examples for detail."], 'required': False}",
    "unhealthy_threshold_count": "{'description': ['The number of consecutive health check failures required before considering a target unhealthy.'], 'required': False}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "vpc_id": "{'description': ['The identifier of the virtual private cloud (VPC). Required when I(state) is C(present).'], 'required': False}",
    "wait": "{'description': ['Whether or not to wait for the target group.'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "wait_timeout": "{'description': ['The time to wait for the target group.'], 'default': 200, 'version_added': '2.4'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create a target group with a default health check
- elb_target_group:
    name: mytargetgroup
    protocol: http
    port: 80
    vpc_id: vpc-01234567
    state: present

# Modify the target group with a custom health check
- elb_target_group:
    name: mytargetgroup
    protocol: http
    port: 80
    vpc_id: vpc-01234567
    health_check_path: /
    successful_response_codes: "200, 250-260"
    state: present

# Delete a target group
- elb_target_group:
    name: mytargetgroup
    state: absent

# Create a target group with instance targets
- elb_target_group:
    name: mytargetgroup
    protocol: http
    port: 81
    vpc_id: vpc-01234567
    health_check_path: /
    successful_response_codes: "200,250-260"
    targets:
      - Id: i-01234567
        Port: 80
      - Id: i-98765432
        Port: 80
    state: present
    wait_timeout: 200
    wait: True

# Create a target group with IP address targets
- elb_target_group:
    name: mytargetgroup
    protocol: http
    port: 81
    vpc_id: vpc-01234567
    health_check_path: /
    successful_response_codes: "200,250-260"
    target_type: ip
    targets:
      - Id: 10.0.0.10
        Port: 80
        AvailabilityZone: all
      - Id: 10.0.0.20
        Port: 80
    state: present
    wait_timeout: 200
    wait: True


```

## License

TODO

## Author Information
  - ['Rob White (@wimnat)']
