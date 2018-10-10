# Ansible module: ansible.module_ec2_asg_facts


Gather facts about ec2 Auto Scaling Groups (ASGs) in AWS

## Description

Gather facts about ec2 Auto Scaling Groups (ASGs) in AWS

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "name": "{'description': ['The prefix or name of the auto scaling group(s) you are searching for.', "Note: This is a regular expression match with implicit '^' (beginning of string). Append '$' for a complete name match."], 'required': False}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "tags": "{'description': ["A dictionary/hash of tags in the format { tag1_name: 'tag1_value', tag2_name: 'tag2_value' } to match against the auto scaling group(s) you are searching for.\n"], 'required': False}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Find all groups
- ec2_asg_facts:
  register: asgs

# Find a group with matching name/prefix
- ec2_asg_facts:
    name: public-webserver-asg
  register: asgs

# Find a group with matching tags
- ec2_asg_facts:
    tags:
      project: webapp
      env: production
  register: asgs

# Find a group with matching name/prefix and tags
- ec2_asg_facts:
    name: myproject
    tags:
      env: production
  register: asgs

# Fail if no groups are found
- ec2_asg_facts:
    name: public-webserver-asg
  register: asgs
  failed_when: "{{ asgs.results | length == 0 }}"

# Fail if more than 1 group is found
- ec2_asg_facts:
    name: public-webserver-asg
  register: asgs
  failed_when: "{{ asgs.results | length > 1 }}"

```

## License

TODO

## Author Information
  - ['Rob White (@wimnat)']
