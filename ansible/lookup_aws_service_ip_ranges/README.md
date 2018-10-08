# Ansible lookup: ansible.lookup_aws_service_ip_ranges


Look up the IP ranges for services provided in AWS such as EC2 and S3

## Description

AWS publishes IP ranges used on the public internet by EC2, S3, CloudFront, CodeBuild, Route53, and Route53 Health Checking.
This module produces a list of all the ranges (by default) or can narrow down the list to the specified region or service.

## Requirements

TODO

## Arguments

``` json
{
    "region": "{'description': ['The AWS region to narrow the ranges to. Examples: us-east-1, eu-west-2, ap-southeast-1']}",
    "service": "{'description': ['The service to filter ranges by. Options: EC2, S3, CLOUDFRONT, CODEbUILD, ROUTE53, ROUTE53_HEALTHCHECKS']}",
}
```

## Examples


``` yaml

vars:
  ec2_ranges: "{{ lookup('aws_service_ip_ranges', region='ap-southeast-2', service='EC2', wantlist=True) }}"
tasks:

- name: "use list return option and iterate as a loop"
  debug: msg="{% for cidr in ec2_ranges %}{{ cidr }} {% endfor %}"
# "52.62.0.0/15 52.64.0.0/17 52.64.128.0/17 52.65.0.0/16 52.95.241.0/24 52.95.255.16/28 54.66.0.0/16 "

- name: "Pull S3 IP ranges, and print the default return style"
  debug: msg="{{ lookup('aws_service_ip_ranges', region='us-east-1', service='S3') }}"
# "52.92.16.0/20,52.216.0.0/15,54.231.0.0/17"

```

## License

TODO

## Author Information
  - ['James Turner <turnerjsm@gmail.com>']
