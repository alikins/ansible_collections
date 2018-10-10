# Ansible module: ansible.module_cloudfront_invalidation


create invalidations for aws cloudfront distributions

## Description

Allows for invalidation of a batch of paths for a CloudFront distribution.

## Requirements

TODO

## Arguments

``` json
{
    "alias": "{'description': ['The alias of the cloudfront distribution to invalidate paths for. Can be specified instead of distribution_id.'], 'required': False}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "caller_reference": "{'description': ['A unique reference identifier for the invalidation paths.'], 'required': False, 'default': 'current datetime stamp'}",
    "distribution_id": "{'description': ['The id of the cloudfront distribution to invalidate paths for. Can be specified insted of the alias.'], 'required': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "target_paths": "{'description': ["A list of paths on the distribution to invalidate. Each path should begin with '/'. Wildcards are allowed. eg. '/foo/bar/*'"], 'required': True}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml


- name: create a batch of invalidations using a distribution_id for a reference
  cloudfront_invalidation:
    distribution_id: E15BU8SDCGSG57
    caller_reference: testing 123
    target_paths:
      - /testpathone/test1.css
      - /testpathtwo/test2.js
      - /testpaththree/test3.ss

- name: create a batch of invalidations using an alias as a reference and one path using a wildcard match
  cloudfront_invalidation:
    alias: alias.test.com
    caller_reference: testing 123
    target_paths:
      - /testpathone/test4.css
      - /testpathtwo/test5.js
      - /testpaththree/*


```

## License

TODO

## Author Information
  - ['Willem van Ketwich (@wilvk)']
