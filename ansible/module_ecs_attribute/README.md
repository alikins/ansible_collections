# Ansible module: ansible.module_ecs_attribute


manage ecs attributes

## Description

Create, update or delete ECS container instance attributes.

## Requirements

TODO

## Arguments

``` json
{
    "attributes": "{'description': ['List of attributes.'], 'required': True, 'suboptions': {'name': {'description': ['The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.'], 'required': True}, 'value': {'description': ['The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.'], 'required': False}}}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "cluster": "{'description': ['The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to apply attributes.'], 'required': True}",
    "ec2_instance_id": "{'description': ['EC2 instance ID of ECS cluster container instance.'], 'required': True}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['The desired state of the attributes.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Set attributes
- ecs_attribute:
    state: present
    cluster: test-cluster
    ec2_instance_id: "{{ ec2_id }}"
    attributes:
      - flavor: test
      - migrated
  delegate_to: localhost

# Delete attributes
- ecs_attribute:
    state: absent
    cluster: test-cluster
    ec2_instance_id: "{{ ec2_id }}"
    attributes:
      - flavor: test
      - migrated
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Andrej Svenke (@anryko)']
