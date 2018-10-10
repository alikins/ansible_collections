# Ansible module: ansible.module_elasticache_parameter_group


Manage cache security groups in Amazon Elasticache

## Description

Manage cache security groups in Amazon Elasticache.
Returns information about the specified cache cluster.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "description": "{'description': ['A user-specified description for the cache parameter group.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "group_family": "{'description': ['The name of the cache parameter group family that the cache parameter group can be used with. Required when creating a cache parameter group.'], 'choices': ['memcached1.4', 'redis2.6', 'redis2.8', 'redis3.2', 'redis4.0']}",
    "name": "{'description': ['A user-specified name for the cache parameter group.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Idempotent actions that will create/modify, destroy, or reset a cache parameter group as needed.'], 'choices': ['present', 'absent', 'reset'], 'required': True}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "values": "{'description': ['A user-specified dictionary of parameters to reset or modify for the cache parameter group.']}",
}
```

## Examples


``` yaml

# Note: None of these examples set aws_access_key, aws_secret_key, or region.
# It is assumed that their matching environment variables are set.
---
- hosts: localhost
  connection: local
  tasks:
    - name: 'Create a test parameter group'
      elasticache_parameter_group:
        name: 'test-param-group'
        group_family: 'redis3.2'
        description: 'This is a cache parameter group'
        state: 'present'
    - name: 'Modify a test parameter group'
      elasticache_parameter_group:
        name: 'test-param-group'
        values:
          activerehashing: yes
          client-output-buffer-limit-normal-hard-limit: 4
        state: 'present'
    - name: 'Reset all modifiable parameters for the test parameter group'
      elasticache_parameter_group:
        name: 'test-param-group'
        state: reset
    - name: 'Delete a test parameter group'
      elasticache_parameter_group:
        name: 'test-param-group'
        state: 'absent'

```

## License

TODO

## Author Information
  - ['Sloane Hertel (@s-hertel)']
