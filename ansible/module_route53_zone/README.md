# Ansible module: ansible.module_route53_zone


add or delete Route53 zones

## Description

Creates and deletes Route53 private and public zones

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "comment": "{'description': ['Comment associated with the zone'], 'default': ''}",
    "delegation_set_id": "{'description': ["The reusable delegation set ID to be associated with the zone. Note that you can't associate a reusable delegation set with a private hosted zone."], 'version_added': 2.6}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "hosted_zone_id": "{'description': ['The unique zone identifier you want to delete or "all" if there are many zones with the same domain name. Required if there are multiple zones identified with the above options'], 'version_added': 2.4}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['whether or not the zone should exist or not'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "vpc_id": "{'description': ['The VPC ID the zone should be a part of (if this is going to be a private zone)']}",
    "vpc_region": "{'description': ['The VPC Region the zone should be a part of (if this is going to be a private zone)']}",
    "zone": "{'description': ['The DNS zone record (eg: foo.com.)'], 'required': True}",
}
```

## Examples


``` yaml

- name: create a public zone
  route53_zone:
    zone: example.com
    comment: this is an example

- name: delete a public zone
  route53_zone:
    zone: example.com
    state: absent

- name: create a private zone
  route53_zone:
    zone: devel.example.com
    vpc_id: '{{ myvpc_id }}'
    vpc_region: us-west-2
    comment: developer domain

- name: create a public zone associated with a specific reusable delegation set
  route53_zone:
    zone: example.com
    comment: reusable delegation set example
    delegation_set_id: A1BCDEF2GHIJKL

```

## License

TODO

## Author Information
  - ['Christopher Troup (@minichate)']
