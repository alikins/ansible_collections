# Ansible module: ansible.module_elb_network_lb


Manage a Network Load Balancer

## Description

Manage an AWS Network Elastic Load Balancer. See U(https://aws.amazon.com/blogs/aws/new-network-load-balancer-effortless-scaling-to-millions-of-requests-per-second/) for details.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "cross_zone_load_balancing": "{'description': ['Indicates whether cross-zone load balancing is enabled.'], 'required': False, 'default': False, 'type': 'bool'}",
    "deletion_protection": "{'description': ['Indicates whether deletion protection for the ELB is enabled.'], 'required': False, 'default': False, 'type': 'bool'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "listeners": "{'description': ['A list of dicts containing listeners to attach to the ELB. See examples for detail of the dict required. Note that listener keys are CamelCased.'], 'required': False}",
    "name": "{'description': ['The name of the load balancer. This name must be unique within your AWS account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_listeners": "{'description': ['If yes, existing listeners will be purged from the ELB to match exactly what is defined by I(listeners) parameter. If the I(listeners) parameter is not set then listeners will not be modified'], 'default': True, 'type': 'bool'}",
    "purge_tags": "{'description': ['If yes, existing tags will be purged from the resource to match exactly what is defined by I(tags) parameter. If the I(tags) parameter is not set then tags will not be modified.'], 'required': False, 'default': True, 'type': 'bool'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "scheme": "{'description': ['Internet-facing or internal load balancer. An ELB scheme can not be modified after creation.'], 'required': False, 'default': 'internet-facing', 'choices': ['internet-facing', 'internal']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Create or destroy the load balancer.'], 'required': True, 'choices': ['present', 'absent']}",
    "subnet_mappings": "{'description': ['A list of dicts containing the IDs of the subnets to attach to the load balancer. You can also specify the allocation ID of an Elastic IP to attach to the load balancer. You can specify one Elastic IP address per subnet. This parameter is mutually exclusive with I(subnets)'], 'required': False}",
    "subnets": "{'description': ['A list of the IDs of the subnets to attach to the load balancer. You can specify only one subnet per Availability Zone. You must specify subnets from at least two Availability Zones. Required if state=present. This parameter is mutually exclusive with I(subnet_mappings)'], 'required': False}",
    "tags": "{'description': ['A dictionary of one or more tags to assign to the load balancer.'], 'required': False}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "wait": "{'description': ['Whether or not to wait for the network load balancer to reach the desired state.'], 'type': 'bool'}",
    "wait_timeout": "{'description': ['The duration in seconds to wait, used in conjunction with I(wait).']}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create an ELB and attach a listener
- elb_network_lb:
    name: myelb
    subnets:
      - subnet-012345678
      - subnet-abcdef000
    listeners:
      - Protocol: TCP # Required. The protocol for connections from clients to the load balancer (Only TCP is available) (case-sensitive).
        Port: 80 # Required. The port on which the load balancer is listening.
        DefaultActions:
          - Type: forward # Required. Only 'forward' is accepted at this time
            TargetGroupName: mytargetgroup # Required. The name of the target group
    state: present

# Create an ELB with an attached Elastic IP address
- elb_network_lb:
    name: myelb
    subnet_mappings:
      - SubnetId: subnet-012345678
        AllocationId: eipalloc-aabbccdd
    listeners:
      - Protocol: TCP # Required. The protocol for connections from clients to the load balancer (Only TCP is available) (case-sensitive).
        Port: 80 # Required. The port on which the load balancer is listening.
        DefaultActions:
          - Type: forward # Required. Only 'forward' is accepted at this time
            TargetGroupName: mytargetgroup # Required. The name of the target group
    state: present

# Remove an ELB
- elb_network_lb:
    name: myelb
    state: absent


```

## License

TODO

## Author Information
  - ['Rob White (@wimnat)']
