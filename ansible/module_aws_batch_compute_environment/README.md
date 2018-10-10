# Ansible module: ansible.module_aws_batch_compute_environment


Manage AWS Batch Compute Environments

## Description

This module allows the management of AWS Batch Compute Environments. It is idempotent and supports "Check" mode.  Use module M(aws_batch_compute_environment) to manage the compute environment, M(aws_batch_job_queue) to manage job queues, M(aws_batch_job_definition) to manage job definitions.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "bid_percentage": "{'description': ['The minimum percentage that a Spot Instance price must be when compared with the On-Demand price for that instance type before instances are launched. For example, if your bid percentage is 20%, then the Spot price must be below 20% of the current On-Demand price for that EC2 instance.']}",
    "compute_environment_name": "{'description': ['The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, and underscores are allowed.'], 'required': True}",
    "compute_environment_state": "{'description': ['The state of the compute environment. If the state is ENABLED, then the compute environment accepts jobs from a queue and can scale out automatically based on queues.'], 'default': 'ENABLED', 'choices': ['ENABLED', 'DISABLED']}",
    "compute_resource_type": "{'description': ['The type of compute resource.'], 'required': True, 'choices': ['EC2', 'SPOT']}",
    "desiredv_cpus": "{'description': ['The desired number of EC2 vCPUS in the compute environment.']}",
    "ec2_key_pair": "{'description': ['The EC2 key pair that is used for instances launched in the compute environment.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "image_id": "{'description': ['The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.']}",
    "instance_role": "{'description': ['The Amazon ECS instance role applied to Amazon EC2 instances in a compute environment.'], 'required': True}",
    "instance_types": "{'description': ['The instance types that may be launched.'], 'required': True}",
    "maxv_cpus": "{'description': ['The maximum number of EC2 vCPUs that an environment can reach.'], 'required': True}",
    "minv_cpus": "{'description': ['The minimum number of EC2 vCPUs that an environment should maintain.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_group_ids": "{'description': ['The EC2 security groups that are associated with instances launched in the compute environment.'], 'required': True}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "service_role": "{'description': ['The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.'], 'required': True}",
    "spot_iam_fleet_role": "{'description': ['The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a SPOT compute environment.']}",
    "state": "{'description': ['Describes the desired state.'], 'required': True, 'default': 'present', 'choices': ['present', 'absent']}",
    "subnets": "{'description': ['The VPC subnets into which the compute resources are launched.'], 'required': True}",
    "tags": "{'description': ['Key-value pair tags to be applied to resources that are launched in the compute environment.']}",
    "type": "{'description': ['The type of the compute environment.'], 'required': True, 'choices': ['MANAGED', 'UNMANAGED']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

---
- hosts: localhost
  gather_facts: no
  vars:
    state: present
  tasks:
  - name: My Batch Compute Environment
    aws_batch_compute_environment:
      compute_environment_name: computeEnvironmentName
      state: present
      region: us-east-1
      compute_environment_state: ENABLED
      type: MANAGED
      compute_resource_type: EC2
      minv_cpus: 0
      maxv_cpus: 2
      desiredv_cpus: 1
      instance_types:
        - optimal
      subnets:
        - my-subnet1
        - my-subnet2
      security_group_ids:
        - my-sg1
        - my-sg2
      instance_role: arn:aws:iam::<account>:instance-profile/<role>
      tags:
        tag1: value1
        tag2: value2
      service_role: arn:aws:iam::<account>:role/service-role/<role>

  - name: show results
    debug: var=aws_batch_compute_environment_action

```

## License

TODO

## Author Information
  - ['Jon Meran (@jonmer85)']
