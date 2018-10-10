# Ansible module: ansible.module_ec2_lc_find


Find AWS Autoscaling Launch Configurations

## Description

Returns list of matching Launch Configurations for a given name, along with other useful information
Results can be sorted and sliced
It depends on boto
Based on the work by Tom Bamford (https://github.com/tombamford)

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "limit": "{'description': ['How many results to show.', 'Corresponds to Python slice notation like list[:limit].']}",
    "name_regex": "{'description': ['A Launch Configuration to match', "It'll be compiled as regex"], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use.'], 'required': True, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "sort_order": "{'description': ['Order in which to sort results.'], 'choices': ['ascending', 'descending'], 'default': 'ascending'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Search for the Launch Configurations that start with "app"
- ec2_lc_find:
    name_regex: app.*
    sort_order: descending
    limit: 2

```

## License

TODO

## Author Information
  - ['Jose Armesto (@fiunchinho)']
