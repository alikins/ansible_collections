# Ansible module: ansible.module_ec2_lc_facts


Gather facts about AWS Autoscaling Launch Configurations

## Description

Gather facts about AWS Autoscaling Launch Configurations

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "name": "{'description': ['A name or a list of name to match.'], 'default': []}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "sort": "{'description': ['Optional attribute which with to sort the results.'], 'choices': ['launch_configuration_name', 'image_id', 'created_time', 'instance_type', 'kernel_id', 'ramdisk_id', 'key_name']}",
    "sort_end": "{'description': ['Which result to end with (when sorting).', 'Corresponds to Python slice notation.']}",
    "sort_order": "{'description': ['Order in which to sort results.', "Only used when the 'sort' parameter is specified."], 'choices': ['ascending', 'descending'], 'default': 'ascending'}",
    "sort_start": "{'description': ['Which result to start with (when sorting).', 'Corresponds to Python slice notation.']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Gather facts about all launch configurations
- ec2_lc_facts:

# Gather facts about launch configuration with name "example"
- ec2_lc_facts:
    name: example

# Gather facts sorted by created_time from most recent to least recent
- ec2_lc_facts:
    sort: created_time
    sort_order: descending

```

## License

TODO

## Author Information
  - ['Loïc Latreille (@psykotox)']
