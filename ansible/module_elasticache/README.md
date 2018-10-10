# Ansible module: ansible.module_elasticache


Manage cache clusters in Amazon Elasticache

## Description

Manage cache clusters in Amazon Elasticache.
Returns information about the specified cache cluster.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "cache_engine_version": "{'description': ['The version number of the cache engine']}",
    "cache_parameter_group": "{'description': ['The name of the cache parameter group to associate with this cache cluster. If this argument is omitted, the default cache parameter group for the specified engine will be used.'], 'version_added': '2.0', 'aliases': ['parameter_group']}",
    "cache_port": "{'description': ['The port number on which each of the cache nodes will accept connections']}",
    "cache_security_groups": "{'description': ['A list of cache security group names to associate with this cache cluster. Must be an empty list if inside a vpc']}",
    "cache_subnet_group": "{'description': ['The subnet group name to associate with. Only use if inside a vpc. Required if inside a vpc'], 'version_added': '2.0'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "engine": "{'description': ['Name of the cache engine to be used.'], 'default': 'memcached', 'choices': ['redis', 'memcached']}",
    "hard_modify": "{'description': ['Whether to destroy and recreate an existing cache cluster if necessary in order to modify its state'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['The cache cluster identifier'], 'required': True}",
    "node_type": "{'description': ['The compute and memory capacity of the nodes in the cache cluster'], 'default': 'cache.m1.small'}",
    "num_nodes": "{'description': ['The initial number of cache nodes that the cache cluster will have. Required when state=present.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_group_ids": "{'description': ['A list of vpc security group names to associate with this cache cluster. Only use if inside a vpc'], 'version_added': '1.6'}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['C(absent) or C(present) are idempotent actions that will create or destroy a cache cluster as needed. C(rebooted) will reboot the cluster, resulting in a momentary outage.'], 'choices': ['present', 'absent', 'rebooted'], 'required': True}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "wait": "{'description': ['Wait for cache cluster result before returning'], 'type': 'bool', 'default': True}",
    "zone": "{'description': ['The EC2 Availability Zone in which the cache cluster will be created']}",
}
```

## Examples


``` yaml

# Note: None of these examples set aws_access_key, aws_secret_key, or region.
# It is assumed that their matching environment variables are set.

# Basic example
- elasticache:
    name: "test-please-delete"
    state: present
    engine: memcached
    cache_engine_version: 1.4.14
    node_type: cache.m1.small
    num_nodes: 1
    cache_port: 11211
    cache_security_groups:
      - default
    zone: us-east-1d


# Ensure cache cluster is gone
- elasticache:
    name: "test-please-delete"
    state: absent

# Reboot cache cluster
- elasticache:
    name: "test-please-delete"
    state: rebooted


```

## License

TODO

## Author Information
  - ['Jim Dalton (@jsdalton)']
