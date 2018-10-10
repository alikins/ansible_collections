# Ansible module: ansible.module_aws_eks_cluster


Manage Elastic Kubernetes Service Clusters

## Description

Manage Elastic Kubernetes Service Clusters

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "name": "{'description': ['Name of EKS cluster'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "role_arn": "{'description': ['ARN of IAM role used by the EKS cluster']}",
    "security_groups": "{'description': ['list of security group names or IDs']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['desired state of the EKS cluster'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "subnets": "{'description': ['list of subnet IDs for the Kubernetes cluster']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "version": "{'description': ['Kubernetes version - defaults to latest']}",
    "wait": "{'description': ['Specifies whether the module waits until the cluster becomes active after creation. It takes "usually less than 10 minutes" per AWS documentation.'], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'description': ['The duration in seconds to wait for the cluster to become active. Defaults to 1200 seconds (20 minutes).'], 'default': 1200}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Create an EKS cluster
  aws_eks_cluster:
    name: my_cluster
    version: v1.10.0
    role_arn: my_eks_role
    subnets:
      - subnet-aaaa1111
    security_groups:
      - my_eks_sg
      - sg-abcd1234
  register: caller_facts

- name: Remove an EKS cluster
  aws_eks_cluster:
    name: my_cluster
    state: absent

```

## License

TODO

## Author Information
  - ['Will Thames (@willthames)']
