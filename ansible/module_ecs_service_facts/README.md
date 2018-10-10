# Ansible module: ansible.module_ecs_service_facts


list or describe services in ecs

## Description

Lists or describes services in ecs.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "cluster": "{'description': ['The cluster ARNS in which to list the services.'], 'required': False, 'default': 'default'}",
    "details": "{'description': ['Set this to true if you want detailed information about the services.'], 'required': False, 'default': False, 'type': 'bool'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "events": "{'description': ['Whether to return ECS service events. Only has an effect if C(details) is true.'], 'required': False, 'default': True, 'type': 'bool', 'version_added': '2.6'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "service": "{'description': ['One or more services to get details for'], 'required': False}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Basic listing example
- ecs_service_facts:
    cluster: test-cluster
    service: console-test-service
    details: true

# Basic listing example
- ecs_service_facts:
    cluster: test-cluster

```

## License

TODO

## Author Information
  - ['Mark Chance (@java1guy)', 'Darek Kaczynski (@kaczynskid)']
  - ['Mark Chance (@java1guy)', 'Darek Kaczynski (@kaczynskid)']
