# Ansible module: ansible.module_ec2_vpc_net


Configure AWS virtual private clouds

## Description

Create, modify, and terminate AWS virtual private clouds.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "cidr_block": "{'description': ['The primary CIDR of the VPC. After 2.5 a list of CIDRs can be provided. The first in the list will be used as the primary CIDR and is used in conjunction with the C(name) to ensure idempotence.'], 'required': True}",
    "dhcp_opts_id": "{'description': ['the id of the DHCP options to use for this vpc']}",
    "dns_hostnames": "{'description': ['Whether to enable AWS hostname support.'], 'default': True, 'type': 'bool'}",
    "dns_support": "{'description': ['Whether to enable AWS DNS support.'], 'default': True, 'type': 'bool'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "multi_ok": "{'description': ['By default the module will not create another VPC if there is another VPC with the same name and CIDR block. Specify this as true if you want duplicate VPCs created.'], 'default': False}",
    "name": "{'description': ['The name to give your VPC. This is used in combination with C(cidr_block) to determine if a VPC already exists.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_cidrs": "{'description': ['Remove CIDRs that are associated with the VPC and are not specified in C(cidr_block).'], 'default': False, 'type': 'bool', 'version_added': '2.5'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['The state of the VPC. Either absent or present.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tags": "{'description': ["The tags you want attached to the VPC. This is independent of the name value, note if you pass a 'Name' key it would override the Name of the VPC if it's different."], 'aliases': ['resource_tags']}",
    "tenancy": "{'description': ['Whether to be default or dedicated tenancy. This cannot be changed after the VPC has been created.'], 'default': 'default', 'choices': ['default', 'dedicated']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: create a VPC with dedicated tenancy and a couple of tags
  ec2_vpc_net:
    name: Module_dev2
    cidr_block: 10.10.0.0/16
    region: us-east-1
    tags:
      module: ec2_vpc_net
      this: works
    tenancy: dedicated

```

## License

TODO

## Author Information
  - ['Jonathan Davila (@defionscode)', 'Sloane Hertel (@s-hertel)']
  - ['Jonathan Davila (@defionscode)', 'Sloane Hertel (@s-hertel)']
