# Ansible module: ansible.module_sts_assume_role


Assume a role using AWS Security Token Service and obtain temporary credentials

## Description

Assume a role using AWS Security Token Service and obtain temporary credentials

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "duration_seconds": "{'description': ["The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) to 43200 seconds (12 hours). The max dependis on the IAM role's sessions duration setting. By default, the value is set to 3600 seconds.s"]}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "external_id": "{'description': ["A unique identifier that is used by third parties to assume a role in their customers' accounts."]}",
    "mfa_serial_number": "{'description': ['The identification number of the MFA device that is associated with the user who is making the AssumeRole call.']}",
    "mfa_token": "{'description': ['The value provided by the MFA device, if the trust policy of the role being assumed requires MFA.']}",
    "policy": "{'description': ["Supplemental policy to use in addition to assumed role's policies."]}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "role_arn": "{'description': ['The Amazon Resource Name (ARN) of the role that the caller is assuming (http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html#Identifiers_ARNs)'], 'required': True}",
    "role_session_name": "{'description': ["Name of the role's session - will be used by CloudTrail"], 'required': True}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Assume an existing role (more details: http://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)
sts_assume_role:
  role_arn: "arn:aws:iam::123456789012:role/someRole"
  role_session_name: "someRoleSession"
register: assumed_role

# Use the assumed role above to tag an instance in account 123456789012
ec2_tag:
  aws_access_key: "{{ assumed_role.sts_creds.access_key }}"
  aws_secret_key: "{{ assumed_role.sts_creds.secret_key }}"
  security_token: "{{ assumed_role.sts_creds.session_token }}"
  resource: i-xyzxyz01
  state: present
  tags:
    MyNewTag: value


```

## License

TODO

## Author Information
  - ['Boris Ekelchik (@bekelchik)', 'Marek Piatek (@piontas)']
  - ['Boris Ekelchik (@bekelchik)', 'Marek Piatek (@piontas)']
