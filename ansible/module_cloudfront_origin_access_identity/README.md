# Ansible module: ansible.module_cloudfront_origin_access_identity


create, update and delete origin access identities for a cloudfront distribution

## Description

Allows for easy creation, updating and deletion of origin access identities.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "caller_reference": "{'description': ['A unique identifier to reference the origin access identity by.'], 'required': False}",
    "comment": "{'description': ['A comment to describe the cloudfront origin access identity.'], 'required': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "origin_access_identity_id": "{'description': ['The origin_access_identity_id of the cloudfront distribution.'], 'required': False}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['If the named resource should exist.'], 'choices': ['present', 'absent'], 'default': 'update_origin_access_identity'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml


- name: create an origin access identity
  cloudfront_origin_access_identity:
    state: present
    caller_reference: this is an example reference
    comment: this is an example comment

- name: update an existing origin access identity using caller_reference as an identifier
  cloudfront_origin_access_identity:
     origin_access_identity_id: E17DRN9XUOAHZX
     caller_reference: this is an example reference
     comment: this is a new comment

- name: delete an existing origin access identity using caller_reference as an identifier
  cloudfront_origin_access_identity:
     state: absent
     caller_reference: this is an example reference
     comment: this is a new comment


```

## License

TODO

## Author Information
  - ['Willem van Ketwich (@wilvk)']
