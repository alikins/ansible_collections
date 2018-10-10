# Ansible module: ansible.module_aws_kms


Perform various KMS management tasks

## Description

Manage role/user access to a KMS key. Not designed for encrypting/decrypting.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "clean_invalid_entries": "{'description': ['If adding/removing a role and invalid grantees are found, remove them. These entries will cause an update to fail in all known cases.', 'Only cleans if changes are being made.'], 'type': 'bool', 'default': True}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "grant_types": "{'description': ['List of grants to give to user/role. Likely "role,role grant" or "role,role grant,admin". Required when C(mode=grant).'], 'required': False}",
    "key_alias": "{'description': ['Alias label to the key. One of C(key_alias) or C(key_arn) are required.'], 'required': False}",
    "key_arn": "{'description': ['Full ARN to the key. One of C(key_alias) or C(key_arn) are required.'], 'required': False}",
    "mode": "{'description': ['Grant or deny access.'], 'required': True, 'default': 'grant', 'choices': ['grant', 'deny']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "role_arn": "{'description': ['ARN of role to allow/deny access. One of C(role_name) or C(role_arn) are required.'], 'required': False}",
    "role_name": "{'description': ['Role to allow/deny access. One of C(role_name) or C(role_arn) are required.'], 'required': False}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

- name: grant user-style access to production secrets
  aws_kms:
  args:
    mode: grant
    key_alias: "alias/my_production_secrets"
    role_name: "prod-appServerRole-1R5AQG2BSEL6L"
    grant_types: "role,role grant"
- name: remove access to production secrets from role
  aws_kms:
  args:
    mode: deny
    key_alias: "alias/my_production_secrets"
    role_name: "prod-appServerRole-1R5AQG2BSEL6L"

```

## License

TODO

## Author Information
  - ['Ted Timmons (@tedder)']
