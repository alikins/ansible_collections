# Ansible module: ansible.module_elb_classic_lb


Creates or destroys Amazon ELB

## Description

Returns information about the load balancer.
Will be marked changed when called only if state is changed.

## Requirements

TODO

## Arguments

``` json
{
    "access_logs": "{'description': ['An associative array of access logs configuration settings (see example)'], 'version_added': '2.0'}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "connection_draining_timeout": "{'description': ['Wait a specified timeout allowing connections to drain before terminating an instance'], 'version_added': '1.8'}",
    "cross_az_load_balancing": "{'description': ['Distribute load across all configured Availability Zones'], 'type': 'bool', 'default': False, 'version_added': '1.8'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "health_check": "{'description': ['An associative array of health check configuration settings (see example)']}",
    "idle_timeout": "{'description': ['ELB connections from clients and to servers are timed out after this amount of time'], 'version_added': '2.0'}",
    "instance_ids": "{'description': ['List of instance ids to attach to this ELB'], 'version_added': '2.1'}",
    "listeners": "{'description': ['List of ports/protocols for this ELB to listen on (see example)']}",
    "name": "{'description': ['The name of the ELB'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_instance_ids": "{'description': ['Purge existing instance ids on ELB that are not found in instance_ids'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "purge_listeners": "{'description': ['Purge existing listeners on ELB that are not found in listeners'], 'type': 'bool', 'default': True}",
    "purge_subnets": "{'description': ['Purge existing subnet on ELB that are not found in subnets'], 'type': 'bool', 'default': False, 'version_added': '1.7'}",
    "purge_zones": "{'description': ['Purge existing availability zones on ELB that are not found in zones'], 'type': 'bool', 'default': False}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "scheme": "{'description': ["The scheme to use when creating the ELB. For a private VPC-visible ELB use 'internal'. If you choose to update your scheme with a different value the ELB will be destroyed and recreated. To update scheme you must use the option wait."], 'choices': ['internal', 'internet-facing'], 'default': 'internet-facing', 'version_added': '1.7'}",
    "security_group_ids": "{'description': ['A list of security groups to apply to the elb'], 'version_added': '1.6'}",
    "security_group_names": "{'description': ['A list of security group names to apply to the elb'], 'version_added': '2.0'}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Create or destroy the ELB'], 'choices': ['present', 'absent'], 'required': True}",
    "stickiness": "{'description': ['An associative array of stickiness policy settings. Policy will be applied to all listeners ( see example )'], 'version_added': '2.0'}",
    "subnets": "{'description': ['A list of VPC subnets to use when creating ELB. Zones should be empty if using this.'], 'version_added': '1.7'}",
    "tags": "{'description': ['An associative array of tags. To delete all tags, supply an empty dict.'], 'version_added': '2.1'}",
    "validate_certs": "{'description': ['When set to C(no), SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "wait": "{'description': ['When specified, Ansible will check the status of the load balancer to ensure it has been successfully removed from AWS.'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "wait_timeout": "{'description': ['Used in conjunction with wait. Number of seconds to wait for the elb to be terminated. A maximum of 600 seconds (10 minutes) is allowed.'], 'default': 60, 'version_added': '2.1'}",
    "zones": "{'description': ['List of availability zones to enable on this ELB']}",
}
```

## Examples


