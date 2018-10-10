# Ansible module: ansible.module_ec2_win_password


gets the default administrator password for ec2 windows instances

## Description

Gets the default administrator password from any EC2 Windows instance. The instance is referenced by its id (e.g. C(i-XXXXXXX)). This module has a dependency on python-boto.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "instance_id": "{'description': ['The instance id to get the password data from.'], 'required': True}",
    "key_file": "{'description': ['Path to the file containing the key pair used on the instance.'], 'required': True}",
    "key_passphrase": "{'version_added': '2.0', 'description': ['The passphrase for the instance key pair. The key must use DES or 3DES encryption for this module to decrypt it. You can use openssl to convert your password protected keys if they do not use DES or 3DES. ex) C(openssl rsa -in current_key -out new_key -des3).']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "wait": "{'version_added': '2.0', 'description': ['Whether or not to wait for the password to be available before returning.'], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'version_added': '2.0', 'description': ['Number of seconds to wait before giving up.'], 'default': 120}",
}
```

## Examples


``` yaml

# Example of getting a password
- name: get the Administrator password
  ec2_win_password:
    profile: my-boto-profile
    instance_id: i-XXXXXX
    region: us-east-1
    key_file: "~/aws-creds/my_test_key.pem"

# Example of getting a password with a password protected key
- name: get the Administrator password
  ec2_win_password:
    profile: my-boto-profile
    instance_id: i-XXXXXX
    region: us-east-1
    key_file: "~/aws-creds/my_protected_test_key.pem"
    key_passphrase: "secret"

# Example of waiting for a password
- name: get the Administrator password
  ec2_win_password:
    profile: my-boto-profile
    instance_id: i-XXXXXX
    region: us-east-1
    key_file: "~/aws-creds/my_test_key.pem"
    wait: yes
    wait_timeout: 45

```

## License

TODO

## Author Information
  - ['Rick Mendes (@rickmendes)']
