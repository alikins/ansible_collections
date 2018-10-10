# Ansible module: ansible.module_ecs_service


create, terminate, start or stop a service in ecs

## Description

Creates or terminates ecs services.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "client_token": "{'description': ['Unique, case-sensitive identifier you provide to ensure the idempotency of the request. Up to 32 ASCII characters are allowed.'], 'required': False}",
    "cluster": "{'description': ['The name of the cluster in which the service exists'], 'required': False}",
    "delay": "{'description': ['The time to wait before checking that the service is available'], 'required': False, 'default': 10}",
    "deployment_configuration": "{'description': ['Optional parameters that control the deployment_configuration; format is \'{"maximum_percent":<integer>, "minimum_healthy_percent":<integer>}'], 'required': False, 'version_added': 2.3}",
    "desired_count": "{'description': ['The count of how many instances of the service. This parameter is required when state=present'], 'required': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "launch_type": "{'description': ['The launch type on which to run your service'], 'required': False, 'version_added': 2.7, 'choices': ['EC2', 'FARGATE']}",
    "load_balancers": "{'description': ['The list of ELBs defined for this service'], 'required': False}",
    "name": "{'description': ['The name of the service'], 'required': True}",
    "network_configuration": "{'description': ['network configuration of the service. Only applicable for task definitions created with C(awsvpc) I(network_mode).', 'assign_public_ip requires botocore >= 1.8.4'], 'suboptions': {'subnets': {'description': ['A list of subnet IDs to associate with the task'], 'version_added': 2.6}, 'security_groups': {'description': ['A list of security group names or group IDs to associate with the task'], 'version_added': 2.6}, 'assign_public_ip': {'description': ["Whether the task's elastic network interface receives a public IP address. This option requires botocore >= 1.8.4."], 'type': 'bool', 'version_added': 2.7}}}",
    "placement_constraints": "{'description': ['The placement constraints for the tasks in the service'], 'required': False, 'version_added': 2.4}",
    "placement_strategy": "{'description': ['The placement strategy objects to use for tasks in your service. You can specify a maximum of 5 strategy rules per service'], 'required': False, 'version_added': 2.4}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "repeat": "{'description': ['The number of times to check that the service is available'], 'required': False, 'default': 10}",
    "role": "{'description': ['The name or full Amazon Resource Name (ARN) of the IAM role that allows your Amazon ECS container agent to make calls to your load balancer on your behalf. This parameter is only required if you are using a load balancer with your service, in a network mode other than `awsvpc`.'], 'required': False}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['The desired state of the service'], 'required': True, 'choices': ['present', 'absent', 'deleting']}",
    "task_definition": "{'description': ['The task definition the service will run. This parameter is required when state=present'], 'required': False}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.
- ecs_service:
    state: present
    name: console-test-service
    cluster: new_cluster
    task_definition: 'new_cluster-task:1'
    desired_count: 0

# Basic provisioning example
- ecs_service:
    name: default
    state: present
    cluster: new_cluster

- name: create ECS service on VPC network
  ecs_service:
    state: present
    name: console-test-service
    cluster: new_cluster
    task_definition: 'new_cluster-task:1'
    desired_count: 0
    network_configuration:
      subnets:
      - subnet-abcd1234
      security_groups:
      - sg-aaaa1111
      - my_security_group

# Simple example to delete
- ecs_service:
    name: default
    state: absent
    cluster: new_cluster

# With custom deployment configuration (added in version 2.3), placement constraints and strategy (added in version 2.4)
- ecs_service:
    state: present
    name: test-service
    cluster: test-cluster
    task_definition: test-task-definition
    desired_count: 3
    deployment_configuration:
      minimum_healthy_percent: 75
      maximum_percent: 150
    placement_constraints:
      - type: memberOf
        expression: 'attribute:flavor==test'
    placement_strategy:
      - type: binpack
        field: memory

```

## License

TODO

## Author Information
  - ['Mark Chance (@java1guy)', 'Darek Kaczynski (@kaczynskid)', 'Stephane Maarek (@simplesteph)', 'Zac Blazic (@zacblazic)']
  - ['Mark Chance (@java1guy)', 'Darek Kaczynski (@kaczynskid)', 'Stephane Maarek (@simplesteph)', 'Zac Blazic (@zacblazic)']
  - ['Mark Chance (@java1guy)', 'Darek Kaczynski (@kaczynskid)', 'Stephane Maarek (@simplesteph)', 'Zac Blazic (@zacblazic)']
  - ['Mark Chance (@java1guy)', 'Darek Kaczynski (@kaczynskid)', 'Stephane Maarek (@simplesteph)', 'Zac Blazic (@zacblazic)']
