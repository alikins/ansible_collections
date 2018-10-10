# Ansible module: ansible.module_iam_user


Manage AWS IAM users

## Description

Manage AWS IAM users

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "managed_policy": "{'description': ['A list of managed policy ARNs or friendly names to attach to the user. To embed an inline policy, use M(iam_policy).'], 'required': False}",
    "name": "{'description': ['The name of the user to create.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_policy": "{'description': ['Detach policies which are not included in managed_policy list'], 'required': False, 'default': False}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Create or remove the IAM user'], 'required': True, 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.
# Note: This module does not allow management of groups that users belong to.
#       Groups should manage their membership directly using `iam_group`,
#       as users belong to them.

# Create a user
- iam_user:
    name: testuser1
    state: present

# Create a user and attach a managed policy using its ARN
- iam_user:
    name: testuser1
    managed_policy:
      - arn:aws:iam::aws:policy/AmazonSNSFullAccess
    state: present

# Remove all managed policies from an existing user with an empty list
- iam_user:
    name: testuser1
    state: present
    purge_policy: true

# Delete the user
- iam_user:
    name: testuser1
    state: absent


```

## License

TODO

## Author Information
  - ['Josh Souza, @joshsouza']
