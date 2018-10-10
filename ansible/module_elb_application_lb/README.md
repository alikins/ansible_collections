# Ansible module: ansible.module_elb_application_lb


Manage an Application load balancer

## Description

Manage an AWS Application Elastic Load Balancer. See U(https://aws.amazon.com/blogs/aws/new-aws-application-load-balancer/) for details.

## Requirements

TODO

## Arguments

``` json
{
    "access_logs_enabled": "{'description': ['Whether or not to enable access logs. When true, I(access_logs_s3_bucket) must be set.'], 'required': False, 'type': 'bool'}",
    "access_logs_s3_bucket": "{'description': ['The name of the S3 bucket for the access logs. This attribute is required if access logs in Amazon S3 are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permission to write to the bucket.'], 'required': False}",
    "access_logs_s3_prefix": "{'description': ["The prefix for the location in the S3 bucket. If you don't specify a prefix, the access logs are stored in the root of the bucket."], 'required': False}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "deletion_protection": "{'description': ['Indicates whether deletion protection for the ELB is enabled.'], 'required': False, 'default': False, 'type': 'bool'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "http2": "{'description': ['Indicates whether to enable HTTP2 routing.'], 'required': False, 'default': False, 'type': 'bool', 'version_added': 2.6}",
    "idle_timeout": "{'description': ['The number of seconds to wait before an idle connection is closed.'], 'required': False, 'default': 60}",
    "listeners": "{'description': ['A list of dicts containing listeners to attach to the ELB. See examples for detail of the dict required. Note that listener keys are CamelCased.'], 'required': False}",
    "name": "{'description': ['The name of the load balancer. This name must be unique within your AWS account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_listeners": "{'description': ['If yes, existing listeners will be purged from the ELB to match exactly what is defined by I(listeners) parameter. If the I(listeners) parameter is not set then listeners will not be modified'], 'default': True, 'type': 'bool'}",
    "purge_rules": "{'description': ['When set to no, keep the existing load balancer rules in place. Will modify and add, but will not delete.'], 'default': True, 'type': 'bool', 'version_added': 2.7}",
    "purge_tags": "{'description': ['If yes, existing tags will be purged from the resource to match exactly what is defined by I(tags) parameter. If the I(tags) parameter is not set then tags will not be modified.'], 'required': False, 'default': True, 'type': 'bool'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "scheme": "{'description': ['Internet-facing or internal load balancer. An ELB scheme can not be modified after creation.'], 'required': False, 'default': 'internet-facing', 'choices': ['internet-facing', 'internal']}",
    "security_groups": "{'description': ['A list of the names or IDs of the security groups to assign to the load balancer. Required if state=present.'], 'required': False, 'default': []}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Create or destroy the load balancer.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "subnets": "{'description': ['A list of the IDs of the subnets to attach to the load balancer. You can specify only one subnet per Availability Zone. You must specify subnets from at least two Availability Zones. Required if state=present.'], 'required': False}",
    "tags": "{'description': ['A dictionary of one or more tags to assign to the load balancer.'], 'required': False}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "wait": "{'description': ["Wait for the load balancer to have a state of 'active' before completing. A status check is performed every 15 seconds until a successful state is reached. An error is returned after 40 failed checks."], 'default': False, 'type': 'bool', 'version_added': 2.6}",
    "wait_timeout": "{'description': ['The time in seconds to use in conjunction with I(wait).'], 'version_added': 2.6}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create an ELB and attach a listener
- elb_application_lb:
    name: myelb
    security_groups:
      - sg-12345678
      - my-sec-group
    subnets:
      - subnet-012345678
      - subnet-abcdef000
    listeners:
      - Protocol: HTTP # Required. The protocol for connections from clients to the load balancer (HTTP or HTTPS) (case-sensitive).
        Port: 80 # Required. The port on which the load balancer is listening.
        # The security policy that defines which ciphers and protocols are supported. The default is the current predefined security policy.
        SslPolicy: ELBSecurityPolicy-2015-05
        Certificates: # The ARN of the certificate (only one certficate ARN should be provided)
          - CertificateArn: arn:aws:iam::12345678987:server-certificate/test.domain.com
        DefaultActions:
          - Type: forward # Required. Only 'forward' is accepted at this time
            TargetGroupName: # Required. The name of the target group
    state: present

# Create an ELB and attach a listener with logging enabled
- elb_application_lb:
    access_logs_enabled: yes
    access_logs_s3_bucket: mybucket
    access_logs_s3_prefix: "/logs"
    name: myelb
    security_groups:
      - sg-12345678
      - my-sec-group
    subnets:
      - subnet-012345678
      - subnet-abcdef000
    listeners:
      - Protocol: HTTP # Required. The protocol for connections from clients to the load balancer (HTTP or HTTPS) (case-sensitive).
        Port: 80 # Required. The port on which the load balancer is listening.
        # The security policy that defines which ciphers and protocols are supported. The default is the current predefined security policy.
        SslPolicy: ELBSecurityPolicy-2015-05
        Certificates: # The ARN of the certificate (only one certficate ARN should be provided)
          - CertificateArn: arn:aws:iam::12345678987:server-certificate/test.domain.com
        DefaultActions:
          - Type: forward # Required. Only 'forward' is accepted at this time
            TargetGroupName: # Required. The name of the target group
    state: present

# Create an ALB with listeners and rules
- elb_application_lb:
    name: test-alb
    subnets:
      - subnet-12345678
      - subnet-87654321
    security_groups:
      - sg-12345678
    scheme: internal
    listeners:
      - Protocol: HTTPS
        Port: 443
        DefaultActions:
          - Type: forward
            TargetGroupName: test-target-group
        Certificates:
          - CertificateArn: arn:aws:iam::12345678987:server-certificate/test.domain.com
        SslPolicy: ELBSecurityPolicy-2015-05
        Rules:
          - Conditions:
              - Field: path-pattern
                Values:
                  - '/test'
            Priority: '1'
            Actions:
              - TargetGroupName: test-target-group
                Type: forward
    state: present

# Remove an ELB
- elb_application_lb:
    name: myelb
    state: absent


```

## License

TODO

## Author Information
  - ['Rob White (@wimnat)']
