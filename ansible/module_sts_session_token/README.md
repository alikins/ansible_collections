# Ansible module: ansible.module_sts_session_token


Obtain a session token from the AWS Security Token Service

## Description

Obtain a session token from the AWS Security Token Service

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "duration_seconds": "{'description': ['The duration, in seconds, of the session token. See http://docs.aws.amazon.com/STS/latest/APIReference/API_GetSessionToken.html#API_GetSessionToken_RequestParameters for acceptable and default values.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "mfa_serial_number": "{'description': ['The identification number of the MFA device that is associated with the user who is making the GetSessionToken call.']}",
    "mfa_token": "{'description': ['The value provided by the MFA device, if the trust policy of the user requires MFA.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Get a session token (more details: http://docs.aws.amazon.com/STS/latest/APIReference/API_GetSessionToken.html)
sts_session_token:
  duration_seconds: 3600
register: session_credentials

# Use the session token obtained above to tag an instance in account 123456789012
ec2_tag:
  aws_access_key: "{{ session_credentials.sts_creds.access_key }}"
  aws_secret_key: "{{ session_credentials.sts_creds.secret_key }}"
  security_token: "{{ session_credentials.sts_creds.session_token }}"
  resource: i-xyzxyz01
  state: present
  tags:
    MyNewTag: value


```

## License

TODO

## Author Information
  - ['Victor Costan (@pwnall)']
