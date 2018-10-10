# Ansible module: ansible.module_efs_facts


Get information about Amazon EFS file systems

## Description

Module searches Amazon EFS file systems

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "id": "{'description': ['ID of Amazon EFS.']}",
    "name": "{'description': ['Creation Token of Amazon EFS file system.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "tags": "{'description': ['List of tags of Amazon EFS. Should be defined as dictionary']}",
    "targets": "{'description': ['list of targets on which to filter the returned results', 'result must match all of the specified targets, each of which can be a security group ID, a subnet ID or an IP address']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# find all existing efs
- efs_facts:
  register: result

- efs_facts:
    name: myTestNameTag

- efs_facts:
    id: fs-1234abcd

# Searching all EFS instances with tag Name = 'myTestNameTag', in subnet 'subnet-1a2b3c4d' and with security group 'sg-4d3c2b1a'
- efs_facts:
    tags:
        name: myTestNameTag
    targets:
        - subnet-1a2b3c4d
        - sg-4d3c2b1a

```

## License

TODO

## Author Information
  - ['Ryan Sydnor (@ryansydnor)']