``` yaml

# Note: None of these examples set aws_access_key, aws_secret_key, or region.
# It is assumed that their matching environment variables are set.

# Basic provisioning example (non-VPC)

- elb_classic_lb:
    name: "test-please-delete"
    state: present
    zones:
      - us-east-1a
      - us-east-1d
    listeners:
      - protocol: http # options are http, https, ssl, tcp
        load_balancer_port: 80
        instance_port: 80
        proxy_protocol: True
      - protocol: https
        load_balancer_port: 443
        instance_protocol: http # optional, defaults to value of protocol setting
        instance_port: 80
        # ssl certificate required for https or ssl
        ssl_certificate_id: "arn:aws:iam::123456789012:server-certificate/company/servercerts/ProdServerCert"
  delegate_to: localhost

# Internal ELB example

- elb_classic_lb:
    name: "test-vpc"
    scheme: internal
    state: present
    instance_ids:
      - i-abcd1234
    purge_instance_ids: true
    subnets:
      - subnet-abcd1234
      - subnet-1a2b3c4d
    listeners:
      - protocol: http # options are http, https, ssl, tcp
        load_balancer_port: 80
        instance_port: 80
  delegate_to: localhost

# Configure a health check and the access logs
- elb_classic_lb:
    name: "test-please-delete"
    state: present
    zones:
      - us-east-1d
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80
    health_check:
        ping_protocol: http # options are http, https, ssl, tcp
        ping_port: 80
        ping_path: "/index.html" # not required for tcp or ssl
        response_timeout: 5 # seconds
        interval: 30 # seconds
        unhealthy_threshold: 2
        healthy_threshold: 10
    access_logs:
        interval: 5 # minutes (defaults to 60)
        s3_location: "my-bucket" # This value is required if access_logs is set
        s3_prefix: "logs"
  delegate_to: localhost

# Ensure ELB is gone
- elb_classic_lb:
    name: "test-please-delete"
    state: absent
  delegate_to: localhost

# Ensure ELB is gone and wait for check (for default timeout)
- elb_classic_lb:
    name: "test-please-delete"
    state: absent
    wait: yes
  delegate_to: localhost

# Ensure ELB is gone and wait for check with timeout value
- elb_classic_lb:
    name: "test-please-delete"
    state: absent
    wait: yes
    wait_timeout: 600
  delegate_to: localhost

# Normally, this module will purge any listeners that exist on the ELB
# but aren't specified in the listeners parameter. If purge_listeners is
# false it leaves them alone
- elb_classic_lb:
    name: "test-please-delete"
    state: present
    zones:
      - us-east-1a
      - us-east-1d
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80
    purge_listeners: no
  delegate_to: localhost

# Normally, this module will leave availability zones that are enabled
# on the ELB alone. If purge_zones is true, then any extraneous zones
# will be removed
- elb_classic_lb:
    name: "test-please-delete"
    state: present
    zones:
      - us-east-1a
      - us-east-1d
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80
    purge_zones: yes
  delegate_to: localhost

# Creates a ELB and assigns a list of subnets to it.
- elb_classic_lb:
    state: present
    name: 'New ELB'
    security_group_ids: 'sg-123456, sg-67890'
    region: us-west-2
    subnets: 'subnet-123456,subnet-67890'
    purge_subnets: yes
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80
  delegate_to: localhost

# Create an ELB with connection draining, increased idle timeout and cross availability
# zone load balancing
- elb_classic_lb:
    name: "New ELB"
    state: present
    connection_draining_timeout: 60
    idle_timeout: 300
    cross_az_load_balancing: "yes"
    region: us-east-1
    zones:
      - us-east-1a
      - us-east-1d
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80
  delegate_to: localhost

# Create an ELB with load balancer stickiness enabled
- elb_classic_lb:
    name: "New ELB"
    state: present
    region: us-east-1
    zones:
      - us-east-1a
      - us-east-1d
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80
    stickiness:
      type: loadbalancer
      enabled: yes
      expiration: 300
  delegate_to: localhost

# Create an ELB with application stickiness enabled
- elb_classic_lb:
    name: "New ELB"
    state: present
    region: us-east-1
    zones:
      - us-east-1a
      - us-east-1d
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80
    stickiness:
      type: application
      enabled: yes
      cookie: SESSIONID
  delegate_to: localhost

# Create an ELB and add tags
- elb_classic_lb:
    name: "New ELB"
    state: present
    region: us-east-1
    zones:
      - us-east-1a
      - us-east-1d
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80
    tags:
      Name: "New ELB"
      stack: "production"
      client: "Bob"
  delegate_to: localhost

# Delete all tags from an ELB
- elb_classic_lb:
    name: "New ELB"
    state: present
    region: us-east-1
    zones:
      - us-east-1a
      - us-east-1d
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80
    tags: {}
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Jim Dalton (@jsdalton)']
